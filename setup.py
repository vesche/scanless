#!/usr/bin/env python

import os
from setuptools import setup

directory = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='scanless',
    packages=[
        'scanless',
        'scanless.static'
    ],
    package_data = {
        'scanless.static': ['*.txt']
    },
    version='2.1.5',
    description='An online port scan scraper.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    license='Unlicense',
    url='https://github.com/vesche/scanless',
    author='Austin Jackson',
    author_email='vesche@protonmail.com',
    entry_points={
        'console_scripts': [
            'scanless = scanless.cli:main',
        ]
    },
    install_requires=[
        'beautifulsoup4',
        'crayons',
        'requests'
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Information Technology',
        'License :: Public Domain',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.9',
        'Topic :: Security'
    ]
)