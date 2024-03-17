## Translation Tool for PDF Documents

This Python script translates text from a PDF file into a specified target language (currently set to English) and creates a new Word document (DOCX) with the translated text.

### Features

* Uses Google Cloud Translate API for translation.
* Handles both text and binary (encoded) PDF files using `PyPDF2`.
* Extracts text from each page of the PDF individually.
* Creates a new Word document with translated paragraphs using `docx`.
* Includes `html` library for unescaping HTML entities within the translated text, ensuring proper character display in the output document.
* Handles errors during translation (logging and basic exception handling).

### Requirements

* Python 3.x ([https://www.python.org/downloads/](https://www.python.org/downloads/))
* Google Cloud Translate API ([invalid URL removed])
* Required libraries:
    * `PyPDF2`: `pip install PyPDF2`
    * `docx`: `pip install docx`
    * `google-cloud-translate`: `pip install google-cloud-translate` (Follow setup instructions for Google Cloud Translate API)
    * `html`: `pip install html`

**Note:** You will need to create a Google Cloud Project and enable the Translate API before using this script.

### Usage

1. **Set Up Google Cloud Translate:**
    * Follow the instructions on [invalid URL removed] to create a project and enable the Translate API.
    * Download the service account key and place it in a secure location. 

2. **Run the Script:**
    * Open a terminal or command prompt and navigate to the directory containing the script (`translation.py`).
    * Set the `GOOGLE_APPLICATION_CREDENTIALS` environment variable to the path of your service account key file. (e.g., `export GOOGLE_APPLICATION_CREDENTIALS=/path/to/your/key.json`)
    * Run the script: `python translation.py`

**Note:** You will be prompted to enter the path to your PDF file.

### Output

A new Word document named "translated_document.docx" will be created in the same directory as the script with the translated text from the PDF.

### Contributing

Feel free to contribute to this project by creating pull requests on GitHub. 
