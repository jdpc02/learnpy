"""
 Lists Challenge
"""

__author__ = 'dev'

MENU = []
MENU.append(["egg", "spam", "bacon"])
MENU.append(["egg", "sausage", "bacon"])
MENU.append(["egg", "spam"])
MENU.append(["egg", "bacon", "spam"])
MENU.append(["egg", "bacon", "sausage", "spam"])
MENU.append(["spam", "bacon", "sausage", "spam"])
MENU.append(["spam", "egg", "spam", "spam", "bacon", "spam"])
MENU.append(["spam", "egg", "sausage", "spam"])
MENU.append(["croissant", "strawberry compote", "ham"])

for MEAL in MENU:
    if not "spam" in MEAL:
        print(MEAL)
        for INGR in MEAL:
            print(INGR)
        print("<><><><><><><><>")
