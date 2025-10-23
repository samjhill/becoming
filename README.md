# 🎵 Becoming Album - Production Workflow

A music production workflow system for tracking your album progress, journaling sessions, and managing files.

**Template Repository**: This is a template for album production workflows. Fork this repo for each new album you create.

**Current Album**: [samjhill/becoming](https://github.com/samjhill/becoming)

## Getting Started

### For a New Album
1. **Fork this repository** for your new album
2. **Follow the setup guide**: See `TEMPLATE_SETUP.md` for detailed instructions
3. **Customize for your album**: Update track names, album title, etc.
4. **Start the server**:
   ```bash
   python3 start-journal-server.py
   ```
5. **Open your browser**: http://localhost:8082

### For This Album
1. **Start the server**:
   ```bash
   python3 start-journal-server.py
   ```
2. **Open your browser**: http://localhost:8082

## Features

### 📝 Production Journal
- Add session notes with technical details
- Track BPM, key, effects, mood, inspiration
- Auto-save to organized markdown files
- Browse your production history

### 🎵 Album Management
- Track song progress (draft → production → mixing → mastering → done)
- Visual dashboard showing completion percentage
- Add songs with metadata (title, key, BPM, notes)
- Monitor overall album progress

### 💾 Git Integration
- One-click commit and push to GitHub
- Automatic backup of all changes
- Version control for your entire project

## Usage

### Adding Journal Entries
1. Go to **Add New Entry** from the homepage
2. Fill in session details (track, notes, BPM, key, etc.)
3. Click **Add Entry** - automatically saved!
4. Use **💾 Commit & Push** to backup to GitHub

### Managing Your Album
1. Go to **Album Overview** from the homepage
2. Add songs with metadata (title, key, BPM, status)
3. Track progress through the pipeline
4. Monitor completion percentage

### Reading Entries
1. Go to **Read Entries** from the homepage
2. Browse entries by date
3. Click any entry to read the full content

## Project Structure

```
your-album-name/
├── README.md            # Your album's documentation
├── TEMPLATE_SETUP.md    # Setup guide for new albums
├── src/ui/              # Web interface pages
├── src/server/          # Python server
├── docs/                # Documentation and journal entries
├── logic-projects/      # Logic Pro sessions
├── stems/               # Exported stems
└── bounces/             # Mixes and masters
```

## Technical Details

- **Server**: Python HTTP server on port 8082
- **Storage**: Songs in `docs/songs.json`, journal entries in `docs/journal/`
- **Git**: Automatic commits with timestamped messages
- **Backup**: One-click push to GitHub

## Troubleshooting

- **Server won't start**: Make sure port 8082 isn't in use
- **Can't access pages**: Check that the server is running
- **Git errors**: Ensure you have a GitHub remote configured

## Requirements

- Python 3.7+
- Git with LFS support
- Modern web browser