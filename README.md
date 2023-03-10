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
* If the player lose all their lives, the game will be over. This will represented by a completed hangman image.
* If the player guess all the letter correctly, the player will win the game.
* The player can choose to play again typing 'Y' when prompted or quit the game by tying 'N'.

## Acseii Art
[Wikapedia](https://en.wikipedia.org/wiki/ASCII_art) state that *ASCII art is a graphic design technique that uses computers for presentation and consists of pictures pieced together from the 95 printable (from a total of 128) characters defined by the ASCII Standard from 1963 and ASCII compliant character sets with proprietary extended characters (beyond the 128 characters of standard 7-bit ASCII). The term is also loosely used to refer to text-based visual art in general. ASCII art can be created with any text editor, and is often used with free-form languages. Most examples of ASCII art require a fixed-width font (non-proportional fonts, as on a traditional typewriter) such as Courier for presentation.*

Used a [Acseii art generator](https://patorjk.com/software/taag/#p=display&f=Graffiti&t=Type%20Something%20) to produce the Hangman title and end game title. 

For hangman gallows and stick man, I first practiced on Notepad and I completed the final version in the py file itself. 

In order to display the image you have use enclose the *string* with three quotation marks, for example: """ *string* """. I had an issue with \ (backslash) as it is a special character in Python, but to you can use *r* which is *raw* python string. The character will be represented as a normal string if you place the *r* before 


## Testing
I have found the Pythontutor very helpful to test small of the code, a for loop etc. I am able to see at what point in the code, error is produced. I research the to come up with the solution or make a few changes run the code again. 

I connect the varies part the of code, and run it in the workspace terminal. Again going through each section of the code, trying to work out why the code is not executing as expected. It could be a simple indentation error or spelling mistake etc. Fix the issues and try again.  I would also redo code and experiment with snippets of code from sources like stackover flow , WC3schools or python blogs, but a lot the code ended up on the cutting floor. 

If the code did not work as expected, I would comment it out and try something else. As the project progressed, I would come back to the line, make changes based growing understanding of what I was doing, and end up using it. 

Finally I asked my daughter and wife to play the game, while they played I note any changes I wanted to make. Which were a few as they saw the game differently to me. For example reprinting the word line later in game, or adding a list of incorrect letter. It was a useful excise.

## Validator Testing

## Deployment 
As Python is a back-end language I am deploying the project to Heroku. To deploy the project, the follow steps must be followed.

* Create a list of dependencies in the requirement file. To start, in the terminal write the following line - 'pip3 freeze > requirements.txt'. Make sure that the file name is an exacted match as Heroku looks for this file name in the same format. This will update the requirements.txt file.
* Once the file has been updated, commit the changes and push to Github.
* Login to Heroku, from the dashboard click "Create new app" and give the app an unique name.
* Select region - Europe and click create app.
* Click settings tab and select Config vars. In the field *key* enter CREDS, all uppercase. In thhe workspace copy the content of the creds.json file. Paste the data into the *value* field. Then click add.
* A config var will have be created, with **port** in the key field and **8000** in the *value* field. Click add. 
* Next create Buildpack to install further dependencies outside of the one used in the requirements.txt file. Click *Add Buildpack*. The first buildpack required will be python, select **python**. Click save changes.
* The next buildpack to select is *node.js*, agian click save changes. (The order must be python then node.js) Node.js is required for the mock terminal. 
* Once you have completed the above you can choose the deployment method. Search for the Github repository name and click *connect*. This will links up Heroku to Github. 
* Select the automatic deploy option. 

Once the deployment is complete, the project will be accessible via the mock terminal. To run the game type 'python3" and it should begin automatically. 

## Credit
Thanks to Simen Dehlin for his guidance. 

The following is a list resource i referred to. 
* W3school
* Google Docs (Google sheets)
* Stackover flow
* Patorjk.com
* FreeCodeCamp.org
* Code Institute 
* Programming with Mosh - https://www.youtube.com/@programmingwithmosh

Webpages:

https://stackoverflow.com/questions/9028036/how-to-link-multiple-scripts
https://docs.gspread.org/en/latest/user-guide.html
https://www.w3schools.com/python/python_functions.asp
https://stackoverflow.com/questions/4394145/
https://www.w3schools.com/python/python_conditions.asppicking-a-random-word-from-a-list-in-python
https://bobbyhadz.com/blog/python-split-word-into-list
https://www.w3schools.com/python/ref_string_replace.asp
https://learnpython.com/blog/python-list-loop/
https://blog.finxter.com/how-to-use-rangelen-in-python/
https://www.w3schools.com/python/python_for_loops.asp
https://stackoverflow.com/questions/31087111/why-does-example-list-result-in-typeerror-list-object-is-not-callable
https://stackoverflow.com/questions/10631473/
https://www.w3schools.com/python/python_while_loops.aspstr-object-does-not-support-item-assignment
https://stackoverflow.com/questions/66134751/how-do-i-properly-print-ascii-art
https://stackoverflow.com/questions/10139866/calling-variable-defined-inside-one-function-from-another-function
 https://stackoverflow.com/questions/920645/when-to-use-while-or-for-in-python
https://flexiple.com/python/if-not-python/
https://stackoverflow.com/questions/7511294/how-to-avoid-repetitive-if-statements-in-python-dictionaries
https://codereview.stackexchange.com/questions/270080/how-possible-it-is-to-shorten-repetitive-if-statements-in-python
https://medium.com/swlh/3-alternatives-to-if-statements-to-make-your-python-code-more-readable-91a9991fb353
https://effectivepython.com/2020/02/02/prevent-repetition-with-assignment-expressions
https://stackoverflow.com/questions/419163/what-does-if-name-main-do
https://stackoverflow.com/questions/41718538/how-do-i-insert-a-restart-game-option
https://python-forum.io/thread-12841.htm
https://www.w3schools.com/python/ref_string_split.asp

