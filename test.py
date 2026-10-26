def find_multiples_of_three(start: int, end: int) -> list:
    if start > end:
        return []
    # เริ่มจากจำนวนถัดไปที่หารด้วย 3 ลงตัว (ไม่จำเป็นต้องเช็กทีละตัว)
    first = start if start % 3 == 0 else start + (3 - start % 3)
    return list(range(first, end + 1, 3))
print(find_multiples_of_three(10, 25))