# -*- coding: utf-8 -*-
""" Just another Python Hangman Game """

import random
from pygame import mixer


def main():
    print_open_msg()
    play_sound()
    secret_word = get_secret_wolrd()

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

        elif not str.isalpha(attempt) or len(attempt) > 1 and len(attempt) == 2:
            """Non alpha characters and two digits are considered typos. Three characters or more are wrong attempts."""
            print("Digite apenas uma letra!")
            continue

        elif attempt in all_attempts:
            """ Repeated attempts do not lose points """
            print("Você já tentou a letra: {}".format(attempt))
            continue

        elif attempt in secret_word:
            """ record correct attempts """
            play_effect_sound_hit()
            all_attempts.append(attempt)
            write_correct_attempt(attempt, successful_letters
                                  , secret_word)
        else:
            """ Record Lose Points and Draw Gallows """
            mistakes += 1
            all_attempts.append(attempt)
            draw_gallows(mistakes)

        hanged = mistakes == 7
        win = "_" not in successful_letters

        print(successful_letters
              )

    if win:
        print_victory_message()

    else:
        print_defeat_message(secret_word)


def draw_gallows(mistakes):
    print("  _______     ")
    print(" |/      |    ")

    if mistakes == 1:
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if mistakes == 2:
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if mistakes == 3:
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if mistakes == 4:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if mistakes == 5:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if mistakes == 6:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if mistakes == 7:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


def print_victory_message():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")


def print_defeat_message(secret_word):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(secret_word))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")


def write_correct_attempt(attempt, successful_letters, secret_word):
    """ write the letters found in the correct position """
    index = 0
    for letter in secret_word:
        if attempt == letter:
            successful_letters[index] = letter
        index += 1


def get_attempt(secret_word):
    attempt = input("Digite uma letra ou uma palavra com {} letras:".format(len(secret_word))).upper()
    return attempt


def starting_successful_letters(word):
    """ Initializes the string that records progress """
    return ["_" for letter in word]


def print_open_msg():
    print("       _______________         ")
    print("      /               \       ")
    print("     /                 \      ")
    print("   //                   \/\  ")
    print("   \|   XXXX     XXXX   | /   ")
    print("    |   XXXX     XXXX   |/     ")
    print("    |   XXX       XXX   |      ")
    print("    |                   |      ")
    print("    \__      XXX      __/     ")
    print("      |\     XXX     /|       ")
    print("      | |           | |        ")
    print("      | I I I I I I I |        ")
    print("      |  I I I I I I  |        ")
    print("      \_             _/       ")
    print("        \_         _/         ")
    print("          \_______/           ")
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************\n")
    print("Desenvolvido por Thiago Vieira especialmente para seu filho João Lucas\n")


def get_secret_wolrd():
    """ Take a random word in the words.txt file """
    words = []
    with open("words.txt", "r") as file:
        for line in file:
            line = line.strip()
            words.append(line)

    number = random.randrange(0, len(words))
    secret_word = words[number].upper()
    return secret_word


def play_sound():
    """ Play Music """
    mixer.init()
    mixer.music.load('music.mp3')
    mixer.music.play(-1)

def play_effect_sound_hit():
    """ Plays a sound for correct attempts """
    effect = mixer.Sound('hit.wav')
    effect.play()

if __name__ == "__main__":
    main()
