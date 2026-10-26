def toggle_case(s: str) -> str:
    result = []
    for ch in s:
        if ch.islower():
            result.append(ch.upper())
        elif ch.isupper():
            result.append(ch.lower())
        else:
            result.append(ch)
    return ''.join(result)
print(toggle_case("Hello World!"))      
print(toggle_case("Python3.9"))         
print(toggle_case("123 ABC xyz!?"))     
print(toggle_case(""))                 
