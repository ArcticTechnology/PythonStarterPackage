#!/usr/bin/python3 -B
from .starterpkg import StarterPkg

def main():
	starterpkg = StarterPkg()
	starterpkg.run()

if __name__ == '__main__':
	raise SystemExit(main())