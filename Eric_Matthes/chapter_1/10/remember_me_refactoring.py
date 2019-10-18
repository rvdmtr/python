#remember_me_refactoring.py
# Рефакторинг - делать код более удобным и читаемым, т.е. разбить
# на функции, модули

import json

def get_stored_username():
	"""Получает хранимое имя пользователя, если оно существует"""
	filename = 'txt_files/username.json'
	try:
		with open(filename) as f_obj: # as псевдоним/alias
			username = json.load(f_obj)# обязательно указываем псевдоним файла,
			# а не переменную
	except FileNotFoundError:
		return None
	else:
		return username


def greet_user():
	"""Приветствует пользователя по имени"""
	
	username = get_stored_username()
	if username:
		print('Welcome back, ' + username.title() + '!') 
		#вывод объекта сохраненного в переменную
	else:
		username = input('What is your name? ')
		filename = 'txt_files/username.json'
		with open(filename,'w') as f_obj:
			json.dump(username,f_obj)
			print('We`ll remember you when you come back, ' + username.title() + '!')

greet_user()
