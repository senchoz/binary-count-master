#!/usr/bin/python3

from random import randint
import datetime as dt
from bcm_lib import decToBin
from bcm_lib import binToDec
from bcm_lib import scoreTable
from bcm_lib import scoreChange
import sys

# Printing random 
# print(f"{18:08b}")
score = 0
scoreTotal = 0
gameTime = 0
roundTime = dt.timedelta(0)
gameStartTime = dt.datetime.now()
roundsToPlay = 10

maxBit = input("Enter numbers size in bits. (Default: 8)\n")

if maxBit:
    maxBit = int(maxBit)
else:
    maxBit = 8

roundsPlayed = 0
#while True:
while roundsPlayed < roundsToPlay:
    try:
        whichType = randint(0, 1)
        if whichType:
            print("Dec > Bin")
            isCorrect, timeForRound = decToBin(maxBit)
        else:
            print("Bin > Dec")
            isCorrect, timeForRound = binToDec(maxBit)

        scoreRound = scoreChange(isCorrect, timeForRound)
        score += scoreRound
        print(f"======")
        print(f"+ {scoreRound}!")
#        score += scoreChange(isCorrect, timeForRound)
        gameTime += timeForRound
        scoreTable(isCorrect, score, gameTime)
        roundsPlayed += 1

    except KeyboardInterrupt:
        gameEndTime = dt.datetime.now()
        print(f"\nYou played:\n {gameEndTime - gameStartTime}")
        print(f"You completed {roundsPlayed} rounds")
        print(f"and earned {score}")
        print("Good job!")
        sys.exit()

gameEndTime = dt.datetime.now()
print(f"\nYou played:\n {gameEndTime - gameStartTime}")
print(f"You completed {roundsPlayed} rounds")
print(f"and earned {score} points")
print("Good job!")
