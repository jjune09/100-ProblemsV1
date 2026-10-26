from typing import Set

def build_set(inputs=None) -> Set[int]:
    # ถ้า inputs ให้มาเป็น iterable จะใช้แทน user input (ทดสอบ)
    result = set()
    if inputs is None:
        while len(result) < 5:
            try:
                v = int(input("Enter integer: "))
                result.add(v)
            except ValueError:
                print("Invalid integer, try again.")
    else:
        for v in inputs:
            result.add(int(v))
            if len(result) == 5:
                break
    return result
print(build_set([10, 20, 30, 40, 50]))