def convert_currency(amount: float, from_currency: str, to_currency: str) -> float:
   
    #ตรวจสอบค่าป้อนเข้าพื้นฐาน
    if amount <= 0:
        raise ValueError("Amount must be a positive number.")
    if not (isinstance(from_currency, str) and isinstance(to_currency, str)):
        raise TypeError("Currency codes must be strings.")

    # อัตราแลกเปลี่ยนเทียบกับ 1 USD ตามโจทย์
    # หมายความว่า 1 USD = X ของสกุลอื่น ๆ
    usd_rates = {
        "USD": 1.0,
        "EUR": 0.85,
        "GBP": 0.75,
        "JPY": 110.0,
        "THB": 32.0
    }

    # แปลงเป็นตัวพิมพ์ใหญ่เสมอ
    from_currency = from_currency.upper()
    to_currency = to_currency.upper()

    # ตรวจสอบสกุลเงินที่รองรับ
    if from_currency not in usd_rates or to_currency not in usd_rates:
        raise ValueError("Unsupported currency code.")

    # ขั้นตอนการแปลงค่า
    # แปลงจากสกุลต้นทาง → USD
    amount_in_usd = amount / usd_rates[from_currency]

    # แปลงจาก USD → สกุลปลายทาง
    converted = amount_in_usd * usd_rates[to_currency]

    return round(converted, 2)
# Example 1
print(convert_currency(100.0, "USD", "EUR"))   # Output: 85.0
# Example 2
print(convert_currency(1000.0, "JPY", "THB"))  # Output: 290.91

