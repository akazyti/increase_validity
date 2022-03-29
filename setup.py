from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in increase_validity/__init__.py
from increase_validity import __version__ as version

setup(
	name="increase_validity",
	version=version,
	description="Increase Quotation Validity",
	author="Zaspi Softwares",
	author_email="zaspisoft@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
