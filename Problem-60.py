def calculate_parking_fee(hours: int, minutes: int) -> int:
    if hours < 0 or minutes < 0:
        raise ValueError("Non-negative required.")
    # แปลงเป็นจำนวนชั่วโมงทั้งหมด (ปัดขึ้นทุกเศษ)
    extra_full_hours = 0
    # ถ้าจอด <= 1 ชั่วโมง -> ฟรี
    total_minutes = hours * 60 + minutes
    if total_minutes <= 60:
        return 0
    # คำนวณนาทีที่เกินจาก 1 ชั่วโมงแรก
    remaining_minutes = total_minutes - 60
    # จำนวนชั่วโมงที่จะคิดค่าบริษัท (ปัดขึ้น)
    charge_hours = (remaining_minutes + 59) // 60
    return charge_hours * 50
print(calculate_parking_fee(1, 30)) 