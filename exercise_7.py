'''
	Lesson: 8
	Exersice: 7
	Author: Aleksandr Plyukhin	
'''

class Complex():
	def __init__(self, x, y):
		self.x = x		
		self.y = y

	def __str__(self):
		return f'{self.x} + {self.y}i'

	def __add__(self, other):
		x = self.x + other.x
		y = self.y + other.y
		return Complex(x,y)

	def __mul__(self, other):
		x = self.x * other.x - self.y * other.y
		y = self.x * other.y + self.y * other.x
		return Complex(x,y)


c1 = Complex(1,2)
c2 = Complex(3,4)

print(c1)
print(c2)
print(c1 + c2)
print(c1 * c2)