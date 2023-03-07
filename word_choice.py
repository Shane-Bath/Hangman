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
letter_guess = user_input.lower()
print(letter_guess)

# check of the letter is in word, if not record wrong guess
# Need to keep count of guess, set max number of guess or min number of guess
# if right guess, print the letter
# if incorrect add to wrong guess and draw hangman
wrong_guesses = 0

for letter in selected_word:
    if letter in letter_guess:
        print(f"{letter_guess}")
    else:
        print("_")




# if wrong_guesses == 4:
#     break 
# print("Game over!") 

"""
create a loop to match the user input with a letter in the word and replace the blank
"""

# if user_input == a letter in the selected_word replace the placeholder with the letter 
# from user_input. if it does not match ask the player to guess agian - range(len())

# for letter in range(len(selected_word)):
#     match = selected_word[letter]
    
#     if match == user_input:
#         placeholder[:match] + selected_word + placeholder[match + 1:]
       
        
       

""" 
create a function that replaces a letter with a "_" 
"""



# def hangman():
#     if i in range(len(selected_word)):
#         choice = user_input()
#         index = selected_word.index(choice)
#         placeholder = placeholder[:index] + selected_word + placeholder[index + 1:]
#         print(placeholder)

# hangman()
