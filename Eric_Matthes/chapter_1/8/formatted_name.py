def get_formatted_name(first_name,last_name):
	"""Возвращает аккуратно отформатированное полное имя"""
	full_name = first_name + ' ' + last_name
	return full_name.title()

musician = get_formatted_name('jimi','hendrix')
print(musician)
#print(get_formatted_name('jimi','hendrix')) - это может быть непонятно


##################
######## не обязательные аргументы
print('\n##################')
print('##################\n')

def get_format_name(first_name,last_name,middle_name=''):
	"""Возвращает аккуратно отформатированное полное имя"""
	if middle_name:
		full_name = first_name + ' ' + middle_name + ' ' + last_name
	else:
		full_name = first_name + ' ' + last_name

	return full_name.title()

musician = get_format_name('wes','borland')
print(musician)

musician = get_format_name('john','hooker','lee')
print(musician)