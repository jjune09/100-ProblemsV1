#input
start = 10
end = 25
def find_non_multiples(number1, number2):
    june = []

    if number1 <= number2:
        for i in range(number1, number2, 1):
            if i%3 != 0 and i%4 != 0 and i%5 != 0 :
                june.append(i)
        return june
    else:
        return june
print(find_non_multiples(start, end))
# Output: [11, 13, 14, 16, 17, 19, 22, 23]


    