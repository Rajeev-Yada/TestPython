import requests
import numpy

print(requests.__version__)

#Set has nno duplicate elements
s2 = set(["Geeks", "For", "Geeks"])
print("Set with the use of List: ", s2)

#tuple can have duplicate elements
tup2 = ('Geeks', 'For')
print("\nTuple with the use of String: ", tup2)

#dictionary with duplicate keys
d = {1: 'Geeks', 2: 'For', 3: 'Geeks'}
print('Dictionary are ' + str(d))
print(d[1])
print(d.get(2))

print('Match case like Switch case in other languages')
number = 2
match number:
    case 1:
        print("One")
    case 2 | 3:
        print("Two or Three")
    case _:
        print("Other number")