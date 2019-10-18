import unittest
from city_functions import get_city_country

class TestCityCountryFunction(unittest.TestCase):
	"""Тесты для city_functions.py"""

	def test_city_country(self):
		formatted_string = get_city_country('santiago','chile')
		self.assertEqual(formatted_string,'Santiago, Chile')

	def test_city_country_population(self):
		formatted_string = get_city_country('santiago','chile',5000000)
		self.assertEqual(formatted_string,'Santiago, Chile - population 5000000')
unittest.main()