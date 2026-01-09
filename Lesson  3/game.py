import random

def guess_the_number():
    secret_number = random.randint(1, 100)
    attempts = 0
    print("Welcome to the 2026 Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed it in {attempts} attempts.")
                break
        except ValueError:
            print("Please enter a valid whole number.")

if __name__ == "__main__":
    guess_the_number()
