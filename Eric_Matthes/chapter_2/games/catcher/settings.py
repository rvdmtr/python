#settings.py

class Settings():
	"""Класс для хранения всех настроек игры Alien Invasion"""
	def __init__(self):
		"""Инициализирует настройки игры"""
		# Параметры экрана
		self.screen_width = 600
		self.screen_height = 400
		self.bg_color = (230,30,230)

		# Настройки кошака
		self.cat_speed_factor = 0.37
		self.cat_limit = 3

		#Параметры пули
		#self.bal_speed_factor = 0.5
		#self.bal_width = 300
		#self.bal_height = 15
		self.ball_color = 60,60,60
		self.balls_allowed = 1

		#Настройки мяча
		self.ball_speed_factor = 0.17
			