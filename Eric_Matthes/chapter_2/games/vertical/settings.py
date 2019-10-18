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
		self.plane_limit = 3

		#Параметры пули
		self.missle_width = 15
		self.missle_height = 3
		self.missle_color = 60,60,60
		self.missles_allowed = 3

		# Настройки противника
		self.fleet_drop_speed = 10

		# Темп ускорения игры
		self.speedup_scale = 2

		self.initialize_dynamic_settings()

	def initialize_dynamic_settings(self):
		"""Инициализирует настройки, изменяющиеся в ходе игры"""
		
		self.plane_speed_factor = 0.37
		self.missle_speed_factor = 0.5
		self.alien_speed_factor = 0.1
		
		self.fleet_direction = 1

	def increase_speed(self):
		"""Увеличивает настройки скорости"""
		self.plane_speed_factor *= self.speedup_scale
		self.missle_speed_factor *= self.speedup_scale
		self.alien_speed_factor *= self.speedup_scale