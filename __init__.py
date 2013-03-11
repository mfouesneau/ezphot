import inspect, os
localpath = '/'.join(os.path.abspath(inspect.getfile(inspect.currentframe())).split('/')[:-1])
__version__ = '0.0dev'
__doc__ = open(localpath+'/README.rst').read()

from .aperture import *
from .profiles import *
import example


