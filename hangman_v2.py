# -----------------------------------------------------------------------
# Imports the random module.
# -----------------------------------------------------------------------

import random
import os

# -----------------------------------------------------------------------
# Guest welcome
# -----------------------------------------------------------------------

print('Hello, ' + os.getlogin() + '. How are you?')
print('Welcome to hangman version 1.0.\nYou have 7 turns to guess a random word.\nGood luck.\n')

# -----------------------------------------------------------------------
# Defines the function with which the player opens the file containing
# the word list and then selects a random value from that word list.
# In this instance that file will be word_list.txt
# /Users/CFPCyOps/PycharmProjects/Hangman/word_list.txt
# -----------------------------------------------------------------------

def generator():
    with open("word_list.txt", "r") as a:
        my_list = a.read().splitlines()
    return random.choice(my_list)

# -----------------------------------------------------------------------
# Calls to the generator function to pass a random string to the
# variable, secret_word.
# -----------------------------------------------------------------------

secret_word = generator()

# -----------------------------------------------------------------------
# Replaces the letters in any given string with the requested character.
# -----------------------------------------------------------------------

def build(secret_word):

    for character in secret_word:
        data_capture = print("*", end="")
    print('\n', end='')

# -----------------------------------------------------------------------
# Defines the function to compare user input against characters within
# the secret_word string.
# -----------------------------------------------------------------------

def check(secret_word, your_guesses, guess, true_guesses, false_guesses):
    status = ""
    matches = 0

    for token in secret_word:
        if token in your_guesses:
            status += token
        else:
            status += "*"

        if token == guess:
            matches += 1

    if matches == 1:
        true_guesses.append(guess)

    if matches == 0:
        false_guesses.append(guess)

    return status

# -----------------------------------------------------------------------
# Defines the function with which remaining turns are calculated based
# on the difference between incorrect guesses, returned as the length of
# the string based on a compiled list and your initial integer of seven.
# -----------------------------------------------------------------------

def turns_remaining(your_guesses, false_guesses, true_guesses):

    false_guess_list_string = ''.join(map(str, false_guesses))

    turns = 7 - len(false_guess_list_string)

    return turns

# -----------------------------------------------------------------------
# Defines the function that will execute the Hangman game script and
# includes the defined parameters of a game.
# -----------------------------------------------------------------------

def hangman(build):
    your_guesses = []
    false_guesses = []
    true_guesses = []
    guess = ''

    while (turns := turns_remaining(your_guesses, false_guesses, true_guesses)) > 0:

        guess = input("Please enter your next guess: ")

        if guess in your_guesses:

            continue

        elif len(guess) == 1:

            your_guesses.append(guess)

            result = check(secret_word, your_guesses, guess, true_guesses, false_guesses)

            if result == secret_word:
                print("Congratulations you win")
                print(secret_word)
                break

            else:
                (turns := turns_remaining(your_guesses, false_guesses, true_guesses))
                print("\nRemaining turns: ", turns)
                print(result)

        else:

            continue

    if turns == 0:
        print(secret_word)
        print("You lose.")

# -----------------------------------------------------------------------
# Calls the Hangman function and executes the game script.
# -----------------------------------------------------------------------

hangman(build(secret_word))
