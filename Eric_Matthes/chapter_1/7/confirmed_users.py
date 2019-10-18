#confirmed_users
#начинаем с двух списков: пользователей для проверки
# и пустого списка для хранения проверенных пользователей
unconfirmed_users = ['alice','brian','candance']
confirmed_users = []

#проверяем каждого пользователя, пока остаются непроверенные
# пользователи. Каждый пользователь, прошедший проверку,
# перемещается в список проверенных. 

while unconfirmed_users:
	current_user = unconfirmed_users.pop()

	print('Verifying user: ' + current_user.title())
	confirmed_users.append(current_user)

#Вывод всех проверенных пользователей
print('\n\nThe following users have been confirmeds: ')

for confirmed_user in confirmed_users:
	print(confirmed_user.title())
