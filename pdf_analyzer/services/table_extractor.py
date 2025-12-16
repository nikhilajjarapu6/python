import os
import json
import pdfplumber
from services.table_validator import TableValidator

class TableExtractor:

    def __init__(self, validator: TableValidator = TableValidator()):
        self.validator = validator

    def extract(self, pdf_path: str, cache_path: str = "tables_cache.json"):
        """
        Extracts tables from PDF.
        If JSON cache exists, loads and returns that instead.
        """

        # 1) Use cache if exists
        if os.path.exists(cache_path):
            print("✔ Loaded tables from cache JSON")
            with open(cache_path, "r", encoding="utf-8") as f:
                return json.load(f)

        print("⏳ Extracting tables from PDF...")
        rows = []

        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                for table in page.extract_tables():

                    if not self.validator.is_valid(table):
                        continue

                    headers = [str(h).strip() for h in table[0]]

                    for row in table[1:]:
                        rows.append({
                            headers[i]: row[i] if i < len(row) else None
                            for i in range(len(headers))
                        })

        # 2) Save cache
        with open(cache_path, "w", encoding="utf-8") as f:
            json.dump(rows, f, indent=2, ensure_ascii=False)

        print("✔ Saved extracted tables to", cache_path)
        return rows
