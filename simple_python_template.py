"""NMTAFE ICTPRG302:
Guess-My-Word Project Application"""
# See the assignment worksheet and journal for further details.
# Begin by completing the TODO items below in the order you specified in the journal
"""
Author: Izayah Chavez
Version:1.0
Copyright: 2023, Izayah Chavez
"""

import random

# File paths
TARGET_WORDS = './word-bank/target_words.txt'
VALID_WORDS = './word-bank/all_words.txt'

# Maximum number of tries
MAX_TRIES = 6

# Variable to track if the player wins
winner = False


# Display game instructions
def game_instruction():
    """
    Displays game instructions.
    """
    print("Wordle is a single player game.")
    print("Guess a five-letter hidden word.")
    print("You have six attempts.")
    print("'🟩' indicates correct letter in correct position.")
    print("'🟨' indicates correct letter in wrong position.")
    print("'🟥' indicates wrong letter.")


# Select a random target word
def select_target_word():
    """
    Selects a random target word from the word list.
    """
    try:
        word_list = open(TARGET_WORDS).read().splitlines()
        return random.choice(word_list)
    except FileNotFoundError:
        print("Error: File not found.")


# Check if a word is valid
def is_valid_word(word):
    """
    Checks if a word is valid.
    """
    try:
        valid_word_list = open(VALID_WORDS).read().splitlines()
        return word in valid_word_list
    except FileNotFoundError:
        print("Error: File not found.")


# Generate clues based on target word and guess
def get_clues(target_word, guess):
    """
    Generates clues based on the target word and the player's guess.


    """
    clues = ""
    for target_char, guess_char in zip(target_word, guess):
        if guess_char == target_char:
            clues += 'O'
        elif guess_char in target_word:
            clues += '+'
        else:
            clues += '-'
    return clues


# Score the guess based on the target word
def score_guess(target, guess):
    """
    Scores the guess based on the target word.
    """
    score = [0, 0, 0, 0, 0]
    for i in range(len(target)):
        if guess[i] == target[i]:
            score[i] = 2
        elif guess[i] in target:
            score[i] = 1
        else:
            score[i] = 0

    symbol_score = ''

    for mark in score:
        if mark == 2:
            symbol_score += '🟩'
        elif mark == 1:
            symbol_score += '🟨'
        else:
            symbol_score += '🟥'

    return ' '.join(symbol_score)


# Play the Wordle game
def play_wordle(is_winner):
    """
    Plays the Wordle game.
    """
    game_instruction()
    target_word = select_target_word()
    attempts = MAX_TRIES
    while attempts > 0:
        guess = input("Enter your guess: ").lower()
        attempts -= 1
        if not is_valid_word(guess):
            print("Invalid word! Please enter a valid word.")
            attempts -= 1
            continue
        if guess == target_word:
            print("Congratulations! You guessed the word correctly!")
            winner = True
            break
        print(score_guess(target_word, guess))
        print(' '.join(guess.upper()))


# Main game loop
print("Game over")
if not winner:
    play_wordle(winner)
