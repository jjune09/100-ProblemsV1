def bank_account_management():
    balance = 0  # เริ่มต้นยอดเงินเป็น 0

    while True:
        print("\n===== BANK ACCOUNT MANAGEMENT SYSTEM =====")
        print("1. Deposit Money")
        print("2. Withdraw Money")
        print("3. Check Balance")
        print("4. Exit Program")
        print("==========================================")

        # รับค่าจากผู้ใช้
        choice = input("Enter your choice (1-4): ")

        #  ฝากเงิน
        if choice == "1":
            try:
                amount = float(input("Enter amount to deposit: "))
                if amount <= 0:
                    print(" Amount must be positive.")
                else:
                    balance += amount
                    print(f" Deposit successful. Current Balance: {balance:.2f} Baht")
            except ValueError:
                print(" Invalid input. Please enter a number.")

        #  ถอนเงิน
        elif choice == "2":
            try:
                amount = float(input("Enter amount to withdraw: "))
                if amount <= 0:
                    print(" Amount must be positive.")
                elif amount > balance:
                    print(" Insufficient balance. Withdrawal not allowed.")
                else:
                    balance -= amount
                    print(f" Withdrawal successful. Current Balance: {balance:.2f} Baht")
            except ValueError:
                print(" Invalid input. Please enter a number.")

        # ตรวจสอบยอดเงิน
        elif choice == "3":
            print(f" Current Balance: {balance:.2f} Baht")

        # ออกจากโปรแกรม
        elif choice == "4":
            print(" Thank you for using the Bank Account Management System.")
            break

        # กรณีใส่เลขไม่ถูก
        else:
            print(" Invalid choice. Please enter 1-4.")
print(bank_account_management())