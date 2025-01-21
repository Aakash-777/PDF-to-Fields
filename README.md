# **PDF to Fields**

This project extracts specific details (Name, Phone Number, and Address) from a PDF and automatically populates form fields in a frontend application. It uses Python (Flask) for the backend, PDFPlumber for text extraction, and the Gemini API for extracting structured information.

---

## **Features**
- Automatically extracts text from uploaded PDFs.
- Populates form fields with Name, Phone Number, and Address.
- Displays extracted raw text for transparency.
- Includes a loader to indicate processing.

---

## **Technologies Used**
- **Backend**: Python, Flask, PDFPlumber
- **API**: Google Gemini API
- **Frontend**: HTML, CSS, JavaScript
- **Styling**: Loader for better UX

---

## **Setup Instructions**

### 1. **Clone the Repository**
```bash
git clone https://github.com/your-username/pdf-details-extractor.git
cd pdf-details-extractor
```

### 2. **Set Up the Python Environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. **Install Dependencies**
```bash
pip install flask flask-cors pdfplumber google-generativeai
```

### 4. **Configure the Gemini API**
- Obtain your API key from Google Gemini.
- Replace `"YOUR_API_KEY"` in `app.py` with your actual API key.

### 5. **Run the Application**
```bash
python app.py
```

### 6. **Access the Application**
- Open your browser and go to: [http://127.0.0.1:5000](http://127.0.0.1:5000).

---

## **Usage**
1. Upload a PDF file.
2. The text is extracted and displayed in the "Extracted Text" section.
3. The fields for Name, Phone Number, and Address are automatically populated.

---

## **Folder Structure**
```
project/
├── app.py                   # Backend logic
├── templates/
│   └── index.html           # Frontend HTML
├── static/
│   ├── styles.css           # Styling
│   └── script.js            # Frontend logic
├── requirements.txt         # Python dependencies
```

---

## **Sample PDF**
Use the provided demo PDF for testing: [Demo PDF](https://drive.google.com/file/d/1WTCFX4gTCwLNfsiWQyxLWyVdABQ3ko7T/view?usp=sharing).

---

## **Future Enhancements**
- Add support for extracting additional fields.
- Deploy the application on platforms like Heroku, Render, or Vercel.
- Include a detailed error log for better debugging.

