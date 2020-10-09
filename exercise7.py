'''
	Lesson: 4
	Exersice: 7
	Author: Aleksandr Plyukhin	
'''

def factorial(n):
	return n*factorial(n-1) if n > 0 else 1

def fact(n):
    for el in range(1, n+1):
        yield factorial(el)

n = int(input("Please, type n: "))

for el in fact(n):
	print(el)