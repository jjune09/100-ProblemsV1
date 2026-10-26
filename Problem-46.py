def calculate_perimeter(a: float, b: float, c: float) -> float:
    # ตรวจสอบค่าที่ถูกต้อง
    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError("Side lengths must be positive numbers.")

    # ตรวจสอบเงื่อนไขสามเหลี่ยม: ผลรวมของสองด้านต้องมากกว่าด้านที่สาม
    if not (a + b > c and a + c > b and b + c > a):
        raise ValueError("Invalid triangle sides. Must satisfy triangle inequality.")

    # คำนวณเส้นรอบรูป
    perimeter = a + b + c
    return perimeter

print(calculate_perimeter(3, 4, 5))