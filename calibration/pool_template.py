from multiprocessing import Pool
import time
import numpy as np


def main(uid):
    """
    main calibration function
    """
    print('worker (id: {}) started at {}'.format(uid, time.time()))

    time.sleep(4)
    
    print('worker (id: {}) finished at {}'.format(uid, time.time()))



if __name__ == '__main__':

    # define __spec__ to be able to run the multiprocessing module in ipython shell
    __spec__ = "ModuleSpec(name='builtins', loader=<class '_frozen_importlib.BuiltinImporter'>)"

    t0 = time.time()
    n = 4
    uids = np.arange(1,n+1)

    print('calibration starting...')

    with Pool(n) as pool:
        results = pool.map(main,uids)

    print('calibration finished. total elapsed time: {}s'.format(time.time()-t0))
