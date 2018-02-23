#!/usr/bin/env python

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
    install_requires=['beautifulsoup4', 'requests']
)
