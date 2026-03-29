"""
This module contains the game logic for the snowman game.
"""
import random
import os
from ascii_art import STAGES

WORDS = ["python", "git", "github", "snowman", "meltdown"]


def get_random_word():
    """Selects a random word from the list."""
    return random.choice(WORDS)

def display_game_state(mistakes, secret_word, guessed_letters):
    """Displays the current state of the game."""
    print(STAGES[mistakes])
    display_word = " ".join(letter if letter in guessed_letters else "_" for letter in secret_word)
    print("Word:", display_word)

def clear_screen():
    """Clears the screen."""
    os.system("cls" if os.name == "nt" else "clear")

def play_again():
    """Ask the user if they want to play again."""
    while True:
        choice = input("Do you want to play again? (y/n): ").strip().lower()
        if choice == "y":
            clear_screen()
            play_game()
            return
        if choice == "n":
            print("Goodbye!")
            return
        print("Invalid choice, please type y or n.")


def play_game():
    """Main game loop."""
    secret_word = get_random_word()
    guessed_letters = []
    mistakes = 0

    print("=" * 28)
    print("Welcome to Snowman Meltdown!")
    print("=" * 28)

    while mistakes < len(STAGES) - 1:
        display_game_state(mistakes, secret_word, guessed_letters)

        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print(f'You already guessed "{guess}". Try again.')
            continue

        guessed_letters.append(guess)

        if guess in secret_word:
            print(f">> Good job! '{guess}' is in the word.")
        else:
            mistakes += 1
            print(f">> Sorry, '{guess}' is not in the word.")

        if set(secret_word).issubset(guessed_letters):
            display_game_state(mistakes, secret_word, guessed_letters)
            print("🎉 Congratulations! You saved the snowman.")
            print(f"The word was: {secret_word}")
            play_again()
            return

    display_game_state(mistakes, secret_word, guessed_letters)
    print("GAME OVER! The snowman has completely melted.")
    print(f"The secret word was: {secret_word}")
    play_again()
