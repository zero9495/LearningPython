'''
	Lesson: 1
	Excersice: 5
	Author: Aleksandr Plyukhin	
'''

description = "This app can give economic information about your firm"
print(description)

ask_receipts = "Please, type receipts: "
receipts = int(input(ask_receipts))

ask_costs = "Please, type costs: "
costs = int(input(ask_costs))

result = receipts - costs
result_string = ""

if result > 0:
	result_string = "profit"
elif result < 0:
	result_string = "loss"
else:
	result_string = "zero profit"

print(f"Your result is {result_string}")

if result > 0:
	profitability = result / receipts
	print("Profitability of your firm = %.2f" % profitability)

	print("")
	ask_number_of_employees = "Please, type number of employees: "
	number_of_employees = int(input(ask_number_of_employees))

	profit_per_employee = result / number_of_employees
	print("Profit per employee = %.2f" % profit_per_employee)