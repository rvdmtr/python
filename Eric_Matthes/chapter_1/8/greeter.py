def greet_user(username):
	""" Выводит простое приветствие. """
	print('Hello, ' + username.title() + '!')

greet_user('sarah')



print('\n\n######################')
print('######################\n')

def display_message(parameter1,parameter2):
	"""Вывод сообщения темы рассматриваемой в данной главе"""
	print('\nThis chapter about ' + parameter1.title() + 's and ' +
	 parameter2.title() + 's and other interesting things')

display_message('argument','function')


print('\n\n######################')
print('######################\n')

def favorite_book(book):
	"""Вывод сообщения темы рассматриваемой в данной главе"""
	print('\nOne of my favorite books is ' + book.title())

favorite_book('Python crash course')