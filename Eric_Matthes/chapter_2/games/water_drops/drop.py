#drop.py

import pygame as pg 
from pygame.sprite import Sprite

class Drop(Sprite):
	"""Класс, представляющий одну каплю"""
	def __init__(self,ai_settings,screen):
		super(Drop,self).__init__()
		self.screen = screen
		self.ai_settings = ai_settings

		# Загрузка изображения капли и назначение
		# атрибута rect
		self.image = pg.image.load("img/al.bmp")
		self.rect = self.image.get_rect()

		# каждая новая капля появляется в левом верхнем углу экрана
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height

		# Сохранение точной позиции
		self.x = float(self.rect.x)
		self.y = float(self.rect.y)

	def blitme(self):
		"""Выводит каплю в текущем положении"""
		self.screen.blit(self.image,self.rect)

	def check_edges(self):
		"""Возвращает True, если капля находится у нижнего края экрана"""
		screen_rect = self.screen.get_rect()
		if self.rect.bottom >= screen_rect.bottom:
			return True

	def update(self):
		"""Перемещает пришельца вниз"""
		self.y += (self.ai_settings.drop_speed_factor)
		self.rect.y = self.y