#!/usr/bin/python3 -B
from .starterpkg import StarterPkg
from .utils.configloader import ConfigLoader

def main():
	configparser = ConfigLoader()
	starterpkg = StarterPkg(configparser)
	starterpkg.run()

if __name__ == "__main__":
	raise SystemExit(main())