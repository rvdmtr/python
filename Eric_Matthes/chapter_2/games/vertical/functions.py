#functions.py

import sys

import pygame as pg
import game_stats as game_stats

from missle import Missle

from alien import Alien


from time import sleep


def check_keydown_events(event,ai_settings,screen,plane,missles):
	"""Реагирует на нажатие клавиш"""
	if event.key == pg.K_UP:
		plane.moving_up = True
	elif event.key == pg.K_DOWN:
		plane.moving_down = True
	elif event.key == pg.K_SPACE:
		fire_missle(ai_settings,screen,plane,missles)
		#Создание новой пули и включение ее в группу missles.
#		if len(missles) < ai_settings.missles_allowed:
#			new_missle = missle(ai_settings,screen,plane)
#			missles.add(new_missle)
	elif event.key == pg.K_q:
		sys.exit()
	#elif event.key == pg.K_p:
		#button_clicked == True

		
def fire_missle(ai_settings,screen,plane,missles):
	"""Выпускает пулю, если максимум еще не достигнут"""
	#Создание новой пули и включение ее в группу missles
	if len(missles) < ai_settings.missles_allowed:
		new_missle = Missle(ai_settings,screen,plane)
		missles.add(new_missle)
	



def check_keyup_events(event,plane): 
	"""Реагирует на отпускание клавиш"""
	if event.key == pg.K_UP:
		plane.moving_up = False
	elif event.key == pg.K_DOWN:
		plane.moving_down = False
# если не передадим plane, не сможем изменить флаг движения

def check_events(ai_settings,screen,stats,play_button,plane,aliens,missles,button_clicked):
	"""Обрабатывает нажатия клавиш и события мыши"""
	for event in pg.event.get():
		if event.type == pg.QUIT:
			sys.exit()
		elif event.type == pg.KEYDOWN:
			check_keydown_events(event,ai_settings,screen,plane,missles)
		elif event.type == pg.KEYUP:
			check_keyup_events(event,plane)
		elif event.type == pg.MOUSEBUTTONDOWN:
			mouse_x,mouse_y = pg.mouse.get_pos()
			check_play_button(ai_settings,screen,stats,play_button,plane,aliens,missles,mouse_x,mouse_y)

# также и здесь, обязательно аргумент plane, дабы была ссылка на нужный объект в функции

def check_play_button(ai_settings,screen,stats,play_button,plane,aliens,missles,mouse_x,mouse_y):
	"""Начать новую игру при нажатии кнопки Play"""
	button_clicked = play_button.rect.collidepoint(mouse_x,mouse_y)
	start_game(ai_settings,screen,stats,play_button,plane,aliens,missles,button_clicked)

def start_game(ai_settings,screen,stats,play_button,plane,aliens,missles,button_clicked):

	if button_clicked and not stats.game_active:
		# Сброс скорости 
		ai_settings.initialize_dynamic_settings()
		pg.mouse.set_visible(False)
		stats.reset_stats()
		stats.game_active = True
		aliens.empty()
		missles.empty()

		create_fleet(ai_settings,screen,plane,aliens)
		plane.center_plane()

def update_screen(ai_settings,screen,stats,plane,aliens,missles,play_button):
	"""Обновляет изображение на экране и отображает новый экран"""
	
	# При каждом проходе цикла перерисовывается экран
	screen.fill(ai_settings.bg_color)

	#Все пули выводятся позади изображений корабля и пришельцев
	for missle in missles.sprites():
		missle.draw_missle()
		
	plane.blitme()
	aliens.draw(screen)

	if not stats.game_active:
		play_button.draw_button()

	# Отображение последнего прорисованного экрана
	pg.display.flip()

def check_missle_alien_collision(ai_settings,screen,plane,aliens,missles):
	"""Обработка коллизий пуль с пришельцами"""
	collisions = pg.sprite.groupcollide(missles,aliens,True,True)

	if len(aliens) == 0:
		missles.empty()
		ai_settings.increase_speed()
		create_fleet(ai_settings,screen,plane,aliens)




def update_missles(ai_settings,screen,stats,play_button,plane,aliens,missles,cnt):
	"""Обновляет позиции пуль и уничтожает старые пули."""
	# Обновление позиции пуль.missle
	missles.update()

	#Удаление пуль, вышедших за край экрана.
	for missle in missles.copy():
		if missle.rect.right >= ai_settings.screen_width:
			#missles.remove(missle)
			cnt += 1
			print(cnt)
			if cnt >= 3:
				play_button.draw_button()
				stats.game_active = False
				pg.mouse.set_visible(True)
		check_missle_alien_collision(ai_settings,screen,plane,aliens,missles)

def check_cnt(cnt):
	if cnt >= 3:
		stats.game_active = False
		pg.mouse.set_visible(True)

def create_alien(ai_settings,screen,aliens):
	"""Создает пришельца и размещает его в ряду"""
	alien = Alien(ai_settings,screen)

	#alien_width = alien.rect.width # определяем ширину на основе созданного экземпляра
	#alien.y = 
	aliens.add(alien)

def create_fleet(ai_settings,screen,plane,aliens):
	alien = Alien(ai_settings,screen)
	create_alien(ai_settings,screen,aliens)


def check_fleet_edges(ai_settings,aliens):
	"""Реагирует на достижение пришельцем края экрана"""
	for alien in aliens.sprites():
		if alien.check_edges():
			change_fleet_direction(ai_settings,aliens)
			break

def change_fleet_direction(ai_settings,aliens):
	"""Меняет направление флота"""
	for alien in aliens.sprites():
		alien.rect.y += ai_settings.fleet_drop_speed
	ai_settings.fleet_direction *= (-1)

def plane_hit(ai_settings,stats,screen,plane,aliens,missles):
	"""Обрабатывает столкновения корабля с пришельцем"""

	if stats.plane_left > 0:
		stats.plane_left -=1

		aliens.empty()
		missles.empty()

		create_fleet(ai_settings,screen,plane,aliens)
		plane.center_plane()

		sleep(1.7)
	else:
		stats.game_active = False
		pg.mouse.set_visible(True)

def update_aliens(ai_settings,stats,screen,plane,aliens,missles):

	check_fleet_edges(ai_settings,aliens)
	aliens.update()

	#if pg.sprite.spritecollideany(plane,aliens):
