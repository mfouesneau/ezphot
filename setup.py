#!/usr/bin/env python

from distutils.core import setup, Extension
from Cython.Distutils import build_ext
import numpy.distutils.misc_util


c_ext = [
         Extension("circular_exact", ["circular_exact.pyx"]),
         Extension("elliptical_exact", ["elliptical_exact.pyx"]),
         Extension("downsample", ["downsample.pyx"])
	 ]

py_modules = ["aperture", "profiles", "example"]

setup(
        name="apphot",
	version='0.0dev',
	author="Morgan Fouesneau",
    	author_email="mfouesn@uw.edu",
	py_modules=py_modules,
	description="Python module for aperture photometry based on astropy",
	long_description=open("README.rst").read(),
        cmdclass={"build_ext": build_ext},
        ext_modules=c_ext,
        include_dirs=numpy.distutils.misc_util.get_numpy_include_dirs(),
	classifiers=[
		"Development Status :: 0 - Beta",
		"Intended Audience :: Science/Research",
		"Operating System :: OS Independent",
		"Programming Language :: Python",
	    ],
    )

# python setup.py build_ext --inplace
