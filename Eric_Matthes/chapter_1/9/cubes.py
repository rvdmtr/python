#cubes.py 9-15

from random import randint

x = randint(1,6)

class Die():
	"""Класс описывающий кубик"""
	def __init__(self, sides):
		self.sides = sides

	def roll_die(self):
		ran = randint(1,self.sides)
		print(ran)

cube = Die(20)
#print(cube.sides)
#cube.roll_die()

def cycle():
	x=1
	while x!=10:
		cube.roll_die()
		x+=1

cycle()

print('\n\n\n######')
#cube = Die(10)
print(cube.sides)
#cycle()

print('\n\n\n######')
cube = Die(30)
print(cube.sides)
cycle()