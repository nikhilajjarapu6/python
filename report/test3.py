import json
import re
from datetime import datetime
import pdfplumber

DATE_FORMATS = ["%d-%m-%Y", "%d/%m/%Y", "%Y-%m-%d", "%d-%b-%Y"]

def parse_date(text):
    for fmt in DATE_FORMATS:
        try:
            return datetime.strptime(text, fmt).date().isoformat()
        except:
            pass
    return None

def extract_grouped_results(pdf_path: str):
    final_output = []
    current_test_name = None
    current_date = None
    parameters_list = []

    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text()

            # Detect headings like: TEST NAME - 29-08-2025 07:40
            matches = re.findall(r"([A-Z][A-Z\s/]+)\s*-\s*(\d{2}-\d{2}-\d{4})", text)
            for test, date in matches:

                if current_test_name and parameters_list:
                    final_output.append({
                        "test_name": current_test_name,
                        "date": current_date,
                        "parameters": parameters_list
                    })

                current_test_name = test.strip()
                current_date = parse_date(date)
                parameters_list = []

            tables = page.extract_tables()
            for table in tables:
                if len(table) < 2:
                    continue

                header = [h.lower().strip() if h else "" for h in table[0]]
                if not ("parameter" in header and "result" in header):
                    continue

                for row in table[1:]:
                    param = row[0] or ""
                    value = str(row[1]).strip() if len(row) > 1 else ""
                    ref_range = row[2] if len(row) > 2 else ""

                    if not param or param.lower() in ["note", "note:"]:
                        continue

                    unit = None
                    unit_match = re.search(r"([a-zA-Z/²³]+)", value)
                    if unit_match:
                        unit = unit_match.group(1)
                        value = value.replace(unit, "").strip()

                    parameters_list.append({
                        "name": param,
                        "value": value,
                        "range": ref_range,
                        "unit": unit
                    })

    # Save last test group
    if current_test_name and parameters_list:
        final_output.append({
            "test_name": current_test_name,
            "date": current_date,
            "parameters": parameters_list
        })

    return final_output


# ----------- MAIN ----------- #
pdf_path = r"D:\Program Collection\Python\report\kiran.pdf"
output_file = r"D:\Program Collection\Python\report\structured_output.json"

data = extract_grouped_results(pdf_path)

with open(output_file, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"[INFO] Structured JSON saved to: {output_file}")
