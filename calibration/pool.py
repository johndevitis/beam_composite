from multiprocessing import Pool, TimeoutError
import time
import sys
import numpy as np
from settings import *

def main(uid):
    print('Worker {} started at {}...'.format(uid, time.time()))
    time.sleep(1)
    print('Worker {} finished at {}'.format(uid, time.time()))
    return results


if __name__ == '__main__':

    # define __spec__ to be able to run the multiprocessing module in ipython shell
    __spec__ = "ModuleSpec(name='builtins', loader=<class '_frozen_importlib.BuiltinImporter'>)"

    t0 = time.time()

    print('Main calibration started: {}'.format(time.ctime()))

    n = PARALLEL_NUM_WORKERS

    if PARALLEL_POOL_ON:
        # multiprocessing anlysis
        with Pool(n) as pool:
            uids = np.arange(1,n+1)
            t0 = time.time()
            results = pool.map(main,uids)
    else:
        # single analysis
        results = main(1)

    # print total run time
    print('Main function finished. Total elapsed time: {}s\n'.format(time.time()-t0))
