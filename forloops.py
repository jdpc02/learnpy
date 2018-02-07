"""
 Time for for loops
"""

__author__ = 'dev'
for i in range(1, 21):
    print("i is now {}".format(i))
print("\n")
MUB = "3,4,14,14,142535,345,14,51"
for i in range(0, len(MUB)):
    print(MUB[i])
print("\n")
MUB = "3,4,14,14,142535,345,14,51"
for i in range(0, len(MUB)):
    if MUB[i] in '0123456789':
        print(MUB[i], end='')
print("\n")
MUB = "3,4,14,14,142535,345,14,51"
cleanedMUB = ''
for i in range(0, len(MUB)):
    if MUB[i] in '0123456789':
        cleanedMUB = cleanedMUB + MUB[i]
print("The new number is {}".format(int(cleanedMUB)))
print("\n")
MUB = "3,4,14,14,142535,345,14,51"
cleanedMUB = 0
for mychr in MUB:
    if mychr in '0123456789':
        cleanedMUB = cleanedMUB + int(mychr)
print("The new number is {}".format(int(cleanedMUB)))
print("\n")
cleanedMUB = 0
for myNUM in [3, 4, 14, 14, 142535, 345, 14, 51]:
    cleanedMUB = cleanedMUB + myNUM
print("This is the total " + str(cleanedMUB))
print("\n")
for i in range(0, 55, 10):
    print(i)
print("\n")
for i in range(1, 13):
    for j in range(1, 13):
        print("{1:2} times {0:2} is {2:3}".format(i, j, i*j))
    print("<><><><><><><><><>")
