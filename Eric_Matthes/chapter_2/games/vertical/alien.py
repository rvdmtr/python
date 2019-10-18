#alien.py

import pygame as pg
from pygame.sprite import Sprite

class Alien(Sprite):
	"""Класс, предстовляющий одного пришельца"""

	def __init__(self,ai_settings,screen):
		"""Инициализирует пришельца и задает его начальную позицию"""
		super(Alien,self).__init__()
		self.screen = screen
		self.ai_settings = ai_settings

		# Загрузка изображения прямоугольника
		self.image = pg.image.load("img/al.bmp")
		self.rect = self.image.get_rect()

		# Каждый новый пришелец появляется в левом верхнем углу экрана
		self.rect.x = ai_settings.screen_width - 40
		self.rect.y = self.rect.height

		# Сохранение точной позиции прямоугольника
		self.x = float(self.rect.x)
		self.y = float(self.rect.y)

	def blitme(self):
		"""Выводит прямоугольник в текущем положении"""
		self.screen.blit(self.image,self.rect)

	def check_edges(self):
		"""Возвращает True, если пришелец находится у края экрана"""
		screen_rect = self.screen.get_rect()
		if self.rect.bottom >= screen_rect.bottom:
			return True
		elif self.rect.top <= 0:
			return True

	def update(self):
		"""Перемещает прямоугольник вниз или вверх"""
		self.y += (self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction)
		self.rect.y = self.y
