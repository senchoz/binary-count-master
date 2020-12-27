#!/usr/bin/python3

from random import randint
from datetime import datetime as dt
import datetime

def decToBin(x):
    maxNum = 2 ** x - 1
    maxDec = len(str(maxNum))
    random_number = randint(0, maxNum)
    print(f'{"-" * maxDec} (10)')
    print(f"{random_number:{maxDec}d}")
    print(f'{"-" * x} (2)')
    timeStart = dt.now()

    answer = int(input(), 2)

    timeStop = dt.now()
    timeLeft = (timeStop - timeStart).total_seconds()

    if answer == random_number:
        return (1, timeLeft)
    else:
        print(f"Error: {answer:{maxDec}d}")
        return (0, timeLeft)


def binToDec(x):
    maxNum = 2 ** x - 1
    maxDec = len(str(maxNum))
    random_number = randint(0, maxNum)
    print(f'{"-" * x} (2)')
    print(f"{random_number:0{x}b}")
    print(f'{"-" * maxDec} (10)')
    timeStart = dt.now()

    answer = int(input())

    timeStop = dt.now()
    timeLeft = (timeStop - timeStart).total_seconds()

    if answer == random_number:
        return (1, timeLeft)
    else:
        print(f"Error: {answer:{maxDec}d}")
        return (0, timeLeft)


def scoreChange(x, y):
    """
    x: 0 for incorrect answer, 1 for correct
    y: seconds spent on previous solution
    """
    if x:
        score = round(1000 / y)
    else:
        score = -(round(y * 10))
    return score


def scoreTable(x, score, gameTime):
    """
    x - 0 for incorrect answer, 1 for correct
    """
    sign = ("-", "+")

    print("=" * 43)
    print(f" {sign[x]} | Score: {score: 8d} | Time: {datetime.timedelta(seconds=gameTime, microseconds=0)}")
    print("=" * 43)



