"""
 Dictionary
"""

__author__ = 'dev'
mydict1 = {
    "abcd": "shortcut here",
    "dm": "dolt minding system",
    "echiiii": "ecchi",
    "bnb": "bob normal bon",
    "cdame": "chimney driver ama",
    "bnb": "baxter's lab"
}
# print(mydict1)
# print(mydict1["cdame"])
# mydict1["fox"] = "wiley and fast"
# print(mydict1)
# mydict1["cdame"] = "come fly with me"
# print(mydict1)
# del mydict1["echiiii"]
# print(mydict1)
#del mydict1 #deletes the entire variable
#mydict1.clear()
#print()
#print(mydict1)
# while True:
#     mykey = input("Please entry entry: ")
#     if mykey == "quit":
#         break
#     desc = mydict1.get(mykey, "No " + mykey + " entry")
#     print(desc)
    # if mykey in mydict1:
    #     desc = mydict1.get(mykey)
    #     print(desc)
    # else:
    #     print("No " + mykey + " entry")

# for i in range(10):
#     for ent in mydict1:
#         print(ent + " is " + mydict1[ent])
#     print("-" * 20)
# dictionary is not ordered the same every time the program runs

# ordkeys = list(mydict1.keys())
# ordkeys.sort()
# ordkeys = sorted(list(mydict1.keys()))
# for i in ordkeys:
#     print(i + " is " + mydict1[i])

# for i in sorted(mydict1.keys()):
#     print(i + " is " + mydict1[i])

# mydictkey1 = mydict1.keys()
# print(mydictkey1)
# mydictval1 = mydict1.values()
# print(mydictval1)

# print(mydict1)
# print(mydict1.items())
# mytup1 = tuple(mydict1.items())
# print(mytup1)
# print(dict(mytup1))

mydict2 = {
    "somethingelse": "what do you mena",
    "chompchompchomp": "watch out its a biter",
    "call_me": "you sure?"
}

# print(mydict1)
# print(mydict2)
# print(mydict2.update(mydict1))
# print(mydict2)

mydict3 = mydict1.copy()
mydict3.update(mydict2)
print(mydict3)
