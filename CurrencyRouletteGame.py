from random import randint
from time import sleep

import requests


def get_money_interval(difficulty):
    try:
        response = requests.get("https://api.exchangerate-api.com/v4/latest/USD")
        data = response.json()
        exchange_rate = data["rates"]["ILS"]
    except Exception as e:
        print("Error fetching exchange rate:", e)
        return None

    random_number = randint(1,100)

    total_value = random_number * exchange_rate

    rounded_value = round(total_value, 2)

    interval_lower = rounded_value - (5 - difficulty)
    interval_upper = rounded_value + (5 - difficulty)

    return interval_lower, interval_upper, total_value, random_number

def get_guess_from_user(lower, upper, total, dollars):
    print(f"How much is {dollars} USD in Israeli Shekels? (to the second decimal number):")
    while True:
        try:
            user_guess = float(input())
            break
        except ValueError:
            print("Invalid input, please enter a number!")
    if lower <= user_guess <= upper:
        print(f"You WON! the total amount was {total} ILS")
        return True
    print(f"You lost! the total amount was {total} ILS")
    return False




def play(difficulty):
    result = get_money_interval(difficulty)
    print("Welcome to the Currency Roulette Game, in this game you will have to guess")
    print("The correct amount of Israeli shekels in Dollars")
    print("Are you ready?")
    sleep(2)
    print("Begin!")
    print()
    if result:
        interval_lower, interval_upper, total_value, dollars = result
        return get_guess_from_user(interval_lower, interval_upper, total_value, dollars)
    else:
        print("Game could not start due to error fetching exchange rate.")
    return False
