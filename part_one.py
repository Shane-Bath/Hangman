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
    list_words = words.col_values(1)
    random_word = random.choice(list_words).lower()
    
    
    placeholder = []
    for letter in random_word:
        placeholder += "_"
    print(placeholder)

    return random_word







# for letter in selected_word:
#     placeholder += "_"
# print(placeholder)