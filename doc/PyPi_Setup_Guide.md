## PyPi Setup Guide
PyPi is the python package index for people to upload their packages for anyone to use.

### Account Setup
1. Go to pypi.org and create an account, make sure to validate your email.
2. Once your account is created, go to Account Settings and create an API token. Your api token will look like this ```pypi-OFJou945u2fd0i94u93ut....```.
3. Create a ```.pypirc``` file in your home directory. The ```.pypirc``` file allows you to define the configuration for package indexes, so that you don’t have to enter the URL, username, or password whenever you upload a package. Now the location of this file is very important in most cases it is your home directory. That is where ```twine``` will look for the ```.pypirc``` file. See this [twines install guide](https://github.com/areed1192/sigma-coding/blob/master/resources%20and%20note/installation_twines.md) for more details.
4. In your ```.pypirc``` add the following. Note that the password is your api token.
```
[distutils]
index-servers=
		pypi
		testpypi
		pypi-username
		testpypi-username
[pypi]
username = __token__
password = pypi-OFJou945u2fd0i94u93ut....
```
If you have a testpypi account with a test api token you can add it to ```.pypirc``` as well.
```
[testpypi]
username = __token__
password = pypi-OFJou945u2fd0i94u93ut....
```

### Result
Now your account should be all setup and ready to be used to upload to PyPi.