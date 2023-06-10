# Python Starter Package
The purpose of this project is to show you how to create a standard python package from scratch. This project is inspired by this excellent getmyip package by @iamtennislover: [https://github.com/iamtennislover/getmyip] and this great guide on deploying python packages by @sigma-coding: [https://github.com/areed1192/sigma-coding].

See "PythonStarterPackage Tutorial.md" in the ```doc/``` directory for a step-by-step setup guide and a detailed explanation of the package resources.

This package can also be used as the skeleton for when you first start building your own packages. To do this, follow the instructions below to install and test this package. 

Below are the Github and PyPi resources for this package.
* Github repo: https://github.com/ArcticTechnology/PythonStarterPackage
* PyPi: https://pypi.org/project/PythonStarterPackage/

## Prerequisites
For Windows, it is recommended to run this app on a Linux emulation layer such as the Git Bash terminal. See the "Instructions for Git Bash" section for details. In addition to Git Bash, make sure you also have Python3 and Pip3 as described below.

For Mac and Linux, this app should work out of the box on the Linux or Mac terminal, but make sure you also have Python3 and Pip3 as described below.

Requirements:
* Python3 (version 3.8 or greater) - Install Python3 here: [https://www.python.org/downloads/]. Check version with: ```python3 --version```.
* Pip3 (version 20.2.1 or greater) - Make sure to install python3-pip in order to use pip install. Check version with: ```pip3 --version```.

## Installation
There are a couple of options to install this app:
* Pip Install - This app is hosted on PyPi and can be installed with the following command:
```
pip3 install PythonStarterPackage
```
* Local Install - Alternatively, you can download or git clone the Github repo and install it locally with the following:
```
git clone https://github.com/ArcticTechnology/PythonStarterPackage.git
cd PythonStarterPackage
pip3 install -e .
```
To uninstall this app:
```
pip3 uninstall PythonStarterPackage
```
* If you used the local install option, you will also want to delete the ```.egg-info``` file located in the ```src/``` directory of the package. This gets created automatically with ```pip3 install -e .```.

## Usage
After installation, you have a few ways to run this app.
* Run this app from the terminal with this command:
```
pythonstarterpackage
```
* Run this app with the python command ```python3 -m```:
```
python3 -m pythonstarterpackage
```
* You can also import the package resources and run them in your own project:
```
from pythonstarterpackage import *
starter = StarterPkg()
starter.run()
```

## Documentation
To deploy this package, first, make sure you have gone through the "PythonStarterPackage Tutorial.md" in the ```doc/``` directory. Once you have a good understanding of how to implement your own package and assuming you have mapped dependencies and tested the package, you can use the following to deploy your package.

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
In order to upload to PyPi make sure to set up your PyPi account first. See "PyPi Setup Guide.md" in ```doc/``` for more details. You will also need to have ```twine``` installed and upgraded. Once you have all of this setup do the following:

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

## Troubleshooting
This section goes over some of the common issues found and how to resolve them.

### "Command Not Found" Error When Running the App
On Linux, if you are getting a ```command not found``` error when trying to run the app, you may need to add ```~/.local/bin/``` to PATH. See this thread for details: [https://stackoverflow.com/a/34947489]. To add ```~/.local/bin/``` to PATH do the following:

1. Add ```export PATH=~/.local/bin:$PATH``` to ```~/.bash_profile```.
```
echo export PATH=~/.local/bin:$PATH > ~/.bash_profile
```
2. Execute command.
```
source ~/.bash_profile
```

### "ImportError: No module named 'tkinter'
Your python version is probably missing tkinter which typically comes default. See this post for details [https://stackoverflow.com/a/25905642]. Install it with the following:
```
sudo apt-get install python3-tk
```
For Mac, use this:
```
brew install python-tk
```

### Instructions for Git Bash
For Windows, it is recommended to run this app on a linux emulation layer like the Git Bash terminal. Here are the instructions for installing and setting up Git Bash:
1. Go to https://git-scm.com/downloads and click download.
```
Version >= 2.34.1
```
2. During the installation setup, make sure to include OpenSSH. The recommended setting should be fine:
```
Use bundled OpenSSH - This uses ssh.exe that comes with Git.
```
3. Leave the other settings as default, click through, and install.
4. Open ```bash.exe``` and install Python3 https://www.python.org/downloads/
5. Proceed to the "Installation" section to install this app.

IMPORTANT: For Windows, use the ```bash.exe``` terminal rather ```git-bash.exe```. There is a known issue with ```git-bash.exe``` messing up Python ```os``` commands in ```import os```. See this thread for details: [https://stackoverflow.com/a/33623136].
* You can find ```bash.exe``` Git folder in the ```bin/``` directory. For example: If ```git-bash.exe``` is here ```C:\Program Files\Git\git-bash.exe``` then you should find ```bash.exe``` here ```C:\Program Files\Git\bin\bash.exe```.

## Support and Contributions
Our software is open source and free for public use. If you found any of these repos useful and would like to support this project financially, feel free to donate to our bitcoin address.

Bitcoin Address 1: 1GZQY6hMwszqxCmbC6uGxkyD5HKPhK1Pmf

![alt text](https://github.com/ArcticTechnology/BitcoinAddresses/blob/main/btcaddr1.png?raw=true)
