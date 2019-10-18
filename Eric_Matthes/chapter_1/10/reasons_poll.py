#reasons_poll.py 10-5

#10-5 
filename = 'txt_files/reasons.txt'#указываем путь к файлу в переменной

prompt = 'Why are you like to programming? \n'
prompt += '(to exit the programm enter quit or exit): '
#сохраняем текст приветствия в переменной
with open(filename,'a') as file_object:
# a - добавить информацию в файл, не перезаписывать
#используем переменную в качетсве аргумента с путем к файлу	
	while True:# пока значение истинно, цикл выполняется
		reason = input(prompt)#введенное пользователем значение в переменную
		if reason in ['quit','Quit','exit','Exit','EXIT']:
		#проверяем, не хочет ли пользователь выйти из программы
			break #выход из программы
		else:
			file_object.write(reason.capitalize() + '\n')
			#пишем в файл введенную пользователем причину
			#print(reason.title() + ' was added to guest book!')
			#continue
