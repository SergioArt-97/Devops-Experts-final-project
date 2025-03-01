import random
from time import sleep

from Score import add_score


def generate_number(difficulty):
    if difficulty == 1:
        return 1
    return random.choice(range(1,difficulty))


def get_guess_from_user(difficulty):
    print(f"The computer has chosen a number between 1 and {difficulty}")
    while True:
        try:
            user_chosen_number = int(input(f"Please provide me with your guess: "))
            if 1 > user_chosen_number or user_chosen_number > difficulty:
                print(f"Chosen number cannot be lower than 1 or higher than {difficulty}!")
                continue
            break
        except ValueError:
            print("Invalid input")
    return user_chosen_number


def compare_results(secret_number, user_number):
    return secret_number == user_number


def play(difficulty):
    print(f"Welcome to the Guessing game, you chose difficulty {difficulty}!")
    print(f"Which means you will have to guess a number that the computer chose based on the difficulty you chose")
    print("are you ready?")
    sleep(2)
    print("Begin!")
    print()
    secret_number = generate_number(difficulty)
    user_number = get_guess_from_user(difficulty)
    print()
    if compare_results(secret_number, user_number):
        print(f"You guessed right the secret number was: {secret_number}")
        add_score(difficulty)
        return True
    print(f"You are wrong, the secret number was {secret_number}")
    return False
