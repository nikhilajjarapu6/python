import pdfplumber
import re
import json
import pandas as pd

# Regex for headings like: TEST NAME - 29-08-2025 08:30
heading_pattern = re.compile(
    r"([A-Z][A-Z\s/&\-]+?)\s*[-–]\s*(\d{2}-\d{2}-\d{4})\s*(\d{2}:\d{2})?"
)

def extract_test_headings(pdf_path):
    headings = []

    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text() or ""
            lines = text.split("\n")

            for line in lines:
                match = heading_pattern.search(line.strip())
                if match:
                    test_name = match.group(1).strip()
                    test_date = match.group(2)
                    test_time = match.group(3) if match.group(3) else None

                    headings.append({
                        "test_name": test_name,
                        "test_date": test_date,
                        "test_time": test_time
                    })

    return headings


pdf_path = r"D:\Program Collection\Python\report\kiran.pdf"
result = extract_test_headings(pdf_path)

output_path = r"D:\Program Collection\Python\report\kiran_tests.json"
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(result, f, indent=4, ensure_ascii=False)

df=pd.DataFrame(result)
json_file=df.to_json(orient="records")
print(json_file[:200])