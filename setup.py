import os
from setuptools import setup


def _read_requirements(file):
    with open(file, encoding='utf-8') as f:
        return f.readlines()


setup(
    name="takanori-cli",
    install_requires=_read_requirements('requirements/base.txt'),
    test_requirements=_read_requirements('requirements/test.txt'),
)
