def calculate_speeding_fine(speed: float, speed_limit: float) -> str:
    # คำนวณส่วนต่างความเร็วที่เกินจากกำหนด
    over_speed = speed - speed_limit

    # ถ้าไม่เกินหรือเท่ากับขีดจำกัด -> ไม่โดนปรับ
    if over_speed <= 0:
        return "No fine."

    # ตรวจสอบช่วงความเร็วที่เกิน และกำหนดค่าปรับ
    if 90 <= over_speed <= 120:
        fine = 500
    elif 121 <= over_speed <= 140:
        fine = 1000
    elif 141 <= over_speed <= 160:
        fine = 1500
    elif over_speed > 160:
        fine = 2000
    else:
        # ถ้าเกินน้อยกว่า 90 ถือว่าไม่โดนปรับ
        return "No fine."

    return f"Fine: {fine} Baht"
print(calculate_speeding_fine(141, 60)) # Output: Fine: 1500 Baht
print(calculate_speeding_fine(200, 100)) # Output: Fine: 2000 Baht
