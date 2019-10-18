# 8-9 magicians.py

def show_magicians(list):
	for item in list:
		print(item.title())

magic_men = ['david','harry','alex']
show_magicians(magic_men)

# 8-10 magicians.py
print('\n#####################')
print('#####################\n')
print('########## 8 -10 ###########')

magic_men = ['david','harry','alex']

def show_magicians(list):
	for item in list:
		print(item.title())


def make_great(items):
	great = []
	for item in items:
		great.append('Great ' + item.title() + '!')
	return great


great_mags=make_great(magic_men)
show_magicians(great_mags)


# 8-10 magicians.py
print('\n#####################')
print('#####################\n')
print('########## 8 -10 alter solution, 8 -11 ###########')

magic_men = ['david','harry','alex'] # определяем списки
great_m = []

def show_magicians(list):
	"""Выводит на экран форматированный список"""
	for item in list:
		print(item.title())

def gm(simple,great_m): #simple - список со значениями, great_m -
# куда будет вставлять измененные значения

	"""Добавляет приписку great"""
	
	while simple:#пока в списке(переданном аргументе - magic_men) 
	#есть элементы, цикл получает True и выполняется
		grm=simple.pop()#извлекаем элемент из списка
		great_m.append('Great ' + grm.title() + '!')# помещаем элемент в 
		#другой список, добавляем приписку
	return great_m # возвращаем значение, чтобы можно было присвоить 
	#его переменной, без этой строчки = пустота
#	print(great_m)
####

greatest=gm(magic_men[:],great_m)#преобразуем список через функцию
# если убрать знак среза, список magic_men будет пустым
show_magicians(greatest)#

print('\n')
show_magicians(magic_men)# выводим доказательство, что список не изменился
# благодаря знаку среза, т.к. мы передаем копию списка