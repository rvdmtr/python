#button.py

import pygame as pg


class Button():

	def __init__(self,ai_settings,screen,msg):
		"""Инициализирует атрибуты кнопки."""
		self.screen = screen
		self.screen_rect = screen.get_rect()
	
		# Назначение размеров и свойств кнопок.
		self.width, self.height = 200, 50
		self.button_color = (20, 120, 170)
		self.text_color = (255, 255, 250)
		self.font = pg.font.SysFont(None, 48)
	
		#Построение объекта rect кнопки и выравнивание по центру экрана
		self.rect = pg.Rect(50,50,self.width,self.height)
		self.rect.center = self.screen_rect.center

		self.mes = msg
	
		# Сообщение кнопки создается только один раз.
		self.prep_msg(msg)

	def prep_msg(self,msg):
		"""Преобразует msg в прямоугольник и выравнивает текст по центру"""
		self.msg_image = self.font.render(msg,True,self.text_color,self.button_color)
		self.msg_image_rect = self.msg_image.get_rect()
		self.msg_image_rect.center = self.rect.center

	def draw_button(self):
		"""Отображение пустой кнопки и вывод сообщения"""
		self.screen.fill(self.button_color,self.rect)
		self.screen.blit(self.msg_image,self.msg_image_rect)