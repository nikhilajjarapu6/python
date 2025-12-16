# app/services/header_extractor.py
import re
from config.constants import TEST_NAMES

class HeaderExtractor:
    """Extracts test headings (name, date, time) from PDF text."""

    # Escape test names for regex
    ESCAPED = [re.escape(t) for t in TEST_NAMES]

    TEST_PATTERN = re.compile(
        rf"(?P<test>{'|'.join(ESCAPED)})",
        re.IGNORECASE
    )

    HEADER_WITH_DATETIME = re.compile(
        r"(?P<date>\d{1,2}-\d{1,2}-\d{4}).{0,20}?(?P<time>\d{1,2}:\d{2})",
        re.DOTALL
    )

    @classmethod
    def extract_headers(cls, text: str):
        matches = list(cls.TEST_PATTERN.finditer(text))
        results = []

        for i, match in enumerate(matches):
            test_name = match.group("test").strip()

            start = match.start()
            end = matches[i+1].start() if i + 1 < len(matches) else len(text)

            chunk = text[start:end]

            dt_match = cls.HEADER_WITH_DATETIME.search(chunk)
            if not dt_match:
                continue

            results.append({
                "test_name": test_name,
                "date": dt_match.group("date"),
                "time": dt_match.group("time")
            })

        return results
