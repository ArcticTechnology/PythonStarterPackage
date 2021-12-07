# Python Starter Package
This is a basic python starter package to be used as a template for creating your own python packages.
* Github repo: https://github.com/ArcticTechnology/PythonStarterPackage
* PyPi: https://pypi.org/project/PythonStarterPackage/

## Installation
This library is hosted on PyPi and can be installed via ```pip```:
```
pip3 install PythonStarterPackage
```
For manual install, see below.

### Manual Install
To manually install this package, clone this repo to your local system. After you clone the repo, navigate into the package to where the ```setup.py``` file is. Then you can use the ```pip install -e .``` command. This will install the package and all its dependencies editable mode. Then you can use the package locally or use it as the starting point for building out your own package.
```
pip3 install -e .
```

## Usage
You can run the app in your terminal with:
```
./main.py
```
You can also import this module into your own project and incorporate it into your own packages. For example:
```
from python_starter_package import *
python_starter = PythonStarterPackage()
python_starter.run()
```

## Documentation
The purpose of this project is to show you how to create a standard python package from scratch. This project is inspired by Sigma-Coding (https://github.com/areed1192/sigma-coding), it is a great detailed guide on deploying python packages.

### Setup
In order to setup the your own standard python package from scratch do the following:

1. Setup the starter package with the files and folders below:
* config - Directory containing all configuration files for your package.
* doc - Directory containing documentation files for your package.
* src/python_starter_package - Core directory containing all the files that make up your program as well as ```__init__.py``` which is the entry point to our package.
  * utils - Sub-directory of python_starter_package containing any utility files for your program.
* test - Directory containing all your test scripts.
* ```main.py``` - Script to run your application.
* .gitignore - Git ignore file for specifying the files that you want git to ignore.
* LICENSE - File defining your package's license.
* README.md - Readme file for documentation.
* requirements.txt - File defining all the requirements of your package.
* setup.py - Script to build your package.

2. Once setup, add the contents and code to the files and directories you created. Copy the contents and code from the PythonStarterPackage available in this repo: https://github.com/ArcticTechnology/PythonStarterPackage.

### Testing
In the directory containing the ```setup.py``` file, you can test the package by installing it in ```pip3``` editable mode. This will allow you make changes to it and test it without having to push the changes everytime.
```
pip3 install -e .
```
Once finished, uninstall with the following:
```
pip3 uninstall PythonStarterPackage
```

### Deployment
Do the following to create the deployment for the package.

1. Create (or overwrite) the requirements.txt document with ```pipreqs```. This is an extremely useful tool because it automatically finds all of the relavent versions of dependencies your package relies on and puts them into the ```requirements.txt``` file. If you don't have ```pipreqs```, install it with ```pip install pipreqs```.
```
pipreqs --force --encoding utf-8
```
2. Upgrade ```setuptools```, ```wheel```, and ```twine``` (```twine``` will be used in the next part).
```
pip3 install --upgrade setuptools wheel twine
```
3. Build the package with ```setup.py```.
```
python3 setup.py sdist bdist_wheel
```
4. Test a local install of the package and run ```main.py``` to make sure it is working.
```
pip3 install .
./main.py
```
5. After testing that it is working, uninstall the package from pip3.
```
pip3 uninstall PythonStarterPackage
```

### Upload to PyPi
In order to upload to PyPi make sure to setup your PyPi account first. See "PyPi Setup Guide.md" in ```doc/``` for more details. You will also need to have ```twine``` installed and upgraded. Once you have all of this setup do the following:

1. Upload using ```twine```.
```
twine upload dist/*
```
2. Install your package with ```pip```.
```
pip install PythonStarterPackage
```
Note: If you get a "Requrements already satisfied..." for PythonStarterPackage when trying to install, it may be because ```pip``` still thinks you have the package already installed from the testing earlier. To cleanly break that connection, simply go to ```./src/``` and delete the ```PythonStarterPackage.egg-info``` directory and its contents. Then try uninstalling and reinstalling again:
3. Finally, run the ```main.py``` to test that the package is working.
```
./main.py
```
4. To uninstall: ```pip uninstall PythonStarterPackage```

## Support and Contributions
Our software is open source and free for public use. If you found any of these repos useful and would like to support this project financially, feel free to donate to our bitcoin address.

Bitcoin Address 1: 1GZQY6hMwszqxCmbC6uGxkyD5HKPhK1Pmf

![alt text](https://github.com/ArcticTechnology/BitcoinAddresses/blob/master/btcaddr1.png?raw=true)

