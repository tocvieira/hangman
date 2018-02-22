import random


def get_user_attempt():
    while True:
        try:
            user_attempt = int(input("Digite o seu número:"))
            if user_attempt == 999:
                break
            elif user_attempt <= 0 or user_attempt > 100:
                print("\n Erro: Digite um valor entre 1 e 100. \n")
            else:
                break

        except ValueError:
            print("Você precisa digitar um número inteiro")
    return user_attempt

def divination(secret_number):
    maximum_number_of_attempt = set_level()
    number_of_attempt = 0
    list_of_attempts = []

    while number_of_attempt < maximum_number_of_attempt:
        user_attempt = get_user_attempt()

        if user_attempt != 999:
            list_of_attempts.append(user_attempt)

        if user_attempt == 999:
            get_tip(list_of_attempts, secret_number)
            continue
        elif secret_number == user_attempt:
            print("Você acertou! O número secreto é {}".format(user_attempt))
            quit()
        else:
            if user_attempt > secret_number:
                print("\nDica: Sua tentativa é MAIOR do que o número secreto \n")
            else:
                print("\nDica: Sua tentativa é MENOR do que o número secreto \n")
            number_of_attempt += 1
        print("\nVocê já tentou {} vezes, restam {}. Digite 999 para obter uma dica. \n".format(number_of_attempt,
                                                         maximum_number_of_attempt - number_of_attempt))
        #get_tip(list_of_attempts, secret_number)
    print("Você tentou os seguintes números {}, porém o número secreto era {}. Infelizmente acabaram suas chances. Você perdeu.".format(list_of_attempts, secret_number))

def get_tip(list_of_attempts, secret_number):
    list_of_minor_attempt = [1]
    list_of_major_attempt = [100]

    for x in list_of_attempts:
        if x < secret_number:
            list_of_minor_attempt.append(x)
        elif x > secret_number:
            list_of_major_attempt.append(x)

    print("\n Hummm Voce quer uma dica ? O número secreto está entre {} e {}".format(max(list_of_minor_attempt), min(list_of_major_attempt),))

def set_level():

    while True:
        try:
            level = int(input("Escolha o nível (1) Fácil (2) Moderado (3) Difícil: "))
            if level not in [1, 2, 3]:
                print("\nErro: Você deve escolher um número inteiro entre 1 e 3\n")
            else:
                break
        except ValueError:
            print("\nErro: Você deve escolher um número inteiro entre 1 e 3\n")
    if level == 1:
        maximum_number_of_attempt = 20
    elif level == 2:
        maximum_number_of_attempt = 10
    elif level == 3:
        maximum_number_of_attempt = 5

    return maximum_number_of_attempt


def main():
    print("*" * 36)
    print("* Bem vindo ao jogo de Adivinhação *")
    print("*" * 36)

    print("\nTente adivinhar o número secreto entre 1 e 100 \n")

    secret_number = random.randrange(1, 101)
    divination(secret_number)
    print("Fim do Jogo")

if __name__ == "__main__":
    main()