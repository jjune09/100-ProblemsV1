from typing import Dict, Tuple

def highest_sales_country(sales: Dict[str, int]) -> Tuple[str, int]:
   
    if not sales:
        raise ValueError("Sales dictionary cannot be empty.")

    # ใช้ฟังก์ชันในตัว max() พร้อม key เพื่อเลือกจากค่าของยอดขาย
    country_with_max_sales = max(sales, key=sales.get)
    highest_value = sales[country_with_max_sales]

    return (country_with_max_sales, highest_value)

sales_data = {
    "Thailand": 1500,
    "Laos": 1200,
    "Vietnam": 1800,
    "Japan": 1700,
    "China": 2000
}

print(highest_sales_country(sales_data))