import random

def main():
    print("*" * 16)
    print("* Hangman Game *")
    print("*" * 16)

    hangman()

def hangman():

    secret_world = get_secret_word()
    win = False
    lose = False
    guesses =[]

    while (not win and not lose):
        user_attempt = get_user_attempt(secret_world)
        if user_attempt in guesses:
            print("You already guessed {}".format(user_attempt))
            continue
        else:
            guesses.append(user_attempt)
            result = check(secret_world, guesses, user_attempt)
            print(result)
            if result == secret_world:
                print("You Win")
                win = True

def get_user_attempt(secret_world):
    while True:
        user_attempt = input("Please enter one letter or a {} letter word:".format(len(secret_world))).upper()
        if user_attempt == secret_world.upper():
            print("You win! The secret word is {}".format(secret_world))
            quit()
        elif not str.isalpha(user_attempt) or len(user_attempt) > 1:
            print("Only one letter is allowed!")
        else:
            break;
    return user_attempt

def get_secret_word():
    words =['Banana',
            'Carro',
            'Escola',
            'Uva',
            'Goiba',
            'Caixa']
    return random.choice(words).upper()

def check(secret_world, guesses, user_attempt):
    status = ''
    matches = 0
    for letter in secret_world:
        if letter in guesses:
            status += letter
        else:
            status += ' _ '
        if letter == user_attempt:
            matches += 1
    if matches > 1:
        print('Yes! The word contains {}: {}'.format(matches, user_attempt))
    elif matches == 1:
        print ("Yes! The word contains {}".format(user_attempt))
    else:
        print("Sorry. The word don't contains {}".format(user_attempt))

    return status


if __name__ == "__main__":
    main()
