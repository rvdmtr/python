class Dog():
	"""Простая модель собаки."""

	def __init__(self,name,age):
		"""Инициализирует атрибуты name и age."""
		self.name = name
		self.age = age

	def sit(self):
		"""Собака садится по команде."""
		print(self.name.title() + " is now sitting.")
	def roll(self):
		"""Собака перекатывается по команде."""
		print(self.name.title() + " rolled over!")


my_dog = Dog('willie', 6)
your_dog = Dog('lucy',3)

print('My dog`s name is ' + my_dog.name.title() + '.')
print('My dog`s age is ' + str(my_dog.age) + ' years old.')
#print('\n')
my_dog.sit()
my_dog.roll()

print('\n')

print('Your dog`s name is ' + your_dog.name.title() + '.')
print('Your dog`s age is ' + str(your_dog.age) + ' years old.')

your_dog.sit()