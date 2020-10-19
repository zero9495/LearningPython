'''
	Lesson: 7
	Exersice: 3
	Author: Aleksandr Plyukhin	
'''

class Cell:
	def __init__(self, count):
		self.count = int(count)

	def __str__(self):
		return str(self.count)

	def __add__(self, other):
		return Cell(self.count + other.count)

	def __sub__(self, other):
		if self.count > other.count:
			return Cell(self.count - other.count)
		else:
			return "Error"

	def __mul__(self, other):
		return Cell(self.count * other.count)

	def __truediv__(self, other):
		if other.count > 0:
			return Cell(self.count // other.count)
		else:
			return "Error"

	def make_order(self, rows):
		return ('*' * rows + '\n') * (self.count // rows) + '*' * (self.count % rows)


c_1 = Cell(10)
c_2 = Cell(3)

print(c_1 + c_2)
print(c_1 - c_2)
print(c_2 - c_1)
print(c_1 * c_2)
print(c_1 / c_2)
print(c_1 / Cell(0))
print(c_1.make_order(3))