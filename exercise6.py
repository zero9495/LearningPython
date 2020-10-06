'''
	Lesson: 4
	Exersice: 6
	Author: Aleksandr Plyukhin	
'''

# a

from itertools import count

for el in count(7):
    if el > 15:
        break
    else:
        print(el)


# b

from itertools import cycle

с = 0
for el in cycle("ABC"):
    if с > 10:
        break
    print(el)
    с += 1