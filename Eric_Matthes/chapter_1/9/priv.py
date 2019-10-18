#####Ex 9-1,9-4(number_served)


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


person = User('john','malkovich',60,175,'malk70')

person.describe_user()
person.greet_user()
person.increment_login_attempts(5)
person.reset_login_attempts()

person = User('christiano','ronaldo',32,185,'CR7')
#person.describe_user()
#person.greet_user()
person.increment_login_attempts(5)
person.increment_login_attempts(1)
person.increment_login_attempts(1)
person.reset_login_attempts()




####Ex 9-7
print('\n##################')
print('###################\nEx9-8\n')


class Privileges():
	"""Описывает привилегии пользователя"""
	def __init__(self):
			self.privileges = ['can add messages','can del users','can ban users']

	def show_privileges(self): #не забывай self указывать, ссылка на атрибуты
		"""Перебирает выданные привелегии и выводит на экран"""
		#name = Admin.first_name + ' ' + Admin.last_name
#		self.privileges = priveleges

		print('Privileges of ' + adm_name.title() + ' are ')
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

#	def show_privileges(self):#не забывай self указывать, ссылка на атрибуты
#		"""Перебирает выданные привелегии и выводит на экран"""
#		name = self.first_name + ' ' + self.last_name
#		print('Privileges of ' + name.title() + ' are ')
#		for priv in self.privileges:#self не забывай
#			print('\t--- ' + priv)



adm = Admin('albert','vasnecov',30,190,'apasas')
adm_name = adm.first_name + ' ' + adm.last_name
#print(adm.first_name.title())

adm.privileges.show_privileges() 
adm.describe_user()