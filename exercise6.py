'''
	Lesson: 3
	Excersice: 6
	Author: Aleksandr Plyukhin	
'''

import string

def int_func(word):
	''' This function returns a word where the first 
		character in every word is upper case

	Args:
		word (str): Word with lower english letters

    Returns:
        word: Word with first upper letter
	'''
	for sign in word:
		if sign not in string.ascii_lowercase :
			print("Function int_func work with lower english letters only")
			return -1

	return word.title()

def int_func_2(sentence):
	''' This function returns a string where the first 
		character in every word is upper case

	Args:
		sentence (str): Sentence with lower english letters.
						Words in sentence parted with space

    Returns:
        sentence: string where the first 
				  character in every word is upper case
	'''
	temp_list = sentence.split(' ')
	for i, word in enumerate(temp_list):
		temp_list[i] = int_func(word)
		if temp_list[i] == -1:
			return
	return ' '.join(temp_list)


description = "This app returns a string where the first "
description += "character in every word is upper case."
print(description)

sentence = input("Please, type sentence: ")

print("Result sentence: ", int_func_2(sentence))