def add(a: float, b: float) -> float:
    return a + b

def subtract(a: float, b: float) -> float:
    return a - b

def multiply(a: float, b: float) -> float:
    return a * b

def divide(a: float, b: float) -> float:
    if b == 0:
        print("Error: Division by zero!")
        return None
    return a / b
print(add(5, 3))       # 8
print(subtract(5, 3))  # 2
print(multiply(5, 3))  # 15
print(divide(6, 3))    # 2.0
print(divide(6, 0))    # Error