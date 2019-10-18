#imp_adm

class User():
#	"""Простая модель пользовательского профиля"""
	def __init__(self,first_name,last_name,age,height,secret):
#		"""Инициализирует атрибуты экземпляра"""
		self.first_name = first_name
		self.last_name = last_name
		self.age = age
		self.height = height
		self.secret = secret
		self.login_attempts = 0
		

	def describe_user(self):
		print('\nInformation about user:\n\t' + 
			'name: ' + self.first_name.title() + ' ' +
		self.last_name.title() + '\n\tage: ' +
		str(self.age) + '\n\theight: ' + str(self.height) + 
		'\n\tpassword: ' + self.secret)


	def greet_user(self):
		print('\nGreeting senior ' + self.first_name.title() + ' '
			+ self.last_name.title())


	def increment_login_attempts(self,increment):
		"""Увеличивает количество попыток входа у пользователя"""
		self.login_attempts += increment
		print('Current login attempts of ' + self.first_name.title() + ' ' +	
			self.last_name.title() + ' is ' + str(self.login_attempts))


	def reset_login_attempts(self):
		self.login_attempts = 0
		print('Login attepmts was reset. Current login  attemps of ' +
			self.first_name.title() + ' ' +	self.last_name.title() + 
			' is ' + str(self.login_attempts) + '\n' 
		)



class Privileges():
	"""Описывает привилегии пользователя"""
	def __init__(self):
			self.privileges = ['can add messages','can del users','can ban users']

	def show_privileges(self): #не забывай self указывать, ссылка на атрибуты
		"""Перебирает выданные привелегии и выводит на экран"""
		#name = Admin.first_name + ' ' + Admin.last_name
#		self.privileges = priveleges

		print('Privileges :')
		for priv in self.privileges:      #self не забывай
			print('\t--- ' + priv)



class Admin(User):
	"""Инициализирует атрибуты потомка"""
	def __init__(self,first_name,last_name,age,
		height,secret
		):#добавили в субкласс атрибут-параметр privileges
		"""Инициализирует атрибуты родителя"""
		super().__init__(first_name,last_name,age,height,secret)
		
		self.privileges = Privileges() # СОЗДАНИЕ ЭКЗЕМПЛЯРА КАК АТРИБУТА КЛАССА
