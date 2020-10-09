'''
	Lesson: 4
	Exersice: 2
	Author: Aleksandr Plyukhin	
'''

input_str = input("Please, type list of numbers parted by space: ")

try:
	input_list = [float(x) for x in input_str.split()]
	new_list = [x for i, x in enumerate(input_list) if i > 0 and input_list[i-1] < x]
	print("New list: ", new_list)
except ValueError:
	print("Elements of list must be a 'float' type")
