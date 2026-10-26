# ตัวแปรเก็บข้อมูลรายรับและรายจ่าย
income_entries = []
expense_entries = []

# ฟังก์ชันเพิ่มรายรับ
def add_income(amount: float, description: str) -> None:
    if amount <= 0:
        print("Error: Amount must be positive.")
        return
    if not description:
        print("Error: Description cannot be empty.")
        return
    income_entries.append((description, amount))
    print(f"Income added: {description} ({amount} Baht)")

# ฟังก์ชันเพิ่มรายจ่าย
def add_expense(amount: float, description: str) -> None:
    if amount <= 0:
        print("Error: Amount must be positive.")
        return
    if not description:
        print("Error: Description cannot be empty.")
        return
    expense_entries.append((description, amount))
    print(f"Expense added: {description} ({amount} Baht)")

# แสดงรายการรายรับ
def display_income_entries() -> None:
    if not income_entries:
        print("No income entries yet.")
    else:
        print("\n=== Income Entries ===")
        for desc, amt in income_entries:
            print(f"{desc}: {amt:.2f} Baht")

# แสดงรายการรายจ่าย
def display_expense_entries() -> None:
    if not expense_entries:
        print("No expense entries yet.")
    else:
        print("\n=== Expense Entries ===")
        for desc, amt in expense_entries:
            print(f"{desc}: {amt:.2f} Baht")

# คำนวณยอดคงเหลือ
def calculate_balance() -> float:
    total_income = sum(amount for _, amount in income_entries)
    total_expense = sum(amount for _, amount in expense_entries)
    balance = total_income - total_expense
    print(f"\n Current Balance: {balance:.2f} Baht")
    return balance
add_income(1000.0, "Salary")
add_income(500.0, "Freelance")
add_expense(150.0, "Groceries")
add_expense(100.0, "Transport")

display_income_entries()
display_expense_entries()

balance = calculate_balance()
print("Final Balance =", balance)