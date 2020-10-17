'''
	Lesson: 6
	Exersice: 5
	Author: Aleksandr Plyukhin	
'''

class Stationery(object):

	def __init__(self, title):
		self.title = title

	def draw(self):
		print("Start drawing")


class Pen(Stationery):
	def __init__(self, title):
		super().__init__(title)
		pass

	def draw(self):
		super().draw()
		print("This is pen", self.title)
		

class Pencil(Stationery):
	def __init__(self, title):
		super().__init__(title)
		pass

	def draw(self):
		super().draw()
		print("This is pencil", self.title)
		

class Handle(Stationery):
	def __init__(self, title):
		super().__init__(title)
		pass

	def draw(self):
		super().draw()
		print("This is handle", self.title)

stationeries = []
stationeries.append(Pen('A'))
stationeries.append(Pencil('B'))
stationeries.append(Handle('C'))

for stationery in stationeries:
	stationery.draw()
	print()