from .aperture import CircularAperture, CircularAnnulus, aperture_photometry
from numpy import empty, multiply

def getCircularProfile(fnd, cx, cy, rl):
	""" Get a circular aperture profile centered on cx, cy
	INPUTS:
		np.ndarray[DTYPE_t, ndim=2] fnd		image
		DTYPE_t cx, 				center x [pixels]
		DTYPE_t cy, 				center y [pixels]
		np.ndarray[DTYPE_t, ndim=1] rl		aperture list [pixels]
	OUTPUTS:
		annuli radius centers 	[pixels]
		counts/pix**2 		[image units]
		annuli areas		[pixels**2]
	"""
	r   = empty(len(rl), dtype=float)
	x   = empty(len(rl), dtype=float)
	da  = empty(len(rl), dtype=float)
	rl2 = multiply(rl,rl)

	x[1:]  = 0.5*(rl[1:]+rl[:-1])
	x[0]   = rl[0]*0.5

	for i in range(1,len(rl)):
		ap    = CircularAnnulus(rl[i-1], rl[i])
		da[i] = ap.area 
		r[i]  = aperture_photometry(fnd, cx, cy,ap) / da[i]
	ap    = CircularAperture(rl[0])
	da[0] = ap.area
	r[0]  = aperture_photometry(fnd, cx, cy,ap) / da[0]

	return x, r, da

