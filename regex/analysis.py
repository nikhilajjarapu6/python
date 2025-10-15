import re

import pdfplumber
import re

# 1. Read PDF text
with pdfplumber.open(r"D:\Program Collection\Python\regex\sample_blood_report.pdf.pdf") as pdf:
    text = pdf.pages[0].extract_text()

# 2. Split into lines
lines = [line.strip() for line in text.splitlines() if line.strip()]

# 3. Prepare a dictionary to store results
fields = {
    "Name": "",
    "Age": "",
    "Sex": "",
    "Ref. Doctor": "",
    "Report Date": "",
    "Lab Id": "",
    "Sample Type": ""
}

# 4. Go line by line and apply rules
for line in lines:
    # ---- Name ----
    if line.lower().startswith("name"):
        parts = line.split(":")
        if len(parts) > 1:
            fields["Name"] = parts[1].strip()

    # ---- Age/Sex ----
    elif "sex" in line.lower() and "/" in line:
        value = line.split(":")[-1].strip()
        if "/" in value:
            age, sex = value.split("/")
            fields["Age"], fields["Sex"] = age.strip(), sex.strip()
        else:
            fields["Age/Sex"] = value

    # ---- Ref. Doctor ----
    elif "ref" in line.lower() and "doctor" in line.lower():
        fields["Ref. Doctor"] = line.split(":")[-1].strip()

    # ---- Report Date ----
    elif "date" in line.lower():
        date_match = re.search(r"\d{1,2}[-/][A-Za-z]{3,}[-/]\d{4}", line)
        if date_match:
            fields["Report Date"] = date_match.group()

    # ---- Lab Id ----
    elif "lab id" in line.lower():
        fields["Lab Id"] = line.split(":")[-1].strip()

    # ---- Sample Type ----
    elif "sample type" in line.lower():
        fields["Sample Type"] = line.split(":")[-1].strip()

# 5. Print results
for key, value in fields.items():
    print(f"{key}: {value}")
