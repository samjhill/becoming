#!/usr/bin/env python3
"""
Start the Production Journal Server
Run this script to start the server that handles saving journal entries
"""

import os
import sys
import subprocess
from pathlib import Path

def main():
    # Get the project root directory
    project_root = Path(__file__).parent
    
    # Change to project root directory
    os.chdir(project_root)
    
    # Start the journal server
    server_script = project_root / 'src' / 'server' / 'journal-server.py'
    
    print("🎧 Starting Production Journal Server...")
    print(f"📁 Project root: {project_root}")
    print(f"📝 Server script: {server_script}")
    print("🌐 Server will be available at: http://localhost:8082")
    
    try:
        subprocess.run([sys.executable, str(server_script)], check=True)
    except KeyboardInterrupt:
        print("\n🛑 Server stopped by user")
    except Exception as e:
        print(f"❌ Error starting server: {e}")

if __name__ == '__main__':
    main()
