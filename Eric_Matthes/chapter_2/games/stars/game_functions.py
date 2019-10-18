#game_functions.py

import sys

import pygame as pg

from star import Star
from random import randint

def check_keydown_events(event):
	"""Реагирует на нажатие клавиш"""
	if event.key == pg.K_q:
		sys.exit()
		

def check_events(ai_settings,screen):
	"""Обрабатывает нажатия клавиш и события мыши"""
	for event in pg.event.get():
		if event.type == pg.QUIT:
			sys.exit()
		elif event.type == pg.KEYDOWN:
			check_keydown_events(event)
		
def update_screen(ai_settings,screen,stars):
	"""Обновляет изображение на экране и отображает новый экран"""
	
	# При каждом проходе цикла перерисовывается экран
	screen.fill(ai_settings.bg_color)

	#Все пули выводятся позади изображений корабля и пришельцев
	stars.draw(screen)

	# Отображение последнего прорисованного экрана
	pg.display.flip()


def get_number_stars_x(ai_settings,star_width):
	"""Вычисляет количество пришельцев в ряду"""
	available_space_x = ai_settings.screen_width
	number_stars_x = int(available_space_x / (star_width))
	return number_stars_x # возвращает вычисленное значение, для дальнейше передачи


def get_number_rows(ai_settings,star_height):
	"""Определяет количество рядов, помещающихся на экране"""
	available_space_y = (ai_settings.screen_height - (2 * star_height))
	number_rows = int(available_space_y / (2 * star_height))
	return number_rows
	

def create_star(ai_settings,screen,stars,star_number,row_number,rn):
	"""Создает звезду и размещает её в ряду"""
	star = Star(ai_settings,screen)
	star_width = star.rect.width# для опред ширины использ созданный выше экземпляр
	star.x = star_width + 2 * star_width * star_number + rn
	#star.x координата отрисовки следующего экземпляра в завимисости от star_number
	star.rect.x = star.x #видимо .х это внутренний атрибут метода rect
	star.rect.y = star.rect.height + 2 * star.rect.height * row_number
	stars.add(star)
	


def create_stars(ai_settings,screen,stars):
	"""Создает флот пришельцев"""
	# Создание пришельца и вычисление количества пришельцев в ряду.
	star = Star(ai_settings,screen)# Обязательно создание экземпляра
	# для передачи его значения атри`бута ширины в качестве alien_width 
	number_stars_x = get_number_stars_x(ai_settings,star.rect.width)
	number_rows = get_number_rows(ai_settings,star.rect.height)

	# Создание первого ряда звезд
	for row_number in range(number_rows):
		for star_number in range(number_stars_x):
			rn = randint(-30,40)
	#Создание пришельца и размещение его в ряду.
	#	create_alien(ai_settings,screen,aliens,alien_number,row_number)
			create_star(ai_settings,screen,stars,star_number,row_number,rn)


