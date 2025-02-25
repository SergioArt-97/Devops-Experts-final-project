import CurrencyRouletteGame
import GuessGame
import MemoryGame

def welcome(name):
    print(f"Hello {name} and welcome to the World of Games (WoG).")
    print("Here you can find many cool games to play")
    print()

def load_game():
    print("""Please choose a game to play:
1. Memory Game - a sequence of numbers will appear for 1 second and you will have to guess it back
2. Guess Game - guess a number and see if you chose the correct number
3. Currency Roulette - try and guess the value of a random amount of USD in ILS""")
    user_game_input = 0
    #game choice loop
    while True:
        try:
            user_game_input = int(input("what is your choice?: "))
            if 1 <= user_game_input <= 3:
                break
            else:
                print("Please choose a relevant corresponding number")
        except ValueError:
            print("Please choose a relevant corresponding number")
    print()

    #difficulty choice loop
    print("Pleas choose the game difficulty from 1 to 5:")
    user_difficulty_choice = 0
    while True:
        try:
            user_difficulty_choice = int(input("what is your choice?: "))
            if 1 <= user_difficulty_choice <= 5:
                break
            else:
                print("Please choose a number between 1 and 5")
        except ValueError:
            print("Please choose a number between 1 and 5")

    if user_game_input == 1:
        print()
        MemoryGame.play(user_difficulty_choice)
    elif user_game_input == 2:
        print()
        GuessGame.play(user_difficulty_choice)
    elif user_game_input == 3:
        print()
        CurrencyRouletteGame.play(user_difficulty_choice)