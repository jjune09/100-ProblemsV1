def find_divisors(num1):
    wang = []
    if not isinstance(num1, int) or num1 <= 0:
        return wang
    for i in range(1, int(num1 ** 0.5) + 1):
        if num1 % i == 0 :
            wang.append(i)
        if i != num1 // i:
            wang.append(num1 // i)
    wang.sort()
    return wang
print(find_divisors(20))
# Output: [1, 2, 4, 5, 10, 20]