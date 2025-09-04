Intelligent Document Processing (IDP)
 
Overview
Intelligent Document Processing (IDP) is a Streamlit-based web application designed for extracting text from PDF files, analyzing content, and exporting results to Microsoft Word. It supports both direct text extraction and Optical Character Recognition (OCR) for scanned documents, providing features like keyword analysis, sentiment analysis, and word cloud visualization.
Features

PDF Text Extraction: Extract text directly from PDFs or use OCR for scanned documents.
Export to Word: Convert extracted text into a downloadable .docx file.
Keyword Analysis: Identify and display the top 10 most frequent keywords (excluding stopwords).
Word Cloud Visualization: Generate a visual word cloud from extracted text.
Sentiment Analysis: Analyze the sentiment (polarity and subjectivity) of the extracted text.
Customizable UI: Choose theme colors and extraction modes (Auto Detect, OCR Only, Text-based Only).
Progress Feedback: Real-time spinners and status updates for user interaction.

Installation
Prerequisites

Python 3.8+
Tesseract OCR installed on your system (Installation Guide)
Poppler-utils for PDF-to-image conversion (Installation Guide)

Setup

Clone the repository:
git clone https://github.com/your-username/idp.git
cd idp


Create a virtual environment:
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate


Install dependencies:
pip install -r requirements.txt


Install NLTK stopwords:
import nltk
nltk.download('stopwords')


Run the application:
streamlit run app.py



Requirements
Create a requirements.txt file with the following:
streamlit==1.25.0
pytesseract==0.3.10
pdf2image==1.16.3
PyPDF2==3.0.1
python-docx==0.8.11
wordcloud==1.9.2
matplotlib==3.7.2
textblob==0.17.1
nltk==3.8.1

Usage

Launch the App: Run streamlit run app.py and open the provided local URL (e.g., http://localhost:8501).
Upload a PDF: Use the file uploader to select a PDF file.
Choose Extraction Mode:
Auto Detect: Attempts direct text extraction; falls back to OCR if no text is found.
OCR Only: Forces OCR for text extraction.
Text-based Only: Uses direct text extraction without OCR.


Customize Settings:
Select a theme color via the color picker.
Enable/disable keyword analysis.


View Results: Extracted text, word/page count, top keywords, sentiment analysis, and word cloud (if applicable).
Export: Download the extracted text as a .docx file.

Example
Upload a PDF, and the app will:

Extract text (e.g., "This is a sample document...").
Display a summary (e.g., "500 words across 3 pages").
Show top keywords (e.g., "document: 15 occurrences").
Generate a word cloud visualization.
Provide sentiment analysis (e.g., "Polarity: 0.2, Subjectivity: 0.5").
Offer a downloadable Word document.

Screenshots
  
Contributing
Contributions are welcome! Please follow these steps:

Fork the repository.
Create a new branch (git checkout -b feature/your-feature).
Commit your changes (git commit -m "Add your feature").
Push to the branch (git push origin feature/your-feature).
Open a Pull Request.

License
This project is licensed under the MIT License. See the LICENSE file for details.
