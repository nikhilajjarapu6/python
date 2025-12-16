import camelot
import re
import json

# CBC PARAM LIST
CBC_PARAMS = [
    "HAEMOGLOBIN",
    "HAEMATOCRIT",
    "RBC COUNT",
    "WBC COUNT",
    "PLATELET COUNT",
    "MEAN CELL VOLUME",
    "MEAN CELL HAEMOGLOBIN",
    "MEAN CELL HAEMOGLOBIN CONCENTRATION",
    "RDW - CV",
    "BLASTS",
    "PROMYELOCYTES",
    "MYELOCYTES",
    "METAMYELOCYTES",
    "BAND FORMS",
    "POLYMORPHS",
    "LYMPHOCYTES",
    "EOSINOPHILS",
    "MONOCYTES",
    "BASOPHILS",
    "PROLYMPHOCYTES",
    "ABNORMAL CELLS",
    "PLASMA CELLS",
    "ATYPICAL CELLS",
    "REACTIVE LYMPHOCYTES",
    "COMMENT",
    "NOTE"
]

# Normalize CBC params for matching
CBC_PARAMS_NORM = [re.sub(r"\s+", " ", p.strip().upper()) for p in CBC_PARAMS]

def normalize(text: str):
    return re.sub(r"\s+", " ", text.strip().upper())

def extract_cbc_lines(pdf_path: str):
    # Read all tables from PDF
    tables = camelot.read_pdf(pdf_path, pages="all", flavor="stream")

    matched_lines = []

    # Process each table
    for table in tables:
        df = table.df

        # Each row in the table
        for i in range(len(df)):
            line = " ".join(df.iloc[i].tolist()).strip()
            line_norm = normalize(line)

            # Match against CBC parameters
            for param in CBC_PARAMS_NORM:
                if line_norm.startswith(param):
                    matched_lines.append(line)
                    break  # avoid duplicates

    return matched_lines

pdf_path = r"D:\Program Collection\Python\report\kiran.pdf"
cbc_data = extract_cbc_lines(pdf_path)

# Save extracted CBC lines to a JSON file
output_json_path = r"D:\Program Collection\Python\report\test_tables.json"

with open(output_json_path, "w", encoding="utf-8") as json_file:
    json.dump(cbc_data, json_file, indent=4)

print(f"Extracted {len(cbc_data)} CBC lines and saved to {output_json_path}")

# for line in cbc_data:
#     print(line)
