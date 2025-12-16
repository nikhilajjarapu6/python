import camelot

pdf_path = r"D:\Program Collection\Python\report\kiran.pdf"

# Extract tables
tables = camelot.read_pdf(pdf_path, pages='7-9', flavor='lattice') 

print(f"Total tables found: {tables.n}")

# Print each table
for idx, table in enumerate(tables):
    print(f"\n=== Table {idx+1} ===")
    print(table.df.to_string(index=False))  # clean print without index
