def calculate_jumps(d: int, s: int) -> int:
    if d <= 0 or s <= 0:
        raise ValueError("Distances must be positive integers.")
    # ถ้ d <= s ต้องการ 1 ครั้งตามโจทย์
    # มิฉะนั้น คำนวณขึ้น/ปัดขึ้น: (d + s - 1) // s
    return 1 if d <= s else (d + s - 1) // s
print(calculate_jumps(d = 20, s = 7))