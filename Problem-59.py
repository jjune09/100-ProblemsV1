from datetime import datetime

def days_between_dates(date1: str, date2: str) -> int:
    fmt = "%Y-%m-%d"
    d1 = datetime.strptime(date1, fmt)
    d2 = datetime.strptime(date2, fmt)
    return abs((d2 - d1).days)
print(days_between_dates("2024-08-01", "2024-08-10"))