# DataForge: Fine-Tuning Data Processing Framework for LLaMA, Qwen, and More
DataForge is a Gradio-based tool designed to assist in processing and preparing text data for fine-tuning large language models (LLMs) such as LLaMA, Qwen, and other transformer models. It simplifies the often complex tasks of loading raw text data, cleaning and formatting it, and finally generating a dataset ready for tokenization and fine-tuning.


## Key Features :
Drag-and-Drop Interface: Easily load .docx, .txt, and .odt files for processing.
Data Cleaning: Automatic removal of duplicates and unnecessary characters or spaces.
Customizable Filename Cleaning: Configure how file names are cleaned and organized.
File Conversion: Convert your files to .txt format, making them compatible with most LLM fine-tuning tools.
JSONL Generation: Automatically processes text into LLaMA-compatible JSONL format for multi-turn conversations or other structured formats.
Stage-wise Processing: Every task has its own output folder, providing you with better version control and understanding of the workflow.


## Target Audience :
AI Researchers: Those who want to fine-tune large language models on custom datasets.
Machine Learning Engineers: Developers who need a streamlined process for cleaning and preparing data for models.
Data Scientists: Individuals dealing with text-heavy datasets looking for efficient data cleaning and conversion pipelines.


## Installation Instructions : 

### Step 1: Clone DataForge Repository

```
git clone https://github.com/yourusername/DataForge.git
```

### Step 2: Set up Virtual Environment (Recommended)

```
python -m venv env
source env/bin/activate  # For Windows: env\Scripts\activate
```

### Step 3: Install Dependencies
```
pip install -r requirements.txt
```

If requirements.txt is not available, manually install dependencies:

```
pip install gradio docx2txt datasets torch accelerate
```

## Usage Instructions :

### Step 1: Start the Gradio Interface
Once everything is installed, you can start DataForge’s Gradio UI with the following command:

```
env\Scripts\activate
python dataforge_ui.py
```

This will open up a local web interface where you can start uploading your files for processing.

### Step 2: Load Data
Drag and drop .docx, .txt, or .odt files into the interface to upload them. DataForge supports bulk uploads and will handle each file individually.

### Step 3: Removing Duplicates
After loading the data, you can proceed to remove duplicate entries from the dataset. DataForge will show you how many duplicates were found and removed.

### Step 4: Clean File Names
You can define how the file names should be cleaned. Options include removing numbers, punctuation, and replacing spaces with underscores.

### Step 5: Convert to Text
Convert all uploaded files into .txt format. This is useful for models that require plain text data as input.

### Step 6: Clean Text Data
The text cleaning step allows you to remove extra spaces, special characters, and ensure consistent formatting throughout the document.

### Step 7: Prepare JSONL for LLaMA Fine-tuning
Once the text is clean and ready, DataForge will automatically format your dataset into JSONL format, compatible with models like LLaMA. The structure of the JSONL will typically follow this format:


## Supported Models :
LLaMA: DataForge is optimized for fine-tuning LLaMA models (2B, 3B, and higher) but is adaptable for other LLMs.
Qwen: Support for tokenization and dataset preparation for Qwen fine-tuning.
HuggingFace Models: Output JSONL format and cleaned datasets are compatible with HuggingFace’s training pipelines.


## Customization :
You can customize the scripts in the scripts/ folder according to your needs.


## File Compatibility :
Ensure that your input files are .docx, .txt, or .odt formats. Unsupported formats may not be processed correctly.


## Contributing  :
We welcome contributions! Make Changes: Implement new features or fix bugs.


## License :
DataForge is licensed under the MIT License. You are free to use, modify, and distribute it as per the terms of the license.


