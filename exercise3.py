'''
	Lesson: 1
	Excersice: 3
	Author: Aleksandr Plyukhin	
'''

description = "This app can calculate your number 'n' as sum 'n + nn + nnn'"
print(description)

ask_number = "Please, type number: "
num = int(input(ask_number))

num2 = int("{0}{0}".format(num))
num3 = int("{0}{0}{0}".format(num))

sum_string = "{0} + {1} + {2}".format(num, num2, num3)
sum = num + num2 + num3

print("Your number n={0} has been calculated as {1} = {2}".format(num, sum_string, sum))