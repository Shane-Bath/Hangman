![asceii hangman log](/hangman.png)


# Hangman Game With Ascii art.

A python hangman game with Ascii art. This is a simple hangman game written in Python. The objective of the game is to guess a hidden word by suggesting letters. The player can only make a limited number of incorrect guesses before losing the game.

## Goal
To create a game of hangman with the following futures.
* Choice of catagories
* Level of Difficulties  - number of lives
* Select a random word save on a Google Spreedsheet
* Title page and end page made from Ascii art
* Hangman Ascii character 
* Store guesses
* Adding words to the spreadsheet from the game.
* 

## Design
I began setting out the design of the game with a handwritten note. Going through basic function and rules of the game. I then used Lucidchart to create a flow chart of the game.

This was a good exercise as It allowed me to break down the game in to smaller parts. With the flow chart and my note, I attempted to write code snippets to build each function of the game out separately, for example select a random word from a list or in this case a google spreadsheet, counting out the number of letters in the word, hiding the word etc. I have attempted this without reference to guides or book but to see what I could do with the knowledge I have at this stage. 

Ascii art add graphics to the game and a 80's esthetic. 

## How to play 
* When you start the game, you will be asked to guess a letter in a the hidden word.
* The player will input a letter using a keyboard and pressing enter
* If the letter is in the hidden word, it will be displayed, along with blank spaces representing the other letters in the hidden word.
* If the letter is not in the hidden word, an ascii image will displayed representing a hangman gallows and figure. 
* The player will lose a life. There will be a limited number of lives for the player.
* The player will be asked to guess again.
* If the player lose all their lives, the game will be over. This will reprsented by a completed hangman image.
* If the player guess all the letter correctly, the player will win the game.
* The player can choose to play again typing 'Y' when prompted or quit the game by tying 'N'.

## pythontutor





## Testing

## Validator Testing

## Deployment 

## Credits













![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

Welcome Shane-Bath,

This is the Code Institute student template for deploying your third portfolio project, the Python command-line project. The last update to this file was: **August 17, 2021**

## Reminders

* Your code must be placed in the `run.py` file
* Your dependencies must be placed in the `requirements.txt` file
* Do not edit any of the other files or your code may not deploy properly

## Creating the Heroku app

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.

-----
Happy coding!