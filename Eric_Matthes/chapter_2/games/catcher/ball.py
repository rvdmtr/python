
import pygame as pg 
from pygame.sprite import Sprite
from random import randint
from cat import Cat

class Ball(Sprite):
	"""Класс, представляющий одну каплю"""
	def __init__(self,ai_settings,screen):
		super(Ball,self).__init__()
		self.screen = screen
		self.ai_settings = ai_settings

		# Загрузка изображения капли и назначение
		# атрибута rect
		self.image = pg.image.load("img/ball.bmp")
		self.rect = self.image.get_rect()

		# каждая новая капля появляется в левом верхнем углу экрана
		self.rect.x = randint(0,self.ai_settings.screen_width - 40)#self.rect.width
		self.rect.y = self.rect.height - 40

		# Сохранение точной позиции
		self.x = float(self.rect.x)
		self.y = float(self.rect.y)

		self.color = ai_settings.ball_color

	#def blitme(self):
	#	"""Выводит каплю в текущем положении"""
	#	self.screen.blit(self.image,self.rect)

	def draw_ball(self):
		pg.draw.rect(self.screen,self.color,self.rect)

	def update(self):
		"""Перемещает мяч вниз"""
		self.y += (self.ai_settings.ball_speed_factor)
		self.rect.y = self.y




