#!/usr/bin/env python3
"""
Collexa Enterprise Campus Management System
Executable Runner & Server Orchestrator
"""

import os
import sys
import subprocess
import time
import webbrowser
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

def run_system():
    print("=" * 60)
    print("  COLLEXA ENTERPRISE CAMPUS MANAGEMENT ERP")
    print("  Autonomous University Full-Stack Operations Engine")
    print("=" * 60)
    
    # 1. Seed database if not existing
    db_path = BASE_DIR / "backend" / "collexa.db"
    backend_dir = BASE_DIR / "backend"
    frontend_dir = BASE_DIR / "frontend"
    
    print("\n[1/3] Initializing Database & Verification...")
    subprocess.run([sys.executable, "-c", "import sys; sys.path.insert(0, 'backend'); import database, models, seed_data; print('✓ Database Models Verified')"], cwd=BASE_DIR)
    
    print("\n[2/3] Starting FastAPI Backend on http://127.0.0.1:8000...")
    backend_proc = subprocess.Popen(
        [sys.executable, "-m", "uvicorn", "main:app", "--host", "127.0.0.1", "--port", "8000"],
        cwd=backend_dir
    )
    
    print("\n[3/3] Starting Vite Frontend on http://127.0.0.1:5173...")
    npm_cmd = "npm.cmd" if os.name == "nt" else "npm"
    frontend_proc = subprocess.Popen(
        [npm_cmd, "run", "dev", "--", "--host", "127.0.0.1", "--port", "5173"],
        cwd=frontend_dir
    )
    
    time.sleep(2)
    print("\n✓ Collexa Enterprise ERP is live!")
    print("  - Web Application: http://127.0.0.1:5173/")
    print("  - API Documentation: http://127.0.0.1:8000/docs")
    print("  - Press Ctrl+C to terminate both servers.")
    
    try:
        backend_proc.wait()
    except KeyboardInterrupt:
        print("\nShutting down servers...")
        backend_proc.terminate()
        frontend_proc.terminate()
        print("Done.")

if __name__ == "__main__":
    run_system()
