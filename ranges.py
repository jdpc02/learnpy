"""
 Ranges
"""

__author__ = 'dev'
print(range(100))
lists = list(range(5))
print(lists)
even = list(range(0, 5, 2))
odd = list(range(1, 5, 2))
print(even)
print(odd)
alpha = 'abcdefghijklmnopqrstuvwxyz'
print(alpha.index('m'))
print(alpha[12])
print(even.index(2))
print(even[2])
#sevens = range(7, 1000000, 7)
#x = int(input("Specify a positive number below one million: "))
#if x in sevens:
#    print("{} is divisble by seven".format(x))
smalldec = range(0, 10)
newrange = smalldec[::2]
print(newrange)
print(list(newrange))

decim = range(0,20)
myra_nge = decim[3:10:3]
print(list(myra_nge))
print(myra_nge == range(3, 10, 3))
print(range(0, 5, 2) == range(0, 6, 2))
print(list(range(0, 5, 2)))
print(list(range(0, 6, 2)))

r = range(0, 20)
print(r)

for i in r[::-2]:
    print(i)
print('=' * 50)
for i in range(20, 0, -2):
    print(i)
print('=' * 50)
print(range(0, 20)[::-2] == range(19, 0, -2))
print('=' * 50)
# won't work as you can't count down from negative numbers to hit 20
for i in range(0, 20, -2):
    print(i)
print('=' * 50)
backstr = "egaugnal lufrewop yrev a si nohtyP"
print(backstr[::-1])

print(list(range(0, 5, 4)))
o = range(0, 100, 4)
print(o)
p = o[::5]
for i in p:
    print(i)
