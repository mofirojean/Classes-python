#Class that describes the type and name of a restaurant
class Restaurant:
	def __init__(self, restaurant_name, restaurant_type):
		"""Initialize name and type attribute"""
		self.restaurant_name = restaurant_name
		self.restaurant_type = restaurant_type
		self.number_served = 0

	def describe_restaurant(self):
		"""describes the restaurant"""
		print(f"The {self.restaurant_name} is a {self.restaurant_type} restaurant")

	def open_restaurant(self):
		"""state of the restaurant"""
		print(f"We are open for business!")

	def set_number_served(self, customers_served):
		self.number_served = customers_served

	def increment_number_serverd(self, increment_served):
		self.number_served += increment_served

class IceCreamStand(Restaurant):
	"""docstring for IceCreamStand"""
	def __init__(self, restaurant_name, restaurant_type):
		super().__init__(restaurant_name, restaurant_type)
		self.flavours = ["Straw Berry", "choacolate", "Black Berry", "Peanut", "Banana", "Water melon"]

	def flavours_list(self):
		print(f"the restaurant has the following flavours {self.flavours} ")
		
# flavours = IceCreamStand("Ice Mania", "Ice Cream")
# flavours.describe_restaurant()
# flavours.flavours_list()
# restaurant = Restaurant("Burger king", "Fast food")
# restaurant.number_served = 30
# print(restaurant.number_served)

# restaurant.set_number_served(50)
# print(restaurant.number_served)

# # incremented 
# restaurant_user = Restaurant("Second wife", "Fast food")
# restaurant_user.number_served = 500
# restaurant_user.increment_number_serverd(20)
# print(restaurant_user.number_served)