#!/usr/bin/env python3
"""
Production Journal Server
Handles saving journal entries directly to the docs folder
"""

import os
import json
from datetime import datetime
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
import threading
import webbrowser

class JournalHandler(BaseHTTPRequestHandler):
    def do_OPTIONS(self):
        """Handle CORS preflight requests"""
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()

    def do_POST(self):
        """Handle POST requests for saving journal entries and Git operations"""
        if self.path == '/save-entry':
            self.save_journal_entry()
        elif self.path == '/api/songs':
            self.save_song()
        elif self.path == '/api/git-commit':
            self.git_commit_and_push()
        else:
            self.send_error(404, "Not Found")

    def do_GET(self):
        """Handle GET requests"""
        if self.path == '/':
            self.serve_ui()
        elif self.path.startswith('/src/ui/'):
            self.serve_ui_file()
        elif self.path == '/add-entry':
            self.serve_add_entry_page()
        elif self.path == '/read-entries':
            self.serve_read_entries_page()
        elif self.path == '/album-overview':
            self.serve_album_overview_page()
        elif self.path == '/api/journal-files':
            self.list_journal_files()
        elif self.path.startswith('/api/journal-file/'):
            self.get_journal_file()
        elif self.path == '/api/songs':
            self.get_songs()
        elif self.path == '/api/git-commit':
            self.git_commit_and_push()
        else:
            self.send_error(404, "Not Found")

    def serve_ui(self):
        """Serve the main UI page"""
        try:
            with open('index.html', 'r') as f:
                content = f.read()
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(content.encode())
        except FileNotFoundError:
            self.send_error(404, "index.html not found")

    def serve_ui_file(self):
        """Serve UI files"""
        try:
            file_path = self.path[1:]  # Remove leading slash
            if file_path.endswith('.html'):
                content_type = 'text/html'
            elif file_path.endswith('.css'):
                content_type = 'text/css'
            elif file_path.endswith('.js'):
                content_type = 'application/javascript'
            else:
                content_type = 'text/plain'
            
            with open(file_path, 'r') as f:
                content = f.read()
            
            self.send_response(200)
            self.send_header('Content-type', content_type)
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(content.encode())
        except FileNotFoundError:
            self.send_error(404, f"File {self.path} not found")

    def serve_add_entry_page(self):
        """Serve the add entry page"""
        try:
            with open('src/ui/add-entry.html', 'r') as f:
                content = f.read()
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(content.encode())
        except FileNotFoundError:
            self.send_error(404, "add-entry.html not found")

    def serve_read_entries_page(self):
        """Serve the read entries page"""
        try:
            with open('src/ui/read-entries.html', 'r') as f:
                content = f.read()
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(content.encode())
        except FileNotFoundError:
            self.send_error(404, "read-entries.html not found")

    def serve_album_overview_page(self):
        """Serve the album overview page"""
        try:
            with open('src/ui/album-overview.html', 'r') as f:
                content = f.read()
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(content.encode())
        except FileNotFoundError:
            self.send_error(404, "Album overview page not found")

    def save_journal_entry(self):
        """Save a journal entry to the docs folder"""
        try:
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            data = json.loads(post_data.decode('utf-8'))
            
            # Create organized folder structure
            now = datetime.now()
            year = now.strftime('%Y')
            month = now.strftime('%m')
            day = now.strftime('%d')
            time_str = now.strftime('%H%M')
            
            # Create filename
            track_slug = data['track'].lower().replace(' ', '-').replace(':', '').replace('_', '-')
            filename = f"{year}-{month}-{day}-{time_str}-{track_slug}.md"
            
            # Create folder structure
            journal_dir = os.path.join('docs', 'journal', year, month)
            os.makedirs(journal_dir, exist_ok=True)
            
            # Create markdown content with all the form fields
            followup_section = ""
            if data.get('followup'):
                followup_section = f"## Follow-up Actions\n{data['followup']}\n\n"

            technical_section = "## Technical Notes\n"
            if data.get('bpm'):
                technical_section += f"- **BPM:** {data['bpm']}\n"
            if data.get('key'):
                technical_section += f"- **Key:** {data['key']}\n"
            if data.get('effects'):
                technical_section += f"- **Effects Used:** {data['effects']}\n"
            if data.get('issues'):
                technical_section += f"- **Recording Issues:** {data['issues']}\n"
            if not any([data.get('bpm'), data.get('key'), data.get('effects'), data.get('issues')]):
                technical_section += "- **BPM:** [Add BPM if relevant]\n"
                technical_section += "- **Key:** [Add key if relevant]\n"
                technical_section += "- **Effects Used:** [List any new effects or plugins]\n"
                technical_section += "- **Recording Issues:** [Note any technical problems]\n"

            creative_section = "## Creative Notes\n"
            if data.get('mood'):
                creative_section += f"- **Mood/Feeling:** {data['mood']}\n"
            if data.get('inspiration'):
                creative_section += f"- **Inspiration:** {data['inspiration']}\n"
            if data.get('challenges'):
                creative_section += f"- **Challenges:** {data['challenges']}\n"
            if data.get('breakthroughs'):
                creative_section += f"- **Breakthroughs:** {data['breakthroughs']}\n"
            if not any([data.get('mood'), data.get('inspiration'), data.get('challenges'), data.get('breakthroughs')]):
                creative_section += "- **Mood/Feeling:** [Describe the creative mood]\n"
                creative_section += "- **Inspiration:** [What inspired this session]\n"
                creative_section += "- **Challenges:** [What was difficult]\n"
                creative_section += "- **Breakthroughs:** [What worked well]\n"

            markdown_content = f"""# Production Journal Entry

**Date:** {data['date']}  
**Track:** {data['track']}  
**Session Time:** {now.strftime('%Y-%m-%d %H:%M:%S')}

## Session Notes
{data['notes']}

{followup_section}{technical_section}

{creative_section}

---
*Auto-generated by Production Journal Server*
"""

            # Save the file
            file_path = os.path.join(journal_dir, filename)
            with open(file_path, 'w') as f:
                f.write(markdown_content)
            
            # Send success response
            response = {
                'success': True,
                'message': f'Entry saved to {file_path}',
                'filename': filename,
                'file_path': file_path
            }
            
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(json.dumps(response).encode())
            
            print(f"✅ Saved journal entry: {file_path}")
            
        except Exception as e:
            error_response = {
                'success': False,
                'message': f'Error saving entry: {str(e)}'
            }
            
            self.send_response(500)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(json.dumps(error_response).encode())
            
            print(f"❌ Error saving entry: {e}")

    def list_journal_files(self):
        """List all journal files in the docs/journal directory"""
        try:
            import glob
            
            # Find all markdown files in docs/journal
            journal_pattern = os.path.join('docs', 'journal', '**', '*.md')
            files = glob.glob(journal_pattern, recursive=True)
            
            # Sort by modification time (newest first)
            files.sort(key=lambda x: os.path.getmtime(x), reverse=True)
            
            file_list = []
            for file_path in files:
                relative_path = os.path.relpath(file_path, 'docs/journal')
                file_info = {
                    'filename': os.path.basename(file_path),
                    'path': relative_path,
                    'full_path': file_path,
                    'modified': datetime.fromtimestamp(os.path.getmtime(file_path)).isoformat()
                }
                file_list.append(file_info)
            
            response = {
                'success': True,
                'files': file_list
            }
            
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(json.dumps(response).encode())
            
        except Exception as e:
            error_response = {
                'success': False,
                'message': f'Error listing files: {str(e)}'
            }
            
            self.send_response(500)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(json.dumps(error_response).encode())

    def get_journal_file(self):
        """Get the content of a specific journal file"""
        try:
            # Extract filename from path
            filename = self.path.replace('/api/journal-file/', '')
            
            # Find the file in docs/journal
            journal_pattern = os.path.join('docs', 'journal', '**', filename)
            import glob
            files = glob.glob(journal_pattern, recursive=True)
            
            if not files:
                self.send_error(404, "File not found")
                return
            
            file_path = files[0]
            
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            response = {
                'success': True,
                'content': content,
                'filename': filename,
                'path': file_path
            }
            
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(json.dumps(response).encode())
            
        except Exception as e:
            error_response = {
                'success': False,
                'message': f'Error reading file: {str(e)}'
            }
            
            self.send_response(500)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(json.dumps(error_response).encode())

    def git_commit_and_push(self):
        """Commit and push changes to Git repository"""
        try:
            import subprocess
            
            # Get current timestamp for commit message
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            
            # Check if there are changes to commit
            result = subprocess.run(['git', 'status', '--porcelain'], 
                                  capture_output=True, text=True, cwd='.')
            
            if not result.stdout.strip():
                response = {
                    'success': True,
                    'message': 'No changes to commit',
                    'output': 'Working directory is clean'
                }
            else:
                # Add all changes
                subprocess.run(['git', 'add', '.'], cwd='.')
                
                # Commit with timestamp
                commit_message = f"Auto-commit: Production journal updates - {timestamp}"
                commit_result = subprocess.run(['git', 'commit', '-m', commit_message], 
                                             capture_output=True, text=True, cwd='.')
                
                if commit_result.returncode == 0:
                    # Try to push to remote
                    push_result = subprocess.run(['git', 'push'], 
                                               capture_output=True, text=True, cwd='.')
                    
                    if push_result.returncode == 0:
                        response = {
                            'success': True,
                            'message': 'Changes committed and pushed successfully',
                            'output': f'Commit: {commit_message}\nPush: {push_result.stdout}'
                        }
                    else:
                        response = {
                            'success': True,
                            'message': 'Changes committed but push failed',
                            'output': f'Commit: {commit_message}\nPush Error: {push_result.stderr}'
                        }
                else:
                    response = {
                        'success': False,
                        'message': 'Failed to commit changes',
                        'output': commit_result.stderr
                    }
            
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(json.dumps(response).encode())
            
            print(f"Git operation: {response['message']}")
            
        except Exception as e:
            error_response = {
                'success': False,
                'message': f'Git operation failed: {str(e)}'
            }
            
            self.send_response(500)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(json.dumps(error_response).encode())
            
            print(f"Git operation error: {e}")

    def get_songs(self):
        """Get all songs from the songs.json file"""
        try:
            songs_file = 'docs/songs.json'
            if os.path.exists(songs_file):
                with open(songs_file, 'r') as f:
                    songs = json.load(f)
            else:
                songs = []
            
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(json.dumps(songs).encode())
            
        except Exception as e:
            error_response = {'error': f'Failed to load songs: {str(e)}'}
            self.send_response(500)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(json.dumps(error_response).encode())

    def save_song(self):
        """Save a new song to the songs.json file"""
        try:
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            song_data = json.loads(post_data.decode('utf-8'))
            
            # Create songs directory if it doesn't exist
            os.makedirs('docs', exist_ok=True)
            
            songs_file = 'docs/songs.json'
            if os.path.exists(songs_file):
                with open(songs_file, 'r') as f:
                    songs = json.load(f)
            else:
                songs = []
            
            # Add new song with ID and timestamps
            new_song = {
                'id': str(int(time.time() * 1000)),
                'title': song_data.get('songTitle', ''),
                'key': song_data.get('songKey', ''),
                'bpm': int(song_data.get('songBpm', 0)) if song_data.get('songBpm') else None,
                'status': song_data.get('songStatus', 'draft'),
                'notes': song_data.get('songNotes', ''),
                'progress': self.get_default_progress(song_data.get('songStatus', 'draft')),
                'createdAt': datetime.now().isoformat(),
                'updatedAt': datetime.now().isoformat()
            }
            
            songs.append(new_song)
            
            # Save updated songs list
            with open(songs_file, 'w') as f:
                json.dump(songs, f, indent=2)
            
            response = {
                'success': True,
                'message': f'Song "{new_song["title"]}" added successfully',
                'song': new_song
            }
            
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(json.dumps(response).encode())
            
            print(f"Song saved: {new_song['title']} ({new_song['status']})")
            
        except Exception as e:
            error_response = {
                'success': False,
                'message': f'Failed to save song: {str(e)}'
            }
            self.send_response(500)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(json.dumps(error_response).encode())
            
            print(f"Error saving song: {e}")

    def get_default_progress(self, status):
        """Get default progress percentage based on status"""
        progress_map = {
            'draft': 10,
            'production': 30,
            'mixing': 70,
            'mastering': 90,
            'done': 100
        }
        return progress_map.get(status, 0)

def start_server(port=8082):
    """Start the journal server"""
    server_address = ('', port)
    httpd = HTTPServer(server_address, JournalHandler)
    
    print(f"🎧 Production Journal Server starting on port {port}")
    print(f"📝 Open http://localhost:{port} to access the journal")
    print(f"💾 Journal entries will be saved to docs/journal/ folder")
    print("Press Ctrl+C to stop the server")
    
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n🛑 Server stopped")
        httpd.server_close()

if __name__ == '__main__':
    start_server()
