import random
def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    secret_number = random.randint(1, 100)
    attempts = 0
    while True:
        try:
         random_number = int(input("Guess a number between 1 and 100: "))
         attempts += 1
         if random_number < secret_number:
             print("Too low!")
         elif random_number > secret_number:
             print("Too high!")
         else:
             print(f"Congratulations! You've guessed the number in {attempts} attempts.")
             break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

number_guessing_game()     