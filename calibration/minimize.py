from scipy.optimize import least_squares
import numpy as np

def obj(x):
    print(x)
    return np.array([10 * (x[1] - x[0]**2), (1 - x[0])])



x0 = np.array([2,2])
res = least_squares(obj, x0)
