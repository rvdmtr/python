def city_country(city,country):
	"""Вывод города и страны"""
	place = city + ', ' + country
	return place.title()

vacation = city_country('moscow','russia')
vac2 = city_country('berlin','germany')
vac3 = city_country('new york','usa')

print(vacation)
print(vac2)
print(vac3)