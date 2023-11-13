from setuptools import setup, find_packages

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name="math_quiz",
    version="1.0",
    author="Neelima Kawatra"
    packages=find_packages(),
    install_requires = required
)
