'''
	Lesson: 2
	Excersice: 5
	Author: Aleksandr Plyukhin	
'''

stop_word = 'Exit'
numbers = []
ask_number = "Please, type number: "

description = "This app can add your number to non-increasing list."
description += f" (Type '{stop_word}' to quit this app.)"
print(description)

while True:
	input_string = input(ask_number)

	if input_string == stop_word:
		break
	else:
		number = int(input_string)
		pos = len(numbers)

		for i in range(len(numbers)):
			if numbers[i] < number:
				pos = i
				break

		numbers.insert(pos, number)
		print(numbers)