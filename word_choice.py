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

random_word = random.choice(list_words)
selected_word = list(random_word)
# split = random_word.split()
split = [*random_word]
print(random_word)
print(selected_word)
print(split)

""" 
create a function that replaces a letter with a "_" 
"""

placeholder = "_"*len(selected_word)
print(placeholder)

# for i in range(len(selected_word)):
#     letter = 