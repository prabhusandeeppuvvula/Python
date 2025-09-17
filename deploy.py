#!/usr/bin/env python3

import subprocess
import os
import signal

# ------------------------
# Configuration
# ------------------------
GIT_REPO = "https://github.com/krishnamaram3/portfolio.git"
CLONE_DIR = os.path.expanduser("~/portfolio")
REACT_DIR = os.path.join(CLONE_DIR, "reactjs")

# ------------------------
# Step 1: Clone or pull repository
# ------------------------
if not os.path.exists(CLONE_DIR):
    print("Cloning repository...")
    subprocess.run(["git", "clone", GIT_REPO, CLONE_DIR], check=True)
else:
    print("Repository already exists, pulling latest changes...")
    subprocess.run(["git", "-C", CLONE_DIR, "pull"], check=True)

# ------------------------
# Step 2: Install dependencies
# ------------------------
print("Installing npm dependencies...")
subprocess.run(["npm", "install"], cwd=REACT_DIR, check=True)
subprocess.run(["npm", "install", "react-scripts"], cwd=REACT_DIR, check=True)

# ------------------------
# Step 3: Stop existing app if running
# ------------------------
try:
    # Kill any process using port 3000
    subprocess.run(
        "fuser -k 3000/tcp", shell=True, check=False, stdout=subprocess.DEVNULL
    )
except Exception as e:
    print(f"No existing app to stop: {e}")

# ------------------------
# Step 4: Start the app in background
# ------------------------
print("Starting React app on port 3000...")
with open("react_app.log", "a") as log_file:
    subprocess.Popen(
        ["npm", "start", "--", "--host", "0.0.0.0"],
        cwd=REACT_DIR,
        stdout=log_file,
        stderr=log_file,
        preexec_fn=os.setsid,
    )

print("App started successfully. Access it at http://localhost:3000")
