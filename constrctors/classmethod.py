import datetime


class Date:
    """A custom Date class demonstrating alternative constructors"""
    
    def __init__(self, year, month, day):
        """Regular constructor - creates Date from individual values"""
        self.year = year
        self.month = month
        self.day = day
    
    @classmethod
    def from_string(cls, date_string):
        """Alternative constructor - creates Date from string format 'YYYY-MM-DD'"""
        # Note: map() returns a map object (iterator), not a list
        # That's why type shows <class 'map'>
        year, month, day = map(int, date_string.split("-"))
        return cls(year, month, day)
    
    @classmethod
    def from_today(cls):
        """Alternative constructor - creates Date from today's date"""
        today = datetime.date.today()
        return cls(today.year, today.month, today.day)
    
    # def __str__(self):
    #     """String representation for print()"""
    #     return f"{self.year}-{self.month:02d}-{self.day:02d}"
    
    # def __repr__(self):
    #     """Developer-friendly representation"""
    #     return f"Date({self.year}, {self.month}, {self.day})"
    

    
    def is_valid(self):
        """Check if the date is valid"""
        try:
            datetime.date(self.year, self.month, self.day)
            return True
        except ValueError:
            return False


if __name__ == "__main__":
    print("=" * 50)
    print("DATE CLASS DEMONSTRATION")
    print("=" * 50)
    
    # Method 1: Regular constructor
    print("\n1️⃣  Creating date using regular constructor:")
    date1 = Date(2025, 10, 5)
    print(f"   Year: {date1.year}, Month: {date1.month}, Day: {date1.day}")
    print(f"   String representation: {date1}")
    print(f"   Developer representation: {repr(date1)}")
    date1.display()
    
    # Method 2: From string (Alternative constructor)
    print("\n2️⃣  Creating date from string:")
    date2 = Date.from_string("2025-12-25")
    print(f"   Year: {date2.year}, Month: {date2.month}, Day: {date2.day}")
    print(f"   String representation: {date2}")
    date2.display()
    
    # Method 3: From today (Alternative constructor)
    print("\n3️⃣  Creating date from today:")
    date3 = Date.from_today()
    print(f"   Year: {date3.year}, Month: {date3.month}, Day: {date3.day}")
    print(f"   String representation: {date3}")
    date3.display()
    
    # Bonus: Validation
    print("\n4️⃣  Date validation:")
    invalid_date = Date(2025, 13, 45)  # Invalid date
    print(f"   Date(2025, 13, 45) is valid? {invalid_date.is_valid()}")
    print(f"   date1 is valid? {date1.is_valid()}")
    
    print("\n" + "=" * 50)
    print("✅ PROGRAM COMPLETED")
    print("=" * 50)