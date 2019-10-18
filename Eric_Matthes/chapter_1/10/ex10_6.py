#10-6
#print('Give me two numbers, and I`ll addition them.')
#print('Enter `q` to quit.')
while True:
	try:
		num1 = input('\nEnter the first number ')
		num2 = input('Enter the second number ')

		total = int(num1) + int(num2)
	
	except ValueError:
		msg = '\nPlease, enter a correct number'
		print(msg)

	else:	
		print('\nTotal: ' + str(total))
		break