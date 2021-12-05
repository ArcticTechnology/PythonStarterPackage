#!/usr/bin/python3 -B
from random import sample
from .utils.common_cmd import CommonCmd as cmd

class PythonStarterPackage:

	def __init__(self):
		self.responses = [
			'The sign your looking for is right beside you.',
			'You better believe it.',
			'Follow your heart.',
			'The answer is within you.',
			'Listen to the little voice inside you.',
			'It would be wise to make a plan.',
			'It always seem to work out in the end.',
			'Do not be afraid of that which is not worth fearing.',
			'You create your own reality.',
			'The truth will be realized.',
			'Everything happens for a reason.',
			'You miss one-hundred precent of the shots you did not take.',
			'Set your mind to it and it will be yours.',
			'Believe in yourself and have the right attitude.',
			'Just do you.',
			'Everyday is a miracle and a blessing.',
			'Nothing is impossible to a willing heart.',
			'Success lies with those who want it.',
			'Do it right from the start.',
			'You learn a little from success and a lot from failures.',
			'Keep moving forward with humble hearts.',
			'Take the high road.']

	def get_response(self):
		return sample(self.responses, 1)[0]

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

if __name__ == '__main__':
	python_starter = PythonStarterPackage()
	python_starter.run()

