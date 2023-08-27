import random


def word_generator(n: int):
    """
    Function create random word in diapason of n nums
    """

    symbols = 'qwertyuiopasdfghjklzxcvbnm1234567890'
    s = [c for c in symbols]
    word = ''
    for _ in range(n):
        word += random.choice(s)
    return word