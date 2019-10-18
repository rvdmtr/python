#test_survey.py

import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
	"""Тесты для класса AnonymousSurvey"""

	def test_store_single_response(self):
		"""Проверяет, что один ответ сохранен правильно"""
		question = 'What language did you first learn to speak?'
		my_survey = AnonymousSurvey(question)
		my_survey.store_response('English')
		#my_survey.store_response('German')

		self.assertIn('English', my_survey.responses)
		#self.assertIn('German', my_survey.responses)

	def test_store_three_response(self):
		"""Проверяет, что три ответа сохранены правильно"""
		question = 'What language did you first learn to speak?'
		my_survey = AnonymousSurvey(question)
		responses = ['English','German','Russian']
		for response in responses:
			my_survey.store_response(response)
		
		for response in responses:
			self.assertIn(response, my_survey.responses)
		



unittest.main()