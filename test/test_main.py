#!/usr/bin/python3 -B
from pythonstarterpackage import *

def test_main():
	configparser = ConfigParser()
	starterpkg = StarterPkg(configparser)
	starterpkg.run()

if __name__ == '__main__':
	raise SystemExit(test_main())