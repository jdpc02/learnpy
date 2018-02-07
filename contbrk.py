"""
 Continue/Break
"""

__author__ = 'dev'
shop_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]
for item in shop_list:
    if item == 'spam':
        print("I am ignoring " + item)
        continue
    print("Buy " + item)
print('\n')
shopList = ["milk", "pasta", "eggs", "spam", "bread", "rice"]
for item in shopList:
    if item == 'spam':
        print("I am ignoring " + item)
        break
    print("Buy " + item)
print('\n')
