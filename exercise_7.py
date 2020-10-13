'''
	Lesson: 5
	Exersice: 7
	Author: Aleksandr Plyukhin	
'''

import random
import json

def create_file(filename):
	with open(filename, "w") as f_obj:
		for i in range(3):
			name = "finm_" + str(i)
			form = 'OOO'
			profit = random.randint(1,10)*1000
			loose = random.randint(1,10)*1000
			print(name, form, profit, loose, file=f_obj)


def read_file(filename):
	dictionary = dict()
	temp_list = []

	with open(filename)	as f_obj:
		for line in f_obj:
			name, form, profit, loose = line.split()
			profit = int(profit)
			loose = int(loose)

			if profit > loose:
				dictionary[name] = profit
				temp_list.append(profit)
			else:
				dictionary[name] = loose
	return dictionary, temp_list


def get_list(filename):
	dictionary, temp_list = read_file(filename)
	average_profit = dict()
	av = sum(temp_list) / len(temp_list) if len(temp_list)>0 else 0
	average_profit['average_profit'] = av

	return [dictionary, average_profit]


filename = "firms.txt"
create_file(filename)
my_list = get_list(filename)
print(my_list)

with open("firms.json", "w") as write_f:
	json.dump(my_list, write_f)