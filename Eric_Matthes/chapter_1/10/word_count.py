def count_words(filename):
	"""Подсчет приблизительного количества строк в файле."""
	try:
		with open(filename) as f_obj:
			contents = f_obj.read()
	except FileNotFoundError:
		#msg = 'Sorry, the file ' + filename.lstrip('txt_files/') + ' doesn`t exist.'
		#print(msg) # Выводим сообщение - файл не найден
		pass # ничего не выводим, программа продолжает выполняться
	else:
		#Подсчет приблизительного количества строк в файле.
		words = contents.split()#разделяем файл на слова, помещаем в список
		num_words = len(words)
		print('The file ' + filename.lstrip('txt_files/') + ' has about ' +
		 str(num_words) + ' words.')



#filename = 'txt_files/alice.txt'
#count_words(filename)

#filename2 = 'txt_files/reasons.txt'
#count_words(filename2)

filenames = ['txt_files/alice.txt','txt_files/guest_book.txt',
				'txtfiles/programming.txt','txt_files/reasons.txt']
for filename in filenames:
	count_words(filename)