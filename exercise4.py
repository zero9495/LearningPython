'''
	Lesson: 1
	Excersice: 4
	Author: Aleksandr Plyukhin	
'''

description = "This app can find greatest digit in your number"
print(description)

ask_number = "Please, type number: "
num = int(input(ask_number))

temp_num = num
greatest_digit = -1

while (temp_num >= 1):
	digit = temp_num % 10

	if digit > greatest_digit:
		greatest_digit = digit

	temp_num = temp_num // 10

print(f"In your number = {num} has been found greatest digit = {greatest_digit}")