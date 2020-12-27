#!/usr/bin/python3

from random import randint
from bcm_lib import decToBin
from bcm_lib import binToDec

# Setting random 8-bit number
# random_number = randint(0, 255)

# Printing random 
# print(f"{18:08b}")
score = 0
maxBit = input("Enter numbers size in bits. (Default: 8)\n")

if maxBit:
    maxBit = int(maxBit)
else:
    maxBit = 8

# print("right!")
# print("try harder!")

#while True:
#    binToDec(max_bit)

while True:
    whichType = randint(0, 1)
#    if binToDec():
    if whichType:
        print("Dec > Bin")
        isCorrect = decToBin(maxBit)
    else:
        print("Bin > Dec")
        isCorrect = binToDec(maxBit)

    if isCorrect:
        score += 1
        cFlag = '+'
    else:
        score -= 1
        cFlag = '-'

    print("=" * 16)
    print(f" {cFlag} | Score: {score:02d} |")
    print("=" * 16)
