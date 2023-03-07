import word_choice
import random

# def select_word():
#     """
#     Seletct a random word form the googlespread sheet
#     """
#     SHEET = GSPREAD_CLIENT.open('Hangman')
#     words = SHEET.worksheet('words')
#     data = words.get_all_values()
#     list_words = words.col_values(1)
#     random_word = random.choice(list_words).lower()
#     print(random_word)

from word_choice import select_word

select_word()
# https://stackoverflow.com/questions/20309456/how-do-i-call-a-function-from-another-py-file