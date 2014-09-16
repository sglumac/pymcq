#!/usr/bin/env python
# -*- coding: utf-8 -*-


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

requirements = [
]

test_requirements = [
    'nose'
]

setup(
    name='pymcq',
    version='0.1.0',
    description='This is a project that integrates latex exam into pyhon for easier creating of mcq tests.',
    long_description=readme + '\n\n' + history,
    author='Slaven Glumac',
    author_email='slaven.glumac@gmail.com',
    url='https://github.com/sglumac/pymcq',
    packages=[
        'pymcq',
    ],
    package_dir={'pymcq': 'pymcq'},
    include_package_data=True,
    install_requires=requirements,
    license="MIT",
    zip_safe=False,
    keywords='pymcq',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2.7',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
