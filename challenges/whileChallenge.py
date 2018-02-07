"""
 While Loop Challenge
"""

__author__ = 'dev'
import random

GUSS = -1
HIGH = 10
ANSW = random.randint(1, HIGH)
print("Please guess a number between 1 and {}".format(HIGH))
print("Press 0 to exit")

while GUSS != ANSW:
    GUSS = int(input())
    if GUSS == 0:
        print("Nice Try!")
        print("The answer is {0}".format(ANSW))
        break
    if GUSS < ANSW:
        print("Please guess higher")
    else:
        print("Please guess lower")
else:
    print("You got it! {0} is the right answer.".format(ANSW))
