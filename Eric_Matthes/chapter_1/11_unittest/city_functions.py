def get_city_country(city,country,population=0):
	"""Возвращает строку с названием города и страны"""
	if population:
		stringa = city.title() + ', ' + country.title()
		stringa += ' - population ' + str(population)
		return stringa
	else:
		stringa = city + ', ' + country
		return stringa.title()