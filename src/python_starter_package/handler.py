from random import sample
from .utils.commoncmd import CommonCmd as cmd
from .utils.configparser import ConfigParser

class PythonStarterPackage:

	def __init__(self):
		data = ConfigParser.get_config()
		self.answers = data['answers']

	def get_response(self):
		return sample(self.answers, 1)[0]

	def splashscreen(self):
		cmd.cls()
		print('Welcome to the Python Starter Package')

	def optionscreen(self):
		print(' ')
		print('What would you like to do?')
		print('(a) Ask me a question, (q) Quit')

	def option_a(self):
		cmd.cls()
		print('What question would you like to ask?')
		print(' ')
		question = input('Type your question: ')
		cmd.cls()
		print('Question: ' + question)
		print(' ')
		answer = self.get_response()
		print('Answer: ' + answer)
		print(' ')
		input()
		cmd.cls()

	def run(self):
		cmd.cls()
		self.splashscreen()

		while True:
			self.optionscreen()
			select = input()

			if select not in ['a', 'q']:
				#'(a) Ask me a question, (q) Quit'
				cmd.cls(); print('Invalid selection. Try again.')

			if select == 'q':
				cmd.cls()
				break

			if select == 'a':
				self.option_a()
