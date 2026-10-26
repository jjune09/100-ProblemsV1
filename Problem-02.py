#input
start = 10
end = 50
def find_multiples_of_three_and_four(number1, number2):
    june = []

    if number1 <= number2:
        for i in range(number1, number2, 1):
            if i%12 == 0:
                june.append(i)
        return june
    else:
        return june
print(find_multiples_of_three_and_four(start, end))
# Output: [12, 24, 36, 48]


    