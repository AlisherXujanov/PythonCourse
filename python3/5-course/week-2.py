# ARCHITECHTURE 

# The new architecture diagram for WordyPy is the following(bold indicates new elements from assignment 1)
# -----------------------------------------
# LETTER
# letter:str
# in_correct_place:bool=False
# in_word:bool=False
# __init__(self, letter:str) -> None
# is_in_correct_place(self) -> bool
# is_in_word(self) -> bool
# -----------------------------------------
# DISPLAY SPECIFICATION
# block_width:int=80
# block_height:int=80
# space_between_letters:int=5
# correct_location_color:str="#00274C"
# incorrect_location_color:str="#FFCB05"
# incorrect_color:str="#D3D3D3"
# word_color:str="#FFFFFF"
# -----------------------------------------
# BOT
# target_word:list[str]
# display_spec:DisplaySpecification
# __init__(self, word_list_file:str, display_spec:DisplaySpecification) -> None
# _tuple_to_str(self, pixels:str) -> str
# _process_image(self, guess:str, guess_image:Image) -> list[Letter]
# make_guess(self) -> str
# record_guess_results(self, guess:str, guess_results:Image) -> None
# -----------------------------------------




import random
from PIL import Image, ImageFont, ImageDraw
from typing import List, Tuple
from IPython.display import display

class Letter:
    def __init__(self, letter: str):
        self.letter = letter
        self.in_correct_place = False
        self.in_word = False

    def __str__(self):
        return f"Letter({self.letter})"

    def __repr__(self):
        return f"Letter({self.letter})"

    def __eq__(self, other):
        return self.letter == other.letter

    def __hash__(self):
        return hash(self.letter)

    def __lt__(self, other):
        return self.letter < other.letter

    def __gt__(self, other):
        return self.letter > other.letter

    def is_in_correct_place(self) -> bool:
        return self.in_correct_place

    def is_in_word(self) -> bool:
        return self.in_word


class DisplaySpecification:
    """A dataclass for holding display specifications for WordyPy. The following
    values are defined:
        - block_width: the width of each character in pixels
        - block_height: the height of each character in pixels
        - correct_location_color: the hex code to color the block when it is correct
        - incorrect_location_color: the hex code to color the block when it is in the wrong location but exists in the string
        - incorrect_color: the hex code to color the block when it is not in the string
        - space_between_letters: the amount of padding to put between characters, in pixels
        - word_color: the hex code of the background color of the string
    """

    block_width: int = 80
    block_height: int = 80
    correct_location_color: str = "#00274C"
    incorrect_location_color: str = "#FFCB05"
    incorrect_color: str = "#D3D3D3"
    space_between_letters: int = 5
    word_color: str = "#FFFFFF"


# Create the implementation of the Bot class here

# YOUR CODE HERE
class Guess:
    def __init__(self, guess: str):
        self.guess = guess

class Bot:
    def __init__(self, target_word: str, display_spec: DisplaySpecification):
        self.target_word = target_word
        self.letters = [Letter(letter) for letter in target_word]
        self.display_spec = display_spec
        self.word_list = []  # Ideally populated with guessable words

    def record_guess_results(self, guess: Guess, guess_image: Image):
        # Improve image processing to infer letter matches
        letters = self._process_image(guess, guess_image)

        for i, letter in enumerate(letters):
            # Update the corresponding letter status in self.letters
            if letter.is_in_correct_place():  # Assuming you have this method defined in Letter
                # Mark as correctly placed
                self.letters[i].in_correct_place = True
            elif letter.is_in_word():  # Assuming you have this method defined in Letter
                # Mark as in word but not in the correct place
                self.letters[i].in_word = True

        # Optionally prune possible guesses based on the results from this guess
        self._prune_word_list()  # This method should filter self.word_list

    def make_guess(self) -> str:
        available_guesses = [
            letter.letter for letter in self.letters if not letter.in_word and not letter.in_correct_place
        ]
        if available_guesses:
            # Return a random available guess
            return random.choice(available_guesses)
        else:
            # Return a random letter from the target word as a fallback option
            return random.choice(self.target_word)


    def _process_image(self, guess: str, guess_image: Image) -> list[Letter]:
        letters = []
        for i in range(len(guess)):
            color = self._tuple_to_str(guess_image.getpixel((i, 0)))
            letter = Letter(guess[i])
            if color == self.display_spec.correct_location_color:
                letter.in_correct_place = True
            elif color == self.display_spec.incorrect_location_color:
                letter.in_word = True
            letters.append(letter)
        return letters


    def _tuple_to_str(self, pixels: Tuple[int]) -> str:  
        return "#" + "".join(f"{x:02X}" for x in pixels[:3])  

    def _prune_word_list(self):
        # Implement pruning logic based on self.letters. You will have to
        # filter out any words that contradict the knowledge in self.letters.
        # For instance, eliminate any words containing letters that are marked as
        # not in the correct word's place or already guessed.
        self.word_list = [word for word in self.word_list if all(letter.is_in_correct_place() or letter.is_in_word() for letter in self.letters)]

