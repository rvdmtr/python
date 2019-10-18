#game_functions.py

import sys

import pygame as pg
#import settings as se

from ball import Ball
from random import randint
from time import sleep


def create_ball(ai_settings,screen):
	"""Создает мяч"""
	ball = Ball(ai_settings,screen)
	ball_width = ball.rect.width
	ball.x = randint(0,self.ai_settings.screen_width - 40)#self.rect.width
	ball.rect.x = ball.x


def check_keydown_events(event,ai_settings,screen,cat,balls):
	"""Реагирует на нажатие клавиш"""
	if event.key == pg.K_RIGHT:
		cat.moving_right = True
	elif event.key == pg.K_LEFT:
		cat.moving_left = True
	elif event.key == pg.K_SPACE:
		start_ball(ai_settings,screen,cat,balls)
	if event.key == pg.K_q:
		sys.exit()

def start_ball(ai_settings,screen,cat,balls):
	if len(balls) < ai_settings.balls_allowed:
		new_ball = Ball(ai_settings,screen)
		balls.add(new_ball)

def check_keyup_events(event,cat):
	if event.key == pg.K_RIGHT:
		cat.moving_right = False
	elif event.key == pg.K_LEFT:
		cat.moving_left = False

def check_events(ai_settings,screen,cat,balls):
	"""Обрабатывает нажатия клавиш и события мыши"""
	for event in pg.event.get():
		if event.type == pg.QUIT:
			sys.exit()
		elif event.type == pg.KEYDOWN:
			check_keydown_events(event,ai_settings,screen,cat,balls)
		elif event.type == pg.KEYUP:
			check_keyup_events(event,cat)


#def check_cat_ball_collisions(cat,ball):
#	"""Обработка коллизий кота и мяча"""
#	#при соприкосновения мяча(коллизия) - мяч перезапускается 
#	collisions = pg.sprite.spritecollide(ball,cat,True,False)
#
#	if ball == False:
#		create_ball(ai_settings,screen)

def update_balls(ai_settings,screen,stats,cat,balls):
	balls.update()

	for ball in balls.copy():
		if ball.rect.bottom >= ai_settings.screen_width:
			#balls.remove(ball)
	#check_cat_ball_collision(ai_settings,screen,cat,balls)
			ball_catch(ai_settings,screen,stats,cat,balls)
			break

def check_cat_ball_collision(ai_settings,screen,cat,balls):
	if pg.sprite.spritecollideany(cat,balls):
		#print('CATCH!!\n--\n')
		ball_catch(ai_settings,screen,stats,cat,balls)



def ball_catch(ai_settings,screen,stats,cat,balls):
	"""Обрабатывает столкновения мяча с котом"""
	if stats.cat_left > 0:
		stats.cat_left -=1
		balls.empty()
		start_ball(ai_settings,screen,cat,balls)
		cat.center_cat()
		sleep(1.5)
	else:
		stats.game_active = False

def update_screen(ai_settings,screen,cat,balls):
	"""Обновляет изображеие на экране и отображает новый экран"""
	screen.fill(ai_settings.bg_color)
	
	for ball in balls.sprites():
#		ball.draw_ball()
		balls.draw(screen)
	cat.blitme()
	#ball.blitme()
	pg.display.flip()







