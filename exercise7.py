'''
	Lesson: 4
	Exersice: 7
	Author: Aleksandr Plyukhin	
'''

from math import factorial

def fact(n):
    for el in range(1, n+1):
        yield factorial(el)

n = int(input("Please, type n: "))

for el in fact(n):
	print(el)