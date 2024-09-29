import os
import shutil
import json

def process_articles_to_jsonl():
    """Processes text articles into ShareGPT-style JSONL format and copies them to the processed_data directory."""
    
    articles = []
    input_directory = "data/clean_data"
    processed_data_dir = "data/processed_data"  # Single directory for both intermediate and final data
    
    # Ensure the processed_data directory exists
    os.makedirs(processed_data_dir, exist_ok=True)
    
    # Iterate through files in the input directory
    for filename in os.listdir(input_directory):
        if filename.endswith(".txt"):
            file_path = os.path.join(input_directory, filename)
            
            # Copy the file to processed_data directory
            shutil.copy(file_path, processed_data_dir)
            print(f"Copied {filename} to {processed_data_dir}")
            
            # Read the content of the file
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read().strip()
            
            # Extract title as user input (assuming the title is the file name minus extension)
            title = os.path.splitext(filename)[0]
            
            # Create a ShareGPT-like structure for the conversation
            article = {
                'conversations': [
                    {'from': 'human', 'value': f'اكتب حلقة كاملة عن "{title}"'},
                    {'from': 'gpt', 'value': content}  # Use the full content from the text file
                ]
            }
            
            articles.append(article)
    
    # Define the output file path
    output_file = os.path.join(processed_data_dir, "finetune_data.jsonl")

    # Write the articles to a JSONL file
    with open(output_file, 'w', encoding='utf-8') as jsonl_file:
        for article in articles:
            jsonl_file.write(json.dumps(article, ensure_ascii=False) + '\n')
    
    print(f"Processed {len(articles)} articles into {output_file}")
    return f"Processed {len(articles)} articles and saved to {output_file}"
