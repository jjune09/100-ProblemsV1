def find_divisors(num: int) -> list:
    divisors = []  # สร้าง list เก็บตัวหาร
    for i in range(1, num + 1):  # วนตั้งแต่ 1 ถึง num
        if num % i == 0:  # ถ้าหารลงตัว
            divisors.append(i)  # เก็บค่า i ลงใน list
    return divisors
print(find_divisors(12))  
# Output: [1, 2, 3, 4, 6, 12]