from settings import *
import pyDOE
import numpy as np
import pandas as pd
from multiprocessing import Pool
import time


def gen_start_values(n=1,fname = 'calibration_start_values.csv'):
    """
    generates n latin hypercube experiments and saves them to disk.
    this creates a dependency on pyDOE library (bsd license)
    """
    values = pyDOE.lhs(n)
    np.savetxt(fname,values)
    return values


def main(uid):
    """
    main calibration function
    """
    print('worker (id: {}) started at {}'.format(uid, time.time()))

    time.sleep(5)

    print('worker (id: {}) finished at {}'.format(uid, time.time()))



if __name__ == '__main__':

    # define __spec__ to be able to run the multiprocessing module in ipython shell
    __spec__ = "ModuleSpec(name='builtins', loader=<class '_frozen_importlib.BuiltinImporter'>)"

    t0 = time.time()
    n = CALIBRATION_NUM_TRIALS
    uids = np.arange(1,n+1)

    print('calibration starting...')

    with Pool(n) as pool:
        results = pool.map(main,uids)

    print('calibration finished. total elapsed time: {}s'.format(time.time()-t0))
