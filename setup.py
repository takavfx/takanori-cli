import os
from setuptools import setup
from setuptools import find_packages

here = os.path.abspath(os.path.dirname(__file__))

def _read_requirements(file):
    with open(file, encoding='utf-8') as f:
        return f.readlines()

about = {}
with open(os.path.join(here, 'takanoricli', '__init__.py'), 'r', encoding='utf-8') as f:
    exec(f.read(), about)

setup(
    name=about['__title__'],
    version=about['__version__'],
    url=about['__url__'],
    description=about['__description__'],
    install_requires=_read_requirements('requirements/requirements.txt'),
    test_requirements=_read_requirements('requirements/requirements_test.txt'),
    python_requires='>=3.7.*',
    packages=['takanoricli'],
    package_dir={"takanoricli": "takanoricli"},
    entry_points={
        'console_scripts': [
            'taka = takanoricli.cli:main'
        ]
    },
)