import st7py as st7
import api
from settings import *
import numpy as np
from multiprocessing import Pool, TimeoutError
import time


def single_analysis(uid):
    print('Worker {} started...\n'.format(uid))
    if MAIN_DEBUG_MODE: return # do nothing if in debug mode, else...
    try:
        st7.start() # start api and open model file
        api.main(uid) # run main user function if not in debug mode
    finally:
        # close model file and release api
        st7.stop()
        print('Worker {} finished...\n'.format(uid))


if __name__ == '__main__':
    # define __spec__ to be able to run the multiprocessing module in ipython shell
    __spec__ = "ModuleSpec(name='builtins', loader=<class '_frozen_importlib.BuiltinImporter'>)"
    n = CAL_N_TRIALS
    t0 = time.time()
    print('Main calibration started: {}'.format(time.ctime()))

    if CAL_PARALLEL_POOL:   # multiprocessing anlysis
        with Pool(n) as pool:
            uids = np.arange(1,n+1)
            t0 = time.time()
            pool.map(single_analysis,uids)

    else:                   # single analysis
        single_analysis(1)

    # print total run time
    print('Main calibration finished. Total elapsed time: {}s\n'.format(time.time()-t0))
