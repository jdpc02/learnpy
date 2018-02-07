"""
 While Loops
"""

__author__ = 'dev'
GROC = "eggs", "bacon", "longganisa", "fried rice"
HULA = ""
while HULA not in GROC:
    HULA = input("What do you want for breakfast? ")
    if HULA == "longganisa":
        print("Kain na!")
        break
    if HULA == "quit":
        print("Not hungry anymore?")
        break
else:
    print("Breakfast is served!")
