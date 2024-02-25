from flask import Flask, request
from flask_cors import CORS, cross_origin
from PyPDF2 import PdfReader

app = Flask(__name__)

# Enable CORS
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/upload", methods=["POST"])
@cross_origin()
def upload():
    # Handle file upload
    file = request.files["file"]

    # Save file
    file.save("uploads/" + file.filename)

    # Read file
    reader = PdfReader(file)
    page = reader.pages[0]
    text = page.extract_text()

    print(text)        

    return "File uploaded successfully"
