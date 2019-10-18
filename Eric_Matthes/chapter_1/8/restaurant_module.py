class Restaurant():
	"""Простая модель ресторана"""
	def __init__(self,restaurant_name,cuisine_type):
		"""Инициализирует атрибуты описания ресторана"""
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
		self.number_served = 0

	def describe_restaurant(self):
		print('The name of our restaurant is ' + 
			self.restaurant_name.title() + '.\n' + 
			'The kitchen in a restaurant is ' + 
			self.cuisine_type.title() + '.\n' +
			'Number of served tables is ' + str(self.number_served) +
			'.\n'
			)

	def open_restaurant(self):
		print('Our restaurant ' + self.restaurant_name.title() + ' is open')

###### Ex 9-5

	def set_number_served(self,number):
		self.number_served = number

	def increment_number_served(self,number):
		self.number_served += number