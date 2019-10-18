####10-1
filename = 'txt_files/learning_python.txt'

with open(filename) as file_object:
	lines = file_object.readlines()

print(lines)
#print('\n')

#for line in lines:
#	lang = 'Python'
#	print(line.rstrip())
#	if lang in line:
#		print(line.replace('Python','C'))
		

print('\n\n####### 10-2 #######\n')
message = 'I really like python'
message = message.replace('python','test')
print(message)#.replace('python','test\n'))

for line in lines:
	lang = 'Python'
	print(line.rstrip())
	if lang in line:
		print(line.replace('Python','C++'))


