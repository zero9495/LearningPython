'''
	Lesson: 8
	Exersice: 3
	Author: Aleksandr Plyukhin	
'''

class MyOwnError(Exception):
	def __init__(self, txt):
		self.txt = txt


def convert_1(x):
	try:
		float(x)
		return x
	except ValueError:
		raise MyOwnError("Elements of list must be a 'float' type")


stop_word = 'stop'

temp_list = []

while True:
	x = input("Please, type float element: ")

	if x == stop_word:
		break;

	try:
		temp_list.append(convert_1(x))
	except MyOwnError as err:
		print(f'{err}: {x}')

print(temp_list)