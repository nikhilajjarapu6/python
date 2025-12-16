import tabula

pdf_path = r"D:\Program Collection\Python\report\kiran.pdf"

# Extract tables from all pages
tables = tabula.read_pdf(pdf_path, pages="all", multiple_tables=True)

print(f"Total tables found: {len(tables)}")

for idx, table in enumerate(tables, start=1):
    print(f"\n===== TABLE {idx} =====")
    print(table)  # or: print(table.to_string())
