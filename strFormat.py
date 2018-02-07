__author__ = 'dev'
age = 24
print("My age is " + str(age) + " years")
print("""January: {2}
February: {0}
March: {2}
April: {1}
May: {2}
June: {1}
July: {2}
August: {2}
September: {1}
October: {2}
November: {1}
December: {2}""".format(28,30,31)
)

print("My age is %d %s, %d %s" % (age, "years", 6, "months"))

for i in range(1, 12):
    print("#%2d squared is %4d and cubed is %4d" %(i, i ** 2, i ** 3))

print("Pi is approximately %12.10f" %(22/7))

for i in range(1, 12):
    print("#{0:2} squared is {1:<4} and cubed is {2:<4}".format(i, i ** 2, i ** 3))

print("Pi is approximately {0:12.10f}".format(22/7))
