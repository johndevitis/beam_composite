from settings import *
import user as ui
import numpy as np
import pandas as pd
from multiprocessing import Pool
import time


def main(uid):
    """
    main sensitivity function
    """
    print('worker (id: {}) started at {}'.format(uid, time.time()))

    time.sleep(5)

    print('worker (id: {}) finished at {}'.format(uid, time.time()))



if __name__ == '__main__':

    # define __spec__ to be able to run the multiprocessing module in ipython shell
    __spec__ = "ModuleSpec(name='builtins', loader=<class '_frozen_importlib.BuiltinImporter'>)"

    t0 = time.time()
    n = SENSITIVITY_NUM_STEPS
    uids = np.arange(1,n+1)

    print('sensitivity studies starting...')

    with Pool(n) as pool:
        results = pool.map(main,uids)

    print('sensitivity studies finished. total elapsed time: {}s'.format(time.time()-t0))
