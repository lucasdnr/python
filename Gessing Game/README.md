# Guessing Game

## Overview

Welcome to the Guessing Game! This simple Python program allows users to play a guessing game where they attempt to guess a randomly generated secret number between 1 and 100. The game provides different difficulty levels with varying numbers of attempts, and users earn or lose points based on their guessing accuracy.

## How to Play

1. Run the program.
2. The game will prompt you to choose a difficulty level:
   - (1) Easy: 20 attempts
   - (2) Normal: 10 attempts
   - (3) Pro: 5 attempts
3. Guess the secret number by entering a number between 1 and 100 when prompted.
4. After each attempt, the game will provide feedback on whether your guess was correct, greater than the secret number, or less than the secret number.
5. Your score is calculated based on the number of attempts and the accuracy of your guesses.
6. The game ends when you either correctly guess the secret number or run out of attempts.

## Scoring

- Correct Guess: You earn points equal to your remaining attempts.
- Incorrect Guess: Points are deducted based on the difference between your guess and the secret number.

## Example

```
*********************************
Welcome to Guessing Game v0.1.0!
*********************************
What is the difficulty level?
(1) Easy (2) Normal (3) Pro
Set the level: 2
Attempt 1 of 10
Enter your number between 1 and 100: 50
Your number is: 50
You failed! Your number is greater than the secret number
Attempt 2 of 10
Enter your number between 1 and 100: 30
Your number is: 30
You failed! Your number is less than the secret number
...
The secret number was 42. Total points 670
End
```

Feel free to modify and explore the code to enhance your gaming experience!