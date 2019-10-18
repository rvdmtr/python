vacations = {}

polling_active = True

while polling_active:
	name = input('What is your name? ')
	vacation = input('Where your want to taste your vacation? ')
	vacations[name] = vacation

	cont = input('Would you like to answer another person? (yes /no) ')
	if cont == 'no':
		polling_active = False

print('\n --- Poll results ---')
for name,vacation in vacations.items():
	print(name.title() + ' would like to spend vacation in ' + vacation.title())last