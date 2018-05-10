#!/usr/bin/python
from setuptools import setup, Extension
import os
import sys


setup(
    name = 'hidapi_armv7l',
    version = '0.7.99.post21',
    description = """
		A Cython interface to the hidapi from https://github.com/signal11/hidapi
		hidapy and python2,x build on armv7l.
		Raspberry Pi 2B,3B,3B+ / BeagleBone / PocketBeagle / NanoPi / etc... support.		
		""",
    author = 'Y.Kitagami',
    author_email = 'kitagami@artifactnoise.com',
    url = 'https://github.com/nonNoise/cython-hidapi',
    packages=['hidapi_armv7l'],
    package_dir = {'hidapi_armv7l': 'hidapi_armv7l'},
    package_data={'hidapi_armv7l': ['./hidraw.so','./hid.so']},
    classifiers = [
        'Operating System :: Linux :: armv7l',
        'License :: OSI Approved :: BSD License',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    install_requires = ['setuptools>=19.0'],
)
