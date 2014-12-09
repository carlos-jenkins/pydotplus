#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2014 Carlos Jenkins <carlos@jenkins.co.cr>
# Copyright (c) 2014 Lance Hepler
# Copyright (c) 2004-2011 Ero Carrera <ero@dkbza.org>
# Copyright (c) 2004-2007 Michael Krause <michael@krause-software.de>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

from setuptools import setup, find_packages


def find_version(filename):
    import os
    import re

    here = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(here, filename)) as fd:
        version_match = re.search(
            r"^__version__ = ['\"]([^'\"]*)['\"]", fd.read(), re.M
        )
        if version_match:
            return version_match.group(1)
    raise RuntimeError('Unable to find version string.')


def find_requirements(requirements):
    import string
    with open(requirements, 'r') as fd:
        reqs = []
        for line in fd:
            line = line.strip()
            if line and line[:1] in string.ascii_letters:
                reqs.append(line)
    return reqs


setup(
    name='pydotplus',
    version=find_version('lib/pydotplus/version.py'),
    package_dir={'': 'lib'},
    packages=find_packages('lib'),

    # Dependencies
    install_requires=find_requirements('requirements.txt'),

    # Metadata
    author='PyDotPlus Developers',
    author_email='carlos@jenkins.co.cr',
    description='Python interface to Graphviz\'s Dot language',
    long_description=open('README.rst', 'r').read(),
    url='http://pydotplus.readthedocs.org/',

    keywords='graphviz dot graphs visualization',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Scientific/Engineering :: Visualization',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
)
