prompt = '\nPlease, enter the topping which one you want in your pizza '
prompt += '\n(Enter `quit` to close the program): '

while True:
	message = input(prompt)
	if message == 'quit':
		break
	else:
		print(message.title() + ' added to your pizza! ')