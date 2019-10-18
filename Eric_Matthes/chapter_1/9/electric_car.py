#electric_car.py
"""Набор классов для представления электромобилей"""
from car import Car

class Battery():
	"""Простая модель аккумулятора электромобиля"""
	def __init__(self,battery_size=70):
		"""Инициализация атрибутов аккумулятора"""
		self.battery_size = battery_size

	def describe_battery(self):
		"""Выводит информацию о мощности аккумулятора"""
		print("This car has a " + str(self.battery_size) + "-kWh battery.")

	def get_range(self):
		"""Выводит приблизительный запас хода для аккумулятора"""
		if self.battery_size == 70:
			range = 240
		elif self.battery_size == 85:
			range = 270
		message = "This car can go approximately " + str(range)
		message += " miles on a full charge."
		print(message)


class ElectricCar(Car):
	"""Представляет аспекты машины, специфические для электромобилей."""
	def __init__(self,make,model,year):
		"""
		Инициализирует атрибуты класса-родителя.
		Затем инициализирует атбрибуты, специфические для электромобиля
		"""
		super().__init__(make,model,year)
		self.battery = Battery()