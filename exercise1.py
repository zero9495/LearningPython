'''
	Lesson: 1
	Excersice: 1
	Author: Aleksandr Plyukhin	
'''

description = "This app can double numbers"
print(description)

ask_name = "Please, type your name: "
name = input(ask_name)

ask_number = f"Hi, {name}. Please, type number: "
num = int(input(ask_number))
print(f"Doubled number: {2*num}")