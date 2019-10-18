#vertical_game.py

#import sys # импортируем данный модул в модуле gf
import pygame as pg
from pygame.sprite import Sprite

from settings import Settings
from plane import Plane
import functions as f
from game_stats import GameStats 
from button import Button


###-----Основная функция игры - определение функции
def run_game():
	# Инициализирует игру и создает объект экрана.
	pg.init()
	
	pg.display.set_caption('vertical_game')
	ai_settings = Settings() # присвоение объекта
	stats = GameStats(ai_settings)


	#назначение параметров экрана
	screen = pg.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))	
	
	play_button = Button(ai_settings,screen,"GO!")
	# Создание корабля
	plane = Plane(ai_settings,screen)
	#Создание группы
	missles = pg.sprite.Group()
	aliens = pg.sprite.Group()
	button_clicked = False
	cnt = 0

	f.create_fleet(ai_settings,screen,plane,aliens)

	# Запуск основного цикла игры
	while True:
		f.check_events(ai_settings,screen,stats,play_button,plane,aliens,missles,button_clicked)
		#Проверяет Основной ввод от игрока 
		if stats.game_active:
			plane.update()# цикл обновляет позицию корабля на основании ввода игрока

			f.update_missles(ai_settings,screen,stats,play_button,plane,aliens,missles,cnt)#обновление позиции всех выпущенных пуль
			
			#print(len(missles)) #отобразить количество неудаленных пуль
			f.update_aliens(ai_settings,stats,screen,plane,aliens,missles)

			f.update_screen(ai_settings,screen,stats,plane,aliens,missles,play_button)
			#Обновленные позиции игровых элементов используются для вывода нового
			# экрана 
		else:
			#screen.fill(ai_settings.bg_color)
			f.update_screen(ai_settings,screen,stats,plane,aliens,missles,play_button)
			play_button.draw_button()

		#print(cnt)


### ---------- Запуск основной функции игры
	
run_game()


