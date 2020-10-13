'''
	Lesson: 5
	Exersice: 3
	Author: Aleksandr Plyukhin	
'''

'''
from random import random

names = ["Liam","Olivia","Noah","Emma","Oliver","Ava","William","Sophia","Elijah","Isabella"]

with open("names.txt", "w") as f_obj:
	for name in names:
		num = round(15000 + random()*10000, 2)
		print(name, num, file=f_obj)
'''

filename = "names.txt"

with open(filename) as f_obj:
	content = f_obj.readlines()

total_salary = 0
print("Employees with salary < 20000:")

for line in content:
	name = line.split()[0]
	salary = float(line.split()[1])
	if salary < 20000:
		print("{} with salary {}".format(name, salary))
	total_salary += salary

print()
mean_salary = round(total_salary / len(content), 2)
print("Mean salary = {}".format(mean_salary))