import os
import shutil
import subprocess
import sys

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
        print(" permissions denied to move the file.")


# Ask the user for their choice
user_choice = input("Choose: magisk , ksu , playintegrityfix , lsposed:   ")

#Lsposed
if user_choice == "lsposed":
    url = "https://github.com/LSPosed/LSPosed/releases/download/v1.9.2/LSPosed-v1.9.2-7024-zygisk-release.zip"
    file_name = "LSPosed-v1.9.2-7024-zygisk-release.zip"
    download_file(url, file_name)

    if check_file_exists(file_name):
        print("#### LSPosed downloaded successfully####")
        source = file_name
        destination = "/storage/emulated/0/Download/"
        move_file(source, destination)
    else:
        print("Failed to download LSPosed. Please try again later.")

#Magisk
elif user_choice == "magisk":
    url = "https://github.com/topjohnwu/Magisk/releases/download/v28.1/Magisk-v28.1.apk"
    file_name = "Magisk-v28.1.apk"
    download_file(url, file_name)

    if check_file_exists(file_name):
        print("#### Magisk downloaded successfully####")
        source = file_name
        destination = "/storage/emulated/0/Download/"
        move_file(source, destination)
    else:
        print("Failed to download Magisk. Please try again later.")

#playintegrityfix
if user_choice =="playintegrityfix":
    url="https://github.com/chiteroman/PlayIntegrityFix/releases/download/v18.2/PlayIntegrityFix_v18.2.zip"
    file_name="PlayIntegrityFix_v18.2.zip"
    download_file(url, file_name)

    if check_file_exists(file_name):
       print("##### PlayIntegrityFix_v18.2.zip Downloaded#####")
       source=file_name
       destination="/storage/emulated/0/Download/"
       move_file(source, destination)
    else:
       print("Failed to download Magisk. Please try again later")

#ksu
if user_choice =="ksu":
  url="https://github.com/backslashxx/KernelSU/releases/download>
  file_name="KernelSU_v1.0.2-6_11991-magic-release.apk"
  download_file(url, file_name)

  if check_file_exists(file_name):
     print("###### kernel su downloaded#####")
     source=file_name
     destination="/storage/emulated/0/Download/"
     move_file(source, destination)
  else:
     print("Failed to download ksu. Please try again later")
else:
    print("Invalid choice. Please choose either magisk or lsposed or playintegrityfix")
    exit(1)
