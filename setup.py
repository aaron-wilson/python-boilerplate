#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Setup file
"""

import sys
from setuptools import setup, find_packages


def setup_package():
    entry_points = {
        "console_scripts": [
            "mypkg = mypkg.cli:main",
        ],
    }

    package_data = {
        "mpykg": ["configs/*.yml"],
        # "": ["*"],
    }

    setup(
        name="mypkg",
        url="github.com/myorg/mypkg",
        version="0.1.0",
        packages=["mypkg"],
        # packages=find_packages(exclude="tests"),
        package_data=package_data,
        # include_package_data=True,
        entry_points=entry_points,
        # install_requires=["dep==0.1.0"],
    )


if __name__ == "__main__":
    setup_package()
