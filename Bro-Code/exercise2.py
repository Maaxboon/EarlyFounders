# Shopping cart Program

item = input("What item would you like?: ")
price = float(input("What is the price?: "))
quantity = int(input("How many would you buy?: "))
total = price * quantity

print(f"You have bought {quantity} x {item}/s")
print(f"Your total is: KES{total}")