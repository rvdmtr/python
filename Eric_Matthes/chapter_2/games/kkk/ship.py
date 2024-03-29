#ship.py

import pygame as pg

class Ship():
	def __init__(self,ai_settings,screen):
		"""Инициализирует корабль и задает его начальную позицию"""
		self.screen = screen #здесь он появляется в токче координат экрана?
		self.ai_settings = ai_settings

		#Загрузка изображения корабля и получение прямоугольника
		self.image = pg.image.load("img/ship.bmp")
		self.rect = self.image.get_rect()#преобразование поверхности в прямоугольник
		self.screen_rect = screen.get_rect()
		#Каждый новый корабль(жизнь) появляется у нижнего края экрана
		# Центруем по нижней границе "поверхность" корабля относительно
		# поверхности экрана
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom

		# Сохранение вещественной координаты центра корабля
		self.center = float(self.rect.centerx)

		# Флаг перемещения 
		self.moving_right = False
		self.moving_left = False

	def update(self):
		"""Обновляет позицию корабля с учетом флага."""
		# Обновляет атрибут center, не rect
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.center += self.ai_settings.ship_speed_factor
			#self.rect.centerx +=1

		if self.moving_left and self.rect.left > 0:
			self.center -= self.ai_settings.ship_speed_factor
			#self.rect.centerx -=1

			# Обновление атрибута rect на основании self.cebter
		self.rect.centerx = self.center

	def blitme(self):
		"""Рисует корабль в текущей позиции"""
		self.screen.blit(self.image,self.rect)
