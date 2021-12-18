from random import randint


def guessing():
    """


    """
    
    while True:
        try:
            guess = int(input('Guess the number: '))
            break
        except ValueError:
            print("It's not a number")
    return guess


def game():
    """
    Simple game of guessing a number drawn by a computer.
    Number is within range 1 - 100.
    """

    answer = randint(1, 100)

    while True:
        guess = guessing()
        if guess > answer:
            print('Too big!')
            continue
        if guess < answer:
            print('Too small')
            continue
        if guess == answer:
            print('You win!')
            return


game()
