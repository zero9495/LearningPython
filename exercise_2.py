'''
	Lesson: 7
	Exersice: 2
	Author: Aleksandr Plyukhin	
'''

from abc import ABC, abstractmethod

class Clothes(ABC):
	def __init__(self, name):
		self.name = name

	@property
	@abstractmethod
	def tissue_consumption(self):
		pass


class Coat(Clothes):
	def __init__(self, name, size):
		super().__init__(name)
		self.size = size

	@property
	def tissue_consumption(self):
		return self.size/6.5 + 0.5


class Suit(Clothes):
	def __init__(self, name, height):
		super().__init__(name)
		self.height = height

	@property
	def tissue_consumption(self):
		return self.height*2 + 0.3


clothes = []
clothes.append(Coat('a', 2))
clothes.append(Coat('b', 3))

for c in clothes:
	print(c.tissue_consumption)