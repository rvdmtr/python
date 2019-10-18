#game_stats.py

class GameStats():
	"""Отслеживание статистики"""

	def __init__(self,ai_settings):
		self.ai_settings = ai_settings
		self.reset_stats()

		self.game_active = True

	def reset_stats(self):
		"""Инициализирует статистику меняющуюся в ходе игры"""
		self.cat_left = self.ai_settings.cat_limit