'''
	Lesson: 2
	Excersice: 3
	Author: Aleksandr Plyukhin	
'''

seasons = ['Winter', 'Spring', 'Summer', 'Autumn']
months = dict()

for season_num in range(4):
	for month_of_season_num in range(3):
		months[(season_num*3 + month_of_season_num + 11) % 12 + 1] = season_num

description = "This app give name of season of the year according to number of month"
print(description)

ask_month_number = "Please, type number of month (from 1 to 12): "
month_number = int(input(ask_month_number))

if month_number >= 1 and month_number <= 12:
	print(f"Month with number {month_number} refers to {seasons[months[month_number]]}")
else:
	print("Error: Number of month must be between 1 and 12")