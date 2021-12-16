"""
Flask RESTful Quick Start Setup
"""

import sys
import os
from setuptools import setup
from setuptools import Command
from setuptools.command.test import test as TestCommand
from datetime import datetime

NAME = 'keytop-apis'
VERSION = '1.0'
AUTHOR = 'Amy Jiang'
REQUIRED_PYTHON_VERSION = (3, 0)
PACKAGES = ['']
INSTALL_DEPENDENCIES = [
    'requests'
]
SETUP_DEPENDENCIES = [
]
TEST_DEPENDENCIES = [
    'pytest'

]
EXTRA_DEPENDENCIES = {
    'dev': [
        'pytest'
    ]
}

if sys.version_info < REQUIRED_PYTHON_VERSION:
    sys.exit('Python >= 3 is required. Your version:\n'+sys.version)


class PyTest(TestCommand):
    """
    Use pytest to run tests
    """
    user_options = [('pytest-args=', 'a', "Arguments to pass into py.test")]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args = []

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest
        errno = pytest.main(self.pytest_args)
        sys.exit(errno)


setup(
    name=NAME,
    version=VERSION,
    author=AUTHOR,
    packages=PACKAGES,
    include_package_data=True,
    install_requires=INSTALL_DEPENDENCIES,
    setup_requires=SETUP_DEPENDENCIES,
    tests_require=TEST_DEPENDENCIES,
    extras_require=EXTRA_DEPENDENCIES,
    cmdclass={
        'test': PyTest
    }
)
