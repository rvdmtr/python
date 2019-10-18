#greet_user.py

import json

filename = 'txt_files/username.json'

with open(filename) as f_obj: # as псевдоним/alias
	username = json.load(f_obj)# обязательно указываем псевдоним файла,
	# а не переменную

print('Welcome back, ' + username.title() + '!') # вывол объекта сохраненного в переменную