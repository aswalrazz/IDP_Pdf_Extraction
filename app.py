import streamlit as st
import pytesseract
from pdf2image import convert_from_path
import tempfile
import PyPDF2
import pandas as pd
from io import BytesIO


st.title("INTELLIGENT DOCUMENT PROCESSING (IDP)")

st.write("Upload a PDF file to extract text and export the results to Excel.")


uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

if uploaded_file is not None:
    st.write("Uploaded file:", uploaded_file.name)
    
   
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_file:
        temp_file.write(uploaded_file.read())
        temp_pdf_path = temp_file.name

    try:
        
        pdf_reader = PyPDF2.PdfReader(temp_pdf_path)
        extracted_text = ""
        for page in pdf_reader.pages:
            extracted_text += page.extract_text()

        if extracted_text.strip():
            st.subheader("Extracted Text (Text-based PDF):")
            st.text_area("Text Output", extracted_text, height=300)
        else:
            st.write("No extractable text found. Trying OCR...")

            
            images = convert_from_path(temp_pdf_path)
            ocr_text = ""
            for page_num, img in enumerate(images, start=1):
                text = pytesseract.image_to_string(img)
                ocr_text += f"\n--- Page {page_num} ---\n{text}"

            st.subheader("Extracted Text (OCR):")
            extracted_text = ocr_text
            st.text_area("Text Output", extracted_text, height=300)

        
        if extracted_text.strip():
            st.write("Export the extracted text to Excel:")
            
            
            data = {"Page Number": [], "Extracted Text": []}
            if "--- Page" in extracted_text:  
                for page_text in extracted_text.split("\n--- Page"):
                    if page_text.strip():
                        page_number, text = page_text.split("---\n", 1)
                        data["Page Number"].append(page_number.strip())
                        data["Extracted Text"].append(text.strip())
            else:  
                data["Page Number"].append("All")
                data["Extracted Text"].append(extracted_text.strip())
            
            df = pd.DataFrame(data)
            
            
            output = BytesIO()
            with pd.ExcelWriter(output, engine="xlsxwriter") as writer:
                df.to_excel(writer, index=False, sheet_name="Extracted_Text")
            output.seek(0)
            
            
            st.download_button(
                label="Download Excel File",
                data=output,
                file_name="extracted_text.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )
    except Exception as e:
        st.error(f"An error occurred: {e}")
