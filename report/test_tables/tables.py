import pdfplumber
import json

def is_valid_table(table):
    if not table or len(table) < 2:
        return False

    header = table[0]

    if len(header) == 1:
        return False
    
    header_text = " ".join(str(h).upper() for h in header)
    valid_keywords = ["PARAMETER", "TEST", "RESULT", "VALUE", "RANGE"]


    keyword_found = False
    for k in valid_keywords:
        if k in header_text:
            keyword_found = True
            break

    if not keyword_found:
        return False


    return True


def extract_tables_from_pdf(pdf_path):
    all_tables = []

    with pdfplumber.open(pdf_path) as pdf:
        for page_num, page in enumerate(pdf.pages, start=1):
            tables = page.extract_tables()

            for table_num, table in enumerate(tables, start=1):

                # FILTER GARBAGE TABLES
                if not is_valid_table(table):
                    continue

                headers = [str(h).strip() for h in table[0]]
                rows = table[1:]

                for row in rows:
                    row_dict = {
                        headers[i]: (row[i] if i < len(row) else None)
                        for i in range(len(headers))
                    }
                    all_tables.append(row_dict)

    return all_tables


def save_to_json(data, output_path):
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)


if __name__ == "__main__":
    pdf_path = r"D:\Program Collection\Python\report\kiran.pdf"
    # output_json_path = r"D:\Program Collection\Python\report\test_tables.json"
    output_json_path = r"D:\Program Collection\Python\report\result_data\test_tables.json"

    tables_data = extract_tables_from_pdf(pdf_path)
    save_to_json(tables_data, output_json_path)

    print(f"Extracted {len(tables_data)} rows from tables and saved to {output_json_path}")
