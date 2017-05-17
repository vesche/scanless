#!/usr/bin/env python

from setuptools import setup

setup(
    name='scanless',
    packages=['scanless', 'scanless.cli', 'scanless.scanners'],
    version='1.0.4',
    description='An online port scan scraper.',
    license='Unlicense',
    url='https://github.com/vesche/scanless',
    author='Austin Jackson',
    author_email='austinjackson892@gmail.com',
    entry_points={
        'console_scripts': [
            'scanless = scanless.cli.main:main',
        ]
    },
    install_requires=['beautifulsoup4', 'requests']
)
