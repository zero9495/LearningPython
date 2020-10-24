'''
	Lesson: 8
	Exersice: 2
	Author: Aleksandr Plyukhin	
'''

class MyZeroDivisionError(Exception):
	def __init__(self, txt):
		self.txt = txt

numerator = float(input("Please, type numerator: "))
denominator = float(input("Please, type denominator: "))

try:
	if denominator == 0:
		raise MyZeroDivisionError("Denominator must be greater than null!")
except ValueError:
	print("Вы ввели не число")
except MyZeroDivisionError as err:
	print(err)
else:
	print(f"numerator/denominator = {numerator/denominator}")