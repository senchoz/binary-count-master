#!/usr/bin/python3

from random import randint
import datetime as dt
from bcm_lib import decToBin
from bcm_lib import binToDec
from bcm_lib import scoreTable
from bcm_lib import scoreChange
import sys
from bcm_lib import clear

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

clear()
print(f"Set {maxBit} bit")

f = open("score.log", "a")

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


        clear()

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
        clear()
        print(f"\nTime played: {gameEndTime - gameStartTime}")
        print(f"Rounds completed: {roundsPlayed}")
        print(f"Points earned: {score}")
        print("Good job!")

        f.write(f"Date: {gameEndTime}")
        f.write(f"\nTime played: {gameEndTime - gameStartTime}\n")
        f.write(f"Rounds completed: {roundsPlayed}\n")
        f.write(f"Points earned: {score}\n")
        f.write(f"{'=' * 32}\n")
        f.close()
        sys.exit()

gameEndTime = dt.datetime.now()
clear()
#print(f"\nYou played:\n {gameEndTime - gameStartTime}")
print(f"\nTime played: {gameEndTime - gameStartTime}")
print(f"Rounds completed: {roundsPlayed}")
print(f"Points earned: {score}")
print("Good job!")

f.write(f"Date: {gameEndTime}")
f.write(f"\nTime played: {gameEndTime - gameStartTime}\n")
f.write(f"Rounds completed: {roundsPlayed}\n")
f.write(f"Points earned: {score}\n")
f.write(f"{'=' * 32}\n")
f.close()
