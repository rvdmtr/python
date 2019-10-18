#game_stats.py

class GameStats():
	def __init__(self,ai_settings):
		self.ai_settings = ai_settings
		self.reset_stats()

		# Игра запускается в активном состоянии.
		self.game_active = False

	def reset_stats(self):
		"""Инициализирует статистику меняющуюся в ходе игры"""
		self.plane_left = self.ai_settings.plane_limit