#name = input('Please enter your name: ')
#print('Hello, ' + name.title() + '!')

#Иногда подсказка может занимать более одной строки
#в таком случае можно сделать следующее

prompt = 'If you tell us who you are, we can personalize the messages you see.'
prompt += '\nWhat is your first name? '

name = input(prompt)
print('\nHello, ' + name.title() + '!')

age = input('how old are you?: ')
age = int(age)
print(age)
