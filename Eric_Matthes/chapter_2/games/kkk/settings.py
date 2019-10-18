#settings.py

class Settings():
	"""Класс для хранения всех настроек игры Alien Invasion"""
	def __init__(self):
		"""Инициализирует настройки игры"""
		# Параметры экрана
		self.screen_width = 600
		self.screen_height = 400
		self.bg_color = (230,30,230)

		# Настройки корабля
		self.ship_speed_factor = 0.37

		#Параметры пули
		self.bullet_speed_factor = 0.5
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = 60,60,60
		self.bullets_allowed = 3

		#Настройки пришельцев
		self.alien_speed_factor = 0.07
		self.fleet_drop_speed = 10
		# fleet_direction = 1 обозначает движение вправо; а -1 - влево
		self.fleet_direction = 1

	