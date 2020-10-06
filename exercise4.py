'''
	Lesson: 3
	Excersice: 4
	Author: Aleksandr Plyukhin	
'''

def my_func(x, y):
	''' This function returns x raised to the power y

	Args:
		x (float): Base
		y (int): Power

    Returns:
        result: x raised to the power y
	'''
	try:
		x = float(x)
	except ValueError:
		return print("Argument x must be 'float' type")

	try:
		y = float(y)
		if y % 1 != 0:
			return print("Argument y must be 'int' type")
		y = int(y)
	except ValueError:
		return print("Argument y must be 'int' type")

	result = 1

	if y > 0:
		for _ in range(abs(y)):
			result *= x
	else:
		for _ in range(abs(y)):
			result /= x

	return result


description = "This app can return x raised to the power y."
print(description)

x = input("Please, print x: ")
y = input("Please, print y: ")
result = my_func(x,y)

print(f"{x}**({y}) = {result}")