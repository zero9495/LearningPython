'''
	Lesson: 6
	Exersice: 2
	Author: Aleksandr Plyukhin	
'''

class Road(object):

	def __init__(self, length, width):
		self.__length = length
		self.__width = width

	def weight(self):
		return self.__width * self.__length * 25 * 5

r = Road(3, 4)
print(r.weight())