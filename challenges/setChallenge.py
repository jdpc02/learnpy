"""
 Set Challenge
"""

__author__ = 'dev'
VOWELS = { "a", "e", "i", "o", "u"}
MYINPUT = ( "something to test with" )

MYINPUT = input("Specify a string: ")
print(sorted(set(MYINPUT) - VOWELS))
