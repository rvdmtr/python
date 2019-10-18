#write_message.py
filename = 'txt_files/programming.txt'

with open(filename,'w') as file_object:
#запись в файл, w затирает предыдущие данные
	file_object.write('I love progs. \n')
	file_object.write('I love creating new games.\n')

with open(filename,'a') as file_object:
#присоединение данных в существующий файл
	file_object.write('I also love finding meaning in large datasets. \n')
	file_object.write('I love creating apps that can run in a browser.\n')

