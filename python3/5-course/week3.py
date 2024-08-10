# You now understand the rules of WordyPy and how to read the game state from an image.
# Now your job is to read in a WordyPy partial play and provide a next good guess.
# What's a good guess? A good guess is one which:

# Continues to adhere to the rules of WordPy
# Does not repeat words which have already been played
# Uses the knowledge of previous guesses to pick a new good word
# Unlike previous assignments there are no guardrails for this task -- you can complete this
# using whatever software architecture you like! In addition, I've put my code in a new module
# for you to import, called wordy. You can just import this module and begin making calls to it.
# You should be able to understand how it works by reading the module documentation.

import wordy
import PIL
import random


def solution(board: PIL.Image) -> str:
    """The student solution to the problem.

    You must write code to query the wordy module and make
    a guess for the word. You needs to inspect the module to
    understand how to do this, and this function should only return
    the guess that you are going to make based on the game board state.

    Returns:
        str: The guess that you are going to make.
    """
    new_guess = ""
    # YOUR CODE HERE
    # Get the target word
    target_word = wordy.__last_target_word

    # Get the known pattern
    known_pattern = wordy.__known_pattern

    # Get the list of words
    word_list = wordy.get_word_list()

    # Filter the word list to only include words of the same length as the target word
    word_list = [word for word in word_list if len(word) == len(target_word)]

    # Filter the word list to only include words that match the known pattern
    for i, pattern in enumerate(known_pattern):
        if pattern == wordy.CORRECT_LOCATION:
            word_list = [
                word for word in word_list if word[i] == target_word[i]]
        elif pattern == wordy.IN_WORD:
            word_list = [word for word in word_list if word[i] in target_word]
        elif pattern == wordy.UNSEEN:
            pass

    # Choose a random word from the filtered list
    new_guess = random.choice(word_list)
    return new_guess


# The autograder for this assignment is easy, it will try and play
# a few rounds of the game and ensure that errors are not thrown. If
# you can make it through five rounds we'll assume you have the right
# solution!
#
# You SHOULD NOT change anything in the wordy module, instead you
# must figure out how to write the solution() function in this notebook
# to make a good guess based on the board state!
for i in range(5):
    try:
        # Get an image of the current board state from wordy.
        # Note that the image contains some number of random guesses (always less than 5 guesses).
        image = wordy.get_board_state()
        # Create a new *good* guess based on the image and rules of wordy
        new_guess = solution(image)  # your code goes in solution()!
        # Send that guess to wordy to make sure it doesn't throw any errors
        wordy.make_guess(new_guess)
    except Exception as e:
        raise e
