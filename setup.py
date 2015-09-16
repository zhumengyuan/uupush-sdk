#!/usr/bin/env python

import os
from setuptools import setup, find_packages


here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.md')).read()

requires = [
    'requests',
]

# Use part of the sphinx docs index for the long description

setup(
    name="uupush-sdk",
    version='0.0.1',
    packages=find_packages(),
    install_requires=requires,
    description='uucin push sdk',
    long_description=README,
    author="liulinlin",
    author_email="liulinlin@zhumengyuan.com",
    license="BSD",
    url="https://github.com/zhumengyuan/uucin-sdk",
    include_package_data=True,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Framework :: Django",
    ]
)
