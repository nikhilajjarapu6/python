import re
text="QWERTYUIOP asdfghjkl zxcvbnm !@#$%^&*() h1234567890 ,./;'[]\ Hello world 13.59" 

print(re.findall(r"\w",text))  #except special charecters and space
print(re.findall(r"[a-z]",text))  #only lower caase
print(re.findall(r"[A-Z]",text))  #only upper case
print(re.findall(r"\d",text))     #only digits
print(re.findall(r"\s",text))     #space chars
print(re.findall(r"[^a-zA-Z0-9\s]",text)) #only special chars  [^\w\s]
print("5. Complete words:", re.findall(r'\b\w+\b', text))
print("6. Words starting with a-z:", re.findall(r'\b[a-z]\w+\b', text))
print("7. Words starting with A-Z:", re.findall(r'\b[A-Z]\w*\b', text))
print("8. Special characters:", re.findall(r'[^\w\s]', text))
print("9. Only symbols:", re.findall(r'[!@#$%^&*(),./;\'\[\]]', text))
print("10. 2+ uppercase:", re.findall(r'[A-Z]{2,}', text))
print("11. 3+ lowercase:", re.findall(r'[a-z]{3,}', text))
print("12. Number sequences:", re.findall(r'\d+', text))

text = "Glucose: 98.76 mg/dL"
pattern = r"Glucose:\s*\d+\.?\d*\s*mg/dL|MG/DL"
print("Or usage :",re.findall(pattern,text,re.IGNORECASE))
print("13.ignore case :",re.findall(r"glucose:\s*\d+\.\d*\s*mg/dl",text,re.IGNORECASE))
print("14.extracting decimeals:",re.findall(r"\d+\.?\d*",text))

