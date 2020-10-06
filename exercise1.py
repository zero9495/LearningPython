'''
	Lesson: 3
	Excersice: 1
	Author: Aleksandr Plyukhin	
'''

def ask_float(name):
	''' This function asking the user float number 

	Args:
		name (str): The name of number

    Returns:
        number: A number a 'float' type
	'''
	ask_number = f"Please, type {name}: "
	while True:
		try:
			return float(input(ask_number))
		except ValueError:
			msg = (f"{name} must be a 'float' type").capitalize()
			print(msg)


def division(numerator, denominator):
	''' This function print result of devision numerator by denominator 

	Args:
		numerator (float): The numerator
		denominator (float): The denominator (not null)
	'''
	try:
		print(f"numerator/denominator = {numerator/denominator}")
	except ZeroDivisionError:
		print("You cannot divide by zero")


description = "This app can divide your numerator by your denominator."
print(description)

numerator = ask_float("numerator")
denominator = ask_float("denominator")
division(numerator, denominator)