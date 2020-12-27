#!/usr/bin/python3

from random import randint

def decToBin(x):
    maxNum = 2 ** x - 1
    maxDec = len(str(maxNum))
    random_number = randint(0, maxNum)
    print(f'{"-" * maxDec} (10)')
    print(f"{random_number:{maxDec}d}")
    print(f'{"-" * x} (2)')

    answer = int(input(), 2)

    if answer == random_number:
        return 1
    else:
        print(f"Error: {answer:{maxDec}d}")
        return 0


def binToDec(x):
    maxNum = 2 ** x - 1
    maxDec = len(str(maxNum))
    random_number = randint(0, maxNum)
    print(f'{"-" * x} (2)')
    print(f"{random_number:0{x}b}")
    print(f'{"-" * maxDec} (10)')

    answer = int(input())

    if answer == random_number:
        return 1
    else:
        print(f"Error: {answer:{maxDec}d}")
        return 0

