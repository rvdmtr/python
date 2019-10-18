
#import sys # импортируем данный модул в модуле gf
import pygame as pg
from pygame.sprite import Sprite

from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard

from button import Button
from ship import Ship
#from alien import Alien
import game_functions as gf


###-----Основная функция игры - определение функции
def run_game():
	# Инициализирует игру и создает объект экрана.
	pg.init()
	pg.display.set_caption('Alien Invasion')
	ai_settings = Settings() # присвоение объекта

	#назначение параметров экрана
	screen = pg.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
	#Создание экземляра для хранения игровой статистики и счета
	stats = GameStats(ai_settings)
	sb = Scoreboard(ai_settings,screen,stats)
	#Создание кнопки Play
	play_button = Button(ai_settings,screen,"Play")
	# Создание корабля
	ship = Ship(ai_settings,screen)
	# Создание пришельца
	#alien = Alien(ai_settings,screen)
	#Создание пустой группы элементов
	bullets = pg.sprite.Group()
	aliens = pg.sprite.Group()
	button_clicked = False

	filename = 'history_record.txt'

	# Создание флота пришельцев, группы - передаем функции пустую группу
	gf.create_fleet(ai_settings,screen,ship,aliens)
	# Запуск основного цикла игры
	while True:
		gf.check_events(ai_settings,screen,stats,sb,play_button,ship,aliens,bullets,button_clicked,filename)
		#Проверяет Основной ввод от игрока 
		if stats.game_active:
			ship.update()# цикл обновляет позицию корабля на основании ввода игрока
			gf.update_bullets(ai_settings,screen,stats,sb,ship,aliens,bullets)#обновление позиции всех выпущенных пуль
			#print(len(bullets)) #отобразить количество неудаленных пуль
			gf.update_aliens(ai_settings,screen,stats,sb,ship,aliens,bullets)
			gf.update_screen(ai_settings,screen,stats,sb,ship,aliens,bullets,play_button)
			#Обновленные позиции игровых элементов используются для вывода нового
			# экрана 
		else:
			screen.fill(ai_settings.bg_color)
			gf.update_screen(ai_settings,screen,stats,sb,ship,aliens,bullets,play_button)
		#	print(play_button.mes)
			play_button.draw_button()




### ---------- Запуск основной функции игры
	
run_game()

#read_record(filename,stats)

