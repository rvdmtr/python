import pygame as pg

class Rocket():
	def __init__(self,ai_settings,screen):
		self.screen = screen 
		#переданные параметры экрана из модуля игры из settings в экземпляр ракеты

		self.ai_settings = ai_settings 
		# переданные настройки скорость, экран из модуля игры в атрибут экземпляра

		self.image = pg.image.load('img/ship.bmp')
		# Переводим поверхности в прямоугольники
		self.rect = self.image.get_rect() # поверхность рисунка
		self.screen_rect = screen.get_rect() # поверхность самого экрана

		# Центруем поверхность персонажа относительно экрана
		self.rect.centerx = self.screen_rect.centerx # рисунок в центре экрана на х
		self.rect.centery = self.screen_rect.centery # рисунок в центре экрана на у

		# Сохранение вещественной координаты центра корабля
		self.centerx = float(self.rect.centerx) # чтобы можно было перемещаться
		self.centery = float(self.rect.centery) # на дробные числа

		# Флаг перемещения	
		self.moving_right = False
		self.moving_left  = False
		self.moving_up = False
		self.moving_down = False

	def update(self):
		"""Обновляет позицию корабля с учетом флага."""
		# Обновляет атрибут centerx, не rect
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.centerx += self.ai_settings.rocket_speed_factor #ссылка на число перемещения

		if self.moving_left and self.rect.left > 0:
			self.centerx -= self.ai_settings.rocket_speed_factor

		if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
			self.centery += self.ai_settings.rocket_speed_factor

		if self.moving_up and self.rect.top > 0:
			self.centery -= self.ai_settings.rocket_speed_factor

		# Обновление атрибута rect на основании self.center
		self.rect.centerx = self.centerx #нажали клавишу-координата сохранилась
		self.rect.centery = self.centery
		# без данных инструкций, корабль не сдвинется с места

	def blitme(self):
		"""Вывод на экран изображения"""
		self.screen.blit(self.image,self.rect)

