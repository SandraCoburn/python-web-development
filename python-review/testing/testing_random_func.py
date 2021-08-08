import random


def guess_game(guess, answer):
    if 0 < guess < 11:
        if guess == answer:
            print('you are a genius!')
            return True
    else:
        print('hey you, I said 1~10')


answer = random.randint(1,10)
if __name__ == '__main__':
    while True:
        try:
            guess = int(input('guess a number 1~10: '))
            if (guess_game(guess, answer)):
                break
        except ValueError:
            print('please enter a number')
            continue