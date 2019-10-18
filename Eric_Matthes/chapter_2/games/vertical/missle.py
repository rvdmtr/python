#missle.py

import pygame as pg
from pygame.sprite import Sprite

class Missle(Sprite):
	"""Класс для управления пулями, выпущенными кораблем."""
	def __init__(self,ai_settings,screen,plane):
		"""Создает объект пули в текущей позиции корабля."""
		super(Missle,self).__init__() # super().__init__
		self.screen = screen 

		#Создание пули в позиции (0,0) и назначение правильной позиции.
		self.rect = pg.Rect(0,0,ai_settings.missle_width,ai_settings.missle_height)
		self.rect.centery = plane.rect.centery
		self.rect.right = plane.rect.right

		#Позиция пули хранится в вещественном формате
		self.x = float(self.rect.x)

		self.color = ai_settings.missle_color
		self.speed_factor = ai_settings.missle_speed_factor

	def update(self):
		"""Перемещает пулю по экрану."""
		#Обновление позиции пули в вещественном формате.centerx
		self.x += self.speed_factor

		#Обновление позиции прямоуглоьника.
		self.rect.x = self.x

	def draw_missle(self):
		"""Вывод пули на экран"""
		pg.draw.rect(self.screen,self.color,self.rect)
