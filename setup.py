#!/usr/bin/env python
"""The setup and build script for the python-telegram-bot library."""

import codecs
import os
from setuptools import setup, find_packages


def requirements():
    """Build the requirements list for this project"""
    requirements_list = []

    with open('requirements.txt') as requirements:
        for install in requirements:
            requirements_list.append(install.strip())

    return requirements_list

with codecs.open('README.rst', 'r', 'utf-8') as fd:
    execfile(os.path.join('telegram', 'version.py'))

    setup(name='python-telegram-bot',
          version=__version__,
          author='Leandro Toledo',
          author_email='devs@python-telegram-bot.org',
          license='LGPLv3',
          url='https://github.com/python-telegram-bot/python-telegram-bot',
          keywords='python telegram bot api wrapper',
          description='Not just a Python wrapper around the Telegram Bot API',
          long_description=fd.read(),
          packages=find_packages(exclude=['tests*']),
          install_requires=requirements(),
          include_package_data=True,
          classifiers=[
              'Development Status :: 5 - Production/Stable',
              'Intended Audience :: Developers',
              'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)',
              'Operating System :: OS Independent',
              'Topic :: Software Development :: Libraries :: Python Modules',
              'Topic :: Communications :: Chat',
              'Topic :: Internet',
              'Programming Language :: Python',
              'Programming Language :: Python :: 2',
              'Programming Language :: Python :: 2.6',
              'Programming Language :: Python :: 2.7',
              'Programming Language :: Python :: 3',
              'Programming Language :: Python :: 3.3',
              'Programming Language :: Python :: 3.4',
              'Programming Language :: Python :: 3.5',
          ],)
