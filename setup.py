#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup
from scanless import __version__

setup(
    name='scanless',
    packages=['scanless', 'scanless.scanners'],
    version=__version__,
    description='An online port scan scraper.',
    license='Unlicense',
    url='https://github.com/vesche/scanless',
    author='Austin Jackson',
    author_email='vesche@protonmail.com',
    entry_points={
        'console_scripts': [
            'scanless = scanless.scanless:main',
        ]
    },
    install_requires=['beautifulsoup4', 'requests'],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Intended Audience :: Information Technology",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Topic :: Security"
    ]
)