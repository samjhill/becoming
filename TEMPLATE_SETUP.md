# 🎵 Album Template Setup Guide

This repository is designed as a template for album production workflows. Follow these steps to set up a new album project.

## 🚀 Quick Setup

### 1. Fork This Repository
- Click the "Fork" button on GitHub
- Choose your GitHub account as the destination

### 2. Rename Your Repository
- Go to your forked repository settings
- Change the repository name to your album name (e.g., "my-new-album")
- Update the description if needed

### 3. Clone Your Fork
```bash
git clone https://github.com/YOUR_USERNAME/YOUR_ALBUM_NAME.git
cd YOUR_ALBUM_NAME
```

### 4. Customize for Your Album

#### Update Album Title
Replace "Becoming" with your album name in these files:
- `src/ui/album-overview.html` - Update the title in the header
- `README.md` - Update the album name and repository links

#### Update Track Names
**Note**: The system now automatically manages tracks through the Album Overview page. You don't need to manually edit the dropdown anymore!

Instead, simply:
1. Start the server: `python3 start-journal-server.py`
2. Go to the Album Overview page
3. Click "Add New Song" to create your tracks
4. The tracks will automatically appear in the Add Entry dropdown with "Track: " prefix

#### Update Homepage
Edit `index.html` and update:
- Album name in the header
- Repository links
- Any custom descriptions

### 5. Set Up Git Remote
```bash
git remote set-url origin https://github.com/YOUR_USERNAME/YOUR_ALBUM_NAME.git
```

### 6. Start Working
```bash
python3 start-journal-server.py
```

## 📁 Project Structure

Your album project will have this structure:
```
your-album-name/
├── README.md                    # Your album's README
├── TEMPLATE_SETUP.md           # This setup guide (can be deleted)
├── src/ui/                     # Web interface
│   ├── add-entry.html         # Add journal entries
│   ├── read-entries.html      # Browse journal entries
│   └── album-overview.html    # Manage songs and album progress
├── src/server/                 # Python server
│   └── journal-server.py      # Backend API server
├── docs/                       # Documentation and journal entries
│   ├── songs.json             # Your song catalog (auto-generated)
│   └── journal/               # Auto-organized journal entries by date
├── logic-projects/            # Logic Pro sessions
├── stems/                     # Exported stems
├── bounces/                   # Mixes and masters
└── samples/                   # Custom samples
```

## 🎯 Best Practices

### Naming Convention
- Repository: `your-album-name` (lowercase, hyphens)
- Tracks: Use descriptive names like "Track 01: Song Name"

### File Organization
- Keep Logic Pro projects in `logic-projects/[track-name]/`
- Export stems to `stems/[track-name]/`
- Save bounces to `bounces/[track-name]/`

### Git Workflow
- Commit frequently with descriptive messages
- Use the "Commit & Push" button in the UI for quick backups
- Tag important milestones (demos, final mixes, etc.)

## 🔧 Customization Options

### Adding More Tracks
**Easy Method**: Use the Album Overview page to add songs - they'll automatically appear in the Add Entry dropdown!

**Advanced Method**: If you need to customize the static options:
1. Edit `src/ui/add-entry.html` - modify the static dropdown options (General, Sound Design, Mixing, Mastering)
2. Songs added via Album Overview will automatically appear with "Track: " prefix

### Custom Fields
You can add more fields to journal entries by:
1. Editing the form in `src/ui/add-entry.html`
2. Updating the server to handle new fields in `src/server/journal-server.py`
3. Modifying the markdown template generation

### Styling
All UI files use CSS that can be customized:
- `src/ui/add-entry.html` - Add entry form styling
- `src/ui/read-entries.html` - Journal reader styling
- `src/ui/album-overview.html` - Album dashboard styling

### Features Overview
Your template includes:
- **Production Journal**: Track sessions with technical details (BPM, key, effects, mood, inspiration)
- **Album Management**: Visual dashboard for song progress and album completion
- **Git Integration**: One-click commit and push to backup your work
- **Smart Organization**: Auto-organized journal entries by date
- **Track Management**: Create, edit, and delete songs with full CRUD operations

## 🆘 Need Help?

- Check the main README.md for usage instructions
- Look at the server logs for any errors
- Make sure all dependencies are installed (Python 3.7+)

## 🎵 Happy Producing!

Your album workflow system is now ready. Start creating music and tracking your progress!
