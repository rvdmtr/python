#main.py
import sys

import pygame as pg 
import pygame.sprite as Sprite

from settings import Settings
import game_functions as  gf



def run_game():
	"""Инициализирует игру и создает объект экрана"""
	pg.init()

	pg.display.set_caption('water drops')
	ai_settings = Settings()# присвоение объекта

	#назначение параметров экрана
	screen = pg.display.set_mode((ai_settings.screen_width,
		ai_settings.screen_height))

	#Создание пустой группы капель
	drops = pg.sprite.Group()

	# Создание сетки капель, группы - передаем функции пустую группу
	gf.create_fleet(ai_settings,screen,drops)

	while True:
		gf.check_events()#проверка ввода от игрока

		gf.born_drop(ai_settings,screen,drops)

		gf.rem_drops(ai_settings,drops)

		gf.update_drops(ai_settings,drops)
		#print(len(drops))
		gf.update_screen(ai_settings,screen,drops)


### ---------- Запуск основной функции игры
	
run_game()