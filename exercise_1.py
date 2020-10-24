'''
	Lesson: 8
	Exersice: 1
	Author: Aleksandr Plyukhin	
'''

class Date():
	def __init__(self, date_str):
		self.date_str = date_str

	@staticmethod
	def validate(dd, mm, yyyy):
		return (1 <= dd <= 31) and (1 <= mm <= 12) and (yyyy > 0)

	@classmethod
	def get_date_int(cls, date_str):
		dd, mm, yyyy = date_str.split('-')
		dd, mm, yyyy = int(dd), int(mm), int(yyyy)

		if Date.validate(dd, mm, yyyy) is True:
			return dd, mm, yyyy
		else:
			print('Error')
			return None, None, None


date_str = "11-11-2011"
date = Date(date_str)
dd, mm, yyyy = date.get_date_int(date_str)
print(dd, mm, yyyy)
print(Date.validate(21, 30, 2020))