# **PDF to Fields**

This project extracts specific details (Name, Phone Number, and Address) from a PDF and automatically populates form fields in a frontend application. It uses Python (Flask) for the backend, PDFPlumber for text extraction, and the Gemini API for extracting structured information.

---

## **Features**
- Automatically extracts text from uploaded PDFs.
- Populates form fields with Name, Phone Number, and Address.
- Includes a loader to indicate processing.

---

## **Technologies Used**
- **Backend**: Python, Flask, PDFPlumber
- **API**: Google Gemini API
- **Frontend**: HTML, CSS, JavaScript

---

## **Setup Instructions**

### 1. **Clone the Repository**
```bash
git clone https://github.com/your-username/PDF-to-Fields.git
cd PDF-to-Fields
```

### 2. **Set Up the Python Environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. **Install Dependencies**
```bash
pip install -r requirements.txt
```

### 4. **Configure the Gemini API**
- Obtain your API key from Google Gemini.
- Create a `.env` file and add this line inside `GEMINI_API_KEY = your_actual_api_key` with your actual API key.

### 5. **Run the Application**
```bash
python app.py
```

### 6. **Access the Application**
- Open your browser and go to: [http://127.0.0.1:5000](http://127.0.0.1:5000).

---

## **Usage**
1. Upload a PDF file.
2. The fields for Name, Phone Number, and Address are automatically populated.

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
├── venv/                    # Virtual Environment
├── .env                     # Environment Variables for API Keys and other Secrets
```

---

## **Sample PDF**
Use the provided demo PDF for testing: [Demo PDF](https://drive.google.com/file/d/1WTCFX4gTCwLNfsiWQyxLWyVdABQ3ko7T/view?usp=sharing).

---

## **Deployed Link**
Use the application through this link: [https://pdf-to-fields.onrender.com/](https://pdf-to-fields.onrender.com/).

`  The website might initially take 50sec or more to load up due to inactivity (since I am using the free service in render)`

---

## **Future Enhancements**
- Add support for extracting additional fields.
- Optimize processing for instant results.
- Implement Optical Character Recognition (OCR) for extracting text from images inside the pdf

