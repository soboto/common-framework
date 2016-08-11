import os
import sys
from setuptools import setup, find_packages

if sys.version_info[0] > 2:
    sys.exit('Python > 2 is unsupported.')

setup(
    name='soboto-common-framework',
    version='1.0.0',
    license='Apache License, Version 2.0',

    install_requires=[],

    description='',
    long_description=open('README.md').read(),

    author='Dennis Bunskoek',
    author_email='dbunskoek@leukeleu.nl',

    url='https://github.com/soboto/common-framework',
    download_url='',

    packages=find_packages(),
    include_package_data=True,

    zip_safe=False,
    classifiers=[]
)
