import os
import re

def clean_text_data(remove_dots, remove_harakat, remove_special_chars, remove_extra_spaces, remove_links):
    """
    Cleans the content of .txt files in the converted_data directory and saves them in the clean_data directory,
    while preserving line breaks and removing empty lines. Pattern removal is skipped.
    """
    converted_data_dir = "data/converted_data"
    clean_data_dir = "data/clean_data"
    
    # Ensure the output directory exists
    os.makedirs(clean_data_dir, exist_ok=True)

    def remove_arabic_harakat(text):
        arabic_harakat = re.compile(r'[\u0610-\u061A\u064B-\u065F]')
        return arabic_harakat.sub('', text)

    cleaned_files = []

    # Iterate over the .txt files in the converted_data directory
    for filename in os.listdir(converted_data_dir):
        if filename.endswith(".txt"):
            txt_path = os.path.join(converted_data_dir, filename)
            cleaned_path = os.path.join(clean_data_dir, filename)

            try:
                # Read the original text line by line to preserve line breaks
                with open(txt_path, 'r', encoding='utf-8') as file:
                    lines = file.readlines()

                cleaned_lines = []

                # Apply cleaning to each line while preserving line breaks
                for line in lines:
                    line = line.strip()

                    # Remove empty lines (whitespace-only lines)
                    if not line:
                        continue
                    
                    # Remove links
                    if remove_links and re.search(r'http[s]?://\S+', line):
                        continue  # Skip this line if it contains a link

                    # Remove dots
                    if remove_dots:
                        line = line.replace('.', '')

                    # Remove Arabic harakat
                    if remove_harakat:
                        line = remove_arabic_harakat(line)

                    # Remove special characters (non-alphanumeric)
                    if remove_special_chars:
                        line = re.sub(r'[^\w\s]', '', line)

                    # Remove extra spaces, but preserve existing line breaks
                    if remove_extra_spaces:
                        line = ' '.join(line.split())

                    # Append cleaned line (keeping the line break)
                    cleaned_lines.append(line + '\n')

                # Write the cleaned lines to the clean_data directory, preserving line breaks
                with open(cleaned_path, 'w', encoding='utf-8') as cleaned_file:
                    cleaned_file.writelines(cleaned_lines)

                cleaned_files.append(filename)

            except Exception as e:
                print(f"Error cleaning {filename}: {e}")

    return f"Cleaned {len(cleaned_files)} text files."
