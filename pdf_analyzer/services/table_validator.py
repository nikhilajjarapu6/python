# app/services/table_validator.py

class TableValidator:
    """Validates extracted PDF tables."""

    VALID_KEYWORDS = ["PARAMETER", "TEST", "RESULT", "VALUE", "RANGE"]

    @staticmethod
    def is_valid(table) -> bool:
        if not table or len(table) < 2:
            return False

        header = table[0]

        if len(header) == 1:
            return False  # garbage table

        header_text = " ".join(str(h).upper() for h in header)

        return any(k in header_text for k in TableValidator.VALID_KEYWORDS)
