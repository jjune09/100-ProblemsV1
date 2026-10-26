def check_membership(s: set, value: str) -> bool:
    """
    ตรวจสอบว่า value อยู่ในเซต s หรือไม่
    Return True ถ้ามีอยู่, False ถ้าไม่มี
    """
    return value in s

s = {1, 2, 3, 'a', 'e', 'i', 'o', 'u', "red", "green", "blue"}
print(check_membership(s, 2))       
print(check_membership(s, 'a'))         
print(check_membership(s, 'yellow'))