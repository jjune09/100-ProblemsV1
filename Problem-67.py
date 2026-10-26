from datetime import date
from typing import Tuple

def calculate_age(day_of_birth: int, month_of_birth: int, year_of_birth: int) -> Tuple[int, int, int]:
    # วันที่ปัจจุบัน
    today = date.today()
    
    # วันที่เกิด
    birth_date = date(year_of_birth, month_of_birth, day_of_birth)
    
    # เริ่มคำนวณส่วนต่างเบื้องต้น
    years = today.year - birth_date.year
    months = today.month - birth_date.month
    days = today.day - birth_date.day

    # ปรับกรณีวันที่ติดลบ (ต้องยืมจากเดือนก่อนหน้า)
    if days < 0:
        months -= 1
        # หาวันสุดท้ายของเดือนก่อนหน้า
        prev_month = today.month - 1 if today.month > 1 else 12
        prev_year = today.year if today.month > 1 else today.year - 1
        days_in_prev_month = (date(prev_year, prev_month + 1, 1) - date(prev_year, prev_month, 1)).days
        days += days_in_prev_month

    # ปรับกรณีเดือนติดลบ (ต้องยืมจากปี)
    if months < 0:
        months += 12
        years -= 1

    return (years, months, days)
print(calculate_age(15, 8, 1990))
print(calculate_age(10, 3, 2000))
# Output: (33, 10, 2)  # Assuming today's date is 2024-06-17
# Output: (24, 3, 7)   # Assuming today's date is