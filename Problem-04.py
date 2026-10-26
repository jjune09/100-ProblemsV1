def calculate_sum_and_average():
    deejai = []
    sum = 0
    average = 0

    for i in range(1, 6, 1):
        apple = float(input(f'Enter number {i}'))
        deejai.append(apple)
    for i in deejai:
        sum = sum = i
    average = sum / len(deejai)
    print(f'sum = {sum} \nAverage = {average}')
calculate_sum_and_average()

