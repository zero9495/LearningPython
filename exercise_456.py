'''
	Lesson: 8
	Exersice: 4,5,6
	Author: Aleksandr Plyukhin	
'''

class Storage():
	def __init__(self):
		self.office_equipments = dict()
		for type_name in ['Printer', 'Scaner', 'Xerox']:
			self.office_equipments[type_name] = []

	def __str__(self):
		string = ""
		for type_name in self.office_equipments:
			count = len(self.office_equipments[type_name])
			string += f'{type_name} (count {count}): '
			
			for x in self.office_equipments[type_name]:
				string += f"'{x}' "
			string += '\n'
		return string

	def put_in(self, office_equipment):
		type_name = type(office_equipment).__name__
		self.office_equipments[type_name].append(office_equipment)

	def put_out(self, type_name, count):
		if type(count).__name__ != 'int':
			return print("'count' must be a 'int' type")
		temp_list = []
		for _ in range(count):
			temp_list.append(self.office_equipments[type_name].pop(0))
		return temp_list


class OfficeEquipment():
	def __init__(self, equipment_param):
		self.equipment_param = equipment_param

	def __str__(self):
		return self.equipment_param


class Printer(OfficeEquipment):
	def __init__(self, equipment_param, printer_param):
		super().__init__(equipment_param)
		self.printer_param = printer_param

	def __str__(self):		
		return super().__str__() + ', ' + self.printer_param


class Scaner(OfficeEquipment):
	def __init__(self, equipment_param, scaner_param):
		super().__init__(equipment_param)
		self.scaner_param = scaner_param

	def __str__(self):		
		return super().__str__() + ', ' + self.scaner_param


class Xerox(OfficeEquipment):
	def __init__(self, equipment_param, xerox_param):
		super().__init__(equipment_param)
		self.xerox_param = xerox_param

	def __str__(self):		
		return super().__str__() + ', ' + self.xerox_param


storage = Storage()
storage.put_in(Printer('equipment_param value','printer_param value'))
storage.put_in(Printer('equipment_param value2','printer_param value2'))
storage.put_in(Scaner('equipment_param value','scaner_param value'))
storage.put_in(Xerox('equipment_param value','xerox_param value'))
print(storage)

print(storage.put_out('Printer', '2'))
print(storage.put_out('Printer', 2))
print()
print(storage)