height = input('How tall are you, in inches?(1 inch == 2,54cm) ')
height = int(height)#условие ниже выполняется, сравнивает 2 числа
#а не строку с числом

if height >= 36:
	print('\nYou are tall enough to ride')
else:
	print('\nYou will be able to ride when you are a little older')