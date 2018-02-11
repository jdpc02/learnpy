"""
 Dictionary Challenge
"""

__author__ = 'dev'
LOCATIONS = {
    0: { "desc": "Sitting learning Python",
         "exits": {},
         "namedExits": {}
    },
    1: { "desc": "Standing at end of road before small brick bldg",
         "exits": {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},
         "namedExits": { "2": 2, "3": 3, "5": 5, "4": 4 }
    },
    2: { "desc": "Top of the hill",
         "exits": {"N": 5, "Q": 0},
         "namedExits": { "5": 5 }
    },
    3: { "desc": "Inside bldg",
         "exits": {"W": 1, "Q": 0},
         "namedExits": { "1": 1 }
    },
    4: { "desc": "Valley beside stream",
         "exits": {"N": 1, "W": 2, "Q": 0},
         "namedExits": { "1": 1, "2": 2 }
    },
    5: { "desc": "In a forest",
         "exits": {"W": 2, "S": 1, "Q": 0},
         "namedExits": { "2": 2, "1": 1 }
    }
}

vocab = {
    "QUIT": "Q",
    "NORTH": "N",
    "EAST": "E",
    "WEST": "W",
    "SOUTH": "S",
    "ROAD": "1",
    "HILL": "2",
    "BUILDING": "3",
    "VALLEY": "4",
    "FOREST": "5"
}

LOC = 1
while True:
    AVAILEXITS = ", ".join(LOCATIONS[LOC]["exits"].keys())

    print(LOCATIONS[LOC]["desc"])

    if LOC == 0:
        break
    else:
        ALLEX = LOCATIONS[LOC]["exits"].copy()
        ALLEX.update(LOCATIONS[LOC]["namedExits"])

    DIRECT = input("Where do you want to go? [" + AVAILEXITS + "] ").upper()
    if len(DIRECT) > 1:
        words = DIRECT.split()
        for word in words:
            if word in vocab:
                DIRECT = vocab[word]
                break
    print()
    if DIRECT in ALLEX:
        LOC = ALLEX[DIRECT]
    else:
        print("Not there")
