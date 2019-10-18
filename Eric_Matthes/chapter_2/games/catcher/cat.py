#cat.py

import pygame as pg

class Cat():
	def __init__(self,ai_settings,screen):
		"""Инициализирует кота и задает его начальную позицию"""
		self.screen = screen
		self.ai_settings = ai_settings

		#загрузка изображения и получение прямоугольника
		self.image = pg.image.load("img/cat.bmp")
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()

		#Каждый кот(новая жизнь) появляется внизу по центру
		#центруем по нижней границе поверхность кота относительно
		#поверхности экрана
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom

		#Сохранение вещественной координаты центра кота
		self.center = float(self.rect.centerx)

		#Флаг перемещения кота
		self.moving_right = False
		self.moving_left = False

	def update(self):
		"""Обновляет позицию кота с учетом флага"""
		#Обновляет атрибут center, не rect
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.center += self.ai_settings.cat_speed_factor

		if self.moving_left and self.rect.left > 0:
			self.center -= self.ai_settings.cat_speed_factor

		self.rect.centerx = self.center

	def blitme(self):
		"""Рисует кота в текущей позиции"""
		self.screen.blit(self.image,self.rect)

	def center_cat(self):
		"""Размещает кота в центре нижней стороны"""
		self.center = self.screen_rect.centerx