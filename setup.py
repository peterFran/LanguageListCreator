#!/usr/bin/env python

from distutils.core import setup

setup(name='langtools',
      version='1.0',
      description='Language Translation Tools',
      author='Peter Meckiffe',
      author_email='peterf.meckiffe@gmail.com',
      url='https://www.github.com/peterFran/LanguageListCreator',
      packages=['langtools'],
      package_data={'langtools': ['dictionary/dic/*', 'classify/tagger/*']}
     )