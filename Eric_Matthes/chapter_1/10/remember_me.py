#remember_me.py
import json
#Программа загружает имя пользователя, если оно было сохранено ранее.
#В противном случае она запрашивает имя пользователя и сохраняет его.

filename = 'txt_files/username.json'
try:
	with open(filename) as f_obj: # as псевдоним/alias
		username = json.load(f_obj)# обязательно указываем псевдоним файла,
		# а не переменную

except FileNotFoundError:
	username = input('What is you name? ')
	with open(filename,'w') as f_obj:
		json.dump(username,f_obj)
		print('We`ll remember you when you come back, ' + username.title() + '!')

else:
	print('Welcome back, ' + username.title() + '!') 
	#вывод объекта сохраненного в переменную	



