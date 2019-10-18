class User():
	"""Простая модель пользовательского профиля"""
	def __init__(self,first_name,last_name,age,height,secret):
		"""Инициализирует атрибуты экземпляра"""
		self.first_name = first_name
		self.last_name = last_name
		self.age = age
		self.height = height
		self.secret = secret


	def describe_user(self):
		print('Information about user:\n\t' + 
			'name: ' + self.first_name.title() + ' ' +
		self.last_name.title() + '\n\tage: ' +
		str(self.age) + '\n\theight: ' + str(self.height) + 
		'\n\tpassword: ' + self.secret)


	def greet_user(self):
		print('\nGreetings senior ' + self.first_name.title() + ' '
			+ self.last_name.title())

person=User('john','malkovich',60,170,'pass')
person.describe_user()
person.greet_user()