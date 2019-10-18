#game_functions.py

import sys

import pygame as pg

def check_keydown_events(event,rocket):
	"""Реагирует на нажатие клавиш"""
	if event.key == pg.K_RIGHT:
		rocket.moving_right = True
	elif event.key == pg.K_LEFT:
		rocket.moving_left = True
	elif event.key == pg.K_UP:
		rocket.moving_up = True
	elif event.key == pg.K_DOWN:
		rocket.moving_down = True


def check_keyup_events(event,rocket):
	"""Реагирует на отпускание клавиш"""
	if event.key == pg.K_RIGHT:
		rocket.moving_right = False
	elif event.key == pg.K_LEFT:
		rocket.moving_left = False
	elif event.key == pg.K_UP:
		rocket.moving_up = False
	elif event.key == pg.K_DOWN:
		rocket.moving_down = False

def check_events(rocket):
	"""Обрабатывает нажатия клавиш и события мыши"""
	for event in pg.event.get():
		if event.type == pg.QUIT:
			sys.exit()
		elif event.type == pg.KEYDOWN:
			check_keydown_events(event,rocket)

		elif event.type == pg.KEYUP:
			check_keyup_events(event,rocket)


def update_screen(ai_settings,screen,rocket):
	"""Обновляет изображение на экране и отображает новый экран"""
	# При каждом проходе цикла перерисовывается экран
	screen.fill(ai_settings.bg_color)
	rocket.blitme()

	# Отображение последнего прорисованного экрана
	pg.display.flip()