import gspread
from google.oauth2.service_account import Credentials
import random
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)

def select_word():
    SHEET = GSPREAD_CLIENT.open('Hangman')
    words = SHEET.worksheet('words')
    data = words.get_all_values()
    list_words = words.col_values(1)
    random_word = random.choice(list_words).lower()
    return random_word

selected_word = select_word()
print(selected_word)

#NameError: name 'random_word' is not defined. is it outside the function



# selected_word  list(random_word)
# split = random_word.split() not using 

# print(random_word)
# print(selected_word)
# print(split) not using 
# placeholder = "_"*len(selected_word)
# print(f"{list(placeholder)}")

# invite player to guess the letter
user_input = input("Guess a letter: ")
# I have to save the letter to a variable?
#
letter_guess = user_input.lower()
# print(letter_guess)

# check of the letter is in word, if not record wrong guess
# Need to keep count of guess, set max number of guess or min number of guess
# if right guess, print the letter
# if incorrect add to wrong guess and draw hangman
wrong_guesses = 0
display = []
def check_letter():
    for letter in selected_word:
        if letter in letter_guess:
        # print(f"You have guessed the correct letter {letter_guess} !")
            display.append(letter_guess)
            # print(f"{letter_guess}")
        else:
            display.append("_")
            # print("_")
    return display


check_letter()

# issues to resolve tomorrow

# 1 . the word prints in a vertical column, how to print in a line .append??
# 1.1 'str' object has no attribute 'append'. I dont want a list...
# 1.2 should i pass a parameters check_letter? selected_word, letter_guess ?
# 1.3 will the end= "" work?  https://www.toppr.com/guides/python-guide/questions/what-does-end-do-in-python/
# 1.4 https://www.geeksforgeeks.org/gfact-50-python-end-parameter-in-print/
# 2. Can i record incorrect guesses in the same loop - NO, need to find solution 
# 3. print message to tell the player is guessed the right letter
# 4. remove two letter options from Gsheet list.
# 5. add ascii images.


# if wrong_guesses == 4:
#     break 
# print("Game over!") 
