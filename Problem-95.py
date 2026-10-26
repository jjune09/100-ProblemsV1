with open("students.txt", "w") as f:
    f.write("Alice,90\n")
    f.write("Bob,85\n")

# อ่านไฟล์
with open("students.txt", "r") as f:
    for line in f:
        name, score = line.strip().split(',')
        print(f"{name} scored {score}")

# เขียนต่อท้ายไฟล์
with open("students.txt", "a") as f:
    f.write("Charlie,88\n")

# อ่านทั้งหมดอีกครั้ง
with open("students.txt") as f:
    print("All data:\n", f.read())