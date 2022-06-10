from setuptools import setup


def read_requirements(file):
    with open(file, encoding='utf-8') as f:
        return f.readlines()


setup(
    install_requires=read_requirements('requirements/base.txt')
)
