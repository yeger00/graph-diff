#!/usr/bin/env python
import sys

from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand

with open("README.md", "r") as fh:
    long_description = fh.read()

class PyTest(TestCommand):
    user_options = [("pytest-args=", "a", "Arguments to pass to pytest")]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args = []

    def run_tests(self):
        # import here, cause outside the eggs aren't loaded
        import pytest
        errno = pytest.main(self.pytest_args)
        sys.exit(errno)

setup(
    name="graphdiff",
    version="0.0.4",
    author="Avi Yeger",
    author_email="yeger00@gmail.com",
    description="",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yeger00/",
    packages=find_packages(),
    install_requires=["pydot"],
    tests_require=["pytest", "pytest_mock"],
    cmdclass={"test": PyTest},
)
