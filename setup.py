# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in warranty_management_system/__init__.py
from warranty_management_system import __version__ as version

setup(
	name='warranty_management_system',
	version=version,
	description='Warranty Management System',
	author='Jigar Tarpara',
	author_email='jigartarpara68@gmail.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
