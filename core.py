import hangman
import configure

def main():
    """ Game Menu """

    hangman.print_open_msg()
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


if __name__ == "__main__":
    main()
