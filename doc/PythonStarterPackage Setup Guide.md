## PythonStarterPackage Setup Guide
This guide will go over in depth what each of the contents in the PythonStarterPackage.

### Setup Files
The setup.py and setup.cfg files are the core files that allow setuptools to build this package. See this guide on building and distributing packages with setuptools: https://setuptools.pypa.io/en/latest/userguide/quickstart.html

#### setup.py
The setup.py file is the actual script that gets called when building the package with ```python3 setup.py sdist bdist_wheel```. In the past the configurations are written directly in setup.py, however convention has transitioned from hardcoding configurations into setup.py directly. There should only be one line of code in setup.py which is as follows:
```
from setuptools import setup; setup()
```

#### setup.cfg
Rather than hardcoding setup.py the convention is to put the package configuration details into setup.cfg This is often referred to as the declarative setup. The following will go over the specific instructions that setup.cfg file often contains. See this guide for more details: https://setuptools.pypa.io/en/latest/userguide/declarative_config.html

1. ```[metadata]``` - This section contains all of the key metadata of the package such as name, version, license, etc.
```
[metadata]
name = PythonStarterPackage
version = 0.1.1
author = Arctic
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
* ```version``` - Follows the convention: major.minor.maintenance
* ```classifiers``` - See https://pypi.org/classifiers/ for list of classifiers.
* Deployment status classifiers:
```
Development Status :: 3 - Alpha
Development Status :: 4 - Beta
Development Status :: 5 - Production/Stable
```

2. ```[options]``` - This section contains the critical configurations that tells setuptools what dependencies the package has, which python version the package requires, where to find the package, etc.
```
[options]
install_requires =
	setuptools>=59.5
python_requires = >=3.8
package_dir = =src
packages = find:
```
* ```install_requires =``` - Here you can list all of your package dependencies. The ```pipreqs``` tool makes it easy to map your package dependencies. Simply use ```pipreqs --force --encoding utf-8``` to create a requirements.txt file to help you identify the dependencies.
* ```python_requires = >=3.8``` - Python version required to run your package.
* ```package_dir = =src``` - This is the source directory of your package.
* ```packages = find:``` - This is the key command that tells setuptools to find the resources of your package.

3. ```[options.packages.find]``` - Allows you to specify where you want ```packages = find:``` to find your resources.
```
[options.packages.find]
where = src
```

4. ```[options.entry_points]``` - This is where you define the entry points to your app. See this guide for more on entry points: https://setuptools.pypa.io/en/stable/userguide/entry_point.html
```
[options.entry_points]
console_scripts =
	pythonstarterpackage = pythonstarterpackage.main:main
```

5. ```[options.package_data]``` - This defines files located inside your package that should be included in the build. Things like app assets, environmental variables, photos, etc.
```
[options.package_data]
data =
	data/*.json
```

6. ```[options.data_files]``` - This defines the files located outside your package that should be included in the build. Things like configurations, message catalogs, external data, sample data, etc.
```
[options.data_files]
pythonstarterpackage/config = config/config.json
```

### Package Files
Outside of setup.py and setup.cfg, additional package files include the following:
* .gitignore - Git ignore file for specifying the files that you want git to ignore.
* LICENSE - File defining your package's license.
* README.md - Readme file for documentation.
* requirements.txt - File defining all the requirements of your package.
* test - Directory containing all your test scripts.
* doc - Directory containing all your documentation files.

### Application Files
The application files are located in src/pythonstarterpackage. This is the core directory containing all the files that make up your program. Each of the directories and subdirectories under src/pythonstarterpackage should contain an ```__init__.py``` which is what setuptools will be looking for to know what to include in build.
* ```__init__.py``` - This allows setuptools to know what to include in build.
* ```__main__.py``` - This allows execution on calling the name the directory: ```python3 -m pythonstarterpackage```. See: https://stackoverflow.com/questions/4042905/what-is-main-py
* ```main.py``` - This is the main entry point to your app. This is the file that ```[options.entry_points]``` is pointing to in the setup.cfg file.
* ```starterpkg.py``` - This is the the main python script for our app.
* utils - This is the subdirectory of the pythonstarterpackage containing utility files for your program.

### Result
Once the PythonStarterPackage is setup you should be ready to use this as a template to create your own package.
