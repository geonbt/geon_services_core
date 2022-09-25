from setuptools import setup, find_packages
import codecs
import os


VERSION = '0.1'
DESCRIPTION = 'A package GEON IT Corp. uses for themselves'

# Setting up
setup(
    name="geon_services_core",
    version=VERSION,
    author="Ömer Selçuk Çetin",
    author_email="<omerselcukcetin@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=['flask_restx', 'collections', 'werkzeug', 'flask_restx', 'flask', 'flask_jwt_extended', 'flask_login', 'sqlalchemy', 'json', 'requests'],
    keywords=['python', 'gis', 'qgis', 'geon', 'qwc2'],
    classifiers=[
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)