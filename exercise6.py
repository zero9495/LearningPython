'''
	Lesson: 2
	Excersice: 6
	Author: Aleksandr Plyukhin	
'''

ask_elements_count = "Please, type count of elements that you will type: "
elements_count = int(input(ask_elements_count))

goods = []

for _ in range(elements_count):
	print(f"Please, fill in the information about good №{len(goods)}")
	name = input("Name: ")
	price = float(input("Price: "))
	count = int(input("Count: "))
	measure = input("Measure: ")

	good = (len(goods), dict(name=name, price=price, count=count, measure=measure))
	goods.append(good)
	print()

for good in goods:
	print(good)

#########

vals = []
for good in goods:
	vals.append(list(good[1].values()))

new_list_z = zip(*vals)
new_list = list(new_list_z)

analytics = dict()
analytics['name'] = new_list[0]
analytics['price'] = new_list[1]
analytics['count'] = new_list[2]
analytics['measure'] = new_list[3]

print(analytics)