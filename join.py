"""
 Join
"""

__author__ = 'dev'
# myList = ["a", "b", "c"]
# print(myList)
# newStr = ''
# for c in myList:
#     newStr += c + ", "
# print(newStr)
# newStr = ''
# newStr = ", ".join(myList)
# print(newStr)

# letters = 'abcdefghij'
# print(letters)
# newStr = ' '.join(letters)
# print(newStr)

locate = {
    0: "Sitting learning Python",
    1: "Standing at end of road before small brick bldg",
    2: "Top of the hill",
    3: "Inside bldg",
    4: "Valley beside stream",
    5: "In a forest"
}

exits = [
    {"Q": 0},
    {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},
    {"N": 5, "Q": 0},
    {"W": 1, "Q": 0},
    {"N": 1, "W": 2, "Q": 0},
    {"W": 2, "S": 1, "Q": 0}
]

loc = 1
while True:
    availExists = ", ".join(exits[loc].keys())

    print(locate[loc])

    if loc == 0:
        break

    direct = input("Where do you want to go? [" + availExists + "] ").upper()
    print()
    if direct in exits[loc]:
        loc = exits[loc][direct]
    else:
        print("Not there")
