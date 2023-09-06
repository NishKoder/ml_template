from setuptools import setup, find_packages

setup(
    name='census-income',
    version='1.0.0',
    author='Nishant',
    author_email='nishant@email.com',
    packages=find_packages(),
    install_requires=['pandas','numpy','pymongo']
)