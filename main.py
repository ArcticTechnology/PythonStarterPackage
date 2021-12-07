#!/usr/bin/python3 -B
import sys
from python_starter_package import *

def main(args=None):
	if args is None:
		args = sys.argv[1:]

	python_starter = PythonStarterPackage()
	python_starter.run()

if __name__ == '__main__':
	sys.exit(main())
