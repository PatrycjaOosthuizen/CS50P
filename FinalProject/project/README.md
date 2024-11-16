# PROJECT TITLE : Guess the Country game 🌍

This project is a command-line game, where users guess the letters of a randomly selected country.
The game includes features such as exiting, restarting and a hint. Making it user-friendly and engaging.

##### 🔗 Video Demo: <https://www.youtube.com/watch?v=ch1CLYXuNl4>

### DESCRIPTION

Guess the Country game allows users to play by guessing letters of a country name.
Country name is drawn from a predefined list of countries, the game provides feedback on correct and incorrect guesses.
The objective is to guess the country name. The game allows for multiple attempts and provides an option for hints after a certain number of incorrect guesses.

### FEATURES

- Random selection of countries from a predefined list.
- User input for guessing letters. The input is converted to lowercase and stripped of any leading or trailing white spaces.
- Option to exit, restart the game at any time.
- Displays underscores for unguessed letters and reveals them as they are guessed correctly.
- Hint option appear after four incorrect guesses.
- Provides feedback indicating whether the answer was correct or incorrect.

### REQUIREMENTS

To run this program, ensure you have `Python` installed on your computer. This code uses standard libraries that come with Python.

The `random` module is imported to allow the selection of a random country from the list.

he `re` module (regular expressions) is imported to facilitate pattern matching, specifically for extracting the country name and dialling code from the string format.

To run this code successfully, you need to have the following library installed:
`pyfiglet`: This library can be installed via pip if it is not already available in your environment.
`pip install pyfiglet`

### INSTALLATION

- Clone this repository or download the script file.
- Open your terminal or command prompt.
- Navigate to the directory where the files are located.

### GAME INSTRUCTION

1. Run the script using Python: `python project.py`
2. Follow the on-screen instructions:
   - Press **enter** to start playing.
   - To **end game / exit** , type `-e`
   - To **retry**, type `-r`
3. Upon starting, you will be prompted to guess a letter one at the time or the full country name.
4. You have **eight chances** to make correct guesses.
5. You can reqiuest hint after **four incorrect** guesses by typing `-hint`.

### GAME LOGIC

<u>The game operates as follows:</u>

1. A random movie is selected from a predefined list.
2. The player is presented with underscores representing each letter in the movie title.
3. The player guesses letters one at a time.
4. Correct guesses reveal letters in their respective positions; incorrect guesses are tracked.
5. After a certain number of incorrect guesses, players can request a hint about the country.
6. The game continues until either the player correctly identifies the country name or exhausts their allowed number of incorrect guesses.

### FUNCTIONS

` main()`
Function initiates the game by prompting the user to start playing. It provides options to exit or retry if desired.

`select_country(countries)`
This function randomly selects a country from the list and extracts its name and dialling code using regex.

`question(country_name)`
Function constructs a list where each alphabetic character in country\*name is replaced by an underscore (`_`), while non-alphabetic characters (like spaces and parentheses) remain unchanged.

`game(question, country, code)`
This function handles user input for guessing letters and checks against the selected country name.

`get_result(result)`
Function provides a simple yet effective way to give feedback based on user input. By utilizing ASCII art for its output,
it enhances user interaction through visually appealing text formatting.

`Hint Mechanism:`
If more than four incorrect guesses have been made, users can request a hint that reveals the dialling code of selected country.

`Guess Evaluation:`
If a guessed letter is found in the country name, it replaces underscores in question with that letter.
If the entire country name is guessed correctly, it breaks out of the loop and ends the game.

`Result Feedback:`
After each guess, feedback is provided indicating whether it was correct or incorrect.

### SCREENSHOTS OF THE GAME

![Reference Image](/FinalProject/project/screenshots/image1.png)
![Reference Image](/FinalProject/project/screenshots/image2.png)
![Reference Image](/FinalProject/project/screenshots/image3.png)
![Reference Image](/FinalProject/project/screenshots/image4.png)
![Reference Image](/FinalProject/project/screenshots/image5.png)

** 🔗 List of websites used to create Guess the Country game:**

- <https://countrycode.org/>
- <https://en.m.wikipedia.org/wiki/List_of_country_calling_codes>
- <https://en.m.wikipedia.org/wiki/List_of_countries_and_dependencies_by_area>
