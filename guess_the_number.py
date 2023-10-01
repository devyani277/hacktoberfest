import random

def generate_random_number(min_value, max_value):
    return random.randint(min_value, max_value)

def play_game():
    min_value = 1
    max_value = 100
    secret_number = generate_random_number(min_value, max_value)
    attempts = 0

    print("Welcome to Guess the Number!")
    print(f"I'm thinking of a number between {min_value} and {max_value}.")

    while True:
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        attempts += 1

        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts.")
            break

if __name__ == "__main__":
    play_game()
