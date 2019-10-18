
#import sys # импортируем данный модул в модуле gf
import pygame as pg
from pygame.sprite import Sprite

from settings import Settings
from ship import Ship
#from alien import Alien
import game_functions as gf


###-----Основная функция игры - определение функции
def run_game():
	# Инициализирует игру и создает объект экрана.
	pg.init()
	
	pg.display.set_caption('Water drops')
	ai_settings = Settings() # присвоение объекта
	#назначение параметров экрана
	screen = pg.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))	
	# Создание корабля
	ship = Ship(ai_settings,screen)

	# Создание пришельца
	#alien = Alien(ai_settings,screen)

	#Создание пустой группы элементов
	bullets = pg.sprite.Group()
	aliens = pg.sprite.Group()

	# Создание флота пришельцев, группы - передаем функции пустую группу
	gf.create_fleet(ai_settings,screen,ship,aliens)

	# Запуск основного цикла игры
	while True:
		gf.check_events(ai_settings,screen,ship,bullets)
		#Проверяет Основной ввод от игрока 

		ship.update()# цикл обновляет позицию корабля на основании ввода игрока

		gf.update_bullets(bullets)#обновление позиции всех выпущенных пуль
		#print(len(bullets)) #отобразить количество неудаленных пуль

		gf.update_aliens(ai_settings,aliens)

		gf.update_screen(ai_settings,screen,ship,aliens,bullets)
		#Обновленные позиции игровых элементов используются для вывода нового
		# экрана 


### ---------- Запуск основной функции игры
	
run_game()


