import os
import shutil

def organize_files(directory_path):
    """Organizes files in the given directory by their extension.

    Args:
        directory_path (str): The path to the directory to organize.
    """
    if not os.path.exists(directory_path):
        print("Directory does not exist.")
        return

    for filename in os.listdir(directory_path):
        filepath = os.path.join(directory_path, filename)

        # Skip directories, only process files
        if os.path.isfile(filepath):
            file_ext = filename.split('.')[-1] if '.' in filename else 'no_extension'
            folder_name = f"{file_ext}_files"
            folder_path = os.path.join(directory_path, folder_name)

            if not os.path.exists(folder_path):
                os.makedirs(folder_path)

            shutil.move(filepath, os.path.join(folder_path, filename))
            print(f"Moved: {filename} -> {folder_name}/")

def main():
    """Main entry point for File Organizer."""
    print("--- Simple File Organizer ---")
    path = input("Enter the directory path to organize (e.g., ./test_folder): ").strip()
    if path:
        organize_files(path)
    else:
        print("Path cannot be empty.")

if __name__ == '__main__':
    main()