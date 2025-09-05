# Intelligent Document Processing (IDP)

## Overview

The **Intelligent Document Processing (IDP)** application is a Streamlit-based web tool designed to process PDF documents by extracting text, performing keyword analysis, generating visualizations, and exporting results to a Word document. It leverages OCR (Optical Character Recognition) for scanned PDFs and direct text extraction for text-based PDFs, with additional features like sentiment analysis and word cloud generation.

## Features

- **Text Extraction**: Extracts text from PDFs using PyPDF2 for text-based PDFs or Tesseract OCR for scanned documents.
- **Export to Word**: Converts extracted text into a downloadable `.docx` file with proper formatting.
- **Keyword Analysis**: Identifies and displays the top 10 most frequent keywords (excluding stopwords).
- **Word Cloud Visualization**: Generates a word cloud to visually represent word frequency.
- **Sentiment Analysis**: Analyzes the sentiment of the extracted text using TextBlob.
- **Customizable Settings**: Allows users to choose theme colors, text extraction modes (Auto Detect, OCR Only, Text-based Only), and enable/disable keyword analysis.
- **User-Friendly Interface**: Built with Streamlit, featuring a responsive layout, sidebar for settings, and progress animations.

## Requirements

To run the IDP application, ensure the following dependencies are installed:

- Python 3.8+
- Streamlit
- PyPDF2
- pytesseract
- pdf2image
- python-docx
- nltk
- wordcloud
- matplotlib
- textblob

You also need to install **Tesseract OCR** on your system:

- For Windows: Download and install from Tesseract at UB Mannheim.
- For Linux: `sudo apt-get install tesseract-ocr`
- For macOS: `brew install tesseract`

## Installation

1. Clone this repository or download the source code.
2. Install the required Python packages:

   ```bash
   pip install streamlit PyPDF2 pytesseract pdf2image python-docx nltk wordcloud matplotlib textblob
   ```
3. Install Tesseract OCR as per your operating system (see above).
4. Download NLTK stopwords:

   ```python
   import nltk
   nltk.download("stopwords")
   ```

## Usage

1. Run the Streamlit app:

   ```bash
   streamlit run app.py
   ```
2. Open the provided URL (usually `http://localhost:8501`) in your browser.
3. Use the interface to:
   - Upload a PDF file.
   - Customize the theme color and text extraction mode via the sidebar.
   - Enable or disable keyword analysis.
   - View extracted text, keyword analysis, word cloud, and sentiment analysis results.
   - Download the extracted text as a `.docx` file.

## File Structure

- `app.py`: Main application script containing the Streamlit app logic.
- `README.md`: This file, providing an overview and setup instructions.

## How It Works

1. **File Upload**: Upload a PDF via the Streamlit file uploader.
2. **Text Extraction**:
   - **Text-based PDFs**: Uses PyPDF2 to extract text directly.
   - **Scanned PDFs**: Uses pdf2image to convert pages to images and pytesseract for OCR.
3. **Analysis**:
   - **Keyword Analysis**: Filters out stopwords and counts word frequencies using `Counter`.
   - **Word Cloud**: Generates a visual representation using the `wordcloud` library.
   - **Sentiment Analysis**: Uses TextBlob to calculate polarity and subjectivity.
4. **Export**: Saves extracted text to a `.docx` file using `python-docx`.

## Limitations

- OCR performance depends on the quality of the PDF and Tesseract installation.
- Large PDFs may take longer to process due to OCR or text extraction.
- Sentiment analysis accuracy varies based on the content and context.

## Future Improvements

- Add support for additional file formats (e.g., images, scanned documents).
- Enhance OCR accuracy with preprocessing techniques.
- Include more advanced text analysis features (e.g., named entity recognition).
- Optimize performance for large PDFs.

## Contributing

Contributions are welcome! Please submit a pull request or open an issue for bugs, feature requests, or improvements.

## License

This project is licensed under the MIT License.

mail- vaswal919@gmail.com

## Author

Developed with ❤️ by VJ