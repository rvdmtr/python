#settings.py

class Settings():
	"""Класс для хранения всех настроек"""
	def __init__(self):
		"""Инициализирует настройки игры"""
		self.screen_width = 600
		self.screen_height = 400
		self.bg_color = (30,30,100)

		#Настройки капель
		self.drop_speed_factor = 0.009
		