import pdfplumber

# data = []

# with pdfplumber.open(r"D:\Program Collection\Python\report\kiran.pdf") as pdf:
#     for page in pdf.pages:
#         tables = page.extract_tables()
#         for table in tables:
#             data.append(table)

# print(data[:2000])

with pdfplumber.open(r"D:\Program Collection\Python\report\kiran.pdf") as pdf:
    for index,page in enumerate(pdf.pages,start=1):
        if index<15:
            lines=page.extract_text()
            print(lines)