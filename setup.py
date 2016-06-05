from setuptools import setup
import codecs
import os
import re

def get_version():
    with open('pingdomexport/__init__.py', 'r') as fd:
        return re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', fd.read(), re.MULTILINE).group(1)

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
    version=get_version(),
    url='https://github.com/entering/pingdomexport',
    description='Export your pingom data to CSV or database',
    long_description=read_description('README.rst'),
    author='Eduardo Oliveira',
    author_email='me@eduardooliveira.net',
    license='MIT',
    keywords='pingdom export mysql postgres',
    packages=['pingdomexport', 'pingdomexport.load'],
    scripts=['pingdom-run-export'],
    install_requires=read_requirements('requirements.txt'),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: MIT License',
        'Topic :: Utilities',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5'
    ]
)
