def calculate_rectangle_area(width: float, length: float) -> float:
    """
    คำนวณพื้นที่ของสี่เหลี่ยมผืนผ้า
    พารามิเตอร์:
        width (float): ความกว้าง
        length (float): ความยาว
    คืนค่า:
        float: พื้นที่ของสี่เหลี่ยมผืนผ้า
    """
    # ตรวจสอบว่าค่าทั้งสองต้องเป็นบวก
    if width <= 0 or length <= 0:
        raise ValueError("Width and length must be positive numbers greater than 0.")

    # สูตรคำนวณพื้นที่
    area = width * length
    return float(area)

print(calculate_rectangle_area(5, 10)) 