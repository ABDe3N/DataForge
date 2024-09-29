import os
import re
import random
import gradio as gr
from collections import Counter
from scripts.load_files import load_files  # Module 1
from scripts.clean_filenames import clean_filenames  # Module 2
from scripts.convert_docx_to_txt import convert_docx_to_txt  # Module 3
from scripts.clean_text_data import clean_text_data  # Module 4
from scripts.process_articles import process_articles_to_jsonl  # Module 5 (from process_articles.py)

# Ensure required directories exist
os.makedirs('data/raw_data', exist_ok=True)         # For Module 1
os.makedirs('data/rejected_data', exist_ok=True)    # For Module 1
os.makedirs('data/cleanname_data', exist_ok=True)   # For Module 2
os.makedirs('data/converted_data', exist_ok=True)   # For Module 3
os.makedirs('data/clean_data', exist_ok=True)       # For Module 4
os.makedirs('data/processed_data', exist_ok=True)   # For both intermediate and final data

# Initialize a global variable to keep track of displayed patterns
displayed_patterns = set()

# ----------------------------------
# Wrapper for UI to trigger processing (Module 5)
# ----------------------------------
def process_articles_ui(word_count):
    return process_articles_to_jsonl(word_count)

# Gradio UI
with gr.Blocks() as app:
    gr.Markdown("# DataForge.v1")

    ######################################
    # Module 1: Loading Raw Data         #
    ######################################
    
    with gr.Group():
        gr.Markdown("### 1. Load Raw Data")

        # Drag and drop file uploader for raw data
        file_upload = gr.File(label="Drag and Drop Files Here", file_count="multiple")

        # Load button to trigger file processing
        load_button = gr.Button("Load Data")

        # Output textbox to display status messages (success, failure)
        status_output = gr.Textbox(label="Status", interactive=False)

        # Click action for the Load button
        load_button.click(fn=load_files, inputs=[file_upload], outputs=[status_output])

    ######################################
    # Module 2: Cleaning File Names      #
    ######################################

    with gr.Group():
        gr.Markdown("### 2. Clean File Names")

        # Checkboxes stacked vertically
        remove_numbers = gr.Checkbox(label="Remove numbers", value=True)
        remove_dots = gr.Checkbox(label="Remove dots", value=True)
        replace_underscore = gr.Checkbox(label="Replace underscores", value=True)
        replace_plus = gr.Checkbox(label="Replace plus signs", value=True)
        remove_harakat = gr.Checkbox(label="Remove Arabic harakat", value=True)
        remove_special_chars = gr.Checkbox(label="Remove special characters", value=True)
        remove_extra_spaces = gr.Checkbox(label="Remove extra spaces", value=True)

        # Clean button to apply file name cleaning
        clean_button = gr.Button("Clean File Names")

        # Output textbox to display status messages (success, failure)
        clean_output = gr.Textbox(label="Status", interactive=False)

        # Click action for the Clean button
        clean_button.click(fn=clean_filenames, inputs=[remove_numbers, remove_dots, replace_underscore, replace_plus, remove_harakat, remove_special_chars, remove_extra_spaces], outputs=[clean_output])

    ######################################
    # Module 3: Convert DOCX to TXT      #
    ######################################

    with gr.Group():
        gr.Markdown("### 3. Convert DOCX to TXT")

        # Button to trigger the conversion process
        convert_button = gr.Button("Convert to TXT")

        # Output textbox to display conversion status
        convert_output = gr.Textbox(label="Conversion Status", interactive=False)

        # Click action for the Convert button
        convert_button.click(fn=convert_docx_to_txt, inputs=[], outputs=[convert_output])

    ######################################
    # Module 4: Clean Text Data          #
    ######################################

    with gr.Group():
        gr.Markdown("### 4. Clean Text Data")

        # Checkboxes for the different cleaning options
        remove_dots = gr.Checkbox(label="Remove dots", value=True)
        remove_harakat = gr.Checkbox(label="Remove Arabic harakat", value=True)
        remove_special_chars = gr.Checkbox(label="Remove special characters", value=True)
        remove_extra_spaces = gr.Checkbox(label="Remove extra spaces", value=True)
        remove_links = gr.Checkbox(label="Remove links", value=True)

        # Clean button to apply text cleaning
        clean_text_button = gr.Button("Clean Text Data")
        clean_text_output = gr.Textbox(label="Cleaning Status", interactive=False)

        # Click action for the Clean Text button
        clean_text_button.click(fn=clean_text_data, inputs=[
            remove_dots, remove_harakat, remove_special_chars, remove_extra_spaces, 
            remove_links
        ], outputs=[clean_text_output])

    ######################################
    # Module 5: LLaMA and Qwen Data Preparation #
    ######################################
    with gr.Group():
        gr.Markdown("### 5. Prepare Dataset for LLaMA or Qwen")

        process_button = gr.Button("Process Articles")
        process_output = gr.Textbox(label="Process Status", interactive=False)
        
        # Click action to process the articles and generate the JSONL dataset
        process_button.click(fn=process_articles_to_jsonl, inputs=[], outputs=[process_output])

# Launch the Gradio app
app.launch()