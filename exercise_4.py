'''
	Lesson: 6
	Exersice: 4
	Author: Aleksandr Plyukhin	
'''

class Car(object):

	def __init__(self, speed, color, name, is_police):
		self.speed = float(speed)
		self.color = color
		self.name = name
		self.is_police = bool(is_police)

	def go(self):
		print("Car rides")

	def stop(self):
		print("Car stopped")

	def turn(self, direction):
		print("Car turn to ", direction)

	def show_speed(self):
		print("Speed = ", self.speed)


class TownCar(Car):
	def __init__(self, speed, color, name, is_police):
		super().__init__(speed, color, name, is_police)
		pass

	def show_speed(self):
		super().show_speed()
		if self.speed > 60:
			print("Speed exceeded!")


class SportCar(Car):
	def __init__(self, speed, color, name, is_police):
		super().__init__(speed, color, name, is_police)
		pass


class WorkCar(Car):
	def __init__(self, speed, color, name, is_police):
		super().__init__(speed, color, name, is_police)
		pass

	def show_speed(self):
		super().show_speed()
		if self.speed > 40:
			print("Speed exceeded!")


class PoliceCar(Car):
	def __init__(self, speed, color, name, is_police):
		super().__init__(speed, color, name, is_police)
		pass

cars = []
cars.append(TownCar(30, 'red', 'kia', False))
cars.append(SportCar(30, 'green', 'lada', False))
cars.append(WorkCar(70, 'blue', 'niva', False))
cars.append(PoliceCar(70, 'yellow', 'moskvich', True))

for car in cars:
	print("Car name: ", car.name)
	print("Car color: ", car.color)
	print("Car speed: ", car.speed)
	print("Car nis_policeame: ", car.is_police)
	car.go()
	car.turn('left')
	car.show_speed()
	car.stop()
	print()