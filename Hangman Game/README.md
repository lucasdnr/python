# Hangman Game

This is a simple implementation of the classic Hangman game in Python. The game randomly selects a word from a provided list and challenges the player to guess the word by suggesting letters.

## How to Play

1. Run the program using a Python interpreter.
   ```
   python hangman-game.py
   ```

2. The game will display a welcome message and initialize a random word for you to guess.

3. Guess letters one at a time by entering them when prompted.

4. The game will inform you if the guessed letter is correct or not. If correct, it will reveal the positions of the letter in the secret word.

5. You have a limited number of attempts to guess the word. Be careful not to exceed this limit, or the game will end.

6. Win the game by successfully guessing all the letters in the secret word, or lose by running out of attempts.

## Features

- **Random Word Selection:** The secret word is randomly selected from a list of words stored in a "words.txt" file.

- **User Input:** Players can input their guesses by entering a letter when prompted.

- **Feedback:** The game provides feedback on each guess, indicating whether the guessed letter is correct or not.

- **Win/Lose Messages:** Upon winning or losing the game, a corresponding message is displayed along with a visual representation of a hanging man in the case of a loss.

## Files

- **words.txt:** A text file containing a list of words from which the secret word is randomly selected.

