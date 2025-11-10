from pathlib import Path
import argparse # We're importing a new library!

# --- CONFIGURATION ---
# We moved the main config into the 'main' function
# because it's better practice.
CATEGORIES = {
    "DOCUMENTS": ['.pdf', '.txt', '.doc', '.docx'],
    "IMAGES":    ['.jpg', '.jpeg', '.png', '.gif'],
    "MUSIC":     ['.mp3', '.wav'],
    "VIDEO":     ['.mp4', '.mov', '.avi'],
    "ARCHIVES":  ['.zip', '.rar', '.gz']
}

# We can find our *own* script's name automatically!
SCRIPT_NAME = Path(__file__).name 
# ---------------------

def organize_directory(target_dir):
    """
    Scans a target directory and organizes all files into
    category subfolders.
    """
    print(f"Scanning directory: {target_dir.resolve()}")

    # We add our script and cleaner to the ignore list
    ignore_list = [SCRIPT_NAME, 'cleaner.py', 'venv']

    # We loop over every item in the folder
    for item in target_dir.iterdir():
        
        # Ignore items in our list or that are folders
        if item.name in ignore_list or item.is_dir():
            print(f"Ignoring: {item.name}")
            continue

        # --- This is all your code from before! ---
        if item.is_file():
            file_extension = item.suffix.lower()
            
            target_folder = None
            for category_name, extensions in CATEGORIES.items():
                if file_extension in extensions:
                    target_folder = target_dir / category_name
                    break
            
            if target_folder is None:
                target_folder = target_dir / "OTHER"
            
            target_folder.mkdir(exist_ok=True)
            
            new_path = target_folder / item.name
            
            item.rename(new_path)
            
            print(f"Moved: '{item.name}' --> {target_folder.name}/")
    
    print("Organization complete!")

# This is the standard "main" function structure
def main():
    # --- THIS IS THE NEW PART ---
    # 1. Create the parser object
    parser = argparse.ArgumentParser(
        description="A script to organize a directory by file type."
    )
    
    # 2. Add the argument we want to accept
    parser.add_argument(
        "target_directory", # The name of the argument
        type=Path,          # The type (we want it as a Path object!)
        help="The directory to scan and organize."
    )
    
    # 3. "Parse" (read) the arguments from the command line
    args = parser.parse_args()
    
    # 4. Use the argument!
    # If the user gives a bad path, this will tell them.
    if not args.target_directory.is_dir():
        print(f"Error: '{args.target_directory}' is not a valid directory.")
        return # Exit the script
        
    # If the path is good, call our main function!
    organize_directory(args.target_directory)

# This line tells Python to run the main() function
if __name__ == "__main__":
    main()