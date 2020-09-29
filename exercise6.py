'''
	Lesson: 1
	Excersice: 6
	Author: Aleksandr Plyukhin	
'''

description = "This app can calculate count of days for achieve target"
print(description)

ask_starting_distance = "Please, type starting distance: "
starting_distance = int(input(ask_starting_distance))

ask_target = "Please, type target: "
target = int(input(ask_target))

distance = starting_distance
count_of_days = 1

while distance < target:
	distance += distance*0.1
	count_of_days += 1

print(f"You will have achieved distance {distance} on {count_of_days} day")