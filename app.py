from flask import Flask, request, jsonify, render_template
import pdfplumber
import google.generativeai as genai
import json
import re

app = Flask(__name__)

# Configure Gemini API
genai.configure(api_key="AIzaSyCuAC-Kmhab5ukLNm3d2X3HSqcLqmPmo3U")
model = genai.GenerativeModel("gemini-1.5-flash")

@app.route("/")
def index():
    """Serve the HTML template."""
    return render_template("index.html")

def extract_text_from_pdf(file):
    """Extract text from the uploaded PDF file."""
    try:
        with pdfplumber.open(file) as pdf:
            text = " ".join(page.extract_text() for page in pdf.pages if page.extract_text())
        return text, None
    except Exception as e:
        return None, str(e)


def extract_details_with_gemini(text):
    """Use Gemini API to extract structured details."""
    prompt = f"""{text}\n\n 
                from the above data extract me the name (without titles), phone number, and address of the person. 
                I do not need any code or method. I want you to extract and return it in a JSON format.
                In case of multiple phone numbers or multiple addresses, use the one appearing first."""
    try:
        response = model.generate_content(prompt)
        # Print raw response for debugging
        # print("Raw Response Text:", response.text)

        # Use regex to extract the JSON portion from the response
        json_match = re.search(r"\{.*\}", response.text, re.DOTALL)
        if not json_match:
            raise ValueError("No valid JSON found in the response")

        # Extract and parse the JSON
        json_text = json_match.group(0)
        parsed_data = json.loads(json_text)

        # Normalize keys (optional)
        normalized_data = {
            "Name": parsed_data.get("name", ""),
            "Phone Number": parsed_data.get("phone", ""),
            "Address": parsed_data.get("address", ""),
        }

        return normalized_data, None
    except json.JSONDecodeError as e:
        return None, f"Failed to parse JSON: {str(e)}"
    except Exception as e:
        return None, str(e)



@app.route("/extract-text", methods=["POST"])
def extract_text():
    """Handle PDF upload and return extracted text."""
    if "pdf" not in request.files:
        return jsonify({"error": "No PDF file provided"}), 400

    file = request.files["pdf"]
    text, error = extract_text_from_pdf(file)

    if error:
        return jsonify({"error": f"Failed to extract text from PDF: {error}"}), 500

    return jsonify({"text": text})

@app.route("/extract-details", methods=["POST"])
def extract_details():
    """Use extracted text to populate fields."""
    data = request.get_json()
    text = data.get("text", "")

    if not text:
        return jsonify({"error": "No text provided."}), 400

    extracted_data, error = extract_details_with_gemini(text)
    if error:
        return jsonify({"error": f"Failed to process text with Gemini API: {error}"}), 500

    return jsonify(extracted_data)

if __name__ == "__main__":
    app.run(debug=True)
