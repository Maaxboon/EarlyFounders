import random

def main():
    # Generate the secret number at random!
    secret_number = random.randint(1,10)

    print("I am thinking of a number between 1 and 10")

    # Get user's guess
    guess = int(input("Enter a guess: "))

    # True if guess is not equal to secret number
    while guess != secret_number:
        
        

if __name__ == "__main__":
    main()