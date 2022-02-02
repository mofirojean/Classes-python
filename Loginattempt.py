class User:
	def __init__(self, first_name, last_name, age, location):
		"""Initializing the various attributes"""
		self.first_name = first_name
		self.last_name = last_name
		self.age = age
		self.location = location
		self.login_attempt = 0

	def describe_user(self):
		print(f"{self.first_name} {self.last_name} is {self.age} old and he leaves in {self.location}")

	def greet_user(self):
		print(f"Hi! {self.first_name} {self.last_name} You are welcome!")

	def increment_login_attempt(self):
		self.login_attempt += 1

	def reset_login_attempts(self):
		self.login_attempt *= 0


class Privileges:
	"""docstring for Privileges for the admin"""
	def __init__(self, privileges = ["can add post", "can delete post", "can ban user"]):
		self.privileges = privileges
		
	def show_privileges(self):
		"""prints out the privileges of an administrator"""
		print(f"Admins have the following privileges {self.privileges}")


class Admin(User):
	"""A simple class for Admins"""
	def __init__(self, first_name, last_name, age, location):
		super().__init__(first_name, last_name, age, location)
		self.admin_privileges = Privileges()

	
		



# admins = Admin("mofiro", "Jean", 18, "Bambili")
# admins.greet_user()
# admins.admin_privileges.show_privileges()

# my_name = User("Mofiro", "Jean", 19, "Bambili")
# my_name.increment_login_attempt()
# print(my_name.login_attempt)
# my_name.reset_login_attempts()
# print(my_name.login_attempt)
# my_name.increment_login_attempt()
# my_name.increment_login_attempt()
# my_name.increment_login_attempt()
# my_name.increment_login_attempt()
# my_name.increment_login_attempt()
# print(my_name.login_attempt)
# my_name.reset_login_attempts()
# print(my_name.login_attempt)