#plane.py

import pygame as pg

class Plane():
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
		self.rect.centery = self.screen_rect.centery
		self.rect.left = self.screen_rect.left

		# Сохранение вещественной координаты центра корабля
		self.center = float(self.rect.centery)

		# Флаг перемещения 
		self.moving_up = False
		self.moving_down = False

	def update(self):
		"""Обновляет позицию корабля с учетом флага."""
		# Обновляет атрибут center, не rect
		if self.moving_up and self.rect.top > self.screen_rect.top:
			self.center -= self.ai_settings.plane_speed_factor
			#self.rect.centerx +=1

		if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
			self.center += self.ai_settings.plane_speed_factor
			#self.rect.centerx -=1

			# Обновление атрибута rect на основании self.center
		self.rect.centery = self.center

	def blitme(self):
		"""Рисует корабль в текущей позиции"""
		self.screen.blit(self.image,self.rect)

	def center_plane(self):
		"""Размещает корабль в центре левой стороны экрана"""
		self.center = self.screen_rect.centery
