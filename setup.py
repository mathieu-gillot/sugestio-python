#!/usr/bin/env python
#from distutils.core import setup
from setuptools import setup, find_packages

setup(name="sugestio",
      version="0.4",
      description="Sugestio library for python",
      url="http://github.com/sugestio/sugestio-python",
      packages=find_packages(),
      install_requires=['oauth2','urllib','csv','simplejson'],
      license = "MIT License",
      keywords="sugestio recommendations library")
