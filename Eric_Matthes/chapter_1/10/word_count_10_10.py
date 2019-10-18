filename = 'txt_files/the.txt'

with open(filename) as f_obj:
	lines = f_obj.read() #считываем содержимое файла в переменную
	words = lines.split() #разделяем на слова и помещаем слова в список
	num_words = len(words) #считаем количество слов
	
	print(lines.lower().count('the')) # считаем количество ВХОЖДЕНИЙ сочетания the
	print(num_words) # вывод общего числа слов
	print(words) # вывод всех слов