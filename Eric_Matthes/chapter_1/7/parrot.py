prompt = '\nTell me something and I will repeat it back to you:'
prompt += '\nEnter  `quit` to end the program. '

#message = ''

#while message != 'quit':
#	message = input(prompt)
#	if message != 'quit':
#		print(message)

active = True#переменная-флаг, пока она истинна, программа выполняется
while active:#проверяем значение переменной, если True, то выполняем ..
	message = input(prompt)# присваиваем введенные пользователем символы 
	#переменной

	if message == 'quit':#проверяем не ввел ли пользователь quit
		active = False#если юзер ввел quit, значит переменная-флаг меняется на
		# False и программа завершается
	else:
		print(message)#если не равно quit, значит программа продолжает работу
		# и выводит введенное юзером сообщение

