'''
	Lesson: 3
	Excersice: 3
	Author: Aleksandr Plyukhin	
'''

def my_func(arg1, arg2, arg3):
	''' This function returns sum of two greatest elements

	Args:
		name (str): The name of variable
		type (str): The type of variable

    Returns:
        temp_list: Two greatest elements
        result: Sum of two greatest elements
	'''
	temp_list = [arg1, arg2, arg3]
	min_value_index = temp_list.index(min(temp_list))
	temp_list.pop(min_value_index)

	result = 0
	try:
		result = float(temp_list[0]) + float(temp_list[1])
	except ValueError:
		result = temp_list[0] + temp_list[1]

	return temp_list, result


description = "This app can return sum of two greatest elements."
print(description)

arg1 = input("Please, type arg1: ")
arg2 = input("Please, type arg1: ")
arg3 = input("Please, type arg1: ")
temp_list, result = my_func(arg1, arg2, arg3)

print(f"{temp_list[0]} + {temp_list[1]} = {result}")