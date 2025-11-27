import random

print("🎯 Welcome to the Number Guessing Game!")

# Generate a random number between 1 and 100
secret_number = random.randint(1, 100)

attempts = 0
guess = 0

while guess != secret_number:
    try:
        guess = int(input("Enter your guess (1–100): "))
        attempts += 1
        
        if guess < secret_number:
            print(" Too Low! Try again.")
        elif guess > secret_number:
            print(" Too High! Try again.")
        else:
            print(f" Correct! You guessed the number in {attempts} attempts.")
    except ValueError:
        print("❗ Please enter a valid number.")