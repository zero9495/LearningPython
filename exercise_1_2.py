'''
	Lesson: 5
	Exersice: 1 and 2
	Author: Aleksandr Plyukhin	
'''

def ask_text():
	''' This function asks text from user

    Returns:
        text: Text from user
	'''
	text_list = []
	string = "string"

	while len(string) != 0:
		string = input("Type row [{}]: ".format(len(text_list)))
		text_list.append(string)

	return "\n".join(text_list)


def exercise_1(filename):
	text = ask_text()
	with open(filename, "w") as out_f:
		out_f.write(text)

	print()
	print("Your rows were written to file '{}'".format(filename))


def exercise_2(filename):
	print("Content:")

	with open(filename) as f_obj:
		content = f_obj.readlines()

	for line in content:
	    print(line, end="")

	print()
	print("Count of words in rows:")
	for i, line in enumerate(content):
	    print("row[{}]: {} words".format(i, len(line.split())))
	print("Count of rows: {}".format(len(content)))


description = "This app can ask text from you, write it to file.\n"
description += "Then app give you infromation about rows in file.\n"
description += "To stop asking type empty string."
print(description)

filename = "out_file.txt"
exercise_1(filename)
exercise_2(filename)