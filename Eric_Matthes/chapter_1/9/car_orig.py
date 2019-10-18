class Car():
	"""Простая модель автомобиля"""
	def __init__(self,make,model,year):
		"""Инициализирует атрибуты экземпляра"""
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0



	def get_descriptive_name(self):
		"""Возвращает аккуратно отформатированное описание"""
		long_name = str(self.year) + ' ' + self.make + ' ' + self.model
		return long_name.title()

	def read_odometer(self):
		"""Выводит пробег машины в милях."""
		print("This car has " + str(self.odometer_reading) + " miles on it.\n")

### Изменение значения атрибута с использованием метода
	def update_odometer(self,mileage):
		"""
		Устанавливает на одометре заданное значение.
		При попытке обратной подкрутки изменение отклоняется
		"""
		if mileage >= self.odometer_reading:
			self.odometer_reading = mileage
		else:
			print('You can`t roll back and odometer!')


### Изменение значения атрибута c приращением

	def increment_odometer(self,miles):
		"""Увеличивает показания одомета с заданным приращением"""
		self.odometer_reading += miles





my_new_car = Car('audi','a4','2019')
print(my_new_car.get_descriptive_name())

my_new_car.read_odometer()



###### Изменение значений атрибутов #######
### Прямое изменение значения атрибута
my_new_car.odometer_reading = 23
my_new_car.read_odometer()



### Изменение значения атрибута с использованием метода
#	def update_odometer(self,mileage):
#		"""
#		Устанавливает на одометре заданное значение.
#		При попытке обратной подкрутки изменение отклоняется
#		"""
#		if mileage >= self.odometer_reading:
#			self.odometer_reading = mileage
#		else:
#			print('You can`t roll back and odometer!')


### Изменение значения атрибута c приращением

#	def update_odometer(self,miles):
#		"""Увеличивает показания одомета с заданным приращением"""
#		self.odometer_reading += miles

my_used_car = Car('Subaru','outback',2013)
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23500)
my_used_car.read_odometer()

my_used_car.update_odometer(23400)
my_used_car.read_odometer()

my_used_car.increment_odometer(100)
my_used_car.read_odometer()


#################################
#################################
##### Наследование классов

print('\n#####################')
print('#####################\n')


class Battery():
	"""Простая модель аккумулятора электромобиля"""
	def __init__(self,battery_size=70):
		"""Инициализирует атрибуты аккумулятора"""
		self.battery_size = battery_size

	def describe_battery(self):
		"""Выводит информацию о мощности аккумулятора."""
		print('This car has a ' + str(self.battery_size) + '-kWh battery')

	def upgrade_battery(self):
		"""Показывает и устанавливает мощность аккумулятора"""
		if self.battery_size != 85:
			self.battery_size = 85

	def get_range(self):
		"""Выводит приблиительный запас хода для аккумулятора."""
		if self.battery_size == 70:
			range = 240
		elif self.battery_size ==85:
			range = 270

		message = 'This car can go approximately ' + str(range)
		message += ' miles on a full charge'
		print(message)



class ElectricCar(Car):
	"""Представляет аспекты машины, специфические для электомобилей."""
	def __init__(self,make,model,year):
		"""Инициализирует атрибуты класса-родителя.
		Затем инициализирует атрибуты, специфические для электромобиля.
		"""
		super().__init__(make,model,year)

		self.battery = Battery()




my_tesla = ElectricCar('tesla','model y','2019')
print(my_tesla.get_descriptive_name())
#my_tesla.describe_battery()

my_nissan = ElectricCar('nissan','leaf','2019')
print(my_nissan.get_descriptive_name())
my_nissan.battery.describe_battery()
print(my_nissan.battery.battery_size)
my_nissan.battery.get_range()


my_nissan.battery.upgrade_battery()

my_nissan.battery.describe_battery()
print(my_nissan.battery.battery_size)
my_nissan.battery.get_range()
#################################
#################################
print('\n#####################')
print('#####################\n')

#class Battery():
#	"""Простая модель аккумулятора электромобиля"""
#	def __init__(self,battery_size=70):
#		"""Инициализирует атрибуты аккумулятора"""
#		self.battery_size = battery_size
#
#	def describe_battery(self):
#		"""Выводит информацию о мощности аккумулятора"""
#		print('This car has a ' + str(self.battery_size) + '-kWh battery')

my_tesla.battery.describe_battery()
my_tesla.battery.get_range()