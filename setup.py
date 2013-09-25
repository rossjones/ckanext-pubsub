from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(
	name='ckanext-pubsub',
	version=version,
	description="pubsub notifications of package updates",
	long_description="""\
	""",
	classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
	keywords='',
	author='Ross Jones',
	author_email='ross@servercode.co.uk',
	url='https://github.com/rossjones/ckanext-pubsub',
	license='',
	packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
	namespace_packages=['ckanext', 'ckanext.pubsub'],
	include_package_data=True,
	zip_safe=False,
	install_requires=[

	],
	entry_points=\
	"""
        [ckan.plugins]
		pubsub=ckanext.pubsub.plugin:PubSubPlugin
	""",
)
