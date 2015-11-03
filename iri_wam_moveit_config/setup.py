#!/usr/bin/env python

from distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup

d = generate_distutils_setup(
   ##  don't do this unless you want a globally visible script
   #scripts=['bin/package_name'], 
   #packages=['iri_info_gain_demo'],
   packages=['simple_example'],
   package_dir={'': 'scripts'},
   requires=[]
)

setup(**d)

