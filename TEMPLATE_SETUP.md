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
- `src/ui/add-entry.html` - Update track options if needed
- `README.md` - Update the album name and repository links

#### Update Track Names
Edit `src/ui/add-entry.html` and replace the track options:
```html
<select id="track" name="track">
    <option value="Track 01: Your Song Name">Track 01: Your Song Name</option>
    <option value="Track 02: Another Song">Track 02: Another Song</option>
    <!-- Add your tracks here -->
</select>
```

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
├── src/server/                 # Python server
├── docs/                       # Documentation and journal entries
│   ├── songs.json             # Your song catalog
│   └── journal/               # Auto-organized journal entries
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
1. Edit `src/ui/add-entry.html`
2. Add new track options to the dropdown
3. Update the album overview page if needed

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

## 🆘 Need Help?

- Check the main README.md for usage instructions
- Look at the server logs for any errors
- Make sure all dependencies are installed (Python 3.7+)

## 🎵 Happy Producing!

Your album workflow system is now ready. Start creating music and tracking your progress!
