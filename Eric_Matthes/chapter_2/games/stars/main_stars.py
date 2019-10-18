
#import sys # импортируем данный модул в модуле gf
import pygame as pg
from pygame.sprite import Sprite

from settings import Settings
from star import Star
#from alien import Alien
import game_functions as gf






###-----Основная функция игры - определение функции
def run_game():
	# Инициализирует игру и создает объект экрана.
	pg.init()
	
	pg.display.set_caption('Stars')
	ai_settings = Settings() # присвоение объекта
	#назначение параметров экрана
	screen = pg.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))	
	# Создание звезды
	star = Star(ai_settings,screen)
	stars = pg.sprite.Group()

	# Создание групы звезд, группы - передаем функции пустую группу
	gf.create_stars(ai_settings,screen,stars)

	# Запуск основного цикла игры
	while True:
		gf.check_events(ai_settings,screen)
		#Проверяет Основной ввод от игрока 

		gf.update_screen(ai_settings,screen,stars)


### ---------- Запуск основной функции игры
	
run_game()


