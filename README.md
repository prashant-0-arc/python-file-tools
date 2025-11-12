# Python File Automation Tools

This repository contains a simple but powerful command-line script to automate file management.

##  Smart File Organizer (`organizer.py`)

A script that organizes any target directory by moving files into categorized subfolders.

### Features
* Scans a user-provided directory from the command line.
* Sorts files based on their extensions (e.g., `.png` -> `IMAGES/`, `.pdf` -> `DOCUMENTS/`).
* Creates category folders if they don't already exist.
* Moves all uncategorized files into an `OTHER/` folder.

### Tech Used
* Python
* `pathlib` library for modern file system manipulation.
* `argparse` library to accept command-line arguments.

### How to Run
```bash
# Example: Organize your 'Downloads' folder
python organizer.py C:\Users\YourName\Downloads
