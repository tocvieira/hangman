# -*- coding: utf-8 -*-
""" Just another Python Hangman Game

The Hangman is a game in which the player has to guess which is
the proposed word, having as a tip the number of letters and the theme
connected to the word. With each wrong letter, a part of the body of
the hangman is drawn.

The game ends either with the correctness of the word or
with the completion of the body parts of the hangman.

Available functions:
- Only alpha characters are accepted;
- Repeated attempts are not penalized;
- Possibility of trying the word in its entirety.
- Sound Music
- Sound Effects
- To get a hint type: dica
"""

import ast
import pathlib
import random

from pygame import mixer


MUSIC_FILE = pathlib.Path('music.mp3')
HIT_FILE = pathlib.Path('hit.wav')
WORDS_FILE = pathlib.Path('words.txt')
WORDS_AND_HINTS_FILE = pathlib.Path('words_and_hints.txt')

DEFAULT_WORDS_AND_HINTS = [
    ('bicicleta', 'brinquedo'),
]


HANGING_LACE = r"""{0}     |/|
{0}     |/|
{0}     |/|
{0}     |/|
{0}     |/|
{0}     |/|
{0}     |/| /¯)
{0}     |/|/\/
{0}     |/|\/
{0}    (¯¯¯)
{0}    (¯¯¯)
{0}    (¯¯¯)
{0}    (¯¯¯)
{0}    (¯¯¯)
{0}    /¯¯/\
{0}   / ,^./\
{0}  / /   \/\
{0} / /     \/\
{0}( (       )/)
{0}| |       |/|
{0}| |       |/|
{0}| |       |/|
{0}( (       )/)
{0} \ \     / /
{0}  \ `---' /
{0}   `-----''"""


HANGING_MAN = """\
  _______
 |/      |
 |      {0}
 |      {1}{2}{3}
 |       {4}
 |      {5} {6}
 |
_|___
"""


SKULL = r"""{0}    _______________
{0}   /               \
{0}  /                 \
{0}//                   \/\
{0}\|   XXXX     XXXX   | /
{0} |   XXXX     XXXX   |/
{0} |   XXX       XXX   |
{0} |                   |
{0} \__      XXX      __/
{0}   |\     XXX     /|
{0}   | |           | |
{0}   | I I I I I I I |
{0}   |  I I I I I I  |
{0}   \_             _/
{0}     \_         _/
{0}       \_______/"""


TROPHY = r"""{0}  ___________
{0} '._==_==_=_.'
{0} .-\\:      /-.
{0}| (|:.     |) |
{0} '-|:.     |-'
{0}   \\::.    /
{0}    '::. .'
{0}      ) (
{0}    _.' '._
{0}   '-------'"""


def main():
    """ Main function for hangman game. """

    print_open_msg()
    play_sound()
    # secret_word = get_secret_word()
    word_and_hint = random.choice(get_secret_word_and_hint())
    secret_word, hint = word_and_hint
    secret_word = secret_word.upper()
    if not hint:
        hint = 'sem dicas =/'

    successful_letters = starting_successful_letters(secret_word)
    print(successful_letters)

    hanged = False
    win = False
    mistakes = 0
    all_attempts = []

    while not hanged and not win:

        attempt = get_attempt(secret_word)

        if attempt == secret_word:
            print_victory_message()
            quit()

        elif attempt == "DICA":
            print("\n A dica é: {}\n".format(hint))
            continue

        elif (not str.isalpha(attempt)
              or len(attempt) > 1
              and len(attempt) == 2):
            # Non alpha characters and two digits are considered typos.
            # Three characters or more are wrong attempts.
            print("Digite apenas uma letra!")
            continue

        elif attempt in all_attempts:
            # Repeated attempts do not lose points
            print("Você já tentou a letra: {}".format(attempt))
            continue

        elif attempt in secret_word:
            # record correct attempts
            play_effect_sound_hit()
            all_attempts.append(attempt)
            write_correct_attempt(attempt,
                                  successful_letters,
                                  secret_word)
        else:
            # Record Lose Points and Draw Gallows
            mistakes += 1
            all_attempts.append(attempt)
            draw_gallows(mistakes)

        hanged = mistakes == 7
        win = "_" not in successful_letters

        print(successful_letters)

    if win:
        print_victory_message()

    else:
        print_defeat_message(secret_word)


def draw_gallows(mistakes):
    """ Prints hanging man status according to number of mistakes. """

    print(HANGING_MAN
          .format("(_)" if mistakes > 0 else '',
                  "\\" if mistakes > 1 else '',
                  "|" if mistakes > 2 else '',
                  "/" if mistakes > 3 else '',
                  "|" if mistakes > 4 else '',
                  "/" if mistakes > 5 else '',
                  "\\" if mistakes > 6 else ''))


def print_victory_message():
    """ Prints message when winning condition is reached. """

    print("Parabéns, você ganhou!")
    print(TROPHY.format(5 * ' '))


def print_defeat_message(secret_word):
    """ Prints message when losing condition is reached. """

    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(secret_word))
    print(SKULL.format(''))


def write_correct_attempt(attempt, successful_letters, secret_word):
    """ write the letters found in the correct position """
    index = 0
    for letter in secret_word:
        if attempt == letter:
            successful_letters[index] = letter
        index += 1


def get_attempt(secret_word):
    """ Returns the input attempt. """
    return input("Digite uma letra ou uma palavra com {} letras:"
                 .format(len(secret_word))).upper()


def starting_successful_letters(word):
    """ Initializes the string that records progress """
    return ["_" for letter in word]


def print_open_msg():
    """ Prints game opening message. """

    print(HANGING_LACE.format(7 * ' '))
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************\n")
    print("Desenvolvido por Thiago Vieira especialmente para "
          "seu filho João Lucas\n")


# def get_secret_word():
#     """ Take a random word in the words.txt file """
#     words = []
#     with open("words.txt", "r") as file:
#         for line in file:
#             line = line.strip()
#             words.append(line)
#
#     number = random.randrange(0, len(words))
#     secret_word = words[number].upper()
#     return secret_word


def get_secret_word_and_hint():
    """ Retrieves list of word and hint tuples.  """
    words_and_hints = []

    if WORDS_AND_HINTS_FILE.is_file():
        with WORDS_AND_HINTS_FILE.open("rt") as words_and_hints_file:
            file_content = words_and_hints_file.read()
            words_and_hints = ast.literal_eval(file_content)
    elif WORDS_AND_HINTS_FILE.is_file():
        with WORDS_AND_HINTS_FILE.open("rt") as words_file:
            words_and_hints = [(word, '')
                               for raw_line in words_file.readlines()
                               for word in (raw_line.strip(), )
                               if word]
    else:
        words_and_hints = DEFAULT_WORDS_AND_HINTS

    return words_and_hints


def play_sound():
    """ Play Music """
    if not MUSIC_FILE.is_file():
        return
    mixer.init()
    mixer.music.load(str(MUSIC_FILE))
    mixer.music.play(-1)


def play_effect_sound_hit():
    """ Plays a sound for correct attempts """
    if not HIT_FILE.is_file():
        return
    effect = mixer.Sound(str(HIT_FILE))
    effect.play()


if __name__ == "__main__":
    main()
