#pizza.py

def make_pizza(*toppings):# символ * указывает, что может быть 
# передано любое количество аргументов - создает пустой кортеж(неизменяемый список) и 
#в него "упаковываются" переданные аргументы
	print(toppings)

make_pizza('peperoni')
make_pizza('peperoni','mushrooms','extra cheese','green peppers')


print('\n\n#########')
print('#########\n')
def make_pizza(*toppings):
	"""Выводит описание пиццы."""
	print('\nMaking a pizza with the following toppings: ')
	for topping in toppings:
		print('- ' + topping)

make_pizza('peperoni')
make_pizza('peperoni','mushrooms','extra cheese','green peppers')
	

print('\n\n#########')
print('#########\n')
def make_pizza(size,*toppings):
	"""Выводит описание пиццы."""
	print('\nMaking a ' + str(size) + 
		'-inch pizza with following toppings:')
	for topping in toppings:
		print('- ' + topping)

make_pizza(15,'peperoni')
make_pizza(23,'peperoni','mushrooms','extra cheese','green peppers')
	