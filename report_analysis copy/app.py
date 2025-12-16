from fastapi import FastAPI, UploadFile, File
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import json
import os

from src.extractors import extract_text_in_order
from src.parsers import (
    extract_patient_parse,
    demographics_parse,
    discharge_condition_parse,
    medication_parse
)

app = FastAPI(title="Patient Report API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---------- Paths ----------
FRONTEND_PATH = r"D:\Nikhil\python\report_analysis\frontend\index.html"
DEFAULT_PDF_PATH = r"D:\Program Collection\Python\report_analysis copy\data\raw\kiran.pdf"
UPLOAD_FOLDER = r"D:\Nikhil\python\report_analysis\data\uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# ---------- Global JSON Holders ----------
patient_json = None
diagnosis_json = None
discharge_json = None
medication_json = None


def load_pdf_and_extract(pdf_path: str):
    """Extract and parse data from a given PDF file."""
    global patient_json, diagnosis_json, discharge_json, medication_json

    all_text, patient_demographics, discharge_text, medication_text, test_data, follow_up = extract_text_in_order(pdf_path)

    patient = extract_patient_parse(patient_demographics)
    diagnosis = demographics_parse(patient_demographics)
    discharge = discharge_condition_parse(discharge_text)
    medication = medication_parse(medication_text)

    # Convert dicts to JSON-compatible objects
    patient_json = json.loads(json.dumps(patient, indent=2))
    diagnosis_json = json.loads(json.dumps(diagnosis, indent=2))
    discharge_json = json.loads(json.dumps(discharge, indent=2))
    medication_json = json.loads(json.dumps(medication, indent=2))

    print(f"✅ Extraction complete for: {os.path.basename(pdf_path)}")


# ---------- Startup ----------
@app.on_event("startup")
def startup_event():
    """Load default PDF when app starts."""
    print("Extracting default PDF data...")
    load_pdf_and_extract(DEFAULT_PDF_PATH)


# ---------- Routes ----------
@app.get("/report_home", response_class=HTMLResponse)
def open_html():
    with open(FRONTEND_PATH, encoding="utf-8") as file:
        return file.read()


@app.get("/")
def home():
    return {"message": "Patient Report API is running 🚀"}


# ---------- Upload Endpoint ----------
@app.post("/upload_pdf")
async def upload_pdf(file: UploadFile = File(...)):

    try:
        if not file.filename.endswith(".pdf"):
            return JSONResponse(content={"error": "Only PDF files are allowed"}, status_code=400)

        file_path = os.path.join(UPLOAD_FOLDER, file.filename)
        with open(file_path, "wb") as buffer:
            buffer.write(await file.read())

        load_pdf_and_extract(file_path)

        return JSONResponse(content={"message": f"File '{file.filename}' processed successfully."}, status_code=200)

    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)


# ---------- Data Endpoints ----------
@app.get("/patients")
def get_patient_details():
    if patient_json:
        return JSONResponse(content=patient_json, status_code=200)
    return JSONResponse(content={"error": "Patient data not available"}, status_code=404)


@app.get("/diagnosis")
def get_diagnosis():
    if diagnosis_json:
        return JSONResponse(content=diagnosis_json, status_code=200)
    return JSONResponse(content={"error": "Diagnosis data not available"}, status_code=404)


@app.get("/discharge")
def get_discharge_condition():
    if discharge_json:
        return JSONResponse(content=discharge_json, status_code=200)
    return JSONResponse(content={"error": "Discharge data not available"}, status_code=404)


@app.get("/medication")
def get_medication():
    if medication_json:
        return JSONResponse(content=medication_json, status_code=200)
    return JSONResponse(content={"error": "Medication data not available"}, status_code=404)
