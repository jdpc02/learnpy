"""
 Sets
"""

__author__ = 'dev'
set1 = {
    "mine",
    "yours",
    "ours"
}
print(set1)
for i in set1:
    print(i)

print("*" * 10)

set2 = set([
    "heap",
    "come",
    "hightower"
])
print(set2)
for j in set2:
    print(j)

set1.add('wonky')
print(set1)
set2.add('yabbadabbadoo')
print(set2)

empset1 = set()
empset1.add("a")
# empset2 = {}
# empset2.add("a") # dict has no add member

# myevent = set(range(0, 40, 2))
# print(myevent)
# sq_tuple = (2, 4, 28)
# sq = set(sq_tuple)
# print(sq)
# print(len(sq))
# print(myevent.union(sq))
# print(len(myevent.union(sq)))
# print(myevent.intersection(sq))
# print(myevent & sq)
# print(sq.intersection(myevent))
# print(sq & myevent)

# print(sorted(myevent))
# sq_tuple = (25, 4, 9, 6, 16)
# sq = set(sq_tuple)
# print(sorted(sq))
# print('myevent minus sq')
# print(sorted(myevent.difference(sq)))
# print(sorted(myevent - sq))
# print('sq minus myevent')
# print(sorted(sq.difference(myevent)))
# print(sorted(sq - myevent))
# print('-'*40)
# print(myevent)
# print(sq)
# myevent.difference_update(sq)
# print(myevent)

# sq.discard(4)
# sq.remove(25)
# sq.discard(8)
# try:
#     sq.remove(8)
# except KeyError:
#     print('No 8')

myevent = frozenset(range(0, 10, 2))
print(myevent)
#even.add(3)
