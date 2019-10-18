#file_reader.py
filename = 'txt_files/pi_digits.txt'#путь к файлу в переменной

#with open(filename) as file_object:# обращение к файлу через переменную
#	contents = file_object.read()
#	print(contents.rstrip())

#with open(filename) as file_object:# обращение к файлу через переменную
#	for line in file_object:
#		print(line.rstrip())

#with open(filename) as file_object:
#	lines = file_object.readlines()
#	print(lines)
#	for line in lines:
#		print(line.rstrip())

with open(filename) as file_object:
	lines = file_object.readlines()

pi_string = ''
for line in lines:
	pi_string += line.strip()

#print(pi_string)
#print(pi_string[:5]+'...')# вывод первых 5 знаков строки
#print(len(pi_string))# реальная длина строки 32 символа

##################проверка вхождения дня рождения пользователя в число ПИ

birthday = input('Enter your birthday, in the form mmddyy: ')
if birthday in pi_string:
	print('Your birthday appears in the digits of pi!')
else:
	print('Your birthday don`t appear in the digits of pi!')
