#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Setup file
'''

import sys
from setuptools import setup


def setup_package():
    entry_points = {
        'console_scripts': [
            'mypkg = mypkg.run:main',
        ],
    }

    package_data = {
        'mpykg': ['configs/*.yml'],
    }

    setup(
        name='mypkg',
        url='github.com/myorg/mypkg',
        version='0.1.0',
        packages=['mypkg'],
        package_data=package_data,
        entry_points=entry_points,
        # install_requires=['dep==0.1.0'],
    )


if __name__ == '__main__':
    setup_package()

