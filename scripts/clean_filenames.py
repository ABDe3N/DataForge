import os
import re
import shutil

def clean_filenames(remove_numbers, remove_dots, replace_underscore, replace_plus, remove_harakat, remove_special_chars, remove_extra_spaces):
    """
    Cleans file names based on the selected options and saves them in the cleanname_data directory.
    This version removes all numbers.
    """
    raw_data_dir = "data/raw_data"
    cleanname_data_dir = "data/cleanname_data"
    
    os.makedirs(cleanname_data_dir, exist_ok=True)

    def remove_arabic_harakat(text):
        # Arabic harakat Unicode range
        arabic_harakat = re.compile(r'[\u0610-\u061A\u064B-\u065F]')
        return arabic_harakat.sub('', text)

    cleaned_files = []

    # Iterate over the files in raw_data
    for filename in os.listdir(raw_data_dir):
        name, ext = os.path.splitext(filename)  # Split the file name and extension
        new_filename = name  # Apply changes to the name part only

        # Option 1: Remove all numbers
        if remove_numbers:
            new_filename = re.sub(r'\d+', '', new_filename)

        # Option 2: Remove dots (but not in the extension)
        if remove_dots:
            new_filename = new_filename.replace('.', '')

        # Option 3: Replace underscores with spaces
        if replace_underscore:
            new_filename = new_filename.replace('_', ' ')

        # Option 4: Replace plus signs with spaces
        if replace_plus:
            new_filename = new_filename.replace('+', ' ')

        # Option 5: Remove Arabic harakat
        if remove_harakat:
            new_filename = remove_arabic_harakat(new_filename)

        # Option 6: Remove special characters (non-alphanumeric)
        if remove_special_chars:
            new_filename = re.sub(r'[^\w\s]', '', new_filename)

        # Option 7: Remove extra spaces
        if remove_extra_spaces:
            new_filename = ' '.join(new_filename.split())

        # Reattach the extension and save the cleaned file name
        final_filename = f"{new_filename}{ext}"
        shutil.copy(os.path.join(raw_data_dir, filename), os.path.join(cleanname_data_dir, final_filename))
        cleaned_files.append(final_filename)

    return f"Cleaned {len(cleaned_files)} files."
