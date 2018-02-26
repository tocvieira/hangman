# -*- coding: utf-8 -*-
""" Hangman Game Menu
You can play the game or configure new words and hints
"""

import hangman
import configure

GALLOWS = r"""{0}    |_______________``\
{0}    [/]           [  ]
{0}    [\]           | ||
{0}    [/]           |  |
{0}    [\]           |  |
{0}    [/]           || |
{0}   [---]          |  |
{0}   [---]          |@ |
{0}   [---]          |  |
{0}  oOOOOOo         |  |
{0} oOO___OOo        | @|
{0}oO/|||||\Oo       |  |
{0}OO/|||||\OOo      |  |
{0}*O\ x x /OO*      |  |
{0}/*|  c  |O*\      |  |
{0}   \_O_/    \     |  |
{0}    \#/     |     |  |
{0}|       |  |     | ||
{0} |       |  |_____| ||__
{0}_/_______\__|  \  ||||  \
{0}/         \_|\  _ | ||\  \
{0}|    V    |\  \//\  \  \  \
{0}|    |    | __//  \  \  \  \
{0}|    |    |\|//|\  \  \  \  \
{0}------------\--- \  \  \  \  \
{0}\  \  \  \  \  \  \  \  \  \  \
{0}_\__\__\__\__\__\__\__\__\__\__\
{0}__|__|__|__|__|__|__|__|__|__|__|
{0}|___| |___|
{0}|###/ \###|
{0}\##/   \##/"""

def main():
    """ Game Menu """

    print_open_msg()
    controler = True

    while controler:
        option = int(input("\nDigite:\n(1) Jogar\n(2) Adicionar Palavras\nQual é a sua escolha:"))
        if option == 1:
            hangman.main()
            controler = False
        elif option == 2:
            configure.main()
            controler = False
        else:
            print("\n\n Erro: Escolha (1) Jogar ou (2) Adicionar Palavras\n")

def print_open_msg():
    """ Prints game opening message. """

    print(GALLOWS.format(7 * ' '))
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************\n")
    print("Desenvolvido por Thiago Vieira especialmente para "
          "seu filho João Lucas\n")

if __name__ == "__main__":
    main()
