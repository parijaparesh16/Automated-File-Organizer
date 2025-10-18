import os
import shutil
from pathlib import Path

# Define file type categories
FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".pptx", ".xlsx", ".csv"],
    "Videos": [".mp4", ".mov", ".avi", ".mkv", ".flv"],
    "Music": [".mp3", ".wav", ".aac", ".flac", ".ogg"],
    "Archives": [".zip", ".rar", ".tar", ".gz", ".7z"],
    "Programs": [".exe", ".msi", ".bat", ".sh", ".apk"],
    "Code": [".py", ".js", ".html", ".css", ".cpp", ".java", ".c", ".php", ".ts"]
}

def organize_files(folder_path):
    folder = Path(folder_path)
    if not folder.exists():
        print("The specified folder does not exist.")
        return

    for file in folder.iterdir():
        if file.is_file():
            ext = file.suffix.lower()
            moved = False
            for category, extensions in FILE_TYPES.items():
                if ext in extensions:
                    target_dir = folder / category
                    target_dir.mkdir(exist_ok=True)
                    shutil.move(str(file), str(target_dir / file.name))
                    moved = True
                    break
            if not moved:
                other_dir = folder / "Others"
                other_dir.mkdir(exist_ok=True)
                shutil.move(str(file), str(other_dir / file.name))
    print("✅ Files organized successfully!")

if __name__ == "_main_":
    path = input("Enter the folder path to organize: ").strip()
    organize_files(path)