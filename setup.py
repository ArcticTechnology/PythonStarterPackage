from setuptools import setup
from setuptools import find_packages

# Load the README file.
with open(file='README.md', mode='r') as readme_handle:
	long_description = readme_handle.read()

setup(

	# Define the library name, this is what is used along with `pip install`.
	name='PythonStarterPackage',

	# Define the Author of the repository.
	author='Arctic',

	# Define the Author's email, so people know who to reach out to.
	author_email='arctic.technology.mail@gmail.com',

	# Define the version of this library.
	# Read this as
	#- MAJOR VERSION 0
	#- MINOR VERSION 1
	#- MAINTENANCE VERSION 0
	version='0.1.2',

	license='MIT',

	# Define a small description of the library. This appears
	# when someone searches for the library on https://pypi.org/search.
	description='A python starter package to be used as a template for creating your own python packages.',

	# Define a long description which is set to README file.
	long_description=long_description,

	# Specifies that the long description is a MARKDOWN.
	long_description_content_type='text/markdown',

	# Define the URL of the GitHub.
	url='https://github.com/ArcticTechnology/PythonStarterPackage',

	# Define the dependencies the library needs in order to run.
	install_requires=[
		'setuptools>=49.2',
	],

	# Define the keywords of the library.
	keywords='starter, package, template',

	# Define the package dir.
	package_dir={'': 'src'},

	# Define the packages to "build."
	packages=find_packages(where='src'),

	# # Define any package data.
	# package_data={
	#	 # And include any files found subdirectory of the "td" package.
	#	 "td": ["app/*", "templates/*"],
	# },

	# Define whether any package data should be included, like photos and JSON files.
	include_package_data=True,

	# Define the python version necessary to run this library.
	python_requires='>=3.8',

	# Define classifiers that give some characteristics about the package.
	# For a complete list go to https://pypi.org/classifiers/.
	classifiers=[
		# Define phase of development the library is in.
		'Development Status :: 3 - Alpha',
		#'Development Status :: 4 - Beta',
		#'Development Status :: 5 - Production/Stable',


		# Define the audience this library is intended for.
		'Intended Audience :: Developers',
		'Intended Audience :: Science/Research',
		'Intended Audience :: Financial and Insurance Industry',

		# Define the license that guides the library.
		'License :: OSI Approved :: MIT License',

		# Define the natural language.
		'Natural Language :: English',

		# Define the operating system that can use this library.
		#'Operating System :: POSIX :: Linux',
		#'Operating System :: Microsoft :: Windows',
		#'Operating System :: MacOS',
		'Operating System :: OS Independent',

		# Define the version of Python.
		'Programming Language :: Python',
		'Programming Language :: Python :: 3',
		'Programming Language :: Python :: 3.8',

		# Define the topics that the library covers.
		'Topic :: Database',
		'Topic :: Education',
		'Topic :: Office/Business'
	]
)