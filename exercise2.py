'''
	Lesson: 1
	Excersice: 2
	Author: Aleksandr Plyukhin	
'''

description = "This app can format seconds into HH:MM:SS"
print(description)

ask_seconds = "Please, type seconds: "
seconds = int(input(ask_seconds))

ss = seconds % 60
mm = (seconds // 60) % 60
hh = (seconds // 60) // 60

print("Your %d seconds formatted into %d:%d:%d" % (seconds, hh, mm, ss))