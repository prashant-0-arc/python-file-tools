from pathlib import Path

TARGET_DIR = Path('.')
JUNK_EXTENSIONS = [".tmp", ".log"]

IGNORE_LIST = ["venv", "cleaner.py"]

def main():
    print(f"Scanning Directory: {TARGET_DIR.resolve()}")

    for item in TARGET_DIR.iterdir():
        if item.name in IGNORE_LIST or item.is_dir():
            print(f"Ignoring: {item.name}")
            continue

        if item.is_file():
            file_extension = item.suffix.lower()

        if file_extension in JUNK_EXTENSIONS:
            item.unlink()
            print(f"DELETED: {item.name}")

if __name__ == "__main__":
    main()
