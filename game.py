import random

print("Welcome to 'Guess the Number'!")
number = random.randint(1, 100)
attempts = 0

while True:
    guess = input("Enter your guess (1-100): ")
    attempts += 1

    if not guess.isdigit():
        print("Please enter a valid number.")
        continue

    guess = int(guess)

    if guess < number:
        print("Too low!")
    elif guess > number:
        print("Too high!")
    else:
        print(f"Congratulations! You guessed the number in {attempts} attempts.")
        break
