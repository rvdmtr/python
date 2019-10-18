#from printing_functions import print_models, show_completed_models
from printing_functions import *


#Список моделей, которые необходимо напечатать.
unprinted_models = ['iphone case','robot pendant','dodecahedron']
completed_models = []

# Цикл последовательно печатает каждуйю модель до конца списка
# После пчати каждая пожмедб перемещается в список completed_models

while unprinted_models:
	current_design = unprinted_models.pop()
	# Печать модели на 3D-принтере
	print('Printing model: ' + current_design)
	completed_models.append(current_design)

# Вывод всех готовых моделей
print('\nThe following models habe been printed: ')
for completed_model in completed_models:
	print(completed_model)


########################################
########################################
########################################
### Или можно сделать так
print('\n#############')
print('#############\n')
print('----------------')

#def print_models(unprinted_designs,completed_models):
#	"""
#	Имитирует печать моделей, пока список не станет пустым.
#	Каждая модель после печати перемещается в completed_models.
#	"""
#	while unprinted_designs:
#		current_design = unprinted_designs.pop()
#
#	# Имитация печати модели на 3D-принтере. 
#		print('Printing model: ' + current_design)
#		completed_models.append(current_design)

#def show_completed_models(completed_models):
#	"""Выводит информацию обо всех напечатанных моделях"""
#	print('\nThe following models have been printed: ')
#	for completed_model in completed_models:
#		print(completed_model)


unprinted_designs = ['iphone case','robot pendant','dodecahedron']
completed_models = []
#print_models(unprinted_designs[:],completed_models) # синтаксис среза, создает копию списка
print_models(unprinted_designs,completed_models)
show_completed_models(completed_models)
print('-------')
print(unprinted_designs)