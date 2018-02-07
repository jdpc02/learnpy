"""
 If Challenge
"""

__author__ = 'dev'
NAMED = input("What is your Name? ")
AGE = int(input("How old are you {0}?".format(NAMED)))

if 18 < AGE < 31:
    print("Welcome to the holiday")
else:
    print("Hello {0}! Hope you are doing well at {1}".format(NAMED, AGE))
