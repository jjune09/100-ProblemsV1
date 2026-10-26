with open("employee.txt", "w") as f:
    while True:
        name = input("Enter name (or quit): ")
        if name.lower() == "quit":
            break
        salary = input("Enter salary: ")
        f.write(f"{name},{salary}\n")