# translation
A simple python script that uses Google's Cloud Translation API to translate a PDF document from any supported language to English and export it to a Word doc

**Requirements:**
This script uses Google's Cloud Translation API.  As a result, you'll need to have that setup and functiong before you can use the script.  You will need:
- A Google Cloud Project
- Google's CLI
- A working API key (recommend you limit access to only the Translation API as it is a paid service after 500,000 characters)

Additionally, you'll need a few python modules:
- html
- PyPDF2
- docx

**Virtualenv**
Given the various requirements for setting all of this up, it's highly recommended you use a python virtual environment: https://python.land/virtual-environments/virtualenv
