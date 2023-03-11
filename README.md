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

## Acseii Art
[Wikapedia](https://en.wikipedia.org/wiki/ASCII_art) state that *ASCII art is a graphic design technique that uses computers for presentation and consists of pictures pieced together from the 95 printable (from a total of 128) characters defined by the ASCII Standard from 1963 and ASCII compliant character sets with proprietary extended characters (beyond the 128 characters of standard 7-bit ASCII). The term is also loosely used to refer to text-based visual art in general. ASCII art can be created with any text editor, and is often used with free-form languages. Most examples of ASCII art require a fixed-width font (non-proportional fonts, as on a traditional typewriter) such as Courier for presentation.*

Used a [Acseii art generator](https://patorjk.com/software/taag/#p=display&f=Graffiti&t=Type%20Something%20) to produce the Hangman title and end game title. 

For hangman gallows and stick man, I first practiced on Notepad and I completed the final version in the py file itself. 

In order to display the image you have use enclose the *string* with three quotation marks, for example: """ *string* """. I had an issue with \ (backslash) as it is a special character in Python, but to you can use *r* which is *raw* python string. The character will be represented as a normal string if you place the *r* before 


## Testing

## Validator Testing

## Deployment 
## Credits