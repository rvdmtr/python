#game_functions.py

import sys

import pygame as pg
from bullet import Bullet
from alien import Alien

def check_keydown_events(event,ai_settings,screen,ship,bullets):
	"""Реагирует на нажатие клавиш"""
	if event.key == pg.K_RIGHT:
		ship.moving_right = True
	elif event.key == pg.K_LEFT:
		ship.moving_left = True
	elif event.key == pg.K_SPACE:
		fire_bullet(ai_settings,screen,ship,bullets)
		#Создание новой пули и включение ее в группу bullets.
#		if len(bullets) < ai_settings.bullets_allowed:
#			new_bullet = Bullet(ai_settings,screen,ship)
#			bullets.add(new_bullet)
	elif event.key == pg.K_q:
		sys.exit()
		
def fire_bullet(ai_settings,screen,ship,bullets):
	"""Выпускает пулю, если максимум еще не достигнут"""
	#Создание новой пули и включение ее в группу bullets
	if len(bullets) < ai_settings.bullets_allowed:
		new_bullet = Bullet(ai_settings,screen,ship)
		bullets.add(new_bullet)
	



def check_keyup_events(event,ship): 
	"""Реагирует на отпускание клавиш"""
	if event.key == pg.K_RIGHT:
		ship.moving_right = False
	elif event.key == pg.K_LEFT:
		ship.moving_left = False
# если не передадим ship, не сможем изменить флаг движения

def check_events(ai_settings,screen,ship,bullets):
	"""Обрабатывает нажатия клавиш и события мыши"""
	for event in pg.event.get():
		if event.type == pg.QUIT:
			sys.exit()
		elif event.type == pg.KEYDOWN:
			check_keydown_events(event,ai_settings,screen,ship,bullets)
		elif event.type == pg.KEYUP:
			check_keyup_events(event,ship)

# также и здесь, обязательно аргумент ship, дабы была ссылка на нужный объект в функции

def update_screen(ai_settings,screen,ship,aliens,bullets):
	"""Обновляет изображение на экране и отображает новый экран"""
	
	# При каждом проходе цикла перерисовывается экран
	screen.fill(ai_settings.bg_color)

	#Все пули выводятся позади изображений корабля и пришельцев
	for bullet in bullets.sprites():
		bullet.draw_bullet()
		
	ship.blitme()
	aliens.draw(screen)

	# Отображение последнего прорисованного экрана
	pg.display.flip()


def update_bullets(bullets):
	"""Обновляет позиции пуль и уничтожает старые пули."""
	# Обновление позиции пуль.bullet
	bullets.update()

	#Удаление пуль, вышедших за край экрана.
	for bullet in bullets.copy():
		if bullet.rect.bottom <= 0:
			bullets.remove(bullet)


def get_number_aliens_x(ai_settings,alien_width):
	"""Вычисляет количество пришельцев в ряду"""
	available_space_x = ai_settings.screen_width
	number_aliens_x = int(available_space_x / (2 * alien_width))
	return number_aliens_x # возвращает вычисленное значение, для дальнейше передачи


def get_number_rows(ai_settings,alien_height):
	"""Определяет количество рядов, помещающихся на экране"""
	available_space_y = (ai_settings.screen_height - 
		(alien_height))
	number_rows = int(available_space_y / (2 * alien_height))
	return number_rows
	

def create_alien(ai_settings,screen,aliens,alien_number,row_number):
	"""Создает пришельца и размещает его в ряду"""
	alien = Alien(ai_settings,screen)
	alien_width = alien.rect.width# для опред ширины использ созданный выше экземпляр
	alien.x = alien_width + 2 * alien_width * alien_number
	#alien.x координата отрисовки следующего экземпляра в завимисости от alien_number
	alien.rect.x = alien.x #видимо .х это внутренний атрибут метода rect
	alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
	aliens.add(alien)
	


def create_fleet(ai_settings,screen,ship,aliens):
	"""Создает флот пришельцев"""
	# Создание пришельца и вычисление количества пришельцев в ряду.
	alien = Alien(ai_settings,screen)# Обязательно создание экземпляра
	# для передачи его значения атри`бута ширины в качестве alien_width 
	number_aliens_x = get_number_aliens_x(ai_settings,alien.rect.width)
	number_rows = get_number_rows(ai_settings,alien.rect.height)

	# Создание п(ервого ряда пришельцев.
	for row_number in range(number_rows):
		for alien_number in range(number_aliens_x):
			#Создание пришельца и размещение его в ряду.
	#	create_alien(ai_settings,screen,aliens,alien_number,row_number)
			create_alien(ai_settings,screen,aliens,alien_number,row_number)


def check_fleet_edges(ai_settings,aliens):
	"""Реагирует на достижение пришельцем края экрана."""
	for alien in aliens.sprites():
		if alien.check_edges():
			change_fleet_direction(ai_settings,aliens)
			break

def change_fleet_direction(ai_settings,aliens):
	"""Опускает весь флот и меняет направление флота."""
	for alien in aliens.sprites():
		alien.rect.y += ai_settings.fleet_drop_speed
	ai_settings.fleet_direction *= (-1)


def update_aliens(ai_settings,aliens):
	"""Проверяет, достиг ли флот края экрана,
	после чего обновляет позиции всех пришельцев во флоте"""
	check_fleet_edges(ai_settings,aliens)
	aliens.update()
# используется метод update для ГРУППЫ aliens, что приводит к автоматическому
# вызову метода update каждого пришельца alien
