"""
 Ordered Sets with Tuples
"""

__author__ = 'dev'
t1 = "a", "b", "c"
print(t1)
print("a", "b", "c")
print(("a", "b", "c"))
mylis1 = "This is here", "she did", 8888
mylis2 = "Over that section", "they went", 1234, ((1, "One may"), (2, "Two count"), (3, "Three's a crowd"))
print(mylis1)
print(mylis2[1])
print(mylis2[0])
mylis3 = mylis1[2], "Try to change"
print(mylis3)
mylis4 = ["Why they do", "Sober Him", 9876]
print("This is a list")
print(mylis4)
mylis4[0] = "Not any more"
print(mylis4)

a = b = c = 71
print(a, b, c)
a, b = 18, 14
print(a, b)
a, b = b, a
print("a is now {0}".format(a))
print("b is now {0}".format(b))

a, b, c = mylis1
print(a)
print(b)
print(c)

a, b, c, d = mylis2
print(a)
print(b)
print(c)
print(d)
print(d[0])
print(d[2][1])

mylis5 = "Fifth One", "High Five", 5555, [(1, "One One"), (2, "Get Two")]
print(mylis5)
mylis5[3].append((3, "Third's a charm"))
title, artist, year, tracks = mylis5
tracks.append((4, "Forth Timer"))
print(title)
print(artist)
print(year)
for song in tracks:
    track, title = song
    print('\tTrack {}, Title: {}'.format(track, title))
