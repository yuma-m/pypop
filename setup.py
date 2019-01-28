from setuptools import setup, find_packages
version = '0.1.0'

setup(
    name='pypop',
    version=version,
    description="A python library to compose pop songs automatically.",
    keywords='music pops',
    author='Yuma Mihira',
    url='https://github.com/yuma-m/pypop',
    license='MIT',
    install_requires=[
        'attrs',
        'pychord',
    ],
    packages=find_packages(exclude=['test']),
    long_description=open('README.rst').read(),
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Topic :: Multimedia :: Sound/Audio",
        "License :: OSI Approved :: MIT License",
    ],
)
