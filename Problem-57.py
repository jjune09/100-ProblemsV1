def compare_string_lengths(str1: str, str2: str) -> str:
   
    # ตรวจสอบความถูกต้องของข้อมูลนำเข้า
    if not str1 or not str2:
        raise ValueError("Both strings must be non-empty.")

    len1 = len(str1)
    len2 = len(str2)
    diff = abs(len1 - len2)

    if len1 > len2:
        return f"The first string is longer by {diff} character(s)."
    elif len2 > len1:
        return f"The second string is longer by {diff} character(s)."
    else:
        return "Both strings are of equal length."
print(compare_string_lengths("apple", "banana"))        
#Output: "The second string is longer by 1 character(s)."
