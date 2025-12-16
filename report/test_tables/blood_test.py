import json
import pandas as pd
import re
from headers_extraction import extract_from_pdf,extract_test_headers


CBC_PARAMS = [
    "HAEMOGLOBIN",
    "HAEMATOCRIT(PCV)",
    "RBC COUNT",
    "WBC COUNT",
    "PLATELET COUNT",
    "MEAN CELL VOLUME (MCV)",
    "MEAN CELL HAEMOGLOBIN (MCH)",
    "MEAN CELL HAEMOGLOBIN CONCENTRATION (MCHC)",
    "RDW - CV",
    # "BLASTS",
    # "PROMYELOCYTES",
    # "MYELOCYTES",
    # "METAMYELOCYTES",
    # "BAND FORMS",
    "POLYMORPHS",
    "LYMPHOCYTES",
    "EOSINOPHILS",
    "MONOCYTES",
    # "BASOPHILS",
    # "PROLYMPHOCYTES",
    # "ABNORMAL CELLS / PLASMA CELLS",
    # "ATYPICAL CELLS",
    # "REACTIVE LYMPHOCYTES",
    # "COMMENT",
    # "NOTE"
]


with open(r"D:\Program Collection\Python\report\test_tables.json", "r", encoding="utf-8") as f:
    table_rows = json.load(f)

df = pd.DataFrame(table_rows)

df.columns = [col.strip().upper() for col in df.columns]

# Normalize PARAMETER column (merge multiline names, upper-case)
df['PARAMETER'] = df['PARAMETER'].fillna('').str.upper().str.replace("\n", " ").str.strip()


CBC_PARAMS_UPPER = [p.upper() for p in CBC_PARAMS]

# Filter only CBC rows
df_cbc = df[df['PARAMETER'].isin(CBC_PARAMS_UPPER)].copy()
df_cbc.reset_index(drop=True, inplace=True)

# Save filtered CBC JSON
df_cbc.to_json(r"D:\Program Collection\Python\report\result_data\cbc_filtered.json", orient='records', indent=4)
print("Filtered CBC rows:")
print(df_cbc)


def merge_headings(pdf_path:str,df_cbc:pd.DataFrame):
    full_text = extract_from_pdf(pdf_path)
    headings = extract_test_headers(full_text)
    cbc_headings = [
        h for h in headings
        if h["test_name"].upper() in [
            "COMPLETE BLOOD COUNT",
            "COMPLETE BLOOD PICTURE"
        ]
    ]
    sections = []
    heading_idx = 0
    section = None

    for idx, row in df_cbc.iterrows():
        param = row["PARAMETER"].upper().strip()

        if param == "HAEMOGLOBIN":
            # Start a new section
            if heading_idx < len(cbc_headings):
                heading = cbc_headings[heading_idx]
                heading_idx += 1
            else:
                heading = {"test_name": "COMPLETE BLOOD COUNT", "date": None, "time": None}

            section = {
                "test_name": heading["test_name"],
                "date": heading["date"],
                "time": heading["time"],
                "properties": []
            }
            sections.append(section)

        # Append current row to the current section
        if section is not None:
            section["properties"].append({
                "PARAMETER": row["PARAMETER"],
                "RESULT": row["RESULT"],
                "NORMAL RANGE": row["NORMAL RANGE"]
            })

    return sections


def extract_out_of_range(df_cbc: pd.DataFrame):
 
    out_of_range_rows = []

    for idx, row in df_cbc.iterrows():
        result = str(row['RESULT']).strip()
        normal_range = str(row['NORMAL RANGE']).strip()

        if normal_range.lower() in ('', 'null', 'na', 'none'):
            continue

        # Extract numeric value from Result (first number found)
        result_match = re.search(r"[-+]?\d*\.?\d+", result.replace(",", ""))
        if not result_match:
            continue
        result_value = float(result_match.group())

        # Extract numeric range
        range_match = re.findall(r"[-+]?\d*\.?\d+", normal_range.replace(",", ""))
        if len(range_match) == 2:
            lower = float(range_match[0])
            upper = float(range_match[1])
        else:
            continue  

        if result_value < lower:
            flag = "LOW"
        elif result_value > upper:
            flag = "HIGH"
        else:
            continue  

        flagged_row = row.copy()
        flagged_row["FLAG"] = flag

        out_of_range_rows.append(flagged_row)

    return pd.DataFrame(out_of_range_rows)


df_out_of_range = extract_out_of_range(df_cbc)
df_out_of_range.reset_index(drop=True, inplace=True)


df_out_of_range.to_json(r"D:\Program Collection\Python\report\result_data\cbc_out_of_range.json",
                        orient='records', indent=4)

# print("Out-of-range CBC rows:")
# print(df_out_of_range)
# pdf_path = r"D:\Program Collection\Python\report\kiran.pdf"   
pdf_path=r"D:\Program Collection\Python\report_analysis copy\data\raw\KIMS _ EHR (19).pdf"
merged_cbc = merge_headings(pdf_path,df_cbc)

# Save to JSON
with open("merged_cbc.json", "w", encoding="utf-8") as f:
    json.dump(merged_cbc, f, indent=4, ensure_ascii=False)
