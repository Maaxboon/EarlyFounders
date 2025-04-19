#!/usr/bin/env python
# A small ATM simulator:
# A user can:
# Check balance
# Deposit Money
# Withdraw money

# variables
balance = 5000 # Initial balance
attempts = 0
max_attempts = 3

# Simulate pin check with max attempts
while attempts < max_attempts:
    pin = input("Enter your 4-digit pin: ")
    if pin == "1234":
        print("Access granted.\n")

        while True:
            print("\n--- ATM MENU ---")
            print("1. Check balance")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Exit")

            choice = input("Choose an option(--4): ")
            if choice == "1":
                print(f"Your balance is: KES {balance}")
            elif choice == "2":
                amount = int(input("Enter amount to deposit: "))
                if amount > 0:
                    balance += amount
                    print(f"Deposited KES {amount}. New balance: KES {balance}")
                else:
                    print("Invalid amount.")
            elif choice == "3":
                amount = int(input("Enter amount to withdraw: "))
                if 0 < amount <= balance:
                    balance -= amount
                    print(f"Withdrew KES {amount}. New balance: KES {balance}")
                else:
                    print("Insufficient funds or invalid amount.")
            elif choice == "4":
                amount = int(input("Thank you for using our ATM. Goodbye!"))
                break
            else:
                print("Invalid option. Try again.")
        break # exit PIN loop once done
    else:
        attempts += 1
        print(f"incorrect PIN. Attempts left: {max_attempts - attempts}")
if attempts == max_attempts:
    print("Too many incorrect attempts. Card blocked.")
            
