'''
	Lesson: 4
	Exersice: 1
	Author: Aleksandr Plyukhin	
'''

from sys import argv

def salary(hours, wage, premium):
	''' This function calculate salary 

	Args:
		hours (float): Number of work hours
		wage (float): Monetary compensation for work hour
		premium (float): Additional Monetary compensation

    Returns:
        salary: Monetary compensation that has been calculated by formula
	'''
	return hours*wage + premium

script_name, hours, wage, premium = argv
hours, wage, premium = float(hours), float(wage), float(premium)

print(salary(hours, wage, premium))