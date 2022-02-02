def function():
	print("helloo")

function()

# Class that describes a dogs
class Dog:
	"""A simple attempt to modify a Dog"""
	def __init__(self, name, age):
		"""initialize name and age attricutes"""
		self.name = name
		self.age = age

	def sit(self):
		"""simulate the dog sitting by a command"""
		print(f"{self.name} is now sitting")

	def roll_over(self):
		"""simulate yjr dog rolling over by a command"""
		print(f"{self.name} rolled over")

my_dog = Dog("valence", 6)
your_dog = Dog("lucy", 3)

print(f"My dog's name is {my_dog.name}!")
print(f"My dog is {my_dog.age} years old")
my_dog.sit()
my_dog.roll_over()

print(f"My dog's name is {your_dog.name}!")
print(f"My dog is {your_dog.age} years old")
your_dog.sit()
your_dog.roll_over()

# Class that describes the type and name of a restaurant
class Restaurant:
	def __init__(self, restaurant_name, restaurant_type):
		"""Initialize name and type attribute"""
		self.restaurant_name = restaurant_name
		self.restaurant_type = restaurant_type

	def describe_restaurant(self):
		"""describes the restaurant"""
		print(f"The {self.restaurant_name} is a {self.restaurant_type} restaurant")

	def open_restaurant(self):
		"""state of the restaurant"""
		print(f"We are open for business!")

restaurant1 = Restaurant("Burger king", "Cafeteria")
restaurant2 = Restaurant("Pita Pan", "Cafe")
restaurant3 = Restaurant("Kalifonia Pizza Kitchen", "Fast food")

# print(f"I love eating from {restaurant.restaurant_name} restaurant")
# print(f"{restaurant.restaurant_name} is a {restaurant.restaurant_type} restaurant")
# calling the methods
restaurant1.describe_restaurant()
restaurant1.open_restaurant()

restaurant2.describe_restaurant()
restaurant2.open_restaurant()

restaurant3.describe_restaurant()
restaurant3.open_restaurant()

class User:
	def __init__(self, first_name, last_name, age, location):
		"""Initializing the various attributes"""
		self.first_name = first_name
		self.last_name = last_name
		self.age = age
		self.location = location

	def describe_user(self):
		print(f"{self.first_name} {self.last_name} is {self.age} old and he leaves in {self.location}")

	def greet_user(self):
		print(f"Hi! {self.first_name} {self.last_name} You are welcome!")

my_name = User("Mofiro", "Jean", 19, "Bambili")
print(f"hello am called {my_name.first_name}")
my_name.describe_user()
my_name.greet_user()