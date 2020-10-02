'''
	Lesson: 2
	Excersice: 4
	Author: Aleksandr Plyukhin	
'''

description = "This app can number words in your sentence."
print(description)

ask_sentence = "Please, type your sentence: "
sentence = input(ask_sentence)

for i, word in enumerate(sentence.split(' ')):
	print(f'{i} : {word[:10]}')