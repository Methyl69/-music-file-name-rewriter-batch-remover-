import os


def remove_first_n_characters_from_filenames(directory, n):
    for filename in os.listdir(directory):
        # Process only .mp3 files
        if filename.endswith('.mp3') or filename.endswith('.m4a'):
            # New filename with the first n characters removed
            new_filename = filename[n:].strip()
            # Get full paths
            old_file_path = os.path.join(directory, filename)
            new_file_path = os.path.join(directory, new_filename)

            # Rename the file
            os.rename(old_file_path, new_file_path)
            print(f"Renamed: {filename} -> {new_filename}")


# Directory containing the mp3 files
directory_path = r'C:\Users\User\Downloads\rivals' #enter file location here
characters_to_remove = 5  # Number of characters to remove from the start

remove_first_n_characters_from_filenames(directory_path, characters_to_remove)
