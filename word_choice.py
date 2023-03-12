import gspread
from google.oauth2.service_account import Credentials
import random
from acsii import title
from acsii import stage_one
from acsii import stage_two
from acsii import stage_three
from acsii import stage_four
from acsii import stage_five
from acsii import game_over

# from acsii import title
#  displaying all the acsii graphics? why
print(title)
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
wrong_guesses = 5
# number of guesses allowed 5

# create a list. 
placeholder = []

# for letter in range(len(selected_word)):
for letter in selected_word:
    placeholder += "_"
print(placeholder)


while wrong_guesses > 0:
    user_input = input("Guess a letter: ")
    letter_guess = user_input.lower()
    if letter_guess in selected_word:
        for i in range(len(selected_word)):
            if selected_word[i] == letter_guess:
                placeholder[i] = letter_guess
            
                
        print("Correct")
        print(placeholder)
    
    else:
        wrong_guesses -= 1
        print(f"you have {wrong_guesses} guess left !")
    
    if "_" not in placeholder:
        print("You win")
        break

    if wrong_guesses == 4:
        print(stage_one)
    if wrong_guesses == 3:
        print(stage_two)
    if wrong_guesses == 2:
        print(stage_three)
    if wrong_guesses == 1:
        print(stage_four)
    if wrong_guesses == 0:
        print(stage_five)
        print(f"Game over you have no guess left")
        print(game_over)
        break
                 
    
# Issues with above code:
# 1. Can I reduce it.
# 1.2 if wrong_guess
# 1.3 from acsii import
# 2 Error log
# 2.1 input a single letter
# 2.2 if num input - error go again 
# 2.3 if upper case - error go again 
# 2.4 if repeat of letter? Do i penalize
# 3. How to remove blank for space between two words
# 3.1 Do I remove more than single words from list??
# 4 I dont want to repeat the placeholder - How to keep it to one line
# 5. Is even this the appropriate method?
# 6. prevent multiple letter inputted (error catching )


# Solved 
# 1. While loop continues even if all letters guessed
#    need to stop while loop if all letter guessed - SOLVED
# 4. Introduce the acsii images - SOLVEDish
# 1 . the word prints in a vertical column, how to print in a line .append?? SOLVED
# 1.1 'str' object has no attribute 'append'. I dont want a list...    SOLVED
# 3. print message to tell the player is guessed the right letter
# 5. add ascii images.  DONE
# 7 run the game while loop (solved)
# 8 looping through list, and replacing _ if match is throwing up an error - see bug
# 9 end game once all the letters have been guessed. SOLVED




# https://understandingdata.com/posts/the-comprehensive-guide-to-google-sheets-with-python/


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













