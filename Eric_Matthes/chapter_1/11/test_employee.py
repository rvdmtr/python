#ex 11-3 

import unittest
from employee import Employee

class TestCaseEmployee(unittest.TestCase):
	"""Тест повышения salary default и заданное значение"""

	def setUp(self):
		"""Создание объекта для теста"""

		self.my_employee = Employee('John','Doe',200000)

	def test_default_raise(self):
		"""Проверяет значение по умолчанию метода give_raise"""
		self.my_employee.give_raise()
		sal = self.my_employee.year_salary
		#print(sal)
		self.assertEqual(sal, 205000)

	def test_custom_raise(self):
		"""Проверяет значение по умолчанию метода give_raise"""
		self.my_employee.give_raise(11000)
		sal = self.my_employee.year_salary
		#print(sal)
		self.assertEqual(sal, 211000)

unittest.main()