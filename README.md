![asceii hangman log](/images//hangman.png)


# Hangman Game With Ascii art.

Python hangman game with Ascii art. This is a simple hangman game written in Python. The objective of the game is to guess a hidden word by suggesting letters. The player can only make a limited number of incorrect guesses before losing the game.

## Goal
To create a game of hangman with the following futures.
* Choice of categories
* Level of difficulties  - number of lives
* Select a random word save on a Google Spreadsheet
* Title page and end page made from Ascii art
* Hangman Ascii character 
* Store guesses

## Design
I began setting out the design of the game with a handwritten note. Going through basic function and rules of the game. I then used Lucidchart to create a flow chart of the game.

![Lucidchart](/images/flowchart.png)

This was a good exercise as It allowed me to break down the game in to smaller parts. With the flow chart and my note, I attempted to write code snippets to build each function of the game out separately, for example select a random word from a list or in this case a google spreadsheet, counting out the number of letters in the word, hiding the word etc.


## How to play 
* When you start the game, you will be asked to guess a letter in the hidden word.
* The player will input a letter using a keyboard and pressing enter
* If the letter is in the hidden word, it will be displayed, along with blank spaces representing the other letters in the hidden word.
* If the letter is not in the hidden word, an ascii image will be displayed representing a hangman gallows and figure. 
* The player will lose a life. There will be a limited number of lives for the player.
* The player will be asked to guess again.
* If the player loses all their lives, the game will be over. This will be represented by a completed hangman image.
* If the player can guess all the letter correctly, the player will win the game.
* The player can choose to play again typing '1' when prompted or quit the game by tying '2'.

## Acseii Art
[Wikapedia](https://en.wikipedia.org/wiki/ASCII_art) state that *ASCII art is a graphic design technique that uses computers for presentation and consists of pictures pieced together from the 95 printable (from a total of 128) characters defined by the ASCII Standard from 1963 and ASCII compliant character sets with proprietary extended characters (beyond the 128 characters of standard 7-bit ASCII). The term is also loosely used to refer to text-based visual art in general. ASCII art can be created with any text editor, and is often used with free-form languages. Most examples of ASCII art require a fixed-width font (non-proportional fonts, as on a traditional typewriter) such as Courier for presentation.*

I Used a [Acseii art generator](https://patorjk.com/software/taag/#p=display&f=Standard&t=Hangman) to produce the Hangman title and end game title. 

For hangman gallows and stick man, I first practiced on Notepad and I completed the final version in the py file itself. 

In order to display the image, you have use enclose the *string* with three quotation marks, for example: """ *string* """. I had an issue with \ (backslash) as it is a special character in Python, but to you can use *r* which is *raw* python string. The character will be represented as a normal string if you place the *r* before the apostrophes.


## Testing
I have found the Pythontutor very helpful to test and step into the code. Being able to see at what point in the code, an error is produced and the order that the code is read by the terminal helped me to better understand what I was attempting to do. 

![pythontutor](/images/pythontutor.png)

It allowed me to make a changes and I was better able to understand how the changes impacted the code. Often the error could be as simple as an incorrect indentation (often), or a syntax error etc. If the solution to the problem was not obvious to me,  I could  focus my research on the problem and try to come up with a solution.
Then redo the code and experiment with snippets of code from sources like stackover flow , WC3schools or python blogs, try again in pythontutor. A lot of the code ended up on the cutting floor and 

If the code did not work as expected, I would comment it out and try something else. As the project progressed, I would come back to the line, make changes based on my growing understanding of what I was doing, and sometimes end up using the line of code as I implemented the concept correctly.

As an example, restarting the game proved to be an issue. I unfortunately spent a significant amount of time trying to resolve in gitpod, unsuccessfully. I attempted a number of fixes and solutions, going down a few blind alleys. I designed the code to check the variable wrong_guess to see at what stage of the player was in the game. This variable determined the beginning and end of the game. Even though I reset wrong_guess back to the original state in the function that controlled the restart of the game, the terminal would not recognize this, and it would continue to run the code in the end state. Eventually using Pythontutor I began to understand the'global frame' and that my reset function was not resetting the wrong_guess because it was out of the global frame. The variable had been assigned 5 in the reset_game() function, but it did not change the "global" variable. To resolve this I assigned the **global** keyword to the wrong_guesses, which allowed for the variable to updated. 

Without being able to step in each line of the code and see that it was not being reset to 5, it would hae been difficult for me to pin point the issue. 

I have no doubt that I have come up with a convoluted code to produce what the game actually does, and there will be a much more efficient way of doing, it out there. But I now have a much better understanding of Python and it concepts. Thanks in large part to trying to brute force a solution onto a problem, experimenting and breaking the code, then fixing it.  

Finally I asked my daughter and wife to play the game, while they played I noted any changes I wanted to make. Which were a few as they saw the game differently to me. It was a useful exercise.

## Validator Testing
I could not find any official python validator.

## Bugs
I had originally coded  the game into different functions and modules. Unfortunately, this created a number of issues and introduced bugs into the game. Due to time pressure and in order to get a working code, I abandoned the multiple modules approach, and I placed the body of the main code is one main module and fewer functions. This resolved most of the issues.

However an example of a bug remains. When the player reaches the end of game, there is an option to select a number 1 or 2, to either continue or end the game. When I ran the code from the main module part_one.py, if the player selects 2 the game ends, breaks in the terminal. When the game is run from the run.py file, when the player select 2, the secret word line is printed along with the placeholder and the end game line is repeated. If the player selects 2 again the game will end. 

I attempted a number of solutions, including moving the while == true loop which contains the break word.  Change the number_guess variable to 0 etc, but not quite fixing the bug. Unfortunately to due time and as it is not game breaking, it remains in the game.

After the game was deployed to Heroku, the display did not show the placeholders in the same style as the terminal. The terminal placeholders had a gap between each letter, but on Heroku display there were no gaps. I did not want to use the list display style with the square brackets, and I had changed to .join style _ _ _ _ _ originally. But for playability and I decided to revert back to the list style **['_','_',]** . This was forced on me, and would have preferred to display the placeholder with brackets and commas.

## Deployment 
As Python is a back-end language I am deploying the project to Heroku. To deploy the project, the follow steps must be followed.

* Create a list of dependencies in the requirement file. To start, in the terminal write the following line - 'pip3 freeze > requirements.txt'. Make sure that the file name is an exacted match as Heroku looks for this file name in the same format. This will update the requirements.txt file.
* Once the file has been updated, commit the changes and push to Github.
* Login to Heroku, from the dashboard click "Create new app" and give the app an unique name.
* Select region - Europe and click create app.
* Click settings tab and select Config vars. In the field *key* enter CREDS, all uppercase. In the workspace copy the content of the creds.json file. Paste the data into the *value* field. Then click add.
* A config var will have be created, with **port** in the key field and **8000** in the *value* field. Click add. 
* Next create Buildpack to install further dependencies outside of the one used in the requirements.txt file. Click *Add Buildpack*. The first buildpack required will be python, select **python**. Click save changes.
* The next buildpack to select is *node.js*, again click save changes. (The order must be python then node.js) Node.js is required for the mock terminal. 
* Once you have completed the above you can choose the deployment method. Search for the Github repository name and click *connect*. This will links up Heroku to Github. 
* Select the automatic deploy option. 

Once the deployment is complete, the project will be accessible via the mock terminal. To run the game type 'python3" and it should begin automatically. 

## Credit
Thanks to Simen Dehlin for his guidance. 

The following is a list resource I referred to. 
* W3school
* Google Docs (Google sheets)
* Stackoverflow
* [Patorjk.com](https://patorjk.com/software/taag/#p=display&f=Standard&t=Hangman)
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
https://stackoverflow.com/questions/10851906/python-3-unboundlocalerror-local-variable-referenced-before-assignment
https://stackoverflow.com/questions/11178061/print-list-without-brackets-in-a-single-row
https://www.geeksforgeeks.org/clear-screen-python/
https://stackoverflow.com/questions/8761778/limiting-python-input-strings-to-certain-characters-and-lengths
https://stackoverflow.com/questions/23294658/asking-the-user-for-input-until-they-give-a-valid-response?noredirect=1&lq=1
https://stackoverflow.com/questions/2084508/clear-terminal-in-python

![acsii final image](/images/winner.png)

