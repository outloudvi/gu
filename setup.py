#!/usr/bin/env python
# coding: utf-8

from gu.version import __version__, __description__

try:
    from setuptools import setup, Command
    setuptools_available = True
except ImportError:
    from distutils.core import setup, Command
    setuptools_available = False


setup(
    name='gu-cli',
    version=__version__,
    description=__description__,
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url='https://github.com/outloudvi/gu',
    author='Outvi V',
    author_email='git+oss@outv.im',
    license='MIT',
    packages=['gu', 'gu.sender'],
    scripts=['bin/gu'],
    install_requires=[
        'PyYAML',
    ],
    classifiers=[
        'Topic :: Communications',
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Console',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8'
    ])
