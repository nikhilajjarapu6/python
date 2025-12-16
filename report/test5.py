import pdfplumber
import re
import json

pdf_path = r"D:\Program Collection\Python\report\kiran.pdf"
output_json = "lab_results.json"

heading_pattern = re.compile(r"([A-Z][A-Z\s/&\-]+?)\s*-\s*(\d{2}-\d{2}-\d{4})\s*(\d{2}:\d{2})?")
extra_info_keywords = ["NOTE", "INTERPRETATION", "METHOD", "REPORT", "COMMENTS", "NA", "Null"]

def clean(text):
    return re.sub(r'\s+', ' ', text).strip()

def extract_tests(pdf_path):
    results = []
    current_test = None

    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text() or ""
            lines = text.split("\n")

            # 🔹 Detect test heading
            for line in lines:
                match = heading_pattern.search(line)
                if match:
                    if current_test:
                        results.append(current_test)

                    current_test = {
                        "test_name": match.group(1).strip(),
                        "test_date": match.group(2),
                        "test_time": match.group(3) if match.group(3) else None,
                        "details": [],
                        "remarks": [],
                        "extra_info": []
                    }
                    break

            # 🔹 Extract tables & text blocks under same test
            if current_test:
                tables = page.extract_tables()
                for table in tables:
                    for row in table:
                        if len(row) >= 3 and row[1]:  
                            current_test["details"].append({
                                "name": clean(row[0]),
                                "value": clean(row[1]),
                                "range": clean(row[2]) if len(row) > 2 else ""
                            })
                        elif any(kw in clean(" ".join(row)).upper() for kw in extra_info_keywords):
                            current_test["extra_info"].append(clean(" ".join(row)))
                        else:
                            current_test["remarks"].append(clean(" ".join(row)))

    if current_test:
        results.append(current_test)

    return results


if __name__ == "__main__":
    extracted_data = extract_tests(pdf_path)

    with open(output_json, "w", encoding="utf-8") as f:
        json.dump(extracted_data, f, indent=4, ensure_ascii=False)

    print(f"\n🎯 Extraction Complete! JSON saved to: {output_json}")
