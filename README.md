# Universal-File-to-Text-Converter
Streamlit-based web application that allows users to upload various file types—including images (jpg, jpeg, png, webp), documents (pdf, docx, xls), and extract text from them.

Project Overview
The Universal File to Text Converter is a Streamlit-based web application that allows users to upload various file types (images, PDFs, DOCX, and XLS) and extract text from them. The extracted text can be copied to the clipboard or downloaded as a .txt file. The app provides a smooth and engaging user experience with animations and a modern UI.

Features
File Upload: Supports multiple file formats (JPG, JPEG, PNG, WEBP, PDF, DOCX, XLS).

Text Extraction:

Images: Uses Tesseract OCR for text extraction.

PDFs: Uses pdfplumber for text extraction.

DOCX: Uses python-docx for text extraction.

Excel: Uses pandas for text extraction.

Copy to Clipboard: One-click button to copy extracted text.

Download Text: Save extracted text as a .txt file.

Interactive UI:

Drag-and-drop file uploader.

Real-time progress animations.

Modern and responsive design.

File Directory Structure

universal-file-to-text-converter/
│
├── app.py                  # Main Streamlit application file
├── requirements.txt        # List of Python dependencies
├── README.md               # Project documentation
├── assets/                 # Folder for static assets (e.g., images, icons)
│   └── logo.png            # Example logo for the app
├── tests/                  # Folder for unit tests
│   └── test_app.py         # Test cases for the application
└── .gitignore              # Specifies files to ignore in Git



Installation
Prerequisites
Python 3.8 or higher: Ensure Python is installed on your system.

Tesseract OCR: Install Tesseract OCR for text extraction from images.

Windows: Download from UB Mannheim's Tesseract page.

macOS: Install using Homebrew:

brew install tesseract
Linux: Install using the package manager:


sudo apt-get install tesseract-ocr
Steps to Run the Application
Clone the repository:


git clone https://github.com/your-username/universal-file-to-text-converter.git
cd universal-file-to-text-converter
Install the required Python packages:


pip install -r requirements.txt
Run the Streamlit app:


streamlit run app.py
Open your browser and navigate to http://localhost:8501.


Upload a File:

Drag and drop or click to upload a file (JPG, JPEG, PNG, WEBP, PDF, DOCX, XLS).

The app will display the file name and size.

Extract Text:

The app will automatically extract text from the uploaded file.

Extracted text will be displayed in a text area.

Copy Text:

Click the Copy to Clipboard button to copy the extracted text.

Download Text:

Click the Download Text File button to save the extracted text as a .txt file.

Dependencies
The project uses the following Python libraries:

Streamlit: For building the web app.

Pillow (PIL): For image processing.

pytesseract: For OCR-based text extraction from images.

pdfplumber: For text extraction from PDFs.

python-docx: For text extraction from DOCX files.

pandas: For text extraction from Excel files.

To install all dependencies, run:


pip install streamlit pillow pytesseract pdfplumber python-docx pandas
Contributing
Contributions are welcome! Follow these steps:

Fork the repository.

Create a new branch:


git checkout -b feature/your-feature-name
Commit your changes:



git commit -m "Add your feature"
Push to the branch:


git push origin feature/your-feature-name
Open a pull request.

License
This project is licensed under the MIT License. See the LICENSE file for details.

Acknowledgments
Streamlit: For providing an excellent framework for building web apps.

Tesseract OCR: For enabling text extraction from images.

BrijRaj Softworks: For developing and maintaining the project.

Contact
For questions or feedback, please contact:

Email: parthabhuyan2022@gmail.com

Website: www.brijRajsoftworks.com
