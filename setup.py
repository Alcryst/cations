from setuptools import setup

setup(
	name = 'cations',
	version = '1.0.0',
	packages = ['cations_dir'],
	entry_points = {
		'console_scripts': [
			'cations = cations_dir.__main__:main'
		]
	})
