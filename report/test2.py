import pdfplumber
import re
import json

pdf_path = r"D:\Program Collection\Python\report\kiran.pdf"
output_file = r"D:\Program Collection\Python\report\final_results.json"


# 🔹 Detect headings in this format:
#   TEST NAME - DD-MM-YYYY HH:MM
def is_heading(line):
    return bool(re.match(r'^([A-Z0-9 ,/()]+)\s*-\s*(\d{2}-\d{2}-\d{4}\s+\d{2}:\d{2})$', line.strip()))


# 🔹 Extract test name & date from heading
def parse_heading(heading):
    match = re.match(r'^(.+?)\s*-\s*(\d{2}-\d{2}-\d{4}\s+\d{2}:\d{2})$', heading.strip())
    if match:
        return match.group(1).strip(), match.group(2).strip()
    return heading, None  # fallback


# 🔹 Main extraction logic
def extract_tests_with_tables(pdf_path):
    all_tests = []
    current_test_name = None
    current_test_date = None

    with pdfplumber.open(pdf_path) as pdf:
        for page_num, page in enumerate(pdf.pages, start=1):

            # Extract text and detect headings
            lines = (page.extract_text() or "").split("\n")
            for line in lines:
                if is_heading(line):
                    current_test_name, current_test_date = parse_heading(line)

            # Extract tables
            raw_tables = page.extract_tables()

            for table in raw_tables:
                # Skip invalid/noisy tables
                if not table or len(table) < 2 or len(table[0]) < 3:
                    continue

                header = [h.strip() for h in table[0]]  # first row = column names

                # Convert rows to JSON format (Parameter-Value-Range)
                results = []
                for row in table[1:]:
                    if len(row) < 3:
                        continue
                    results.append({
                        "Parameter": row[0].strip(),
                        "Result": row[1].strip(),
                        "Normal Range": row[2].strip()
                    })

                if results:
                    all_tests.append({
                        "test_name": current_test_name,
                        "test_date": current_test_date,
                        "results": results,
                        "page": page_num
                    })

    return all_tests


# 🔹 Save as JSON
final_data = extract_tests_with_tables(pdf_path)

with open(output_file, "w", encoding="utf-8") as f:
    json.dump(final_data, f, indent=2, ensure_ascii=False)

print(f"🎯 Extraction completed. JSON saved at:\n{output_file}")
