def check_prime(number):
    prime_list = []
    if number > 1:
        for i in range(1, number):
            if number%i == 0:
                prime_list.append(i)
        if len(prime_list) == 1:
            return "is prime"
        else:
            return "is not prime"
    else:
        return "is not prime"
print(check_prime(18))
# Output: is not prime(18)
# Output: is prime(17)