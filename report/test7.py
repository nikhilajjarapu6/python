import re
import fitz
import json


TEST_NAMES = [
    "COMPLETE BLOOD COUNT",
    "COMPLETE URINE EXAMINATION",
    "CREATININE",
    "ELECTROLYTES",
    "BLOOD UREA",
    "LIVER FUNCTION TEST WITH PROTEINS",
    "PRO CALCITONIN",
    "ARTERIAL BLOOD GASES (ABG)",  # FIXED
    "SERUM ALBUMIN",
    "FLUID CULTURE & SENSITIVITY",
    "TACROLIMUS -",
    "X-RAY",
    "BRONCHIAL WASH-FUNGAL STAIN",
    "BRONCHIAL WASH-GRAMS STAIN",
    "GENE-XPERT"
]


# Escape each name properly
escaped_tests = [re.escape(name) for name in TEST_NAMES]

# Detect test name
TEST_HEADER = re.compile(
    rf"(?P<test>{'|'.join(escaped_tests)})",
    re.IGNORECASE
)

# Detect date + time
DATE_TIME = re.compile(
    r"(?P<date>\d{1,2}-\d{1,2}-\d{4})\s+(?P<time>\d{1,2}:\d{2})",
    re.IGNORECASE
)

# Detect header with date/time
HEADER_PATTERN = re.compile(
    rf"(?P<test>{'|'.join(escaped_tests)})\s*[-:]\s*(?P<date>\d{{1,2}}-\d{{1,2}}-\d{{4}})\s+(?P<time>\d{{1,2}}:\d{{2}})",
    re.IGNORECASE
)


def extract_parameters(chunk: str):
    return {"raw_text": chunk.strip()}


def extract_all_tests(text: str):
    results = []
    matches = list(TEST_HEADER.finditer(text))

    for i, match in enumerate(matches):
        test_name = match.group("test").strip()

        start = match.start()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)

        chunk = text[start:end]

        # Try header first
        header = HEADER_PATTERN.search(chunk)

        if header:
            date = header.group("date")
            time = header.group("time")
        else:
            # fallback
            dt = DATE_TIME.search(chunk)
            date = dt.group("date") if dt else None
            time = dt.group("time") if dt else None

        results.append({
            "test_name": test_name,
            "date": date,
            "time": time,
            "parameters": extract_parameters(chunk)
        })

    return results


def extract_from_pdf(pdf_path: str, save_json=True):
    doc = fitz.open(pdf_path)
    text = ""

    for page in doc:
        text += page.get_text()

    doc.close()

    data = extract_all_tests(text)

    if save_json:
        with open("results.json", "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

    return data


# -------------------------
# USAGE EXAMPLE
# -------------------------
if __name__ == "__main__":
    pdf_path = r"D:\Program Collection\Python\report\kiran.pdf"   # <-- replace
    output = extract_from_pdf(pdf_path)

    print(json.dumps(output, indent=4))
