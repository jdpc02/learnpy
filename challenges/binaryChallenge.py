"""
 Binary Challenge
"""

__author__ = 'dev'
INPNUM = int(input("Please enter a number between 1 and 65535: "))
KEPTVAL = INPNUM
OUTNUM = []
#print("{0:>16b}".format(INPNUM))

while INPNUM >= 1:
    if (INPNUM % 2) == 1:
        OUTNUM.insert(0, '1')
    elif (INPNUM % 2) == 0:
        OUTNUM.insert(0, '0')
    INPNUM = INPNUM // 2
for i in OUTNUM:
    print(i, end='')
#print(OUTNUM)
INPNUM = KEPTVAL
powers = []
for power in range(15, -1, -1):
    powers.append(2 ** power)
#print(powers)
print()
printing = False
for power in powers:
    bit = INPNUM // power
    if bit != 0 or power == 1:
        printing = True
    if printing:
        print(bit, end='')
    INPNUM %= power
print()
