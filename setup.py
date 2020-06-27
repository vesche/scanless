#!/usr/bin/env python

from setuptools import setup

setup(
    name='scanless',
    packages=[
        'scanless',
        'scanless.static'
    ],
    package_data = {
        'scanless.static': ['*.txt']
    },
    version='2.1.3',
    description='An online port scan scraper.',
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
        'Programming Language :: Python :: 3.8',
        'Topic :: Security'
    ]
)
