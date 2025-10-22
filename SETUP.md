# 🎧 Album Project Version Control Workflow (Logic Pro + Git LFS)

## 🧭 Overview

This document describes the workflow for setting up version control for a **Logic Pro album project** using **Git** and **Git LFS**.  
The goals are:
- Safe, reliable versioning of all project assets  
- Lightweight, fast commits that don’t balloon the repo  
- Flexible branching for experimentation  
- Clean organization of stems, bounces, and documentation

This system is designed for **a solo music project**, but it can scale if collaborators join later.

---

## 🗂️ 1. Project Folder Structure

```
my-album/
├── logic-projects/
│   ├── track01_may/
│   │   ├── may.logicx
│   │   └── audio/
│   ├── track02_resume/
│   └── ...
├── stems/
│   ├── track01_may/
│   │   ├── drums.wav
│   │   ├── vocals.wav
│   │   └── synths.wav
│   └── ...
├── bounces/
│   ├── rough-mixes/
│   ├── reference-mixes/
│   └── masters/
├── samples/
│   ├── one-shots/
│   └── loops/
├── docs/
│   ├── notes.md
│   ├── lyrics/
│   └── production-journal.md
├── .gitattributes
├── .gitignore
└── SETUP.md
```

- `logic-projects/` — all Logic `.logicx` sessions (untracked in Git to keep repo lean)  
- `stems/` — selected exported stems, tracked with Git LFS  
- `bounces/` — mixes and masters, optional Git LFS tracking  
- `samples/` — any custom one-shots or loops used  
- `docs/` — all text assets: lyrics, notes, plans

---

## 🧹 2. `.gitignore` Template

```gitignore
# Audio and rendered files
*.aif
*.aiff
*.wav
*.caf
*.mp3
*.m4a
*.bwf
*.rex
*.sd2
*.logicx/
*.logic/
*.waveform/

# Logic's hidden directories
*/Audio Files/
*/Freeze Files/
*/Project File Backups/
*/Alternatives/

# Bounces (ignore rough and refs)
bounces/rough-mixes/
bounces/reference-mixes/

# MacOS metadata
.DS_Store

# Ignore external drives or cache dirs
*.external
```

---

## 📦 3. Initialize Git & Git LFS

```bash
# Initialize git
git init

# Install Git LFS (if not installed)
brew install git-lfs
git lfs install

# Track large binary files
git lfs track "*.wav"
git lfs track "*.aiff"

# Commit LFS tracking config
git add .gitattributes
git commit -m "chore: add git-lfs tracking"
```

---

## 🌿 4. Branching Strategy (Creative-Friendly)

| Branch Name            | Purpose                                              |
|-------------------------|-------------------------------------------------------|
| `main`                  | Stable state of the project (finished songs / mixes)   |
| `writing`               | Early sketching, arrangement ideas                     |
| `mixing-[track-name]`   | Dedicated branch for mixing sessions                   |
| `sound-design`          | Experimental patches, synth design, drum tweaks        |
| `mastering`             | Final tweaks before release                            |

---

## 🏷️ 5. Tagging Milestones

```bash
git tag -a v0.1-track1-demo -m "Track 1 first demo"
git push origin --tags
```

Examples:
- `v0.1-track1-demo`
- `v0.5-track1-arrangement`
- `v1.0-track1-final`

---

## 🧠 6. Documentation & Creative Notes

- `docs/notes.md` — project-wide creative ideas, moods, structure  
- `docs/lyrics/` — per-song lyric drafts  
- `docs/production-journal.md` — log what happened in each session (e.g. “added arp line, didn’t like the snare, try again next time”)

---

## 🧰 7. Remote Repository (Optional)

```bash
git remote add origin git@github.com:username/my-album.git
git push -u origin main
```

- Private repo recommended
- Use for encrypted backup or future collaboration

---

## 🧼 8. Best Practices

- ✅ Commit often with meaningful messages  
- 🪶 Keep large raw audio out of Git  
- 🧪 Use branches for bold experiments  
- 🏁 Tag versions at milestones  
- 📝 Keep your docs folder alive as a creative log

---

## 🧭 9. Example Workflow

```bash
# Start new idea
git checkout -b writing-track3

# Work in Logic, bounce some stems
git add stems/track03_interview/*.wav docs/lyrics/track03.txt
git commit -m "feat: first drum + arp stem for The Waiting Room"

# Create alt version
git checkout -b sound-design-track3
git commit -am "exp: glitchy arp variation"

# Merge good ideas back
git checkout writing-track3
git merge sound-design-track3
git push origin writing-track3
```

---

## 🧭 10. Optional Enhancements

- Automate nightly backups with scripts
- Add pre-commit hook to check repo size
- Sync stems to S3 bucket for redundancy
- Link lyrics to session files in markdown

---

## 📌 Summary

- Git tracks structure, text assets, and selected stems  
- Git LFS handles large audio files  
- Logic raw projects live locally  
- Branching gives creative freedom  
- Tagging captures your musical evolution

This gives you a **professional-grade workflow** for your personal album project — future-proof, collaborative-ready, and lightweight once set up.
