""" working with classes and instances """
class Car(object):
	"""discribing a simple car"""
	def __init__(self, manifacturer, model, year):
		"""Initializing attributes to describe a car"""
		self.manifacturer = manifacturer
		self.model = model
		self.year = year
		self.odometer_reading = 0

	def get_descriptive_name(self):
		"""display a well formatted name of the car"""
		long_name = f"{self.year} {self.manifacturer} {self.model}"
		return long_name.title()

	def read_odometer(self):
		"""Print info indicating car's mileage"""
		print(f"This car has {self.odometer_reading} miles on it")

	def fill_gas_tank(self):
		print("The gas tank is filled")

	def update_odometer(self, mileage):
		"""
		Set the odometer reading to the given value.
		Reject the change if it attempts to roll the odometer back.
		"""
		if mileage >= self.odometer_reading:
			self.odometer_reading = mileage
		else:
			print("You can't roll back an odometer!")

	def increment_odometer(self, mile):
		"""
		Add the given amount to the odometer reading.
		making sure no one uses this method as a roll back
		"""
		if mile < 0:
			print("The incremented value entered is negative!")
		else:
			self.odometer_reading += mile

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
			print(f"battery is capicty reseted back  to {self.battery_size}")
		

		
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


my_limo = ElectricCar("Limo", "W-S version", 2019)
print(my_limo.get_descriptive_name())
my_limo.battery.get_range()
print(my_limo.battery.battery_upgrade()
my_limo.battery.get_range()



my_new_car = Car("ford", "A267-74", 2019)
print(my_new_car.get_descriptive_name())
my_new_car.odometer_reading = 23
my_new_car.read_odometer()
my_new_car.fill_gas_tank()

my_tesla = ElectricCar("Tesla", "Model s", 2019)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
my_tesla.fill_gas_tank()

# results from updating an Attribute's value using a method
my_new_car.update_odometer(23)
my_new_car.read_odometer()

# test run
# my_new_car.update_odometer(20)
my_new_car.update_odometer(40)
my_new_car.read_odometer()
my_new_car.update_odometer(30)

my_used_car = Car("lamogini", "B36", 2016)

# increment odometer reading
print(my_used_car.get_descriptive_name())
my_used_car.update_odometer(25000)

my_used_car.increment_odometer(-100)
my_used_car.read_odometer()
