# -*- coding:utf-8 -*-
import os
import setuptools
this_directory = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setuptools.setup(
    name="cgai_DD",
    version="0.0.1",
    author="Master Zhang",
    author_email="360014296@qq.com",
    description="Python API for DingDing Group Robot.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/zxzxde/cgai-DD",
    packages=setuptools.find_packages(),
    classifiers=[
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
)