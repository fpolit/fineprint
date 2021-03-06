#!/usr/bin/env python3


import setuptools

with open("README.md", "r") as readme:
    long_description = readme.read()
    
    
setuptools.setup(
    name="fineprint",
    version="1.0.4",
    author="glozanoa",
    author_email="glozano@uni.pe",
    description="Pretty print text.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/fpolit/fineprint",
    install_requires = [
        'colorama',
    ],
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
