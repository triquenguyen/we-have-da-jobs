from flask import Flask, request
from pymongo import MongoClient
from flask_cors import CORS, cross_origin
from PyPDF2 import PdfReader
from models.jobs import Job
import csv
from utilities.ultilities import getKeyWords   
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
client = MongoClient("mongodb://mongodb:27017/")
db = client["we_got_da_jobs"]
jobs = db["jobs"]

@app.route("/", methods=["GET"])
def index():
    return "Hello World"

@app.route("/jobs")
def get_jobs():
    jobs_list = []
    for job in jobs.find():
        job.pop('_id')
        jobs_list.append(job)
    return {"jobs": jobs_list}


def insert_jobs_from_csv(csv_file):
    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            job = Job(
                company=row['Company'],
                job_link=row['Job_link'],
                job_location=row['Job_location'],
                post_time=row['Post_time'],
                job_description=row['Job_description'],
                seniority_level=row['Seniority_level'],
                employment_type=row['Employment_type'],
                industry=row['Industries'],
                job_function=row['Job_function'],
                job_title=row['Job_title']
            )
            jobs.insert_one(job.__dict__)

@app.post("/upload")
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

    # print(text)   

    # Get keywords
    keywords = getKeyWords(text)

    print(keywords)     

    return "File uploaded successfully"

if __name__ == '__main__':
    # Insert data from CSV file
    insert_jobs_from_csv('./utilities/jobs_data.csv')

    # Print message after insertion
    print("Data inserted successfully from CSV into MongoDB")

    # Run the Flask app
    app.run(debug=True, port=8000, host='0.0.0.0')
