# -*- coding: UTF-8 -*-

__author__ = 'wangjing'

from distutils.core import setup
from setuptools import find_packages
import sys


_version = '0.1'
_packages = find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"])

_short_description = "pylint-redis is a Pylint plugin to aid Pylint in recognising and understanding" \
                     " dangerous function calls caused when using the redis-py and other python redis library"


_classifiers = (
    'Development Status :: 4 - Beta',
    'Environment :: Console',
    'Intended Audience :: Developers',
    'Operating System :: Unix',
    'Topic :: Software Development :: Quality Assurance',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3.3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
)


_install_requires = [
    'pylint-plugin-utils>=0.2.1',
    'pylint>=1.6',
]

setup(
    name='pylint-redis',
    url='https://github.com/wangjild/pylint-redis',
    author='wangjing',
    author_email='wangjild@gmail.com',
    description=_short_description,
    version=_version,
    packages=_packages,
    install_requires=_install_requires,
    license='GPLv3',
    classifiers=_classifiers,
    keywords='pylint redis plugin',
    zip_safe=False,
)
