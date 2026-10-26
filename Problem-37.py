def print_number_pattern(rows: int) -> None:
    for i in range(1, rows + 1):
        # พิมพ์ขีดก่อน (จำนวนขีด = rows - i)
        print('-' * (rows - i), end='')
        # พิมพ์ตัวเลขจาก i ถึง 1
        for j in range(i, 0, -1):
            print(j, end='')
        print()  # ขึ้นบรรทัดใหม่
print_number_pattern(5)