## PythonStarterPackage Tutorial
The purpose of this tutorial is to show you how to create a standard python package from scratch. Feel free to reference the [PythonStarterPackage](https://github.com/ArcticTechnology/PythonStarterPackage) when going through this tutorial. It is what the end result will look like.

This project is inspired by this excellent [getmyip](https://github.com/iamtennislover/getmyip) package by @iamtennislover: and this great [guide on deploying python packages](https://github.com/areed1192/sigma-coding) by @sigma-coding.

### Background
In order to create a Python package that can be used with ```pip```, it is strongly recommended that you use python's ```setuptools``` package to set up your package and then push it to PyPi.

This guide will go over how to create a basic package that you can deploy with ```setuptools```.

### Set up Setuptools
The two critical files at the heart of your package are ```setup.py``` and ```setup.cfg```. These two files are what provides the instructions for ```setuptools``` to build and distribute your packages. Take a look at the ```setup.py``` and ```setup.cfg``` files in this package as a reference. For details on ```setup.py``` and ```setup.cfg``` see this [setuptools quickstart guide](https://setuptools.pypa.io/en/latest/userguide/quickstart.html) for details.

#### setup.py
The ```setup.py``` file is the python file that is called when you build your package with the command ```python3 setup.py sdist bdist_wheel```. In the past the configurations are written directly into ```setup.py```. In some older packages, you may see ```setup.py``` with all of the configurations hardcoded on it. However, that is no longer the convention. The current convention is ```setup.py``` should ONLY have one line of code on it, which is:
```
from setuptools import setup; setup()
```

#### setup.cfg
Rather than hardcoding the configurations to your application on to ```setup.py```, the convention is to put these configurations into a ```setup.cfg``` file. This is often referred to as the declarative setup. See this [guide on declarative setups](https://setuptools.pypa.io/en/latest/userguide/declarative_config.html) for more details.

The ```setup.cfg``` is broken up into sections, denoted by brackets such as ```[metadata]```. Each section provides details about your application and instructions to ```setuptools``` on how to package up your application and how to deploy it. Take a look at the ```setup.cfg``` file in this package as an example. This section will go over the typical contents that you'll find in a ```setup.cfg``` file.

1. ```[metadata]``` - This section contains all of the key metadata of the package such as name, version, license, etc. It looks like the following:
```
[metadata]
name = PythonStarterPackage
version = 0.1.1
author = ArcticTechnology
author_email = arctic.technology.mail@gmail.com
license = MIT
description = Python starter package, a template for creating your own python packages.
long_description = file: README.md
long_description_content_type = text/markdown
keywords = starter, package, template
url = https://github.com/ArcticTechnology/PythonStarterPackage
classifiers =
	Development Status :: 3 - Alpha
	License :: OSI Approved :: MIT License
	Natural Language :: English
	Operating System :: OS Independent
	Programming Language :: Python
	Programming Language :: Python :: 3
	Programming Language :: Python :: 3 :: Only
	Programming Language :: Python :: 3.8
	Programming Language :: Python :: 3.9
	Programming Language :: Python :: 3.10
	Programming Language :: Python :: 3.11
```
* Note that the ```version``` variable follows the convention: major.minor.maintenance
* The ```classifiers``` variable describes additional metadata about the package like the intended usage, language, licensing, etc. See [pypi classifiers](https://pypi.org/classifiers/) for the comprehensive list of classifiers.
* The typical deployment status classifiers are:
```
Development Status :: 3 - Alpha
Development Status :: 4 - Beta
Development Status :: 5 - Production/Stable
```

2. ```[options]``` - This section contains the critical configurations that tell ```setuptools``` what dependencies the package has, which python version the package requires, where to find the package, etc.
```
[options]
install_requires =
	setuptools>=59.5
python_requires = >=3.8
package_dir = =src
packages = find:
```
* The ```install_requires``` variable is where you list all of your package dependencies. The ```pipreqs``` tool makes it easy to map your package dependencies. Simply use ```pipreqs --force --encoding utf-8``` to create a requirements.txt file to help you identify the dependencies. See the dependency mapping section towards the end of this guide for more details.
* The ```python_requires = >=3.8``` variable represents the python version required to run your package.
* The ```package_dir = =src``` variable is the source directory of your package.
* The ```packages = find:``` variable is the key command that tells ```setuptools``` to find the resources of your package.

3. ```[options.packages.find]``` - Allows you to specify where you want ```packages = find:``` to find your resources. Typically, you want to store all of your resources in the ```src``` directory. This is how your ```[options.packages.find]``` would look:
```
[options.packages.find]
where = src
```

4. ```[options.entry_points]``` - This is where you define the entry points to your app. Typically, the entry point to your app is ```main.py```. See this guide for more details on [entry points](https://setuptools.pypa.io/en/stable/userguide/entry_point.html).
```
[options.entry_points]
console_scripts =
	pythonstarterpackage = pythonstarterpackage.main:main
```

5. ```[options.package_data]``` - This defines the package data files located inside your package that should be included in the build. Things like app data, assets, environmental variables, etc.
```
[options.package_data]
data =
	data/*.json
```

6. ```[options.data_files]``` - This defines the non-package data files located outside your package that should be included in the build. Things like documentation, configurations, message catalogs, external data, sample data, etc.
```
[options.data_files]
pythonstarterpackage/config = config/config.json
```

### Package Files
Once you have created ```setup.py``` and ```setup.cfg```, you will want to add additional setup files to the package. These typically include the following files.
* .gitignore - Git ignore file for specifying the files that you want git to ignore.
* LICENSE - File defining your package's license.
* README.md - Readme file for documentation.
* requirements.txt - File defining all the requirements of your package.
* test - Directory containing all your test scripts.
* doc - Directory containing all your documentation files.

Take a look at the contents of each of the above files and directories in this package to see how they are structured.

### Application Files
The application files of your package should be located in a directory with the following naming and path convention: ```src/pythonstarterpackage```. This is the core directory containing all the files that make up your program. Each of the directories and subdirectories under ```src/pythonstarterpackage``` should contain an ```__init__.py``` which is what ```setuptools``` will be looking for to know what to include in the build. This is what each of these files do:
* ```__init__.py``` - This allows ```setuptools``` to know what to include in the build.
* ```__main__.py``` - This allows execution on calling the name the directory: ```python3 -m pythonstarterpackage```. See this guide explaining [main](https://stackoverflow.com/questions/4042905/what-is-main-py).
* ```main.py``` - This is the main entry point to your app. This is the file that ```[options.entry_points]``` is pointing to in the ```setup.cfg``` file.
* ```starterpkg.py``` - This is the main python script for our app.
* utils - This is the subdirectory of the ```pythonstarterpackage``` containing utility files for your program.

### Deploying Your Package
Once your package is set up, you are now ready to deploy your package. The remaining section of this guide will go over how to test, map dependencies, deploy, and upload your package to PyPi.

### Testing
Before you deploy your package you need to test it. You can do this by installing your package using ```pip3``` editable mode. This will allow you to make changes to it and test it without having to push the changes each time.
1. Navigate to the directory containing your ```setup.py``` file. Then use ```pip3``` to install the package in editable mode:
```
pip3 install -e .
```
2. Run the package by calling the package directly:
```
pythonstarterpackage
```
Or use ```python3 -m```:
```
python3 -m pythonstarterpackage
```
3. Testing the import. Run the ```test_main.py``` file:
```
python3 ./test/test_main.py
```
4. Once finished, delete the pythonstarterpackage.egg-info file and uninstall the package with:
```
pip3 uninstall PythonStarterPackage
```

Note: It is recommended that you use a virtual environment when testing your package.
1. To create a virtual environment:
```
virtualenv venv
```
2. Activate the environment use: ```. venv/bin/activate```. On Windows it may be: ```. venv/Script/activate```.

### Dependency Mapping
Next, make sure to check the package dependencies and update the ```setup.cfg``` file as needed. To do this:
1. Create (or overwrite) the requirements.txt document with ```pipreqs```. This is an extremely useful tool because it automatically finds all of the relevant versions of dependencies your package relies on and puts them into the ```requirements.txt``` file. If you don't have ```pipreqs```, install it with ```pip install pipreqs```.
```
pipreqs --force --encoding utf-8
```
2. Once the ```requirements.txt``` is updated, check to see if there are additional dependencies that need to be added or updated in setup.cfg under the ```install_requires =```. If so, add or update it.

### Deployment
Once the package is ready, we can work on deploying the package.

1. Upgrade ```setuptools```, ```wheel```, and ```twine``` (```twine``` will be used in the next part).
```
pip3 install --upgrade setuptools wheel twine
```
2. Build the package with ```setup.py```.
```
python3 setup.py sdist bdist_wheel
```
3. Check the contents of the .whl and .tar.gz distributions. The key things to look for are: (1) all of your package subdirectories like utils are added to both distributions, (2) your config and package data are included in both distributions.
```
unzip -l dist/*.whl && tar --list -f dist/*.tar.gz
```
4. Test a local install of the package and run it to make sure it is working.
```
pip3 install .
pythonstarterpackage
```
5. After testing that it is working, uninstall the package from pip3.
```
pip3 uninstall pythonstarterpackage
```
If there are any issues in the above you can always uninstall the package and delete the distributions then proceed to troubleshoot the issue. Once complete start over from the beginning. The commands below allow you to delete the distributions.
```
rm -rf build dist src/*.egg-info
```
BE CAREFUL not to miscopy the above command, as if you delete something you didn't intend you will not be able to retrieve it.

### Upload to PyPi
In order to upload to PyPi make sure to set up your PyPi account first. See [PyPi Setup Guide.md](https://github.com/ArcticTechnology/PythonStarterPackage/blob/main/doc/PyPi_Setup_Guide.md) in ```doc/``` for more details. You will also need to have ```twine``` installed and upgraded. Once you have all of this setup do the following:

1. Upload using ```twine```.
```
twine upload dist/*
```
2. Install your package with ```pip```.
```
pip3 install pythonstarterpackage
```
Note: If you get a "Requirements already satisfied..." for pythonstarterpackage when trying to install, it may be because ```pip``` still thinks you have the package already installed from the testing earlier. To cleanly break that connection, simply delete the ```./src/PythonStarterPackage.egg-info```. Then try uninstalling and reinstalling again.

3. Finally, run the app with: ```pythonstarterpackage```.
4. Uninstall with: ```pip3 uninstall pythonstarterpackage```.

### Result
After completing this guide, you should now have a working python package that you can install with ```pip```. Now you can modify the package with your own code and turn this package into your own package.

