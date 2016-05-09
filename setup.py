#!/usr/bin/env python

from distutils.core import setup

setup(
    name='python-machinecoinrpc',
    version='0.3',
    description='Enhanced version of python-jsonrpc for use with Machinecoin',
    long_description=open('README.rst').read(),
    author='Jeff Garzik',
    author_email='jgarzik@pobox.com',
    maintainer='Juergen Scholz',
    maintainer_email='jscholz@machinecoin.org',
    url='https://github.com/machinecoin-project/machinecoin-rpc-python',
    packages=['machinecoinrpc'],
    classifiers=[
        'License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)', 'Operating System :: OS Independent'
    ]
)
