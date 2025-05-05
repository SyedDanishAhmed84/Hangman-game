🕹️ Hangman Word Guessing Game in Python
A simple and fun Hangman game built in Python where players guess a word by inputting letters. The game randomly selects a football club name, and the player has 7 chances to guess the correct letters before running out of chances.

🔧 Technologies Used:
Python - Core language used for logic and flow.

Console/Terminal - For interactive gameplay (text-based).

📜 Project Overview:
This Hangman game challenges players to guess a hidden word from a set of football club names, letter by letter. The player has a total of 7 chances to guess wrong before the game ends. With each correct guess, the player gets one step closer to unveiling the entire word. It’s a perfect project for Python beginners to practice string manipulation, loops, and conditionals.

🧑‍💻 How the Game Works:
Word Selection
The game picks a random word from a predefined list of football club names, such as "REALMADRID", "BARCELONA", "LIVERPOOL", or "CHELSEA".

Player Input
The player is prompted to guess a letter. After each guess, the game will reveal the correct position of the guessed letter in the word or reduce the remaining chances if the guess is wrong.

Word Update
The word is displayed as a series of underscores (e.g., _ _ _ _ _ _ for “REALMADRID”). Each correct letter fills in its respective underscore. Incorrect guesses decrease the number of remaining chances.

Game Over or Win
The game ends when the player either:

Correctly guesses all the letters in the word (win 🎉)

Runs out of chances (lose 😞)

🏆 Features:
Random Word Selection: The game randomly selects a word from the football club list.

Case-Insensitive: The game handle uppercase letters

Limited Chances: Players only have 7 chances to guess.

String Manipulation: The game uses string slicing to update the word dynamically as the player makes guesses.

User Interaction: Players input their guesses, and the game responds with the current status of the word and remaining chances.
