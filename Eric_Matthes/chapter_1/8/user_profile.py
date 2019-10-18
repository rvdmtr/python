def build_profile(first,last,**user_info):#две звездочки означают создание
#пустого словаря user_info и упаковывают в него соответствующие переданные
#пары  имя-значение
	"""Строит словарь с информацией о пользователе."""
	profile = {}
	profile['first_name'] = first
	profile['last_name'] = last
	for key,value in user_info.items():
		profile[key] = value
	return profile

user_profile = build_profile('albert','einstein',
	location='princeton',field='physics')
print(user_profile)