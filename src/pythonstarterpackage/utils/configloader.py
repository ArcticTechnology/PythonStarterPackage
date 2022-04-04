import os; import json
from os.path import (
	basename, dirname, exists, normpath
)
from .crawler import Crawler
from .read import read_file

class ConfigParser:

	def __init__(self):
		self.build_loc = 'pythonstarterpackage/config'
		self.dev_loc = 'config'
		self.possible_names = ['config.json']

		self.rootpath = ''
		self.env = ''
		self.configloc = ''
		self.configfile = ''
		self.load()

	def _get_rootpath(self) -> str:
		return dirname(dirname(__file__))

	def _get_env(self) -> str:
		if self.rootpath == '': return ''
		base = basename(normpath(dirname(self.rootpath)))
		if base == 'site-packages':
			return 'build'
		elif base == 'src':
			return 'dev'
		else:
			return ''

	def _get_configloc(self) -> str:
		if self.env == 'build':
			return Crawler.joinpath(dirname(dirname(dirname(self.rootpath))),
					self.build_loc)
		elif self.env == 'dev':
			return Crawler.joinpath(dirname(dirname(self.rootpath)),
					self.dev_loc)
		else:
			return ''

	def _get_configfile(self, filename) -> str:
		if self.configloc == '': return ''
		return Crawler.joinpath(self.configloc, filename)

	def _find(self) -> dict:
		self.rootpath = self._get_rootpath()
		self.env = self._get_env()
		self.configloc = self._get_configloc()

		for filename in self.possible_names:
			self.configfile = self._get_configfile(filename)
			if exists(self.configfile):
				return {'status': 200, 'message': 'Config file found.'}

		return {'status': 400, 'message': 'Error: config file not found.'}

	def _hasContent(self, filepath):
		if exists(filepath): return False
		if os.stat(filepath).st_size > 0:
			return True
		else:
			return False

	def load(self):
		find = self._find()
		if find['status'] == 400: return find['message']
		if self._hasContent(self.configfile):
			return {'status': 200,
					'message': 'Config file loaded.'}
		else:
			return {'status': 400,
					'message': 'Error: config file is empty.'}

	def parse(self):
		try:
			content = ''.join(read_file(self.configfile))
		except:
			return {'status': 400,
						'message': 'Error: config file could not be read.', 'data': None}

		try:
			result = json.loads(content)
			return {'status': 200, 'message': 'Read config file complete.',
					'data': result}
		except:
			return {'status': 400,
				'message': 'Error: config file not structured correctly.',
				'data': None}