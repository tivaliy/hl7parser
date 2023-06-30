#!/usr/bin/env python
import codecs
import os.path
import re

from setuptools import find_packages, setup

here = os.path.abspath(os.path.dirname(__file__))


def read(*parts):
    return codecs.open(os.path.join(here, *parts), "r", encoding="utf-8").read()


def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


install_requires = [
    "hl7apy==1.3.4",
]


setup_options = dict(
    name="hl7parser",
    version=find_version("hl7parser", "__init__.py"),
    description="SDK for HL7 message parsing.",
    long_description=read("README.md"),
    author="Vitalii Kulanov",
    url="https://e2f.com",
    entry_points={
        "console_scripts": [
            "hl7parser=hl7parser.__main__:main",
        ],
    },
    packages=find_packages(exclude=["tests*"]),
    include_package_data=True,
    install_requires=install_requires,
    extras_require={},
    license="Apache License 2.0",
    python_requires=">= 3.9",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: Healthcare Industry",
        "Intended Audience :: Science/Research",
        "Natural Language :: English",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Communications",
        "Topic :: Scientific/Engineering :: Medical Science Apps.",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)

setup(**setup_options)
