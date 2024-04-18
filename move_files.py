import shutil
import os

def move_files(source_dir, destination_dir):
    # Make sure the source directory exists
    if not os.path.exists(source_dir):
        print(f"Source directory '{source_dir}' does not exist.")
        return
    
    # Make sure the destination directory exists, create it if not
    os.makedirs(destination_dir, exist_ok=True)
    
    # Get a list of all files in the source directory
    files = os.listdir(source_dir)
    
    # Move each file to the destination directory
    for file in files:
        source_file = os.path.join(source_dir, file)
        destination_file = os.path.join(destination_dir, file)
        shutil.move(source_file, destination_file)
        print(f"Moved '{source_file}' to '{destination_file}'")

# Example usage
source_directory = 'part2_cropped/wallet/wallet10/MIX/day3/left'
destination_directory = 'selected_images/wallet'

move_files(source_directory, destination_directory)
