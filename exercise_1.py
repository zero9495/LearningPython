'''
	Lesson: 6
	Exersice: 1
	Author: Aleksandr Plyukhin	
'''

import time

class TrafficLight(object):

	def __init__(self):
		self.__color = 'red'
		self.__colors_time = []
		self.__colors_time.append(['red', 7])
		self.__colors_time.append(['yellow', 2])
		self.__colors_time.append(['green', 3])
		self.__colors_time.append(['yellow', 2])
	
	def running(self):
		for i in range(10):
			color_time = self.__colors_time[i%4]
			self.__color = color_time[0]
			print(self.__color)
			time.sleep(color_time[1])

t = TrafficLight()
t.running()