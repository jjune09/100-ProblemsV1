#input
start = 10
end = 25
def find_multiples_of_three(number1, number2):
    june = []

    if number1 <= number2:
        for i in range(number1, number2, 1):
            if i%3 == 0:
                june.append(i)
        return june
    else:
        return june
print(find_multiples_of_three(start, end))
# Output: [12, 15, 18, 21, 24]


    