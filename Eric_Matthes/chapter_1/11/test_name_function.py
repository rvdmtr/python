#test_name_function.py
import unittest
from formatted_name import get_formatted_name

class NamesTestCase(unittest.TestCase):
	"""Тесты для `formatted_name.py`"""

	def test_first_last_name(self):
		"""Имена вида `Janis Joplin` работают правильно?"""
		formatted_name = get_formatted_name('janis','joplin')
		self.assertEqual(formatted_name, 'Janis Joplin')

	def test_first_last_middle_name(self):
		"""Работают ли такие имена, как `Wolfgang Amadeus Mozart`"""
		formatted_name = get_formatted_name(
			'wolfgang','mozart','amadeus')

unittest.main()