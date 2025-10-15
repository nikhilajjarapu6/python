import re


with open(r"D:\Program Collection\Python\regex\report.txt") as file:
    text=file.read()

pattern = (
    r"(?P<label>Patient\s*Name|Age\/Sex|Ref\.?\s*Doctor|Report\s*Date|Hospital)"
    r"\s*[:\-]\s*"
    r"(?P<value>.*?)(?=\s*(?:Patient\s*Name|Age\/Sex|Ref\.?\s*Doctor|Report\s*Date|Hospital|$))"
)

matches = re.finditer(pattern, text, re.IGNORECASE | re.DOTALL)
info = {}
for match in matches:
    label = match.group('label').strip()
    value = match.group('value').strip()
    info[label] = value

for k, v in info.items():
    print(f"{k}: {v}")