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
SHEET = GSPREAD_CLIENT.open('Hangman')

words = SHEET.worksheet('words')

data = words.get_all_values()

list_words = words.col_values(1)

random_word = random.choice(list_words).lower()
# selected_word = list(random_word)
# split = random_word.split() not using 
selected_word = [*random_word]
# print(random_word)
print(selected_word)
# print(split) not using 
placeholder = "_"*len(selected_word)
print(f"{list(placeholder)}")

user_input = input("Guess a letter: ")
print(user_input)

"""
create a loop to match the user input with a letter in the word and replace the blank
"""

# if user_input == a letter in the selected_word replace the placeholder with the letter 
# from user_input. if it does not match ask the player to guess agian - range(len())

for letter in range(len(selected_word)):
    match = selected_word[letter]
    
    if match == user_input:
        placeholder[:match] + selected_word + placeholder[match + 1:]
       
        
       

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
