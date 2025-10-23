# 🎵 Becoming Album - Production Workflow

**"Trello for making an album"** - A music production workflow system for tracking your album progress, journaling sessions, and managing files.

**Template Repository**: Fork this repo for each new album you create.  
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
- **Session tracking** with technical details (BPM, key, effects, mood, inspiration)
- **Auto-organized** markdown files by date
- **Browse history** of all your production sessions

### 🎵 Album Management  
- **Visual dashboard** for song progress tracking
- **Full CRUD operations** - create, edit, delete songs
- **Progress tracking** from draft → production → mixing → mastering → done
- **Smart integration** - songs automatically appear in journal dropdown

### 💾 Git Integration
- **One-click backup** - commit and push to GitHub
- **Version control** for your entire project
- **Auto-organized archives** in `docs/journal/YYYY/MM/`

### 📱 Mobile & Offline Support
- **Responsive design** works perfectly on tablets and phones
- **Seamless offline mode** - entries save locally and sync when online
- **Invisible to user** - automatic fallback with no interruption

## Quick Start

1. **Start the server**: `python3 start-journal-server.py`
2. **Open your browser**: http://localhost:8082
3. **Add songs** in Album Overview
4. **Log sessions** in Add Entry  
5. **Browse history** in Read Entries
6. **Backup changes** with Commit & Push buttons

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

## Requirements

- Python 3.7+
- Git with LFS support
- Modern web browser

**Need help?** Check `TEMPLATE_SETUP.md` for detailed setup instructions.