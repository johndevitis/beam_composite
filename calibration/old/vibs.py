import numpy as np
from scipy import linalg, interpolate
import matplotlib.pyplot as plt


class MAC():

    def __init__(self,u1,u2,**kwargs):
        self.u1 = u1
        self.u2 = u2
        self.m = get_mac(u1,u2)

    def __str__(self):
        return 'Modal Assurance Criterion:\n{}'.format(self.m)

    def plot(self):
        plt.imshow(self.m, aspect='auto', interpolation='none')
        plt.show()



def get_mac(U1,U2):
    """
    returns modal assurance criterion (MAC). U1 and U2 numpy arrays should
    be in the form of [ndof x nmodes].
    modal arrays can have a different number of modes (columns) but must retain the same
    number of DOF (rows).
    suitable for the general case of real normal modes and complex modes. that is, the hermitian operations are performed.
    """
    nm1, nm2 = np.shape(U1)[1], np.shape(U2)[1]
    m = np.empty((nm1,nm2))
    for ii in range(nm1):
        for jj in range(nm2):
            m[ii,jj] = _mac_single(U1[:,ii],U2[:,jj])
    return m


def _mac_single(u1,u2):
    """ macro for get_mac function. returns mac value for 1d arrays"""
    m = (np.inner(u1.conj(),u2)*np.inner(u2.conj(),u1)) / (np.inner(u1.conj(),u1)*np.inner(u2.conj(),u2))
    return m


def freq_residual(f1,f2):
    pass


def pair_modes(f1,f2):
    pass


def interpZ(coords, z, scale, xres=25, yres=50):
    pass


def snap(array,value):
    """findsand returns the nearest value in array"""
    idx = (np.abs(array-value)).argmin()
    return array[idx]


def mag2db(x):
    """ converts magnitude to decibles """
    return 20*np.log10(x)


def hermit(x):
    """
    return Hermitian of array, x. this is equivalent to taking the complex
    conjugate transpose
    """
    return x.conj().T
