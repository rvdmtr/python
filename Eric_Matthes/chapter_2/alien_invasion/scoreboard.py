#scoreboard.py

import pygame as pg
#import pygame.font
#from  pg.sprite import Group

from ship import Ship

class Scoreboard():

	"""Класс для вывода игровой информации"""
	def __init__(self,ai_settings,screen,stats):
		"""Инициализирует атрибуты подсчета очков"""
		self.screen = screen
		self.screen_rect = screen.get_rect()
		self.ai_settings = ai_settings
		self.stats = stats

		# Настройки шрифта для вывода счета
		self.text_color = (30,30,30)
		self.font = pg.font.SysFont(None,48)

		self.prep_images()

	def prep_images(self):
		"""Группировка методов для подготовки изображений"""
		# Подготовка изображений счетов.
		self.prep_score()
		self.prep_high_score()
		self.prep_level()
		self.prep_ships()
		

	def prep_score(self):
		"""Преобразует текущий счет в графическое изображение"""
		rounded_score = int(round(self.stats.score, -1))
		score_str = "{:,}".format(rounded_score)
		self.score_image = self.font.render(score_str,True,self.text_color,self.ai_settings.bg_color)

		# Вывод счета в правой верхней части экрана
		self.score_rect = self.score_image.get_rect()
		self.score_rect.right = self.screen_rect.right - 20
		self.score_rect.top = 20

	def prep_high_score(self):
		"""Преобразует рекордный счет в графическое изображение"""
		high_score = int(round(self.stats.high_score, -1))
		high_score_str = "{:,}".format(high_score)
		self.high_score_image = self.font.render(high_score_str,True,self.text_color,self.ai_settings.bg_color)

		# Рекорд выравнивается по центру верхней стороны.
		self.high_score_rect = self.high_score_image.get_rect()
		self.high_score_rect.centerx = self.screen_rect.centerx
		self.high_score_rect.top = self.screen_rect.top

	def prep_level(self):
		"""Преобразует уровень в графическое изображение"""
		self.level_image = self.font.render(str(self.stats.level),True,self.text_color,self.ai_settings.bg_color)

		# Уровень выводится под текущим счетом.
		self.level_rect = self.level_image.get_rect()
		self.level_rect.right = self.score_rect.right
		self.level_rect.top = self.score_rect.bottom + 10

	def prep_ships(self):
		"""Сообщает количество оставшихся кораблей."""
		self.ships = pg.sprite.Group()
		for ship_number in range(self.stats.ship_left):
			ship = Ship(self.ai_settings,self.screen)
			ship.rect.x = 3 + (ship_number * ship.rect.width * 1.1)
			ship.rect.y = 1
			self.ships.add(ship)



	def show_score(self):
		"""Выводит счет на экран"""
		self.screen.blit(self.score_image,self.score_rect)
		self.screen.blit(self.high_score_image,self.high_score_rect)
		self.screen.blit(self.level_image,self.level_rect)
		self.ships.draw(self.screen)
