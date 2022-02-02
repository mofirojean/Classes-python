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
