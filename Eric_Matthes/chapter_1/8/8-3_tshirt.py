def make_shirt(text='i love python',size='l'):#указано 2 параметра по умолчанию
	"""Получает размер футболки и текст"""
	print('\nSize of your tshirt is: ' + size.title())
	print('Text of you tshirt is: ' + text.capitalize())

make_shirt('l','linux')
make_shirt(text='#python coder',size='l')

make_shirt()
make_shirt(size='XL',text='invest in yourself')

##################### 8-5

print('\n################')
print('################\n')

def describe_city(city,country='russia'):#указан параметр по умолчанию,
# указывается последним
	print(city.title() + ' is in ' + country.title())

describe_city('moscow')
describe_city('reyykjavik','iceland')
describe_city(city='new york',country='usa')


