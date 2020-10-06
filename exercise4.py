'''
	Lesson: 4
	Exersice: 4
	Author: Aleksandr Plyukhin	
'''

input_str = input("Please, type list of numbers parted by space: ")

try:
	input_list = [float(x) for x in input_str.split()]
	new_list = [x for x in input_list if input_list.count(x) == 1]
	print("New list: ", new_list)
except ValueError:
	print("Elements of list must be a 'float' type")