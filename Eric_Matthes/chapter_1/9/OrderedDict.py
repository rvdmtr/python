from collections import OrderedDict
print('\n***** EXERCISE 6-4 ******\n')

glossary = {
	'переменная':'некий контейнер для хранения значеий, как спичечный коробок',
	'список':'набор элементов хранящийся в переменной',
	'цикл':'последовательность определнных действий - цепочка',
	'условие':'условие встречается в цикле, позволяет направить ход программы',
	'множество':'set исключает дубликаты из словаря, оставляет уникальн. знач.',
	'вывод':'результат выполнения программы, вывод на экран - print()',
	'программа':'набор последовательных инструкций из команд, функций, циклов..',
	'словарь':'структура данных, объединяющая взаимосвязанные значения',
	}
#print(glossary)
#print('Переменная: '+ '\n\t' + 'это ' + glossary['переменная'] + '\n')
#print('Список: '+ '\n\t' + 'это ' + glossary['список'] + '\n')
#print('Цикл: '+ '\n\t' + 'это ' + glossary['цикл'] + '\n')
#print('Условие: '+ '\n\t' + 'это ' + glossary['условие'] + '\n')

#for key,value in glossary.items():
#	print('\nТермин: ' + key.title())
#	print('\tОпределение: ' + value)

glos = OrderedDict()
glos['переменная'] = 'некий контейнер для хранения значеий, как спичечный коробок'
glos['список'] = 'набор элементов хранящийся в переменной'
glos['аргумент'] = 'он же параметр(позиционный, по умолчанию и явно указанный).\n'
glos['аргумент'] += '\t\t\tЗначение указываемое в скобках функции, метода'

for term,defin in glos.items():
	print(term.title() + ' -- ' + defin)
#print(glos)