#!/usr/bin/env python3

import subprocess
import os

# ------------------------
# Configuration
# ------------------------
GIT_REPO = "https://github.com/<USERNAME>/Terraform.git"
CLONE_DIR = os.path.expanduser("~/portfolio")

# ------------------------
# Step 1: Clone repository
# ------------------------
if not os.path.exists(CLONE_DIR):
    print("Cloning repository...")
    subprocess.run(["git", "clone", GIT_REPO, CLONE_DIR])
else:
    print("Repository already exists, pulling latest changes...")
    subprocess.run(["git", "-C", CLONE_DIR, "pull"])

# ------------------------
# Step 2: Install dependencies
# ------------------------
REACT_DIR = os.path.join(CLONE_DIR, "reactjs")
print("Installing npm dependencies...")
subprocess.run(["npm", "install"], cwd=REACT_DIR)
subprocess.run(["npm", "install", "react-scripts"], cwd=REACT_DIR)

# ------------------------
# Step 3: Start the app
# ------------------------
print("Starting React app on port 3000...")
subprocess.run(["nohup", "npm", "start", "&"], cwd=REACT_DIR)
