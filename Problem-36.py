def print_diamond_hyphens(n: int) -> None:
    """
    พิมพ์ diamond-shaped pattern ที่แต่ละแถวเป็น '...', '-'...'-', '...'
    n ต้องเป็นจำนวนคู่ (even)
    """
    if n % 2 != 0:
        raise ValueError("n ต้องเป็นจำนวนคู่ (even) ตามโจทย์")

    half = n // 2
    # สร้าง list ของบรรทัดครึ่งบน (รวมกึ่งกลาง)
    lines = []
    for i in range(0, half):
        left = half - i            # จำนวนดาวด้านซ้าย/ขวา
        middle = n - 2*left        # จำนวน hyphen ตรงกลาง
        lines.append('' * left + '-' * middle + '' * left)

    # พิมพ์ครึ่งบน
    for line in lines:
        print(line)
    # พิมพ์ครึ่งล่าง (mirror) — รวมกึ่งกลางแล้วสะท้อน
    for line in reversed(lines):
        print(line)

print_diamond_hyphens(10)