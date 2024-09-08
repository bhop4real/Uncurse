import os


def find_root_directory(start_dir):
    current_dir = os.path.abspath(start_dir)

    while current_dir != os.path.dirname(current_dir):  # While not at the root of the filesystem
        if ".root" in os.listdir(current_dir):
            return current_dir
        current_dir = os.path.dirname(current_dir)  # Move up one directory
    return None  # `.root` not found
