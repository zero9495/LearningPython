'''
	Lesson: 3
	Excersice: 2
	Author: Aleksandr Plyukhin	
'''

def ask_user(name, type):
	''' This function asking the user variable value 

	Args:
		name (str): The name of variable
		type (str): The type of variable

    Returns:
        variable: A variable a 'type' type
	'''
	question = f"Please, type {name}: "
	while True:
		answer = input(question)

		if type == 'int':
			try:
				answer = int(answer)
				break
			except ValueError:
				msg = (f"{name} must be a 'int' type").capitalize()
				print(msg)
		else:
			break
	return answer


def user_info(fname, lname, birthyear, residence_city, email, phone):
	''' This function give detailed information about user 

	Args:
		fname (str): First name
		lname (str): Last name
		birthyear (int): Birthyear
		residence_city (str): Residence city
		email (str): email
		phone (int): Phone
	'''
	msg = f"User named {fname} {lname} born in {birthyear} year "
	msg += f"is residing in {residence_city}. "
	msg += f"You can contact the user by email {email} or phone {phone}."
	print(msg)


description = "This app can give detailed information about user."
print(description)

fname = ask_user("first name", "str")
lname = ask_user("last name", "str")
birthyear = ask_user("birthyear", "int")
residence_city = ask_user("residence city", "str")
email = ask_user("email", "str")
phone = ask_user("phone", "int")

user_info(fname, lname, birthyear, residence_city, email, phone)