import random

def number_guessing_game():
    while True:
        print("Menu:\n1. Start New Game\n2. Show Instructions\n3. Exit")
        choice = input("Please select an option: ").strip()
        if choice == '1':
            target = random.randint(1,100)
            attempts = 0
            while True:
                guess = int(input("Guess a number between 1 and 100: "))
                attempts += 1
                if guess < target:
                    print("Your guess is too low. Try again!")
                elif guess > target:
                    print("Your guess is too high. Try again!")
                else:
                    print(f"Congratulations! You guessed the number correctly in {attempts} attempts.")
                    break
        elif choice == '2':
            print("Instructions: ...")
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid option.")
print(number_guessing_game())

