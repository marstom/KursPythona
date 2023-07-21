"""

Gra hangman

"""

import random


guesses = ["ala ma kota", "python jest fajny", "lubię placki", "jakie piękne", "zuzanna lubi je tylko o północy"]

random_guess = guesses[random.randint(0,len(guesses)-1)]
print(random_guess)

hidden_guess = [' ' if ch==' ' else '.' for ch in random_guess]

stages = [
    """
    ......
    ......
    ......
    ......
    ......
    ......
    """,
    """
    ......
    ......
    ......
    ......
    ......
    ../\..
    """,
    """
    ......
    ...|..
    ...|..
    ...|..
    ...|..
    ../\..
    """,
    """
    ......
    .--|..
    ...|..
    ...|..
    ...|..
    ../\..
    """,
    """
    ......
    .--|..
    .|.|..
    ...|..
    ...|..
    ../\..
    """,
    """
    ......
    .--|..
    .|.|..
    .o.|..
    ...|..
    ../\..
    """,
    """
    ......
    .--|..
    .|.|..
    .o.|..
    .x.|..
    ../\..
    """,
]

print(stages[0])
print(''.join(hidden_guess))


class InvalidLength(Exception):
    pass

def get_ch(ch, guess):
    if len(ch) != 1:
        raise InvalidLength("Must be single character!")


