import os
import shutil

def load_files(files):
    """
    Loads files and copies them to the raw_data directory.
    All files are accepted, and no duplicate checking is done in this step.
    """
    accepted_formats = [".docx", ".odt"]
    raw_data_dir = "data/raw_data"
    rejected_data_dir = "data/rejected_data"

    # Ensure the raw_data and rejected_data directories exist; if not, create them
    os.makedirs(raw_data_dir, exist_ok=True)
    os.makedirs(rejected_data_dir, exist_ok=True)

    loaded_files = []
    accepted_files = []
    rejected_files = []

    # Process each uploaded file
    for file in files:
        # Extract file extension
        file_ext = os.path.splitext(file.name)[1].lower()

        # Construct file paths
        filename = os.path.basename(file.name)
        raw_file_path = os.path.join(raw_data_dir, filename)
        rejected_file_path = os.path.join(rejected_data_dir, filename)

        try:
            # Accept only .docx and .odt files, move to raw_data
            if file_ext in accepted_formats:
                shutil.copy(file.name, raw_file_path)  # Safely copy to raw_data
                accepted_files.append(file.name)
            else:
                # Move rejected files to rejected_data
                shutil.copy(file.name, rejected_file_path)  # Safely copy to rejected_data
                rejected_files.append(file.name)

            loaded_files.append(file.name)
        except Exception as e:
            print(f"Error processing file {file.name}: {e}")
            rejected_files.append(file.name)

    # Count the number of files in the raw_data folder (unique files)
    unique_files_count = len(os.listdir(raw_data_dir))

    # Generate result message in the correct order: Total > Rejected > Accepted > Unique
    result_msg = (f"Total Files: {len(loaded_files)} | Rejected: {len(rejected_files)} | "
                  f"Accepted: {len(accepted_files)} | Unique: {unique_files_count}")
    
    return result_msg
