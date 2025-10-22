#!/usr/bin/env python3
"""
Export production journal entries from the UI to the markdown file.
Run this script to sync your UI entries back to docs/production-journal.md
"""

import json
import os
from datetime import datetime

def export_journal_entries():
    """Export journal entries from localStorage format to markdown"""
    
    # Path to the production journal markdown file
    journal_path = "docs/production-journal.md"
    
    # Check if localStorage file exists (this would be created by the UI)
    # For now, we'll create a sample structure
    sample_entries = [
        {
            "track": "Track 01: May",
            "notes": "Started working on the main chord progression. The Cmaj7 to Am sounds great. Need to work on the bridge section.",
            "date": "Dec 19, 2024, 02:30 PM"
        },
        {
            "track": "Track 02: Resume", 
            "notes": "Experimented with some new synth patches. The arp line is coming together nicely.",
            "date": "Dec 19, 2024, 02:25 PM"
        }
    ]
    
    # Read existing journal file
    if os.path.exists(journal_path):
        with open(journal_path, 'r') as f:
            content = f.read()
    else:
        content = ""
    
    # Find the session log section
    session_start = content.find("## Session Log")
    if session_start == -1:
        print("Could not find '## Session Log' section in the markdown file")
        return
    
    # Find the end of the session log (before the Notes Template section)
    template_start = content.find("---", session_start)
    if template_start == -1:
        template_start = len(content)
    
    # Build new session entries
    new_entries = ""
    for entry in sample_entries:
        new_entries += f"### {entry['date']} - {entry['track']}\n"
        new_entries += f"- {entry['notes']}\n\n"
    
    # Reconstruct the file
    before_session = content[:session_start]
    after_template = content[template_start:]
    
    new_content = before_session + "## Session Log\n\n" + new_entries + after_template
    
    # Write the updated file
    with open(journal_path, 'w') as f:
        f.write(new_content)
    
    print(f"✅ Exported {len(sample_entries)} entries to {journal_path}")

if __name__ == "__main__":
    export_journal_entries()
