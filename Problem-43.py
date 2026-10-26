from typing import Tuple

def calculate_coins(amount: int) -> Tuple[int, int, int, int]:
    
    if amount <= 0:
        raise ValueError("Amount must be a positive integer.")

    # เหรียญแต่ละชนิด
    coins = [10, 5, 2, 1]
    counts = []

    # ทำการแลกโดยใช้ greedy algorithm
    for c in coins:
        count = amount // c   # จำนวนเหรียญชนิดนี้ที่ใช้ได้
        counts.append(count)
        amount %= c           # เหลือเงินที่ต้องแลกต่อ

    # คืนผลลัพธ์เป็น tuple (10s, 5s, 2s, 1s)
    return tuple(counts)

print(calculate_coins(28))