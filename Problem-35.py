def print_diamond_pattern(n: int) -> None:
    """
    พิมพ์ diamond pattern ที่กว้างที่สุดมี n ดาว
    (ขึ้นจาก 1 ถึง n แล้วลงจาก n-1 ถึง 1)
    """
    # ขึ้น: 1..n
    for i in range(1, n + 1):
        print('*' * i)
    # ลง: n-1..1
    for i in range(n - 1, 0, -1):
        print('*' * i)

print_diamond_pattern(3)