import json
import re
from datetime import datetime
from typing import List, Dict, Any, Tuple, Optional

import pdfplumber
import pandas as pd

PDF_PATH = r"D:\Program Collection\Python\report\kiran.pdf"
OUTPUT_FILE = "output.json"

COLUMN_MAPPING = {
    "date": "date",
    "sample date": "date",
    "test": "test_name",
    "test name": "test_name",
    "parameter": "test_name",
    "result": "value",
    "value": "value",
    "units": "unit",
    "unit": "unit",
    "ref range": "ref_range",
    "reference range": "ref_range",
    "biological ref interval": "ref_range",
    "flag": "flag",
    "status": "flag",
}

DATE_FORMATS = ["%d-%m-%Y", "%d/%m/%Y", "%Y-%m-%d", "%d-%b-%Y"]

def parse_date(date_str: str) -> Optional[datetime.date]:
    if not isinstance(date_str, str):
        return None
    for fmt in DATE_FORMATS:
        try:
            return datetime.strptime(date_str.strip(), fmt).date()
        except ValueError:
            continue
    return None

def parse_numeric(value: Any) -> Optional[float]:
    if value is None:
        return None
    s = re.sub(r"[,*#^\s]+$", "", str(value).strip())
    try:
        return float(s.replace(",", ""))
    except ValueError:
        return None

def parse_range(ref_range: Any) -> Tuple[Optional[float], Optional[float]]:
    if not isinstance(ref_range, str):
        return None, None
    nums = re.findall(r"[-+]?\d*\.?\d+", ref_range.strip())
    if "<" in ref_range and nums:
        return None, float(nums[0])
    if ">" in ref_range and nums:
        return float(nums[0]), None
    if len(nums) >= 2:
        return float(nums[0]), float(nums[1])
    if len(nums) == 1:
        return None, float(nums[0])
    return None, None

def extract_tables_from_pdf(pdf_path: str) -> List[Dict[str, Any]]:
    tables = []
    with pdfplumber.open(pdf_path) as pdf:
        for page_num, page in enumerate(pdf.pages, start=1):
            for table in page.extract_tables():
                if table and len(table) >= 2:
                    tables.append({"page": page_num, "rows": table})
    return tables

def normalize_header_row(row: List[Any]) -> Tuple[str, ...]:
    return tuple(str(cell or "").strip().lower() for cell in row)

def stitch_tables_across_pages(tables) -> List[Dict[str, Any]]:
    stitched, current = [], None
    for t in tables:
        header = normalize_header_row(t["rows"][0])
        if not current:
            current = {"header": header, "rows": t["rows"].copy(), "pages": [t["page"]]}
        elif header == current["header"]:
            current["rows"].extend(t["rows"][1:])
            current["pages"].append(t["page"])
        else:
            stitched.append(current)
            current = {"header": header, "rows": t["rows"].copy(), "pages": [t["page"]]}
    if current:
        stitched.append(current)
    return stitched

def normalize_column_name(col: Any) -> str:
    return COLUMN_MAPPING.get(str(col or "").strip().lower(), str(col or "").strip().lower())

def tables_to_records(stitched_tables) -> List[Dict[str, Any]]:
    all_records = []
    for t in stitched_tables:
        rows = t["rows"]
        if len(rows) < 2:
            continue
        header = rows[0]
        body = rows[1:]
        df = pd.DataFrame(body, columns=[normalize_column_name(c) for c in header])
        df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)
        all_records.extend(df.to_dict(orient="records"))
    return all_records

def group_by_test(records):
    grouped = {}
    for rec in records:
        test = rec.get("test_name") or "UNKNOWN"
        grouped.setdefault(test, []).append(rec)
    # Optional: sort within each test by date if present
    for k in grouped:
        grouped[k].sort(key=lambda x: (x.get("date") or ""))
    return grouped

if __name__ == "__main__":
    print(f"[INFO] Reading PDF: {PDF_PATH}")
    tables = extract_tables_from_pdf(PDF_PATH)
    print(f"[INFO] Found {len(tables)} tables")

    stitched = stitch_tables_across_pages(tables)
    print(f"[INFO] Stitched into {len(stitched)} logical tables")

    records = tables_to_records(stitched)
    print(f"[INFO] Extracted {len(records)} total rows")

    # Use ALL records, not only abnormal
    grouped = group_by_test(records)

    # Small console preview
    print("[INFO] Sample records:")
    for i, (test_name, recs) in enumerate(grouped.items()):
        print(f"- {test_name}: {len(recs)} rows")
        for r in recs[:3]:
            print("  ", r)
        if i >= 5:
            break

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(grouped, f, indent=2, ensure_ascii=False)

    print(f"[INFO] Done! Results saved to {OUTPUT_FILE}")
