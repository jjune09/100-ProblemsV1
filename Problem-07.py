def prime_number_in_ramge(number1, number2):
    deeja = ()
    prime_list = []
    sum = 0
    if 1 <= number1 <= number2 <= 10 ** 6:
        for i in range(10, 20):
            check_i = []
            for j in range(1, i):
                if i%j == 0:
                    check_i.append(j)
            if len(check_i) == 1:
                prime_list.append(i)
        for k in prime_list:
            sum = sum + k
        deeja = prime_list, sum
    print(deeja)
prime_number_in_ramge(10, 20)
# Output: ([11, 13, 17, 19], 60)