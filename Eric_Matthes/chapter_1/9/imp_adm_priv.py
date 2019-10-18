from imp_user import User


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
