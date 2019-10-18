#10-3
filename = 'txt_files/guest.txt'

guest_name = input('Enter your name please: ')
with open(filename,'a') as file_object:
	file_object.write(guest_name.title() + '\n')




