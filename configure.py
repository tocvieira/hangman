# -*- coding: utf-8 -*-
""" Script to add words and hints """
import csv
import pathlib

WORDS_AND_HINTS_FILE = pathlib.Path('words_and_hints.csv')


def get_new_words_and_hints():
    """Get New Word and Hint and call function write_csv()"""

    over = False
    while not over:
        word_and_hint = []
        new_word = input("\nDigite uma nova palavra:").strip()
        if not str.isalpha(new_word):
            print("\nError: Só letras são aceitas. \n")
            continue
        else:
            new_hint = input("Digite a dica: ")
            word_and_hint.append(new_word)
            word_and_hint.append(new_hint)
            write_csv(word_and_hint)
            option = input("\nPalavras adicionadas com sucesso. "
                           "Deseja continua ? (S/N): \n").upper()
            if option == "S":
                continue
            else:
                over = True

def write_csv(word_and_hint):
    """Write New Word and Hint on file."""
    if WORDS_AND_HINTS_FILE.is_file():
        with WORDS_AND_HINTS_FILE.open("a") as words_and_hints_file:
            csv_writerow = csv.writer(words_and_hints_file, delimiter='|')
            csv_writerow.writerow(word_and_hint)
    else:
        print("Arquivo de configuração não foi encontrado.\n")
        print("\n ... criando arquivo de configuração ...")
        creating_csv()


def creating_csv():
    """Creating words_and_hints.csv with one word"""
    with open("words_and_hints.csv", "w") as new_file:
        csv_writerow = csv.writer(new_file, delimiter='|')
        amor = ['amor', 'sentimento']
        csv_writerow.writerow(amor)
    main()

def main():
    """ Main Function """
    get_new_words_and_hints()

if __name__ == "__main__":
    main()
