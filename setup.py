# -*- coding: utf-8 -*-

from distutils.core import setup

import image_group_util

NAME = 'image_group_util'
VERSION = image_group_util.__version__
URL = 'https://github.com/Neubias-WG5/ImageGroupUtil'
AUTHOR = "Benjamin Pavie"
AUTHOR_EMAIL = "benjamin.pavie[_at_]kuleuven.vib.be"
DESCRIPTION = 'Library containing utility to download Image Group with their annotation, labels etc...'
with open('README.md') as f:
    LONG_DESCRIPTION = f.read()
CLASSIFIERS = [
    'Intended Audience :: Developers',
    'Intended Audience :: Science/Research',
    'Operating System :: OS Independent',
    'Programming Language :: Python :: 3.5',
    'Topic :: Scientific/Engineering',
    'Topic :: Utilities'
]

if __name__ == '__main__':
    setup(name=NAME,
          version=VERSION,
          author=AUTHOR,
          author_email=AUTHOR_EMAIL,
          url=URL,
          description=DESCRIPTION,
          long_description=LONG_DESCRIPTION,
          classifiers=CLASSIFIERS,
          platforms='any',
          install_requires=[],
          packages=['image_group_util'])