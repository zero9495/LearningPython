'''
	Lesson: 4
	Exersice: 5
	Author: Aleksandr Plyukhin	
'''

from functools import reduce

def my_func(prev_el, el):
    # prev_el - предыдущий элемент
    # el - текущий элемент
    return prev_el * el

temp_list = [x for x in range(100, 1001, 2)]

print(reduce(my_func, temp_list))