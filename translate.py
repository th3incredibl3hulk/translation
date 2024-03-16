def translate_text(target_language: str, text: str) -> str:
  """Translates text into the target language using Google Cloud Translate API.

  Args:
      target_language: The language code (e.g., 'en' for English) to translate to.
      text: The text to translate.

  Returns:
      The translated text with unescaped characters.

  Raises:
      Exception: If an error occurs during translation.
  """
  from html import unescape  # Import for unescape function
  from google.cloud import translate_v2 as translate  # Import for translation

  translate_client = translate.Client()

  try:
    # Translate the text with proper encoding handling
    if isinstance(text, bytes):
      text = text.decode("utf-8")
    translation_result = translate_client.translate(text, target_language=target_language)
    translated_text = translation_result["translatedText"]

    # Unescape HTML entities after translation
    return unescape(translated_text)
  except Exception as e:
    raise Exception(f"Translation error: {e}")
  
def get_pdf_path():
  """Prompts the user for the PDF file path and returns it.

  Returns:
      str: The path to the PDF file entered by the user.
  """
  while True:
    pdf_path = input("Enter the path to the PDF file: ")
    if pdf_path:  # Check if user entered a path
      return pdf_path
    else:
      print("Please enter a valid path to the PDF file.")

# Define paths and language code

pdf_path = get_pdf_path()  # Call the function to get the user-provided path
output_docx = "translated_document.docx"
target_language = "en"  # Replace with your desired language code (e.g., 'es' for Spanish)

import PyPDF2
from docx import Document


def extract_text_from_pdf(pdf_path):
  """Extracts text from a PDF file one page at a time.

  Args:
      pdf_path: The path to the PDF file.

  Returns:
      A generator that yields the extracted text from each page.
  """
  with open(pdf_path, 'rb') as pdf_file:
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    for page_num in range(len(pdf_reader.pages)):
      page = pdf_reader.pages[page_num]
      yield page.extract_text()  # Yield text for each page


def translate_and_create_docx(pdf_path, output_docx, target_language):
  """Translates extracted text from a PDF (page by page) and creates a Word document.

  Args:
      pdf_path: The path to the PDF file.
      output_docx: The path to save the translated Word document.
      target_language: The language code to translate to.
  """
  document = Document()

  for page_text in extract_text_from_pdf(pdf_path):
    try:
      # Translate each page's text using the translate_text function
      translated_text = translate_text(target_language, page_text)
      paragraph = document.add_paragraph(translated_text)
    except Exception as e:
      print(f"Error translating page: {e}")  # Log or handle errors

  document.save(output_docx)
  print("Translation and Word document creation complete!")


# Call the main function
translate_and_create_docx(pdf_path, output_docx, target_language)
