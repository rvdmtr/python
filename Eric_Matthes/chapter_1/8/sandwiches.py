####### 8-12 ##########

import make_sandwich_build_profile_func as m
#from make_sandwich_build_profile_func import *
#from make_sandwich_build_profile_func 
#import make_sandwich, build_profile, make_car

#def make_sandwich(*components):
#	"""Функция получает список компонентов и выводит их описание"""
#	print('\nMake sandwiche with following components: ')
#	for component in components:
#		print('\t- ' + component)


m.make_sandwich('mushrooms','cheese')
m.make_sandwich('tomatoes')
m.make_sandwich('peppers','greens')

##################################
print('\n#############')
print('########## 8-13#######\n')

#def build_profile(first,last,**user_info):# ** - указывает создать словарь и
# помещает в него переданные аргументы
#
#	"""Строит словарь с информацией о пользователе.""" 
#	profile = {}#создаем пустой словарь, в который помещаем значения
#	profile['first_name'] = first
#	profile['last_name'] = last
#	for key,value in user_info.items():#перебираем указанные значения из словаря
#		profile[key] = value
#	return profile

user_profile = m.build_profile('john','malkovich',
location ='new york',field='movies,serials',country='usa',
citizenship='american',language='english')# передаем параметры функции
# и присваиваем результат переменной
print(user_profile)


##################################
print('\n#############')
print('########## 8-14 #######\n')

#def make_car(manufactor,model,**car_info):# ** создает словарь
#	car_dict = {} # создаём пустой словарь
#	car_dict['manufactor'] = manufactor # помещаем в него переданные значения
#	car_dict['model'] = model
#	for key,value in car_info.items(): # перебираем созданный ** словарь
#	#и вставляем переданные значения в словарь car_dict сзданный нами
#		car_dict[key] = value
#	return car_dict

car = m.make_car(
	'Alfa Romeo','Guillia gtr',country='italy',
	sport='true',fast='yes',price='100000$'
	)
print(car)
