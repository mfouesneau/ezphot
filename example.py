"""
Examples
"""
from .aperture import *
from .profiles import *
import pylab as plt
from numpy import arange, log10, linspace, cos, sin, pi, hstack, empty, multiply
import numpy as np
from contextManagers import timeit

	
def plotCircularProfile(fnd, cx, cy, rl):
	""" Plot the profile from circular apertures on top of the original image"""
	def plot_circle(x, y, r, ax=None, **kwargs):
		if ax == None:
			ax = plt.gca()
		t = linspace(0,2*pi, 100)
		ax.plot(cx + r*cos(t), cy + r*sin(t), **kwargs)

	with timeit('Profile Measurements'):
		x, r, da = getCircularProfile(fnd.astype(float), float(cx), float(cy), rl.astype(float))


	with timeit('Plotting part'):
		ax = plt.subplot(111)
		ax.imshow(log10(fnd), origin='lower', aspect='equal', cmap=plt.cm.Greys)
		xlim = ax.get_xlim()
		ylim = ax.get_ylim()
		plot_circle(cx,cy, rl[0],  color='0.0', ax=ax, alpha=1.)
		plot_circle(cx,cy, rl[-1], color='0.0', ax=ax, alpha=1.)
		_y = cy + rl[-1]/r.max()*hstack([r[::-1],r])
		_x = cx + hstack([-x[::-1],x])
		ax.step(_x, _y, where='mid', color='r')
		ax.vlines(cx, _y.min(), _y.max(), color='r', linestyles=':')
		ax.hlines(cy, _x.min(), _x.max(), color='r', linestyles=':')
		ax.set_xlim(xlim)
		ax.set_ylim(ylim)

def profile(r0=4, rn=151, dr=1):
	"""An example of profile"""
	import pyfits
	fn = '/home/morgan/Work/profileFit2d/images/12055_M31-B21-F01_1_F475W.fits'
	fnd = pyfits.getdata(fn)
	cx, cy = 160., 160.
	rl = arange(r0,rn, dr, dtype=float)
	plotCircularProfile(fnd, cx, cy, rl)

