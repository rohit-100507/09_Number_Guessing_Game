# Number Guessing Game 🎯

A simple beginner-friendly Python Number Guessing Game.

The computer generates a random number between **1 and 100**, and the player has to guess the correct number. After every guess, the program gives a hint whether the actual number is **bigger or smaller** than the guessed number.

After guessing the correct number, the player can choose whether to play another round.

## Features

* Generates a random number between 1 and 100
* Takes guesses from the user
* Gives hints when the guess is too high or too low
* Allows the player to play multiple rounds
* Validates the `yes/no` input
* Uses loops and conditional statements

## Concepts I Learned

While creating this project, I practiced:

* `while` loops
* `if`, `elif`, and `else`
* `break`
* `input()`
* Typecasting using `int()`
* String methods using `.lower()`
* Using the `import` statement
* Basic knowledge of Python's `random` module
* Using `random.randint()` to generate a random number

## Random Module

In this project, I learned how to import and use Python's built-in `random` module.

```python
import random

number = random.randint(1, 100)
```

`random.randint(1, 100)` generates a random integer between **1 and 100**.

## How the Game Works

1. The program generates a random number from 1 to 100.
2. The player enters a guess.
3. If the guess is smaller than the number, the program says the number is bigger.
4. If the guess is larger than the number, the program says the number is smaller.
5. If the guess is correct, the round ends.
6. The player can choose to play another round or stop the game.

## Example

```text
WELCOME TO NUMBER GUESSING GAME
GUESS THE NUMBER FROM 1 TO 100

GUESS THE NUMBER :50
WRONG..! NUMBER IS BIGGER THAN 50 TRY AGAIN...

GUESS THE NUMBER :75
WRONG..! NUMBER IS SMALLER THAN 75 TRY AGAIN...

GUESS THE NUMBER :63
RIGHT....! YOUR GUESS IS CORRECT

WANT TO PLAY ANOTHER ROUND ? (yes /no) : no
GAME STOPPED
```

## Purpose

This project was created as a beginner Python practice project to improve my understanding of **loops, conditions, user input, and the `random` module**.
