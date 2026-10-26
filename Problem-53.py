def be_to_ad(be_year: int) -> int:
    # ปกติไทยใช้ BE = AD + 543
    return be_year - 543
print(be_to_ad(2567)) 