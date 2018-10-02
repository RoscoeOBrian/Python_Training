###########################
## PART 10: Simple Game ###
### --- CODEBREAKER --- ###
## --Nope--Close--Match--  ##
###########################

# It's time to actually make a simple command line game so put together everything
# you've learned so far about Python. The game goes like this:

# 1. The computer will think of 3 digit number that has no repeating digits.
# 2. You will then guess a 3 digit number
# 3. The computer will then give back clues, the possible clues are:
#
#     Close: You've guessed a correct number but in the wrong position
#     Match: You've guessed a correct number in the correct position
#     Nope: You haven't guess any of the numbers correctly
#
# 4. Based on these clues you will guess again until you break the code with a
#    perfect match!

# There are a few things you will have to discover for yourself for this game!
# Here are some useful hints:

# Creates three random numbers in a shuffled order
import random
digits = list(range(10))
random.shuffle(digits)

print(digits[:3])

# get Input from gamer
inputstring = input("What is your guess? ")
guess=[]
for i in range(len(inputstring)):
    guess+=[int(inputstring[i])]

# def compare(digits,guess):
if guess[0] == digits[0] and guess[1] == digits[1] and guess[2] == digits[2]:
    print("You won!"")
elif guess[0] == digits[0] or guess[1] == digits[1] or guess[2] == digits[2]:
    print("Match: You've guessed a correct number in the correct position")
elif guess[0] in digits[1 or 2] or guess[1] in digits[0 or 2] or guess[2] in digits[0 or 1]:
    print("Close: You've guessed a correct number but in the wrong position")
else:
    print("Nope: You haven't guess any of the numbers correctly")
