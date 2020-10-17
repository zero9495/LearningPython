'''
	Lesson: 6
	Exersice: 3
	Author: Aleksandr Plyukhin	
'''

class Worker(object):

	def __init__(self, name, surname, position, income):
		self.name = name
		self.surname = surname
		self.position = position
		self._income = {"wage": income*0.7, "bonus": income*0.3}

class Position(Worker):
	def __init__(self, name, surname, position, income):
		super().__init__(name, surname, position, income)
		pass

	def get_full_name(self):
		return self.name + " " + self.surname

	def get_total_income(self):
		return sum(self._income.values())

p = Position("Calvin", "Klein", "manager", 15000)
print(p.get_full_name())
print(p.position)
print(p.get_total_income())