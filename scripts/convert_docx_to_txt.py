import os
import docx

def convert_docx_to_txt():
    """
    Converts all .docx files in the cleanname_data directory to .txt format
    and saves them in the converted_data directory.
    """
    cleanname_data_dir = "data/cleanname_data"
    converted_data_dir = "data/converted_data"
    
    # Ensure the converted_data directory exists
    os.makedirs(converted_data_dir, exist_ok=True)

    converted_files = []

    # Iterate over the .docx files in cleanname_data
    for filename in os.listdir(cleanname_data_dir):
        if filename.endswith(".docx"):
            docx_path = os.path.join(cleanname_data_dir, filename)
            txt_filename = os.path.splitext(filename)[0] + ".txt"
            txt_path = os.path.join(converted_data_dir, txt_filename)

            try:
                # Read the docx file
                doc = docx.Document(docx_path)
                full_text = [para.text for para in doc.paragraphs]

                # Write the full text to a .txt file
                with open(txt_path, 'w', encoding='utf-8') as txt_file:
                    txt_file.write("\n".join(full_text))

                converted_files.append(txt_filename)
            except Exception as e:
                print(f"Error converting {filename}: {e}")

    return f"Converted {len(converted_files)} files to .txt format."
