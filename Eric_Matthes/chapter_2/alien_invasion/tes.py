import pygame as pg

from tes_settings import Settings
from rocket import Rocket
import tes_func as tf


def run_game():
	# Инициализирует игру и создает объект экрана.
	pg.init()
	#screen = pg.display.set_mode((600,400))
	pg.display.set_caption('Tes Invasion')
	ai_settings = Settings() # присвоение объекта
	#назначение параметров экрана
	screen = pg.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))	
	# Создание корабля
	rocket = Rocket(ai_settings,screen)

	while True:
		#for event in pg.event.get():
		#	if event.type == pg.QUIT:
		#		sys.exit()
		tf.check_events(rocket)
		rocket.update()
		tf.update_screen(ai_settings,screen,rocket)
#screen.fill(bg_color)
#pg.display.flip()
run_game()
