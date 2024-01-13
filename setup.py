from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in gym_app/__init__.py
from gym_app import __version__ as version

setup(
	name="gym_app",
	version=version,
	description="Gym Management system",
	author="Dipen",
	author_email="faldu.faldu1991@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
