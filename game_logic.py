"""
This module contains the game logic for the snowman game.
"""
import random
from ascii_art import STAGES

# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]


def get_random_word():
    """Selects a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]

def display_game_state(mistakes, secret_word, guessed_letters):
    """
    Displays the current state of the game.
    """
    # Display the snowman stage for the current number of mistakes.
    print(STAGES[mistakes])
    # Build a display version of the secret word.
    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    print("Word: ", display_word)
    print("\n")

def play_game():
    """
    Main game loop.
    """
    secret_word = get_random_word()
    guessed_letters = []
    mistakes = 0

    print("Welcome to Snowman Meltdown!")
    print("Secret word selected: " + secret_word)  # for testing, later remove this line
    #display_game_state(mistakes, secret_word, guessed_letters)
    # TODO: Build your game loop here.
    while mistakes < len(STAGES) - 1:
        display_game_state(mistakes, secret_word, guessed_letters)
        # For now, simply prompt the user once:
        guess = input("Guess a letter: ").lower()
        print("You guessed:", guess)
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a letter only")
        if guess in guessed_letters:
            print(f'You already guessed "{guess}" letter! Try again')
        guessed_letters.append(guess)
        mistakes += 1


    display_game_state(mistakes, secret_word, guessed_letters)
    print("GAME OVER! The snowman has completely melted.")
    print(f"The secret word was: {secret_word}")