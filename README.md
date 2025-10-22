# 🎧 Becoming Album - Production Workflow

A professional music production workflow system with version control, organized project structure, and intelligent journaling tools.

**GitHub Repository**: [samjhill/becoming](https://github.com/samjhill/becoming)

## 🚀 Quick Start

### 1. Start the Production Journal Server
```bash
python3 start-journal-server.py
```

### 2. Access the Web Interface
Open your browser and navigate to: **http://localhost:8082**

## 🎯 Features

### 📝 Production Journal System
- **Add New Entries**: Create detailed session notes with technical and creative details
- **Browse Entries**: Read and reference your production history
- **Auto-Save**: Entries are automatically saved to organized markdown files
- **Rich Metadata**: Track BPM, key, effects, mood, inspiration, and more
- **Git Integration**: One-click commit and push to GitHub for automatic version control

### 🎵 Album Management System
- **Song Catalog**: Track all songs in your album with status management
- **Progress Dashboard**: Visual progress tracking for individual songs and album completion
- **Status Tracking**: Manage song status (draft → production → mixing → mastering → done)
- **Metadata Management**: Store song details (title, key, BPM, notes, creation date)
- **Completion Statistics**: Real-time album completion percentage and progress metrics

### 🗂️ Organized Project Structure
- **Logic Pro Projects**: Organized by track in `logic-projects/`
- **Stems & Bounces**: Properly categorized in `stems/` and `bounces/`
- **Documentation**: Centralized in `docs/` with version control
- **Journal Archives**: Auto-organized by date in `docs/journal/YYYY/MM/`

### 🔄 Version Control Integration
- **Git LFS**: Handles large audio files efficiently
- **Smart Branching**: Creative-friendly branching strategy
- **Milestone Tagging**: Tag important versions and demos

## 📁 Project Structure

```
becoming/
├── README.md                    # This file
├── SETUP.md                     # Detailed setup guide
├── index.html                   # Main dashboard
├── package.json                 # Project configuration
├── start-journal-server.py      # Server startup script
├── src/
│   ├── ui/
│   │   ├── add-entry.html       # Add new journal entries
│   │   └── read-entries.html    # Browse existing entries
│   ├── server/
│   │   ├── journal-server.py    # Python web server
│   │   └── README.md           # Server documentation
│   └── scripts/
│       └── export-journal.py    # Export utilities
├── docs/
│   ├── notes.md                 # Project notes
│   ├── production-journal.md    # Main journal file
│   └── journal/                 # Auto-organized journal entries
│       ├── 2024/
│       ├── 2025/
│       └── README.md
├── logic-projects/              # Logic Pro sessions
├── stems/                       # Exported stems
├── bounces/                     # Mixes and masters
├── samples/                     # Custom samples
└── .gitattributes              # Git LFS configuration
```

## 🛠️ Installation & Setup

### Prerequisites
- Python 3.7+
- Git with LFS support
- Logic Pro (for music production)

### Setup Steps

1. **Clone and Initialize**
   ```bash
   git clone <your-repo-url>
   cd becoming
   git lfs install
   ```

2. **Start the Journal Server**
   ```bash
   python3 start-journal-server.py
   ```

3. **Access the Interface**
   - Open http://localhost:8082 in your browser
   - Start creating journal entries and organizing your project

## 🎵 Usage Guide

### Adding Journal Entries
1. Navigate to **Add New Entry** from the homepage
2. Fill in session details:
   - **Track**: Select which track you're working on
   - **Session Notes**: What you accomplished
   - **Follow-up Actions**: Things to try next time
   - **Technical Details**: BPM, key, effects used
   - **Creative Notes**: Mood, inspiration, challenges, breakthroughs
3. Click **Add Entry** - it's automatically saved!
4. Click **💾 Commit & Push to GitHub** to backup your changes

### Git Integration
- **One-Click Backup**: Use the "💾 Commit & Push" button on any page
- **Automatic Commit Messages**: Timestamped commits for easy tracking
- **Smart Detection**: Only commits when there are actual changes
- **Error Handling**: Clear feedback if Git operations fail

### Reading Journal Entries
1. Navigate to **Read Entries** from the homepage
2. Browse your entries by date
3. Click any entry to read the full formatted content

### Managing Your Album
1. Navigate to **Album Overview** from the homepage
2. View your album progress dashboard with completion statistics
3. Add new songs with metadata (title, key, BPM, status, notes)
4. Track song status through the production pipeline
5. Monitor overall album completion percentage

### Project Organization
- **Logic Projects**: Save your `.logicx` files in `logic-projects/[track-name]/`
- **Stems**: Export normally and organize in `stems/[track-name]/`
- **Bounces**: Save mixes in `bounces/` with appropriate subfolders
- **Documentation**: Keep notes and lyrics in `docs/`

## 🔧 Technical Details

### Server Architecture
- **Python HTTP Server**: Handles file operations and API endpoints
- **Port**: 8082 (configurable in `src/server/journal-server.py`)
- **API Endpoints**:
  - `POST /save-entry`: Save new journal entries
  - `GET /api/journal-files`: List all journal files
  - `GET /api/journal-file/{filename}`: Get specific file content
  - `POST /api/git-commit`: Commit and push changes to GitHub

### File Organization
- **Journal Files**: Auto-saved as `YYYY-MM-DD-HHMM-track-name.md`
- **Folder Structure**: `docs/journal/YYYY/MM/` for easy navigation
- **Markdown Format**: Rich formatting with sections for different note types

### Version Control
- **Git LFS**: Tracks large audio files without bloating the repository
- **Smart Ignoring**: Excludes temporary Logic Pro files and cache
- **Branching Strategy**: Creative-friendly workflow with dedicated branches

## 🎨 Customization

### Adding New Track Types
Edit the track dropdown in `src/ui/add-entry.html`:
```html
<option value="Track 03: New Track">Track 03: New Track</option>
```

### Modifying Journal Fields
Add new fields to the form in `src/ui/add-entry.html` and update the server in `src/server/journal-server.py`.

### Changing Server Port
Update the port in `src/server/journal-server.py`:
```python
def start_server(port=8083):  # Change port here
```

## 📋 Best Practices

### Journal Entries
- **Be Specific**: Include technical details and creative insights
- **Regular Updates**: Log each session for better tracking
- **Reference Files**: Note which Logic projects or stems you're working with

### File Organization
- **Consistent Naming**: Use track names consistently across folders
- **Regular Commits**: Commit changes frequently with meaningful messages
- **Branch Management**: Use branches for experiments and merge back when ready

### Version Control
- **Tag Milestones**: Tag important versions (demos, finals, etc.)
- **Clean Commits**: Keep commits focused and well-described
- **Backup Strategy**: Use remote repositories for backup

## 🚨 Troubleshooting

### Server Won't Start
- **Port in Use**: Change the port in `src/server/journal-server.py`
- **Permission Issues**: Ensure write access to the `docs/` folder
- **Python Version**: Requires Python 3.7 or higher

### Journal Entries Not Saving
- **Server Running**: Ensure the server is running on port 8082
- **File Permissions**: Check write permissions for the `docs/journal/` folder
- **Browser Console**: Check for JavaScript errors in browser console

### Git LFS Issues
- **Install Git LFS**: Run `git lfs install` in the project directory
- **Track Files**: Ensure `.gitattributes` is properly configured
- **File Size**: Large files should be automatically handled by LFS

## 🤝 Contributing

This is a personal music production workflow, but the system can be adapted for other projects:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

MIT License - Feel free to adapt this workflow for your own music production projects.

## 🎵 Happy Producing!

This workflow is designed to help you focus on creativity while keeping your production process organized and documented. The journal system will help you track your creative evolution and technical decisions, making your album production more intentional and professional.

---

*Built with ❤️ for music producers who value both creativity and organization.*
