try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import codecs
import os
import re

def read_description(filename):
    with codecs.open(filename, encoding='utf-8') as f:
        return f.read()

def read_requirements(filename):
    try:
        with open(filename) as f:
            return f.read().splitlines()
    except IOError:
        import os
        raise IOError(os.getcwd())

setup(
    name='pingdomexport',
    version='0.1',
    url='https://github.com/entering/pingdomexport',
    description='Export your pingom data',
    long_description=read_description('README.rst'),
    author='Eduardo Oliveira',
    author_email='me@eduardooliveira.net',
    license='MIT',
    packages=['pingdomexport'],
    entry_points="""
        [console_scripts]
        pingdomexport=pingdomexport.cli:cli
    """,
    install_requires=read_requirements('requirements.txt'),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: MIT License',
        'Topic :: Monitoring',
        'Topic :: Utilities',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5'
    ]
)
