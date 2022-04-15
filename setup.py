#!/usr/bin/env python
"""This module contains setup instructions for YTVD."""
import codecs
import os

from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

with open(os.path.join(here, "pytube", "version.py")) as fp:
    exec(fp.read())

setup(
    name="YTVD",
    version=__version__,  # noqa: F821
    author="Valerii Goncharuk",
    author_email="lera.goncharuk@gmail.com",
    packages=["ytvd"],
    package_data={"": ["LICENSE"]},
    url="https://github.com/tagezi/ytvd",
    license="GPL 3.0",
    entry_points={
        "console_scripts": [
            "ytvd = ytvd:__main__"]},
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GPL 3.0",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python",
        "Topic :: Internet",
        "Topic :: Multimedia :: Video",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Terminals",
        "Topic :: Utilities",
    ],
    description="Python 3 library for downloading YouTube Videos.",
    include_package_data=True,
    long_description_content_type="text/markdown",
    long_description=long_description,
    zip_safe=True,
    python_requires=">=3.6",
    project_urls={
        "Bug Reports": "https://github.com/tagezi/ytvd/issues",
        "Read the Docs": "https://github.com/tagezi/ytvd",
    },
    keywords=["youtube", "download", "video", "playlist", "channel"],
)
