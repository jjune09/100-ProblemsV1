with open("sales.txt", "w") as file:
    total = 0
    for line in file:
        total += float(line.strip())
print(f"Total sales = {total}")