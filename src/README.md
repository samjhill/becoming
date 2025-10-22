# Becoming Album - Source Code

This folder contains the source code and utilities for the Becoming album project.

## 📁 Structure

### `ui/`
Web interfaces and tools for music production workflow.

- **`journal-ui.html`** - Production journal interface for logging session notes

### `scripts/`
Python utilities for project management and automation.

- **`export-journal.py`** - Export journal entries to markdown format

## 🚀 Usage

### Production Journal UI
1. Open `index.html` in your browser or navigate to `src/ui/journal-ui.html`
2. Add session notes while working on music
3. Entries are automatically exported to markdown format
4. Download the complete journal or copy individual entries

### Scripts
Run Python scripts from the project root:
```bash
python3 src/scripts/export-journal.py
```

## 🛠️ Development

The UI is designed to be:
- **Minimal & distraction-free** - Won't interfere with creative flow
- **Auto-exporting** - Automatically generates markdown files
- **Keyboard-friendly** - Supports shortcuts for quick entry
- **Mobile-responsive** - Works on tablets for studio use

## 📝 Integration

The production journal integrates with your Git workflow:
- Entries can be copied directly into `docs/production-journal.md`
- Exported files can be committed to version control
- Maintains creative process documentation alongside code
