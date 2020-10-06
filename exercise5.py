'''
	Lesson: 3
	Excersice: 5
	Author: Aleksandr Plyukhin	
'''

stop_sign = 'q'

description = "This app can sum elements of list."
description += f" Type '{stop_sign}' into the end to quit app."
print(description)

total_sum = 0


while True:
	s = input("Please, type list of elements parted by space: ")

	is_stop_sign = s.lower().endswith(stop_sign.lower())
	s = s[:(len(s) - len(stop_sign))] if is_stop_sign else s

	temp_list = s.split()
	try:
		temp_list = [float(x) for x in temp_list]
		total_sum += sum(temp_list)
		print("Sum = ", total_sum)

		if is_stop_sign:
			break
	except ValueError:
		print("All elements of list must be 'float' type")
