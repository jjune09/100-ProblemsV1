from typing import Dict, List, Tuple
def calculate_median(provinces: Dict[str, int]) -> List[Tuple[str, int]]:
    if not provinces:
        return []
    # 1️⃣ ดึงค่าจำนวนจังหวัดทั้งหมดออกมา
    values = sorted(provinces.values())
    n = len(values)
    mid = n // 2
    
    # 2️⃣ คำนวณ median
    if n % 2 == 1:
        median = values[mid]
    else:
        median = (values[mid - 1] + values[mid]) / 2

    # 3️⃣ คืนประเทศที่มีค่าจำนวนจังหวัดเท่ากับ median
    return [(country, count) for country, count in provinces.items() if count == median]
data = {
    'Thailand': 76,
    'Laos': 17,
    'Vietnam': 58,
    'Japan': 47,
    'China': 23
}

print(calculate_median(data))