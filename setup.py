from setuptools import find_packages
from distutils.core import setup
from codecs import open
from os import path
from Cython.Build import cythonize
from distutils.extension import Extension

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

extensions = [Extension("*", ["cython_modules/*.pyx"])]

setup (

    ext_modules=cythonize(extensions),

    package_dir={'indoor_ag_controller': ''},

    name='indoor_ag_controller',

    version='0.0.1',

    description='Controls the indoor-ag grow box',
    long_description=long_description,

    # The project's main homepage.
    url='https://github.com/esologic/telapush-application',

    # Author details
    author='Devon Bray',
    author_email='devon@hitchco.xyz',

    classifiers=[
        'Development Status :: 3 - Alpha',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],

    packages=find_packages(exclude=['contrib', 'docs', 'tests']),

    install_requires= [
                            'psutil',
                            'apscheduler',
                            'pygame',
                            'tweepy',
                            'pyserial',
                            'openpyxl',
                            'matplotlib>=2.1.0',
                            'Cython'
                       ]
)