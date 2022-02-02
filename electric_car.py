from car import Car

class Battery:
	"""A simple attempt to model a battery for an electric car."""
	def __init__(self, battery_size = 75):
		"""Initailizing batteries's attribute"""
		self.battery_size = battery_size

	def describe_battery(self):
		"""Print a statement describing the battery size."""
		print(f"This car has a {self.battery_size} KWH battery")

	def get_range(self):
		"""print a statement about the range this battery provides"""
		if self.battery_size == 75:
			car_range = 260
		elif self.battery_size == 100:
			car_range = 315
		print(f"This car can go {car_range} miles on a full charge")

	def battery_upgrade(self):
		"""checkiing if the battery size is 100 if not reset it"""
		if self.battery_size == 100:
			print("Batterycapacity is at 100%")
		elif self.battery_size < 100:
			self.battery_size = 100

	
class ElectricCar(Car):
	"""Represent aspects of a car, specific to electric vehicles."""
	def __init__(self,  manifacturer, model, year):
		"""Initializing the attributes from the parent class
		Then initialize attributes specific to an electric car."""
		super().__init__(manifacturer, model, year)
		# self.battery_size = 75
		self.battery = Battery()

	# def describe_battery(self):
	# 	"""Print a statement describing the battery size."""
	# 	print(f"This car has a {self.battery_size} KWH battery")

	def fill_gas_tank(self):
		"""Overiding the gas method for electric cars"""
		print(f"You can't fill an electric car with gas!")