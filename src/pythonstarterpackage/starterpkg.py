import os
import json
import pkgutil
import requests
from random import sample

class StarterPkg:

	def __init__(self, configparser):
		parser = configparser.parse()

		if parser['status'] == 200:
			config = parser['data']
		else:
			config = {'answers': ['Error: Failed to load config file.']}

		self.answers = config['answers']

	def get_pkg_data(self):
		"""
		Modern way to get package data is with pkgutil.get_data(). See this post:
		https://stackoverflow.com/questions/6028000/how-to-read-a-static-file-from-inside-a-python-package/58941536#58941536
		"""
		pkgdata = pkgutil.get_data(__name__, 'data/default.json')
		return json.loads(pkgdata.decode('utf-8'))

	def get_response(self):
		return sample(self.answers, 1)[0]

	def get_myip(self):
		"""
		Modern way to get get my ip using requests. See this post:
		https://stackoverflow.com/questions/22492484/how-do-i-get-the-ip-address-from-a-http-request-using-the-requests-library/22513161#22513161
		"""
		resp = requests.get('https://www.google.com', stream=True)
		return resp.raw._connection.sock.getsockname()[0]

	def splashscreen(self):
		os.system('clear')
		print('Welcome to the Python Starter Package')

	def optionscreen(self):
		print(' ')
		print('What would you like to do?')
		print('(a) Ask me a question, (ip) Get my IP, (d) Get package data (q) Quit')

	def option_a(self):
		os.system('clear')
		print('What question would you like to ask?')
		print(' ')
		question = input('Type your question: ')
		os.system('clear')
		print('Question: ' + question)
		print(' ')
		print('Answer: ' + self.get_response())
		input()
		os.system('clear')

	def option_ip(self):
		os.system('clear')
		print('Your IP: ' + str(self.get_myip()))

	def option_d(self):
		os.system('clear')
		print('Package data: ' + str(self.get_pkg_data()))

	def run(self):
		os.system('clear')
		self.splashscreen()

		while True:
			self.optionscreen()
			select = input()

			if select not in ['a', 'ip', 'd', 'q']:
				#'(a) Ask me a question, (ip) Get my IP, (d) Get package data (q) Quit'
				os.system('clear'); print('Invalid selection. Try again.')

			if select == 'q':
				os.system('clear')
				break

			if select == 'a':
				self.option_a()

			if select == 'ip':
				self.option_ip()

			if select == 'd':
				self.option_d()