import sys
import pygame as pg

def run_game():
	pg.init()
	screen = pg.display.set_mode((600,400))
	pg.display.set_caption('test key event')

	while True:
		for event in pg.event.get():
			if event.type == pg.QUIT:
				sys.exit()
			elif event.type == pg.KEYDOWN:
				print(event.key)
# проверяем атрибут event.key при обнаружении нажатий клавиш	
				
			
		pg.display.flip()

run_game()