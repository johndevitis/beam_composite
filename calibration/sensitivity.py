from settings import *
from st7macros import *
import user as ui
import numpy as np
import pandas as pd
from multiprocessing import Pool
import time
import sys

class SensitivityParameter():
    pass


def main(uid):
    """
    main processing function. assign's a
    """
    print('worker (id: {}) started at {}'.format(uid, time.time()))

    # assign parameters

    # run nfa solver and get results

    # save results to disk
    results = []

    print('worker (id: {}) finished at {}'.format(uid, time.time()))
    return results



def init(para_name):
    """
    performs initial set up and disk io to load meta data
    """

    # load meta data from excel file as a pandas dataframe
    df = pd.read_excel(XLS_FILE, sheet_name=None)

    # extract desired parameter settings from 'parameters' sheet
    paras = df['parameters'][ df['parameters'].name == 1 ]





def run_nfa():
    pass






if __name__ == '__main__':

    # define __spec__ to be able to run the multiprocessing module in ipython shell
    __spec__ = "ModuleSpec(name='builtins', loader=<class '_frozen_importlib.BuiltinImporter'>)"

    t0 = time.time()
    n = SENSITIVITY_NUM_WORKERS
    uids = np.arange(1,n+1)

    print('sensitivity study starting...')

    para_name = sys.argv[1]
    init(para_name)


    with Pool(n) as pool:
        results = pool.map(main,uids)

    print('sensitivity studies finished. total elapsed time: {}s'.format(time.time()-t0))
