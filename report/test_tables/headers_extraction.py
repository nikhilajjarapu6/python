import re
import fitz
import json
from collections import Counter
# import blood_test


TEST_NAMES = [
    "COMPLETE BLOOD COUNT",
    "COMPLETE BLOOD PICTURE",
    "COMPLETE URINE EXAMINATION",
    "BLOOD CULTURE & SENSITIVITY",
    "URINE CULTURE & SENSITIVITY (CATHETER CATCH)",
    "CREATININE",
    "ELECTROLYTES",
    "BLOOD UREA",
    "LIVER FUNCTION TEST WITH PROTEINS",
    "PRO CALCITONIN",
    "ARTERIAL BLOOD GASES (ABG)",   # fixed
    "SERUM ALBUMIN",
    "FLUID CULTURE & SENSITIVITY",
    "TACROLIMUS -",
    "X-RAY",
    "BRONCHIAL WASH-FUNGAL STAIN",
    "BRONCHIAL WASH-GRAMS STAIN",
    "GENE-XPERT",
    "MAGNESIUM",
    "PHOSPHOROUS",
    "CALCIUM",
    "POST LUNCH PLASMA SUGAR",
    "URIC ACID",
    "ESR",
    "VDRL",
    "HBsAg",
    "HCV",
    "HIV 1 & 2 Antibody tes",
    "ANTI HEPATITS ""B"" CORE ANTIGEN-IGM",
    "ANTI HEPATITIS B SURFACE ANTIBODIES",
    "PROTHROMBIN TIME[PT]",
    "ACTIVATED PARTIAL THROMBOPLASTIN TIME",
    "GLYCOSYLATED HAEMOGLOBIN (HBA1C)",
    "LIPID PROFILE",
    "FASTING PLASMA SUGAR",
    "THYROID PROFILE",
    "BLOOD GROUPING AND RH",
    "EPSTEIN BARR VIRUS SEROLOGY",
    "CMV QUANTITATIVE",
    "PRE ALBUMIN",
    "SINGLE ANTIGEN BEAD PANEL",
    "TB QUANTIFERRON",
    "PUS CULTURE & SENSITIVITY",
    "BEDSIDE ULTRASOUND",
    "BEDSIDE CAROTID DOPPLER / NECK VESSELS",
    "U/S UPPER/LOWER LIMB ARTERIAL BOTH LIMBS"

]

escaped_tests = [re.escape(t) for t in TEST_NAMES]


TEST_HEADER = re.compile(
    rf"(?P<test>{'|'.join(escaped_tests)})",
    re.IGNORECASE
)


# HEADER_WITH_DATETIME = re.compile(
#     rf"(?P<test>{'|'.join(escaped_tests)})\s*[-:]\s*"
#     r"(?P<date>\d{1,2}-\d{1,2}-\d{4})\s+"
#     r"(?P<time>\d{1,2}:\d{2})",
#     re.IGNORECASE
# )

HEADER_WITH_DATETIME = re.compile(
    r"(?P<date>\d{1,2}-\d{1,2}-\d{4}).{0,20}?(?P<time>\d{1,2}:\d{2})",
    re.DOTALL
)




def extract_test_headers(text: str):
    results = []
    test_matches = list(TEST_HEADER.finditer(text))

    for i, match in enumerate(test_matches):
        test_name = match.group("test").strip()


        start = match.start()
        end = test_matches[i + 1].start() if i + 1 < len(test_matches) else len(text)
        chunk = text[start:end]

        
        header_match = HEADER_WITH_DATETIME.search(chunk)
        if not header_match:
            continue

        date = header_match.group("date")
        time = header_match.group("time")

        if not re.match(r"\d{2}-\d{2}-\d{4}", date):
            continue
        if not re.match(r"\d{1,2}:\d{2}", time):
            continue

        results.append({
            "test_name": test_name,
            "date": date,
            "time": time
        })

    return results


HEADER_BLOCK = re.compile(
    r"\d{1,2}-\d{1,2}-\d{4}\s+\d{1,2}:\d{2}\s*:?\s*(AM|PM).*?(?=\n)",
    re.IGNORECASE | re.DOTALL
)



def extract_from_pdf(pdf_path: str):
    doc = fitz.open(pdf_path)
    text = ""

    for page in doc:
        text += page.get_text()

    doc.close()
    text=HEADER_BLOCK.sub("", text)
    return text



def save_json(data, filename="headers.json"):

    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)


def count_test(json_path, test_name):
    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    count = sum(1 for item in data if item["test_name"].upper() == test_name.upper())
    return count

def count_all_tests(json_path):
    with open(json_path,"r",encoding="utf-8") as f:
        data=json.load(f)
    count=0
    for item in data:
        count+=1
    print(count)

    names = [item["test_name"] for item in data]
    print(dict(Counter(names)))

def extract_header(json_path,heading):
    with open(json_path,"r",encoding="utf-8") as f:
        data=json.load(f)
    
    

if __name__ == "__main__":
    pdf_path = r"D:\Program Collection\Python\report_analysis copy\data\raw\KIMS _ EHR (19).pdf"   
    full_text = extract_from_pdf(pdf_path)

    headers = extract_test_headers(full_text)
    save_json(headers)

    # print(json.dumps(headers, indent=4))
    
    # print(count_test(r"D:\Program Collection\Python\headers.json","LIVER FUNCTION TEST WITH PROTEINS"))
    # count_all_tests(r"D:\Program Collection\Python\headers.json")

