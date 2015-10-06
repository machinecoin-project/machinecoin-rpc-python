#!/usr/bin/env python

from distutils.core import setup

setup(name='python-machinecoinrpc',
      version='0.1',
      description='Enhanced version of python-jsonrpc for use with Machinecoin',
      long_description=open('README').read(),
      author='Juergen Scholz',
      author_email='<j.scholz@machinecoin.org>',
      maintainer='Juergen Scholz',
      maintainer_email='<j.scholz@machinecoin.org>',
      url='https://github.com/machinecoin-project/python-machinecoinrpc',
      packages=['machinecoinrpc'],
      classifiers=['License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)', 'Operating System :: OS Independent'])
