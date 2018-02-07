"""
 Lists, Ranges and Tuples
"""

__author__ = 'dev'
parrot_list = ["there again", "here again", "while here"]
parrot_list.append("My Red Parrot")

for state in parrot_list:
    print("This parrot is " + state)

even = [0, 2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]
print(even + odd)
numbers1 = even + odd
numbers2 = numbers1
print(numbers1.sort())
numbers1.sort()
print(numbers1)
numbers_in_order = sorted(numbers2)
print(numbers_in_order)

list1 = []
list2 = list()
print(list1)
print(list2)

another = even
another.sort(reverse=True)
print(even)
print("Another points to the same list as even?")
print(another is even)

even2 = [0, 2, 4, 6, 8]
another2 = list(even2)
print("Another2 has the same contents as Even2?")
print(another2 == even2)
print("Another2 points to the same list as even2?")
print(another2 is even2)
another2.sort(reverse=True)
print(even2)
print(another2)
print("Another2 the same as Even2?")
print(another2 is even2)
