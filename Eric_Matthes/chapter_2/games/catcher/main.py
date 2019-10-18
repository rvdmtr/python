#space - start the catcher game
#when you catch the ball three times, the game is over
#q - quit

#main.py
import sys

import pygame as pg 
import pygame.sprite as Sprite

from settings import Settings
from cat import Cat
from ball import Ball
from game_stats import GameStats

import game_functions as  gf



def run_game():
	"""Инициализирует игру и создает объект экрана"""
	pg.init()

	pg.display.set_caption('ball catcher')
	ai_settings = Settings()# присвоение объекта
	stats = GameStats(ai_settings)

	#назначение параметров экрана
	screen = pg.display.set_mode((ai_settings.screen_width,
		ai_settings.screen_height))

	#cats = pg.sprite.Group()
	balls = pg.sprite.Group()

	cat = Cat(ai_settings,screen)
	
	#gf.create_ball(ai_settings,screen)
	ball = Ball(ai_settings,screen)


	while True:
		gf.check_events(ai_settings,screen,cat,balls)#проверка ввода от игрока

		#ball.update(ai_settings,ball)#обновляет позицию кота на основании ввода игрока
		
		cat.update()
		#ball.update()
		gf.update_balls(ai_settings,screen,stats,cat,balls)
		gf.update_screen(ai_settings,screen,cat,balls)


### ---------- Запуск основной функции игры
	
run_game()