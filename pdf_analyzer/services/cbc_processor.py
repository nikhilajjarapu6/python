# app/services/cbc_processor.py
import re
import pandas as pd
from services.header_extractor import HeaderExtractor

class CBCProcessor:

    def __init__(self, cbc_params: list):
        self.cbc_params = [p.upper() for p in cbc_params]

    def filter_cbc(self, table_rows: list):
        df = pd.DataFrame(table_rows)
        df.columns = [c.strip().upper() for c in df.columns]

        if "PARAMETER" not in df.columns:
            return pd.DataFrame()

        df["PARAMETER"] = df["PARAMETER"].fillna("").str.upper()
        return df[df["PARAMETER"].isin(self.cbc_params)].reset_index(drop=True)

    def extract_out_of_range(self, df_cbc):
        out_rows = []

        for idx, row in df_cbc.iterrows():
            result = str(row.get("RESULT", "")).strip()
            normal_range = str(row.get("NORMAL RANGE", "")).strip()

            nums = re.findall(r"[-+]?\d*\.?\d+", result)
            if not nums:
                continue

            result_value = float(nums[0])

            range_nums = re.findall(r"[-+]?\d*\.?\d+", normal_range)
            if len(range_nums) != 2:
                continue

            lower, upper = map(float, range_nums)

            if result_value < lower:
                flag = "LOW"
            elif result_value > upper:
                flag = "HIGH"
            else:
                continue

            flagged = row.copy()
            flagged["FLAG"] = flag
            out_rows.append(flagged)

        return pd.DataFrame(out_rows)

    def merge_headings(self, pdf_path: str, df_cbc):
        text = HeaderExtractor.read_pdf_text(pdf_path) \
               if hasattr(HeaderExtractor, "read_pdf_text") else None

        headings = HeaderExtractor.extract_headers(text)

        cbc_headings = [
            h for h in headings
            if h["test_name"].upper() in ("COMPLETE BLOOD COUNT", "COMPLETE BLOOD PICTURE")
        ]

        sections = []
        h_idx = 0
        section = None

        for idx, row in df_cbc.iterrows():
            param = row["PARAMETER"]

            if param == "HAEMOGLOBIN":
                heading = cbc_headings[h_idx] if h_idx < len(cbc_headings) else {
                    "test_name": "COMPLETE BLOOD COUNT",
                    "date": None,
                    "time": None
                }
                h_idx += 1

                section = {
                    "test_name": heading["test_name"],
                    "date": heading["date"],
                    "time": heading["time"],
                    "properties": []
                }
                sections.append(section)

            if section:
                section["properties"].append({
                    "PARAMETER": row["PARAMETER"],
                    "RESULT": row.get("RESULT"),
                    "NORMAL RANGE": row.get("NORMAL RANGE")
                })

        return sections
