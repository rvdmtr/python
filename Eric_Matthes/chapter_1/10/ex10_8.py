#10-8
def print_names(filename):
	"""Разбивка файла на список имен и вывод на экран"""
	try:
		with open(filename) as f_obj:
			contents = f_obj.read()
			names = contents.split()
			for name in names:
				print('\t' + name.title())
			print('\n---#\n')	
	except FileNotFoundError:
		#print('Sorry ' + filename.lstrip('txt_files/') + ' not found\n' +
		#	'\n***\n')
		pass


filenames = ['txt_files/cats.txt','txt_files/dogs.txt']
for filename in filenames:
	print_names(filename)