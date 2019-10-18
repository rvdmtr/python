#Exercise 7-5, 7-6(active = True)


prompt = '\nPlease, enter your age to show your price '
prompt += '\n(Enter `quit` to close the program:) '

#active = True
#Обрати внимание, если стоит команда break, цикл сразу завершается, если
#идет проверка на False переменной-флага, то после присвоения ей False
#программа дальше проверяет нижестоящие условия, т.е. программа не завершается
#аналогично команде break, что не совсем удобно, удобно использовать break, если 
#в текущем прохоже цикла не требуется проверка нижеидущих условий

while True:
	age = input(prompt)
	
	if age == 'quit':
		break
#		active = False
#		continue - запускает цикл заново, соответственно если 
#		while active(False), цикл не запускается
	else:
		age = int(age)

	if age < 3:
		print('\nFor ' + str(age) + ' years old ticket is free ')
		continue
	elif age < 12:
		print('\nFor ' + str(age) + ' years old ticket cost is 10$ ')
		continue
	elif age > 12:
		print('\nFor ' + str(age) + ' years old ticket cost is 15$ ')
		continue
	#elif age =='quit':
	#	break

	
