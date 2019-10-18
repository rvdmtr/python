#10-4 # guest_book

filename = 'txt_files/guest_book.txt'

prompt = 'Hello! Enter your name, please\n'
prompt += '(To exit the programm enter quit or exit): '

with open(filename,'a') as file_object:
	
	while True:
		name = input(prompt)
		if name in ['quit','Quit','exit','Exit','EXIT']:
			break
		else:
			file_object.write(name.title() + '\n')
			print(name.title() + ' was added to guest book!')
			#continue
