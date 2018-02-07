"""
 Dictionary Challenge
"""

__author__ = 'dev'
LOCATE = {
    0: "Sitting learning Python",
    1: "Standing at end of road before small brick bldg",
    2: "Top of the hill",
    3: "Inside bldg",
    4: "Valley beside stream",
    5: "In a forest"
}

EXITS = {
    0: {"Q": 0},
    1: {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},
    2: {"N": 5, "Q": 0},
    3: {"W": 1, "Q": 0},
    4: {"N": 1, "W": 2, "Q": 0},
    5: {"W": 2, "S": 1, "Q": 0}
}

vocab = {
    "QUIT": "Q",
    "NORTH": "N",
    "EAST": "E",
    "WEST": "W",
    "SOUTH": "S"
}

LOC = 1
while True:
    AVAILEXITS = ", ".join(EXITS[LOC].keys())

    print(LOCATE[LOC])

    if LOC == 0:
        break

    DIRECT = input("Where do you want to go? [" + AVAILEXITS + "] ").upper()
    if len(DIRECT) > 1:
        # for word in vocab:
        #     if word in DIRECT:
        #         DIRECT = vocab[word]
        words = DIRECT.split()
        for word in words:
            if word in vocab:
                DIRECT = vocab[word]
                break
    print()
    if DIRECT in EXITS[LOC]:
        LOC = EXITS[LOC][DIRECT]
    else:
        print("Not there")
