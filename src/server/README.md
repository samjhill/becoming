# Production Journal Server

This Python server handles saving journal entries directly to your docs folder, bypassing browser file download restrictions.

## 🚀 Quick Start

### Option 1: Using the startup script
```bash
python3 start-journal-server.py
```

### Option 2: Direct server execution
```bash
python3 src/server/journal-server.py
```

### Option 3: Using npm scripts
```bash
npm run journal-server
```

## 📁 How It Works

1. **UI sends data** to the server via HTTP POST
2. **Server creates organized folders** in `docs/journal/YYYY/MM/`
3. **Server saves markdown files** with proper formatting
4. **Server responds** with success/error status

## 🎯 Features

- **Automatic folder creation** - Creates year/month folders as needed
- **Organized filenames** - `YYYY-MM-DD-HHMM-track-name.md`
- **Rich markdown format** - Includes sections for technical notes, creative notes, etc.
- **Error handling** - Provides feedback on save success/failure
- **CORS enabled** - Works with the web UI

## 🔧 Server Details

- **Port:** 8081 (different from the static file server)
- **Endpoint:** `POST /save-entry`
- **Response:** JSON with success status and file path

## 📝 File Organization

Files are saved to:
```
docs/journal/
├── 2024/
│   ├── 01/
│   ├── 12/
│   └── ...
└── 2025/
    └── ...
```

## 🛠️ Troubleshooting

- **Port conflicts:** Change port in `journal-server.py` if 8081 is in use
- **Permission errors:** Make sure the server can write to the docs folder
- **CORS issues:** The server includes CORS headers for cross-origin requests
