#import user
from settings import *
import st7py as st7
import numpy as np
from multiprocessing import Pool, TimeoutError
import time
import sys

def single_analysis(uid):
    print('Worker {} started...\n'.format(uid))
    # do nothing if in debug mode, else...
    if not MAIN_DEBUG_MODE:
        # run main user function if not in debug mode
        #results = user.main(uid)
        results = sys.argv[1](uid)
        print('Worker {} finished...\n'.format(uid))
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
            results = pool.map(single_analysis,uids)
    else:
        # single analysis
        results = single_analysis(1)

    # print total run time
    print('Main function finished. Total elapsed time: {}s\n'.format(time.time()-t0))
