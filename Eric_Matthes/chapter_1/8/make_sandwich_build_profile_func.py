def make_sandwich(*components):
	"""Функция получает список компонентов и выводит их описание"""
	print('\nMake sandwiche with following components: ')
	for component in components:
		print('\t- ' + component)


def build_profile(first,last,**user_info):# ** - указывает создать словарь и
# помещает в него переданные аргументы

	"""Строит словарь с информацией о пользователе.""" 
	profile = {}#создаем пустой словарь, в который помещаем значения
	profile['first_name'] = first
	profile['last_name'] = last
	for key,value in user_info.items():#перебираем указанные значения из словаря
		profile[key] = value
	return profile


def make_car(manufactor,model,**car_info):# ** создает словарь
	car_dict = {} # создаём пустой словарь
	car_dict['manufactor'] = manufactor # помещаем в него переданные значения
	car_dict['model'] = model
	for key,value in car_info.items(): # перебираем созданный ** словарь
	#и вставляем переданные значения в словарь car_dict сзданный нами
		car_dict[key] = value
	return car_dict