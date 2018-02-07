"""
 Iterators Challenge
"""

__author__ = 'dev'
MYLIST = ["one", "two now", "three", "four again"]
MYITER = iter(MYLIST)
for i in range(1, len(MYLIST) + 1):
    print(next(MYITER))
