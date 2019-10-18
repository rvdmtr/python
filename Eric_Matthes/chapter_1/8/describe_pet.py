#Использование позиционных аргументов, строгий порядок передачи 

def describe_pet(animal_type,pet_name):
	"""Выводит информацию о животном"""
	print('\nI have a ' + animal_type + '.')
	print('My ' + animal_type + '`s name is ' + pet_name.title() + '.')

describe_pet('hamster','harry')
describe_pet('dog','willie')


print('\n\n################')
print('################\n\n')

#Использование именованых аргументов 

def describe_pet(
		pet_name,animal_type='dog'
		): # задали значение по умолчанию, порядок важен
	"""Выводит информацию о животном"""
	print('\nI have a ' + animal_type + '.')
	print('My ' + animal_type + '`s name is ' + pet_name.title() + '.')

describe_pet(animal_type='hamster',pet_name='harry')
describe_pet(
		pet_name='gillie',animal_type='cat'
			)#обрати внимание, порядок передачи не столь важен

print('\n#############')

describe_pet('rex')
describe_pet('rex','dinosaur')
describe_pet(pet_name='rex',animal_type='fish')