'''
	Lesson: 2
	Excersice: 2
	Author: Aleksandr Plyukhin	
'''

description = "This app get list from you and give you new list with pairwise replaced elements"
print(description)

ask_separator = "Please, type separator that you will use: "
separator = input(ask_separator)

ask_list = "Please, type list of elements parted with your separator : "
in_list_str = input(ask_list)

in_list = in_list_str.split(separator)

for n in range(1, (len(in_list) // 2) + 1):
	n1 = n*2 - 2
	n2 = n*2 - 1
	in_list[n1], in_list[n2] = in_list[n2], in_list[n1]

print("Your new list: ", in_list)