import os
import shutil
import subprocess
import sys
from datetime import datetime

# Check if 'wget' library is installed, and install it if not
try:
    import wget
except ImportError:
    print("'wget' library is not installed. Installing now...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "wget"])
    import wget

# Function to check if the file exists
def check_file_exists(file_path):
    return os.path.exists(file_path)

# Function to create a backup of a file
def create_backup(file_path):
    try:
        if check_file_exists(file_path):
            # Get the current timestamp for the backup file name
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            backup_file = f"{file_path}.backup_{timestamp}"
            shutil.copy(file_path, backup_file)
            print(f"Backup created successfully: {backup_file}")
            return backup_file
        else:
            print(f"File {file_path} does not exist. No backup created.")
            return None
    except Exception as e:
        print(f"Failed to create backup: {e}")
        return None

# Function to download the file using wget
def download_file(url, file_name):
    os.system(f"wget {url} -O {file_name}")

# Function to move the file to the destination folder
def move_file(source, destination):
    try:
        shutil.move(source, destination)
        print(f"File successfully moved to {destination}")
    except FileNotFoundError:
        print("Source or destination not found. Please check the paths.")
    except PermissionError:
        print("Permissions denied to move the file.")

# Ask the user for their choice
user_choice = input("Choose: magisk, ksu, playintegrityfix, lsposed, adaway, fdroid, newpipe:   ")

# Lsposed
if user_choice == "lsposed":
    url = "https://github.com/LSPosed/LSPosed/releases/download/v1.9.2/LSPosed-v1.9.2-7024-zygisk-release.zip"
    file_name = "LSPosed-v1.9.2-7024-zygisk-release.zip"

    # Create a backup if the file already exists
    if check_file_exists(file_name):
        create_backup(file_name)

    download_file(url, file_name)

    if check_file_exists(file_name):
        print("#### LSPosed downloaded successfully####")
        source = file_name
        destination = "/storage/emulated/0/Download/"
        move_file(source, destination)
    else:
        print("Failed to download LSPosed. Please try again later.")

# Magisk
elif user_choice == "magisk":
    url = "https://github.com/topjohnwu/Magisk/releases/download/v28.1/Magisk-v28.1.apk"
    file_name = "Magisk-v28.1.apk"

    # Create a backup if the file already exists
    if check_file_exists(file_name):
        create_backup(file_name)

    download_file(url, file_name)

    if check_file_exists(file_name):
        print("#### Magisk downloaded successfully####")
        source = file_name
        destination = "/storage/emulated/0/Download/"
        move_file(source, destination)
    else:
        print("Failed to download Magisk. Please try again later.")

# Play Integrity Fix
elif user_choice == "playintegrityfix":
    url = "https://github.com/chiteroman/PlayIntegrityFix/releases/download/v18.2/PlayIntegrityFix_v18.2.zip"
    file_name = "PlayIntegrityFix_v18.2.zip"

    # Create a backup if the file already exists
    if check_file_exists(file_name):
        create_backup(file_name)

    download_file(url, file_name)

    if check_file_exists(file_name):
        print("#### Play Integrity Fix downloaded successfully####")
        source = file_name
        destination = "/storage/emulated/0/Download/"
        move_file(source, destination)
    else:
        print("Failed to download Play Integrity Fix. Please try again later.")

# KernelSU
elif user_choice == "ksu":
    url = "https://github.com/tiann/KernelSU/releases/download/v0.6.9/KernelSU_v0.6.9_11991-release.zip"
    file_name = "KernelSU_v0.6.9_11991-release.zip"

    # Create a backup if the file already exists
    if check_file_exists(file_name):
        create_backup(file_name)

    download_file(url, file_name)

    if check_file_exists(file_name):
        print("#### KernelSU downloaded successfully####")
        source = file_name
        destination = "/storage/emulated/0/Download/"
        move_file(source, destination)
    else:
        print("Failed to download KernelSU. Please try again later.")

# AdAway
elif user_choice == "adaway":
    url = "https://github.com/AdAway/AdAway/releases/download/v6.1.4/AdAway-6.1.4-20241027.apk"
    file_name = "AdAway-6.1.4-20241027.apk"

    # Create a backup if the file already exists
    if check_file_exists(file_name):
        create_backup(file_name)

    download_file(url, file_name)

    if check_file_exists(file_name):
        print("#### AdAway downloaded successfully####")
        source = file_name
        destination = "/storage/emulated/0/Download/"
        move_file(source, destination)
    else:
        print("Failed to download AdAway. Please try again later.")

# F-Droid
elif user_choice == "fdroid":
    url = "https://f-droid.org/F-Droid.apk"
    file_name = "F-Droid.apk"

    # Create a backup if the file already exists
    if check_file_exists(file_name):
        create_backup(file_name)

    download_file(url, file_name)

    if check_file_exists(file_name):
        print("#### F-Droid downloaded successfully####")
        source = file_name
        destination = "/storage/emulated/0/Download/"
        move_file(source, destination)
    else:
        print("Failed to download F-Droid. Please try again later.")

# NewPipe
elif user_choice == "newpipe":
    url = "https://github.com/TeamNewPipe/NewPipe/releases/download/v0.25.1/NewPipe_v0.25.1.apk"
    file_name = "NewPipe_v0.25.1.apk"

    # Create a backup if the file already exists
    if check_file_exists(file_name):
        create_backup(file_name)

    download_file(url, file_name)

    if check_file_exists(file_name):
        print("#### NewPipe downloaded successfully####")
        source = file_name
        destination = "/storage/emulated/0/Download/"
        move_file(source, destination)
    else:
        print("Failed to download NewPipe. Please try again later.")

else:
    print("Invalid choice. Please choose either magisk, ksu, playintegrityfix, lsposed, adaway, fdroid, or newpipe.")
    exit(1)
