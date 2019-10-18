#tes_settings.py

class Settings():
	"""Класс для хранения всех настроек игры Alien Invasion"""
	def __init__(self):
		"""Инициализирует настройки игры"""
		# Параметры экрана
		self.screen_width = 600
		self.screen_height = 400
		self.bg_color = (30,30,230)

		# Настройки корабля
		self.rocket_speed_factor = 0.37