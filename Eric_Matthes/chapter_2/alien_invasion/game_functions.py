#game_functions.py

import sys

import pygame as pg
import game_stats as gs

from bullet import Bullet
from alien import Alien

from time import sleep



def check_keydown_events(event,ai_settings,screen,stats,sb,play_button,ship,aliens,bullets,button_clicked,filename):
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
	elif event.key == pg.K_p:
		button_clicked = True
		start_game(ai_settings,screen,stats,sb,play_button,ship,aliens,bullets,button_clicked,filename)	
	elif event.key == pg.K_q:
		write_record(filename,stats)
		sys.exit()

def write_record(filename,stats):
	"""Записывает рекорд в файл history record"""
	#filename = history_record.txt
	with open(filename, 'w') as file_object:
		file_object.write(str(stats.high_score))

def read_record(filename,stats):
	with open(filename, 'r') as file_object:
		hist_rec = file_object.read()
		stats.high_score = int(hist_rec)
		print(hist_rec)

		
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

def check_events(ai_settings,screen,stats,sb,play_button,ship,aliens,bullets,button_clicked,filename):
	"""Обрабатывает нажатия клавиш и события мыши"""
	for event in pg.event.get():
		if event.type == pg.QUIT:
			write_record(stats)
			sys.exit()
		elif event.type == pg.KEYDOWN:
			check_keydown_events(event,ai_settings,screen,stats,sb,play_button,ship,aliens,bullets,button_clicked,filename)

		elif event.type == pg.KEYUP:
			check_keyup_events(event,ship)
		elif event.type == pg.MOUSEBUTTONDOWN:
			mouse_x, mouse_y = pg.mouse.get_pos()
			check_play_button(ai_settings,screen,stats,sb,play_button,ship,aliens,bullets,mouse_x,mouse_y)

def check_play_button(ai_settings,screen,stats,sb,play_button,ship,aliens,bullets,mouse_x,mouse_y):
	"""Запускает новую игру при нажатии кнопки Play"""
	button_clicked = play_button.rect.collidepoint(mouse_x,mouse_y)
	start_game(ai_settings,screen,stats,sb,play_button,ship,aliens,bullets,button_clicked)

def start_game(ai_settings,screen,stats,sb,play_button,ship,aliens,bullets,button_clicked,filename):
    
	if button_clicked and not stats.game_active:
		# Сброс игровых настроек.
		ai_settings.initialize_dynamic_settings()

		#Считываем предыдущий рекорд
		read_record(filename,stats)

		# Указатель мыши скрывается
		pg.mouse.set_visible(False)

		# Сброс игровой статистики
		stats.reset_stats()
		stats.game_active = True

		# Сброс изображений счетов и уровня.
		#sb.prep_score()
		#sb.prep_high_score()
		#sb.prep_level()
		#sb.prep_ships()
		sb.prep_images()

		#Очистка списков пришельцев и пуль
		aliens.empty()
		bullets.empty()

		# Создание нового флота и размещение корабля в центре.
		create_fleet(ai_settings,screen,ship,aliens)
		ship.center_ship()

def update_screen(ai_settings,screen,stats,sb,ship,aliens,bullets,play_button):
	"""Обновляет изображение на экране и отображает новый экран"""
	
	# При каждом проходе цикла перерисовывается экран
	screen.fill(ai_settings.bg_color)

	#Все пули выводятся позади изображений корабля и пришельцев
	for bullet in bullets.sprites():
		bullet.draw_bullet()
		
	ship.blitme()
	aliens.draw(screen)

	# Вывод счета
	sb.show_score()

	# Кнопка Play отображается, если игра неактивна
	if not stats.game_active:
		play_button.draw_button()

	# Отображение последнего прорисованного экрана
	pg.display.flip()

def check_bullet_alien_collision(ai_settings,screen,stats,sb,ship,aliens,bullets):
		"""Обработка коллизий пуль с пришельцами."""
	#проверка попаданий в пришельцев.
	#при обнаружении попадания(коллизия) - удалить пулю и пришельца
		collisions = pg.sprite.groupcollide(bullets,aliens,True,True)

		if collisions:
				for aliens in collisions.values():
					stats.score += ai_settings.alien_points * len(aliens)
					sb.prep_score()
					check_high_score(stats,sb)

		start_new_level(aliens,ai_settings,screen,stats,sb,ship,bullets)



def start_new_level(aliens,ai_settings,screen,stats,sb,ship,bullets):
	"""Старт нового уровня""" 
	if len(aliens) == 0:
		#Проверка группы aliens и создание нового флота
		bullets.empty()
		ai_settings.increase_speed()
		#Увеличение уровня
		stats.level += 1
		sb.prep_level()
		create_fleet(ai_settings,screen,ship,aliens)
	

def check_high_score(stats,sb):
	"""Проверяет, появился ли новый рекорд"""
	if stats.score > stats.high_score:
		stats.high_score = stats.score
		sb.prep_high_score()


def update_bullets(ai_settings,screen,stats,sb,ship,aliens,bullets):
	"""Обновляет позиции пуль и уничтожает старые пули."""
	# Обновление позиции пуль.bullet
	bullets.update()

	#Удаление пуль, вышедших за край экрана.
	for bullet in bullets.copy():
		if bullet.rect.bottom <= 0:
			bullets.remove(bullet)
	check_bullet_alien_collision(ai_settings,screen,stats,sb,ship,aliens,bullets)



def get_number_aliens_x(ai_settings,alien_width):
	"""Вычисляет количество пришельцев в ряду"""
	available_space_x = ai_settings.screen_width - 2 * alien_width
	number_aliens_x = int(available_space_x / (2 * alien_width))
	return number_aliens_x # возвращает вычисленное значение, для дальнейше передачи


def get_number_rows(ai_settings,ship_height,alien_height):
	"""Определяет количество рядов, помещающихся на экране"""
	available_space_y = (ai_settings.screen_height - 
		(3 * alien_height) - ship_height)
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
	# для передачи его значения атрибута ширины в качестве alien_width 
	number_aliens_x = get_number_aliens_x(ai_settings,alien.rect.width)
	number_rows = get_number_rows(ai_settings,ship.rect.height,alien.rect.height)

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

def ship_hit(ai_settings,screen,stats,sb,ship,aliens,bullets):
	"""Обрабатывает столкновени корабля с пришельцем"""
	
	if stats.ship_left > 0:
		# Уменьшение ships_left
		stats.ship_left -=1

		# Обновление игровой информации
		sb.prep_ships()

		# Очистка списков пришельцев и пуль.
		aliens.empty()
		bullets.empty()

		# Создание нового флота и размещение корабля в центре.
		create_fleet(ai_settings,screen,ship,aliens)
		ship.center_ship()
	
		# Пауза
		sleep(0.5)
	else:
		stats.game_active = False 
		pg.mouse.set_visible(True)

def check_aliens_bottom(ai_settings,screen,stats,sb,ship,aliens,bullets):
	"""Проверяет, добрались ли пришельцы до нижнего края экрана."""
	screen_rect = screen.get_rect()
	for alien in aliens.sprites():
		if alien.rect.bottom >= screen_rect.bottom:
			# Происходит то же, что при столкновении с кораблем
			ship_hit(ai_settings,screen,stats,sb,ship,aliens,bullets)
			break

def update_aliens(ai_settings,screen,stats,sb,ship,aliens,bullets):
	"""Проверяет, достиг ли флот края экрана,
	после чего обновляет позиции всех пришельцев во флоте"""
	check_aliens_bottom(ai_settings,screen,stats,sb,ship,aliens,bullets)
	check_fleet_edges(ai_settings,aliens)
	aliens.update()
# используется метод update для ГРУППЫ aliens, что приводит к автоматическому
# вызову метода update каждого пришельца alien
	
	#Проверка коллизий "пришелец-корабль"
	if pg.sprite.spritecollideany(ship,aliens):
		#print("Ship hit!!!")
		ship_hit(ai_settings,screen,stats,sb,ship,aliens,bullets)


