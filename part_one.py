import gspread
from google.oauth2.service_account import Credentials
import random
from acsii import title, stage_one, stage_two, stage_three, stage_four, stage_five, game_over, winner
import os
import re

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)

list_of_guess = []
wrong_guesses = 5

print(title)

def clear_screen():
    """
    To clear screen after each turn, on both windowOS and MacOs
    """
    os.system('cls' if os.name == 'nt' else 'clear')

def reset_game():
    global wrong_guesses
    global list_of_guess
    global game_over
    global new_word
    option = input("Do you want to play again?\nChoose 1 for YES OR 2 for NO?\n")
    if option == '1':
        wrong_guesses = 5
        list_of_guess = []
        clear_screen()
        print(title)
        game()
    
    else:
        wrong_guesses = -1
        game_over = True


def game():
    global wrong_guesses
    global list_of_guess
    global game_over 
    while game_over == True:
        
        break

    placeholder = []
    SHEET = GSPREAD_CLIENT.open('Hangman')
    words = SHEET.worksheet('words')
    list_words = words.col_values(1)
    random_word = random.choice(list_words).lower()
    selected_word = random_word
    
    print("The secret word is ?")

    for letter in selected_word:
        placeholder += "_"
    print(''.join(placeholder))
    print("\n")

    while wrong_guesses > 0:
        user_input = input("Guess a letter:\n")
        if not re.match("^[a-z]*$", user_input):
            print("Error, only letter from a-z allowed")
            user_input = input("Guess a letter:\n")
        elif len(user_input) > 1:
            print('Pick one letter only')
            user_input = input("Guess a letter:\n")
        elif user_input in list_of_guess:
            print("You have already used this letter, guess again")
            user_input = input("Guess a letter:\n")
        
        list_of_guess += user_input
        
        clear_screen()
        
        letter_guess = user_input.lower()
     
        if letter_guess in selected_word:
            for i in range(len(selected_word)):
                if selected_word[i] == letter_guess:
                    placeholder[i] = letter_guess
            print(f"{letter_guess} is Correct!\n")
            print("The secert word is ?")
            print(''.join(placeholder))
            print("")
            print("List of your guesses:")
            print(f"{list_of_guess}\n")
        else:
            wrong_guesses -= 1
            print(f"Incorrect, you have {wrong_guesses} guesses left !\n")
            print(f"List of your guesses: {list_of_guess}\n")
            print("The secert word is ?")
            print(''.join(placeholder))

        if "_" not in placeholder:
            print(winner)
            reset_game()

        if wrong_guesses == 4:
            print(stage_one)     
        elif wrong_guesses == 3:
            print(stage_two)  
        elif wrong_guesses == 2:
            print(stage_three)   
        elif wrong_guesses == 1:
            print(stage_four)
        elif wrong_guesses == 0:
            print(wrong_guesses)
            print(stage_five)
            print(f"Game over you have no guess left\n")
            print(f"The secret word is {selected_word} ! \n")
            reset_game()

game()

