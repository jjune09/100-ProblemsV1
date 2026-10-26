fruit = ["apple", "banana", "cherry", "date", "elderberry"]

def average_length_of_strings(all_fruit):
    lenghts = []
    sum_len = 0
    for i in all_fruit:
        sum_j = 0
        for j in range(0, len(i)):
            sum_j = sum_j + 1
        lenghts.append(sum_j)
    for k in lenghts:
        sum_len = sum_len + k
    print(sum_len/5)
average_length_of_strings(fruit) 
# Output: 6.2
