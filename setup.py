from setuptools import setup, find_packages
version = '0.1.1'

setup(
    name='pypop',
    version=version,
    description="A python library to compose pop songs automatically.",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Yuma Mihira',
    keywords='music pops',
    url='https://github.com/yuma-m/pypop',
    license='MIT',
    python_requires='>=3.6',
    install_requires=[
        'attrs',
        'pychord',
    ],
    packages=find_packages(exclude=['test']),
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Topic :: Multimedia :: Sound/Audio",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
)
