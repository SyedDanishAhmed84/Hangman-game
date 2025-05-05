
🎮 Hangman Word Guessing Game in Python
Project Overview:
This is a console-based implementation of the Hangman game built with Python. The game randomly selects a word from a predefined list of football clubs. The player has to guess the correct letters in the word, one at a time, within a limited number of chances (7 attempts). Each time the player guesses correctly, the corresponding letter is revealed. If the guess is wrong, the number of remaining chances decreases. The player wins by correctly guessing all the letters in the word, and they lose when they run out of chances.

How It Works:
Word Selection:
The game begins by randomly selecting a word from a list of football club names (e.g., REALMADRID, BARCELONA, LIVERPOOL, CHELSEA).

Initial Setup:
The word is hidden, and the player sees a series of underscores (e.g., _ _ _ _ _ _ _ for "REALMADRID"). The number of underscores corresponds to the number of letters in the word.

Guessing Loop:
The player is prompted to guess a letter. If the guessed letter is part of the word, it is revealed in the correct positions. If the guess is incorrect, the player loses a chance. This continues until the word is fully guessed or the player runs out of chances.

End Condition:
The game ends in one of two ways:

The player correctly guesses all the letters in the word (win).

The player runs out of guesses (lose).

Game Reset:
After each round, the game is reset with a new random word from the list, allowing the player to play multiple rounds.

Code Breakdown:
Random Word Selection:
The random.choice() function selects a random word from the list of football clubs.

Game Logic:

The loop runs until the player either guesses the word or runs out of chances.

The player's input is validated using simple conditionals: if the letter is in the word, the hidden word is updated; otherwise, the number of remaining chances decreases.

String Manipulation:
The game heavily relies on string slicing and concatenation to update the hidden word after each correct guess.
