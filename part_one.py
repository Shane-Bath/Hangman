import gspread
from google.oauth2.service_account import Credentials
import random
from acsii import title, stage_one, stage_two, stage_three, stage_four, stage_five, game_over, winner

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)

print(title)
quit_game = False
list_of_guess = []

wrong_guesses = 5

def game():
    global wrong_guesses
    global list_of_guess
    global quit_game
    placeholder = []
    SHEET = GSPREAD_CLIENT.open('Hangman')
    words = SHEET.worksheet('words')
    # data = words.get_all_values()   Do i need this if iam only using data in cols
    list_words = words.col_values(1)
    random_word = random.choice(list_words).lower()
    selected_word = random_word

    for letter in selected_word:
        placeholder += " _ "
    print(''.join(placeholder))

    while wrong_guesses > 0:
        user_input = input("\nGuess a letter: ")
        letter_guess = user_input.lower()
        if letter_guess in selected_word:
            for i in range(len(selected_word)):
                if selected_word[i] == letter_guess:
                    placeholder[i] = letter_guess
            print(f"The letter {letter_guess} is Correct!\n")
            print(''.join(placeholder))
        else:
            wrong_guesses -= 1
            list_of_guess += letter_guess
            print(f"Incorrect, you have {wrong_guesses} guesses left !")

            if "_" not in placeholder:
                print(winner)
            
            if wrong_guesses == 4:
                print(stage_one)
            elif wrong_guesses == 3:
                print(stage_two)
        # create a function - statement
                print(f"Your incorrect guesses {list_of_guess}")
            elif wrong_guesses == 2:
                print(stage_three)
                print(f"Your incorrect guesses {list_of_guess} \n")
                print(''.join(placeholder))
            elif wrong_guesses == 1:
                print(stage_four)
                print(f"Your incorrect guesses {list_of_guess} \n")
                print(''.join(placeholder))
            if wrong_guesses == 0:
                print(stage_five)
                print(f"Game over you have no guess left\n")
                print(f"The secret word is {selected_word} !")
                break


game()