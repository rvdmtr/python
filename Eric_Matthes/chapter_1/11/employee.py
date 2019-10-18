#employee.py
class Employee():
	"""Описание работника"""

	def __init__(self,first,last,year_salary):
		"""Сохраняет переданные аргументы в атрибуты"""
		self.first = first
		self.last = last
		self.year_salary = year_salary

	def give_raise(self,up=5000):
		"""Увеличивает ежегодный оклад на 5000 или иное значение"""
		self.year_salary += up
		#full_name = self.first + ' ' + self.last 
		#print(full_name.title() + ', your salary was promoted and now it`s '+ str(self.year_salary))
		print(str(self.year_salary))

#Mark = Employee('Mark','Jens',100000)
#Mark.give_raise()