# Python Starter Package
This is a basic python starter package to be used as a template for creating your own python packages.

## Installation
Currently, this library is not hosted on PyPi. Once it is available, you would be able to install via ```pip```:
```
pip install python_starter_package
```
For manual install, see below.

### Manual Install
To manually install this app, clone this repo to your local system. After you clone the repo, make sure to run the setup.py file, so you can install any dependencies. To run the setup.py file, run the following command in your terminal.

```
pip install -e .
```

This will install all the dependencies listed in the setup.py file. Once done you can use the library wherever you want.

## Usage
You can run this app in your terminal with:
```
./app.py
```

Alternatively, you can import this app in your own project and run it within your program. For example:
```
from python_starter_package import *

python_starter = PythonStarterPackage()
python_starter.run()
```

## Documentation
The purpose of this guide is to show how to create this standard python package from scratch. See packaging.python for more details: https://packaging.python.org/tutorials/packaging-projects/. 

### Setup
First, setup the starter package with the following files and folders:
* config - Directory containing all configuration files for your package.
* src/python_starter_package - Core directory containing all the files that make up your program as well as __init__.py which is the entry point to our package.
 * utils - Directory containing any utility files for your program.
* test - Directory containing all your test scripts.
* app.py - Script to run your application.
* LICENSE - File defining your package's license.
* README.md - Readme file for documentation.
* requirements.txt - File defining all the requirements of your package.
* setup.py - Script to build your package.

Once setup, add the contents and code to the files and directories specified above. Copy the contents and code from the PythonStarterPackage available here.

### Deployment
Next, create the deployment for the starter package.

1. Upgrade to ```setuptools``` and ```wheel```.
```
pip3 install --upgrade setuptools wheel
pip3 install --user --upgrade setuptools wheel
```
2. Build the package with ```setup.py```.
```
python3 setup.py bdist_wheel
```
3. Test the install of the package.
```
pip3 install --user ~/Documents/PythonStarterPackage/dist/python_starter_package-0.1.0-py3-none-any.whl

./app.py
```

Note: To uninstall the package from pip3 use.
```
pip3 uninstall ~/Documents/PythonStarterPackage/dist/python_starter_package-0.1.0-py3-none-any.whl
```

## Support This Project
If you would like to support this project and future projects donate to my Patreon Page. I'm always looking to add more content for individuals like yourself, unfortunately some of the APIs I would require me to pay monthly fees.
