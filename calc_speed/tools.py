       
from scipy.interpolate import interp1d
from scipy import array
import numpy as np
from numbers import Number

def extrap(x, xp, yp):
    """np.interp function with linear extrapolation"""
    
    if isinstance(x, Number):
        x=np.array([x])
        
    
    y = np.interp(x, xp, yp)
    y[x < xp[0]] = yp[0] + (x[x<xp[0]]-xp[0]) * (yp[0]-yp[1]) / (xp[0]-xp[1])
    y[x > xp[-1]]= yp[-1] + (x[x>xp[-1]]-xp[-1])*(yp[-1]-yp[-2])/(xp[-1]-xp[-2])
    return y