from PIL import Image, ImageFont, ImageDraw
import random
from dataclasses import dataclass
import numpy as np


@dataclass
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

    block_width: int = 60
    block_height: int = 60
    correct_location_color: str = "#00274C"
    incorrect_location_color: str = "#FFCB05"
    incorrect_color: str = "#D3D3D3"
    space_between_letters: int = 5
    word_color: str = "#FFFFFF"


def get_display_spec() -> DisplaySpecification:
    """Returns the default display specification for WordyPy."""
    ds = DisplaySpecification()
    if DEBUG:
        print(ds)
    return ds


def get_word_list() -> list[str]:
    """Returns a list of words that can be used in WordyPy."""
    return list(
        set(map(lambda x: x.strip().upper(), open("words.txt", "r").readlines()))
    )


DEBUG: bool = False


def set_debug_mode(debug: bool):
    """Sets the debug mode for WordyPy, printing out extra information when True.

    This command does nothing on the autograder, but may help you understand what
    the game system is doing if you set it to True.
    Args:
        debug: A boolean value indicating if debug mode is enabled.
    """
    global DEBUG
    DEBUG = debug


__last_target_word = None
__last_guesses = None
__known_pattern = None

IN_WORD = 1
CORRECT_LOCATION = 2
UNSEEN = 0


def get_board_state(
    target_word_debug: str = None, guess_words_debug: list[str] = None
) -> Image:
    """Returns an image representing the current state of the board.

    A WordPy board is a single PIL Image that uses the DisplaySpecification
    returned by get_display_spec(). The image will have at least one row
    in it, and at most 5 rows (e.g. there is at least one guess left to be
    made). The board state will follow the rules of WordyPy.

    Args:
        target_word_debug: Optional, a string representing the target word. This defaults to None, and the autograder will not have this parameter, it is only for testing a specific target word.
        guess_words_debug: Optional, a list of strings representing the guess words. This defaults to None, and the autograder will not have this parameter, it is only for testing specific word guess combinations.
    """

    global __last_target_word
    global __last_guesses
    global __known_pattern

    word_list: list[str] = get_word_list()
    display_spec: DisplaySpecification = get_display_spec()

    if target_word_debug == None:
        target_word = random.choice(word_list)
        word_list.remove(target_word)
    else:
        target_word = target_word_debug

    if guess_words_debug == None:
        num_guesses = random.randint(1, 5)
    else:
        num_guesses = len(guess_words_debug)

    guesses: list[str] = []
    if guess_words_debug == None:
        for i in range(0, num_guesses):
            guess = random.choice(word_list)
            word_list.remove(guess)
            guesses.append(guess)
    else:
        guesses = guess_words_debug

    __last_target_word = target_word
    __last_guesses = []  # bug fix, null list and append to it in make_guess()
    __known_pattern = np.zeros(len(target_word), dtype=np.int8)

    if DEBUG:
        print(
            f"Target Word: {target_word}\nNumber of Guesses: {
                num_guesses}\nGuesses: {guesses}"
        )

    def _render_letter(letter: str, target_letter: str, position: int) -> Image:
        color: str = display_spec.incorrect_color
        if letter == target_letter:
            color = display_spec.correct_location_color
        elif letter in target_word:
            color = display_spec.incorrect_location_color

        block = Image.new(
            "RGB",
            (display_spec.block_width, display_spec.block_height),
            color=color,
        )
        draw = ImageDraw.Draw(block)

        X: int = display_spec.block_width // 2
        Y: int = display_spec.block_height // 2

        FONT_SIZE: int = 50
        font = ImageFont.truetype("Roboto-Bold.ttf", FONT_SIZE)
        draw.text((X, Y), letter, size=FONT_SIZE, anchor="mm", font=font)
        return block

    WORD_WIDTH: int = (len(target_word) * display_spec.block_width) + (
        len(target_word) - 1
    ) * display_spec.space_between_letters
    WORD_HEIGHT: int = display_spec.block_height
    final_image = Image.new(
        "RGB", (WORD_WIDTH, WORD_HEIGHT * num_guesses), color=display_spec.word_color
    )

    # For each guess, generate the line image
    for i in range(0, num_guesses):
        # Generate a random guess
        guess = guesses[i]

        word = Image.new(
            "RGB", (WORD_WIDTH, WORD_HEIGHT), color=display_spec.word_color
        )
        curr_loc = 0
        for position, letter in enumerate(guess):
            rendered_letter: Image = _render_letter(
                letter, target_word[position], position
            )
            word.paste(rendered_letter, (curr_loc, 0))
            curr_loc += display_spec.block_width + display_spec.space_between_letters

        final_image.paste(word, (0, i * WORD_HEIGHT))

        # Bug fix: also call make_guess so that __known_pattern is updated
        make_guess(guess)
    return final_image


def make_guess(guess: str) -> bool:
    """Makes a guess for a hidden target word.

    This should only be called after get_board_state() as otherwise there will be no target word to
    guess against. This function will return True if the guess is correct, and False otherwise. If
    the guess does not follow WordyPy rules or does not make best use of the board returned by
    get_board_state() then, the function will raise a ValueError.

    Args:
        guess: A string representing the user's guess for the target word.

    Returns:
        A boolean value indicating if the guess was correct or not.
    """
    global __last_target_word
    global __last_guesses
    global __known_pattern

    if DEBUG:
        print(f"Guess: {guess}")
        print(f"Last Target Word: {__last_target_word}")
        print(f"Last Guesses: {__last_guesses}")

    if __last_target_word == None:
        raise ValueError(
            "You must call get_board_state() before you can make_guess() as there is no target word set"
        )

    if guess == None or type(guess) != str or len(guess) != len(__last_target_word):
        raise ValueError(
            "Your guess must be a string and the same length as the target word."
        )

    if guess in __last_guesses:
        raise ValueError(
            "You have already guessed this word, you must guess a unique word."
        )
    else:
        __last_guesses.append(guess)

    if guess == __last_target_word:
        return True

    # verify that their guess uses all of the same information from
    for position, letter in enumerate(guess):
        if (
            __known_pattern[position] == CORRECT_LOCATION
            and letter != __last_target_word[position]
        ):
            raise ValueError(
                f"You have guessed that the letter {letter} should be in position {
                    position} but a previous guess already was flagged as correct indicating that letter {__last_target_word[position]} should be in this position."
            )

    # verify that all of the known letters in word are in their guess as well
    for position, code in enumerate(__known_pattern):
        if code == IN_WORD and __last_target_word[position] not in guess:
            raise ValueError(
                f"Previous guesses have indicated that letter {
                    __last_target_word[position]} is in the word somewhere, but you have not guessed letter anywhere in your word."
            )
    return False
