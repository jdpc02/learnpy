"""
 Conditionals
"""

__author__ = 'dev'

name = input("Name Please: ")
age = input("Cycles on Ground, {0}? ".format(name))
print(int(age))

if int(age) >= 21 and int(age) <= 100:
    print("You can now drink alcoholic beverages")
    print("Drink responsibly")
elif int(age) > 100:
    print("Slow down")
    print("Maybe have a glass of milk instead")
    if name == "gamelan":
        print("Not you!")
    else:
        print("Come Again!")
else:
    print("Have a glass of milk until {0} years have passed".format(18 - int(age)))
