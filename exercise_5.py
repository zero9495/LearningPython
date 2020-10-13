'''
	Lesson: 5
	Exersice: 5
	Author: Aleksandr Plyukhin	
'''

import random

filename = "numbers.txt"

with open(filename, "w") as f_obj:
	for _ in range(10):
		print(random.randint(0, 10), end=" ", file=f_obj)

with open(filename) as f_obj:
	numbers = f_obj.readlines()[0].split()
	sum_str = " + ".join(numbers)
	sum_int = sum(map(int, numbers))
	print("{} = {}".format(sum_str, sum_int))