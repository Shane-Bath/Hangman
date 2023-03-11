import gspread
from google.oauth2.service_account import Credentials
import random
from acsii import stage_one
# from acsii import title
#  displaying all the acsii graphics? why

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
    # data = words.get_all_values()   Do i need this if iam only using data in cols
    list_words = words.col_values(1)
    random_word = random.choice(list_words).lower()
    return random_word

selected_word = select_word()
print(selected_word)
wrong_guesses = 4
# number of guesses allowed 4


# print(selected_word)
# placeholder = "_"*len(selected_word)
# print(placeholder)

# invite player to guess the letter
user_input = input("Guess a letter: ")
# input letter saved in variable in lower case
letter_guess = user_input.lower()
placeholder = []



# for letter in range(len(selected_word)):
for letter in selected_word:
    placeholder += "_"
print(placeholder)

if letter_guess in selected_word:
    print("Correct")
    user_input
else:
    wrong_guesses -= 1
    print(stage_one)
    print(wrong_guesses)

    

# for i in range(len(selected_word)):
#     if letter_guess  == selected_word[i]:
#         placeholder[i] = letter_guess

# print(placeholder)
# bug TypeError: 'str' object cannot be interpreted as an integer python tutor
# TypeError: 'function' object cannot be interpreted as an integer
# can str be used in a range?

# https://understandingdata.com/posts/the-comprehensive-guide-to-google-sheets-with-python/





# how to stop player inputting multiple letter and nums? 

# input letter saved in variable in lower case
wrong_guesses = 4
# numeber guesses allowed 4

# a while loop to continue the game while player has not reached guess limit
# while wrong_guesses > 0:
#     check_letter()
#     if wrong_guesses == 0:
#         print(game_over)

"""
ask player to guess a single, lower case letter
check if letter is in letter_guess
if matches letter in letter_guess
print(f"{letter_guess}", end= "")
if letter is not in letter_guess
print hangman stage 1 and ask player to guess agian
if all letter have been guessed before wrong guess == 0
player wins 
if wrong_guess == 0 
player loses
offer player to restart game or quit
"""


# I have to save the letter to a variable?
#The for statement iterates through a collection or iterable object or generator function.
# The while statement simply loops until a condition is False.
# https://stackoverflow.com/questions/920645/when-to-use-while-or-for-in-python


# print(letter_guess)

# check of the letter is in word, if not record wrong guess
# Need to keep count of guess, set max number of guess or min number of guess
# if right guess, print the letter
# if incorrect add to wrong guess and draw hangman


# def check_letter():
#     for letter in selected_word:
#         if letter in letter_guess:
#             print(f"{letter_guess}", end= "")
#         else:
#             print("_", end= "")
# check_letter()
# I not sure if this is the best solution.   Should I use a list, range() and len()

# # placeholder = []

# for letter in range(len(selected_word)):
#     placeholder += "_"
# print(placeholder)



# issues to resolve tomorrow

# 1 . the word prints in a vertical column, how to print in a line .append?? SOLVED
# 1.1 'str' object has no attribute 'append'. I dont want a list...    SOLVED
# 1.2 should i pass a parameters check_letter? selected_word, letter_guess ?
# 1.3 will the end= "" work?  https://www.toppr.com/guides/python-guide/questions/what-does-end-do-in-python/
# 1.4 https://www.geeksforgeeks.org/gfact-50-python-end-parameter-in-print/    WORKED
# 2. Can i record incorrect guesses in the same loop - NO, need to find solution 
# 3. print message to tell the player is guessed the right letter
# 4. remove two WORD options from Gsheet list.
# 5. add ascii images.  DONE
# 6. prevent multiple letter inputted (error catching )
# 6.1 only lower case letter and not number
# 7 run the game while loop
# 8 looping through list, and replacing _ if match is throwing up an error - see bug


# if wrong_guesses == 4:
#     break 
# print("Game over!") 


# selected_word  list(random_word)
# split = random_word.split() not using 

#NameError: name 'random_word' is not defined. is it outside the function

# print(random_word)
# print(selected_word)
# print(split) not using 
# placeholder = "_"*len(selected_word)
# print(f"{list(placeholder)}")