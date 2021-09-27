from setuptools import find_packages, setup

setup(
    name='vinculum',
    packages=find_packages(include=['vinculum']),
    version='0.1.0',
    description='Various utilities and functions to make Vinculum stuff easier',
    author='Isaac FLath',
    license='MIT',
    install_requires=['fastcore','nbformat','requests','pandas','numpy','scipy','shelve','matplotlib'],
    setup_requires=['fastcore','nbformat','requests','pandas','numpy','scipy','shelve','matplotlib'],
    tests_require=['fastcore','nbformat','requests','pandas','numpy','scipy','shelve','matplotlib'],
    test_suite='tests',
)