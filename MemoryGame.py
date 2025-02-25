from random import randint
from time import sleep
import sys


def generate_sequence(difficulty):
    generated_list = [randint(1,101) for _ in range(difficulty)]
    return generated_list

def generate_template_sequence(generated_list):
    return "[" + "][".join(" " * len(str(num)) for num in generated_list) + ']'

def ordinal(n):
    return f"{n}{'st' if n == 1 else 'nd' if n == 2 else 'rd' if n == 3 else 'th'}"

def get_list_from_user(difficulty):
    user_list = []
    for i in range(difficulty):
        while True:
            try:
                number = int(input(f"Please provide me with the {ordinal(i + 1)} number in the list (1 - 100): "))
                if number > 100:
                    print("number cannot be above 100!")
                elif number < 1:
                    print("number cannot be below 1!")
                else:
                    user_list.append(number)
                    break
            except ValueError:
                print("Invalid input.")
    return user_list

def is_list_equal(generated_list, user_list):
    if generated_list == user_list:
        print(f"You are right!!!, the list was {generated_list}")
        return True
    print(f"You are wrong, the list was {generated_list}")
    return False


def play(difficulty):
    print(f"Welcome to the Memory Game, you chose difficulty {difficulty}!")
    print(f"Which means you will have to remember a list with {difficulty} items in it")
    print("It will only show for 0.7 seconds and then disappear - after that you will have to guess")
    print("The correct numbers in the correct order")
    print("are you ready?")
    sleep(0.5)
    print("3...")
    sleep(1)
    print("2...")
    sleep(1)
    print("1...")
    sleep(1)
    print("Start!")
    generated_list = generate_sequence(difficulty)
    template_list = generate_template_sequence(generated_list)
    generated_str = str(generated_list)

    print(generated_str, end='', flush=True)
    sleep(0.7)

    sys.stdout.write('\r' + ' ' * len(generated_str) + '\r')
    sys.stdout.flush()

    print(template_list, flush=True)

    user_list = get_list_from_user(difficulty)


    return is_list_equal(generated_list, user_list)
