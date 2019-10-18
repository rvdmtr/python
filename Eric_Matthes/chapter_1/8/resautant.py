#####Ex 9-1,9-4(number_served)

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


res = Restaurant('gili','russian')


##### 9-5
res.set_number_served(5)
res.describe_restaurant()

res.increment_number_served(5)
res.describe_restaurant()

res.increment_number_served(25)
res.describe_restaurant()
res.open_restaurant()


####Ex 9-2
print('\n##################')
print('###################\nEx9-2\n')

mili = Restaurant('mili','italian')
soho = Restaurant('soho','russian')
tbilisi = Restaurant('tbilisi','georgia')

mili.set_number_served(6)
mili.describe_restaurant()
soho.describe_restaurant()
tbilisi.describe_restaurant()


####Ex 9-6
print('\n##################')
print('###################\nEx9-6\n')

class IceCreamStand(Restaurant):
	def __init__(self,restaurant_name,cuisine_type,flavors):#атрибуты потомка
		"""инициализирует атрибуты класса родителя следующая строка"""
		super().__init__(restaurant_name,cuisine_type)#атрибуты класса-родителя
		self.flavors = flavors#добавил атрибут в класс-потомок

	def describe_flavors(self):
		"""Выводит список сортов мороженного"""
		print('List of our ice cream flavors: ')
		for ice_flavor in self.flavors:
			print('  *--- ' + ice_flavor)

stand=IceCreamStand('sweet dream','icecreams',['chocolate','milk','fruit ice'])
#в качестве аргумента атрибуту класса, можно передать список и остальное

stand.open_restaurant()
stand.describe_restaurant()
stand.describe_flavors()

####Ex 9-3
print('\n##################')
print('###################\nEx9-3\n')


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
		print('Information about user:\n\t' + 
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
print('###################\nEx9-7\n')

class Privileges():
	"""Описывает привилегии пользователя"""
#	def __init__(self,privileges=
#	['can add messages','can del users','can ban users']):
	def __init__(self):
		self.privileges = ['can add messages','can del users','can ban users']

	def show_privileges(self):#не забывай self указывать, ссылка на атрибуты
		"""Перебирает выданные привелегии и выводит на экран"""
		#name = self.first_name + ' ' + self.last_name

		print('\n\tPrivileges: ')
		for priv in self.privileges:#self не забывай
			print('\t--- ' + priv)
		

class Admin(User):
	"""Инициализирует атрибуты потомка"""
	def __init__(self,first_name,last_name,age,
		height,secret):#добавили в субкласс атрибут-параметр privileges
		"""Инициализирует атрибуты родителя"""
		super().__init__(first_name,last_name,age,height,secret)
		self.privileges = Privileges() #добавляем атрибут в класс потомок,ссылка
		#на класс Privleges. 

#	def show_privileges(self):#не забывай self указывать, ссылка на атрибуты
#		"""Перебирает выданные привелегии и выводит на экран"""
#		name = self.first_name + ' ' + self.last_name
#		print('Privileges of ' + name.title() + ' are ')
#		for priv in self.privileges:#self не забывай
#			print('\t--- ' + priv)




adm = Admin('albert','vasnecov',30,190,'apasas')

adm.describe_user()
adm.privileges.show_privileges() 