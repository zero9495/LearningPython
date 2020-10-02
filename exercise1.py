'''
	Lesson: 2
	Excersice: 1
	Author: Aleksandr Plyukhin	
'''

my_list = ['a', 1, 2.0, 3 + 4j, [5, 6], (7, 8), set('cde')] 
my_list.extend([dict(f=9), 1==1, b'g', bytearray(b'e'), None])
print(my_list)

for item in my_list:
	print(f'{item} has type {type(item)}')