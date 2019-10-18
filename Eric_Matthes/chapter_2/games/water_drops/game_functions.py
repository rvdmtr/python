#game_functions.py

import sys

import pygame as pg
#import settings as se

from drop import Drop
from random import randint

def check_keydown_events(event):
	"""Реагирует на нажатие клавиш"""
	if event.key == pg.K_q:
		sys.exit()

def born_drop(ai_settings,screen,drops):
	"""Рождение новой капли"""
	if len(drops) < 20:
		new_drop = Drop(ai_settings,screen)
		create_drop(ai_settings,screen,drops,randint(0,5),randint(0,4))
		#drops.add(new_drop)

def check_events():
	"""Обрабатывает нажатия клавиш и события мыши"""
	for event in pg.event.get():
		if event.type == pg.QUIT:
			sys.exit()
		elif event.type == pg.KEYDOWN:
			check_keydown_events(event)

def update_screen(ai_settings,screen,drops):
	"""Обновляет изображеие на экране и отображает новый экран"""
	screen.fill(ai_settings.bg_color)
	drops.draw(screen)
	pg.display.flip()

def rem_drops(ai_settings,drops):
	"""Удаляет капли при выходе их за нижнюю границу экрана"""
	drops.update()
	#screen_rect = screen.get_rect()

	for drop in drops.copy():
		if drop.rect.bottom >= ai_settings.screen_height + 40:
			drops.remove(drop)


def get_number_drops_x(ai_settings,drop_width):
	"""Вычисляет количество капель в ряду"""
	available_space_x = ai_settings.screen_width - 2 * drop_width
	number_drops_x = int((available_space_x) / (2 * drop_width))
	return number_drops_x


def  get_number_rows(ai_settings,drop_height):
	"""Определяет количество рядов, помещающихся на экране"""
	#available_space_y = ai_settings.screen_height - (2 * drop_height)
	available_space_y = ai_settings.screen_height - (2 * drop_height)
	number_rows = int(available_space_y / (2*drop_height))
	return number_rows


def create_drop(ai_settings,screen,drops,drop_number,row_number):
	"""Создает каплю и размещает ее в ряду"""
	drop = Drop(ai_settings,screen)
	drop_width = drop.rect.width # опред ширину капли, созданной из класса выше
	drop.x = 2*randint(drop_width,60)*drop_number#drop_width + 2 * drop_width * drop_number
	#drop.x координата отрисовки следующего экземпляра в завимисости от drop_number
	drop.rect.x = drop.x
	
	drop.y = -2*drop.rect.height + (2 * drop.rect.height * row_number)
	drop.rect.y = drop.y
	drops.add(drop)


def create_fleet(ai_settings,screen,drops):
	"""Создает сетку из капель"""
	#создание капли и вычисление количества кап в ряду
	drop = Drop(ai_settings,screen)
	number_drops_x = get_number_drops_x(ai_settings,drop.rect.width)
	number_rows = get_number_rows(ai_settings,drop.rect.height)
	#Создание первого ряда капель
	for row_number in range(number_rows):
		#for drop_number in range(0,number_drops_x,2):#вместо 2 рандом проставь
		for drop_number in range(0,number_drops_x,randint(1,number_drops_x)):
			create_drop(ai_settings,screen,drops,drop_number,row_number)
	print(number_rows)
	print(number_drops_x)

def update_drops(ai_settings,drops):
	drops.update()

# используется метод update для ГРУППЫ drops, что приводит к автоматическому
# вызову метода update каждой капли
