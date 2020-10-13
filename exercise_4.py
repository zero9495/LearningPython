'''
	Lesson: 5
	Exersice: 4
	Author: Aleksandr Plyukhin	
'''

dictionary = dict()
dictionary["one"] = "один"
dictionary["two"] = "два"
dictionary["three"] = "три"
dictionary["four"] = "четыре"

def translate(string):
	''' This function translate string from english to russian 

	Args:
		string (str): string in english

    Returns:
        string: string in russian
	'''
	for eng in dictionary:
		string = string.lower().replace(eng, dictionary[eng])
	return string

eng_file_name = "english_numbers.txt"
rus_file_name = "russian_numbers.txt"

with open(eng_file_name, encoding="utf-8") as f_eng:
	with open(rus_file_name, "w", encoding="utf-8") as f_rus:
		for line in f_eng:
			new_line = translate(line)
			f_rus.write(new_line)