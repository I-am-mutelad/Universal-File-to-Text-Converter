import streamlit as st
from PIL import Image
import pytesseract
import pdfplumber
from docx import Document
import pandas as pd
import io
import time
import base64

# Configure Tesseract path (for Windows)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Set page configuration
st.set_page_config(
    page_title="Universal File to Text Converter",
    page_icon="📄",
    layout="centered",
    initial_sidebar_state="expanded",
)

# Custom CSS for modern and attractive UI
st.markdown(
    """
    <style>
    /* General Styling */
    body {
        font-family: 'Arial', sans-serif;
        background-color: #f4f4f9;
        color: #333;
    }

    /* Header and Title */
    .stApp header h1 {
        color: #4CAF50;
        font-size: 2.5rem;
        font-weight: bold;
        text-align: center;
        margin-bottom: 20px;
    }

    /* File Uploader */
    .file-uploader {
        border: 2px dashed #4CAF50;
        border-radius: 15px;
        padding: 30px;
        text-align: center;
        margin: 20px auto;
        background-color: #ffffff;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        transition: all 0.3s ease;
    }

    .file-uploader:hover {
        border-color: #45a049;
        box-shadow: 0 6px 8px rgba(0, 0, 0, 0.15);
    }

    /* Buttons */
    .stButton button {
        background-color: #4CAF50;
        color: white;
        border-radius: 8px;
        padding: 12px 24px;
        font-size: 16px;
        font-weight: bold;
        transition: background-color 0.3s ease, transform 0.2s ease;
    }

    .stButton button:hover {
        background-color: #45a049;
        transform: scale(1.05);
    }

    /* Extracted Text Area */
    .stTextArea textarea {
        border-radius: 10px;
        border: 2px solid #4CAF50;
        padding: 15px;
        font-size: 16px;
        color: black;
        background-color: #ffffff;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }

    /* Footer */
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: #4CAF50;
        color: white;
        text-align: center;
        padding: 15px;
        font-size: 16px;
        font-weight: bold;
        box-shadow: 0 -2px 10px rgba(0, 0, 0, 0.1);
    }

    .footer a {
        color: white;
        text-decoration: none;
        transition: color 0.3s ease;
    }

    .footer a:hover {
        color: #d1e7dd;
    }

    /* Animations */
    @keyframes fadeIn {
        from {
            opacity: 0;
        }
        to {
            opacity: 1;
        }
    }

    .stSpinner div {
        animation: fadeIn 0.5s ease-in-out;
    }

    /* Success and Error Messages */
    .stSuccess {
        background-color: #d1e7dd;
        color: #0f5132;
        border-radius: 8px;
        padding: 10px;
        margin: 10px 0;
    }

    .stError {
        background-color: #f8d7da;
        color: #842029;
        border-radius: 8px;
        padding: 10px;
        margin: 10px 0;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Footer with copyright
st.markdown(
    """
    <div class="footer">
        Developed with ❤️ By Partha Bhuyan <br> <a href="https://www.brijrajsoftworks.com" target="_blank">BrijRaj Softworks</a> | © 2024 All Rights Reserved
    </div>
    """,
    unsafe_allow_html=True,
)

# Title and description
st.title("Universal File to Text Converter")
st.markdown(
    "Upload images (JPG, JPEG, PNG, WEBP), documents (PDF, DOCX, XLS), and extract text with ease!"
)

# File uploader
uploaded_file = st.file_uploader(
    "Drag and drop or click to upload a file",
    type=["jpg", "jpeg", "png", "webp", "pdf", "docx", "xls"],
    key="file_uploader",
)

# Function to extract text from images using Tesseract OCR
def extract_text_from_image(image):
    try:
        text = pytesseract.image_to_string(image)
        return text
    except Exception as e:
        st.error(f"Error extracting text from image: {e}")
        return ""

# Function to extract text from PDF using pdfplumber
def extract_text_from_pdf(pdf_file):
    try:
        text = ""
        with pdfplumber.open(pdf_file) as pdf:
            for page in pdf.pages:
                text += page.extract_text()
        return text
    except Exception as e:
        st.error(f"Error extracting text from PDF: {e}")
        return ""

# Function to extract text from DOCX using python-docx
def extract_text_from_docx(docx_file):
    try:
        doc = Document(docx_file)
        text = "\n".join([para.text for para in doc.paragraphs])
        return text
    except Exception as e:
        st.error(f"Error extracting text from DOCX: {e}")
        return ""

# Function to extract text from Excel using pandas
def extract_text_from_excel(excel_file):
    try:
        df = pd.read_excel(excel_file)
        text = df.to_string(index=False)
        return text
    except Exception as e:
        st.error(f"Error extracting text from Excel: {e}")
        return ""

# Display file details and extract text
if uploaded_file is not None:
    st.success("File uploaded successfully!")
    st.write(f"**File Name:** {uploaded_file.name}")
    st.write(f"**File Size:** {uploaded_file.size / 1024:.2f} KB")

    # Show loading animation while processing
    with st.spinner("Extracting text..."):
        time.sleep(2)  # Simulate processing delay
        if uploaded_file.type.startswith("image"):
            image = Image.open(uploaded_file)
            extracted_text = extract_text_from_image(image)
        elif uploaded_file.type == "application/pdf":
            extracted_text = extract_text_from_pdf(uploaded_file)
        elif uploaded_file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
            extracted_text = extract_text_from_docx(uploaded_file)
        elif uploaded_file.type == "application/vnd.ms-excel":
            extracted_text = extract_text_from_excel(uploaded_file)
        else:
            extracted_text = "Unsupported file format."

    # Display extracted text
    if extracted_text:
        st.subheader("Extracted Text")
        st.text_area("Extracted Text", extracted_text, height=300)

        # Copy to clipboard button
        if st.button("Copy to Clipboard"):
            st.write("Text copied to clipboard! 📋")
            st.experimental_set_query_params(copied=True)
            st.write(extracted_text)  # Simulate copying to clipboard

        # Download as .txt file
        st.markdown("### Download Extracted Text")
        st.write("Click the button below to download the extracted text as a .txt file.")
        if st.button("Download Text File"):
            b64 = base64.b64encode(extracted_text.encode()).decode()
            href = f'<a href="data:file/txt;base64,{b64}" download="extracted_text.txt">Download Text File</a>'
            st.markdown(href, unsafe_allow_html=True)
            st.success("File downloaded successfully! 🎉")
    else:
        st.warning("No text could be extracted from the file.")