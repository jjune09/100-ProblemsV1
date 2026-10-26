def fahrenheit_to_celsius(fahrenheit: float) -> float:
    celsius = (fahrenheit - 32) * 5 / 9
    return round(celsius, 1)  # ปัดทศนิยมให้ 1 ตำแหน่ง

def celsius_to_fahrenheit(celsius: float) -> float:
    fahrenheit = (celsius * 9 / 5) + 32
    return round(fahrenheit, 1)
print(fahrenheit_to_celsius(32))
print(celsius_to_fahrenheit(100))
# Output: 0.0
# Output: 212.0