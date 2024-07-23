from setuptools import setup

setup(
	name = 'cations',
	version = '1.0.0',
	packages = ['cations-dir'],
	entry_points = {
		'console_scripts': [
			'cations = cations.__main__:main'
		]
	})