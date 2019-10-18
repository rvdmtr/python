current_number = 0

while current_number < 10:#программа входит в цикл while
	current_number += 1#счетчик увеличивается на 1
	if current_number % 2 == 0:#проверка целого деления числа на 2
		continue#если условие истинно, то continue указывает игнорировать
		#оставшийся код - "print(current_number)" и вернуться к началу
		#цикла while

	print(current_number)



print('\n******************')
print('******************\n')

x = 1 
while x <= 5:
	print(x)
	x+=1



