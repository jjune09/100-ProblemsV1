def convert_thb_to_currency(amount: float, to_currency: str) -> float:
    
    # ตรวจสอบความถูกต้องของข้อมูลนำเข้า
    if amount <= 0:
        raise ValueError("Amount must be a positive number.")
    if not isinstance(to_currency, str):
        raise TypeError("Currency code must be a string.")

    # ตารางอัตราแลกเปลี่ยน (เรตคงที่ตามโจทย์)
    exchange_rates = {
        "USD": 0.030,   # 1 THB = 0.030 USD
        "EUR": 0.027,   # 1 THB = 0.027 EUR
        "GBP": 0.023,   # 1 THB = 0.023 GBP
        "JPY": 3.4,     # 1 THB = 3.4 JPY
        "AUD": 0.045    # 1 THB = 0.045 AUD
    }

    # แปลงค่า currency code ให้เป็นตัวใหญ่เสมอ
    currency = to_currency.upper()

    if currency not in exchange_rates:
        raise ValueError(f"Unsupported currency: {to_currency}")

    # คำนวณการแปลงค่าเงิน
    converted_amount = amount * exchange_rates[currency]
    return round(converted_amount, 2)  # ปัดทศนิยม 2 ตำแหน่ง

print(convert_thb_to_currency(1000.0, "USD"))  
print(convert_thb_to_currency(1000.0, "JPY")) 
# Output: 30.0
# Output: 3400.0
