'''
	Lesson: 5
	Exersice: 6
	Author: Aleksandr Plyukhin	
'''

dictionady = dict()

with open("subjects.txt", encoding="utf-8") as f_obj:
	for line in f_obj:
		subject, hours = line.split(":")

		hours = sum([int(y)
				for x in hours.split()
				for y in x.split("(") if y.isdigit()])

		dictionady[subject] = hours
		
print(dictionady)