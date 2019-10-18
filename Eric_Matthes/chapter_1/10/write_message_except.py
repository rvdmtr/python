filename = 'txt_files/alice.txt'

try:
	with open(filename) as f_obj:
		contents = f_obj.read()
except FileNotFoundError:
	msg = 'Sorry, the file ' + filename + ' does not exist.'
	print(msg)
else:
	#Подсчет приблизительного количества строк в файле.
	words = contents.split()
	num_words = len(words)
	print('The file ' + filename.lstrip('txt_files/') + ' has about ' + str(num_words) + ' words.')


##########
#dm = '\n\n###########\n###########\n'
#print(dm)

title = 'Alice in Wonderland'
print(title.split())

