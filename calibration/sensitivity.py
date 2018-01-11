from settings import *
import st7py
import st7macros
import user as ui
import numpy as np
import pandas as pd
from multiprocessing import Pool
import time
import sys
import itertools

#from sqlitedict import SqliteDict



def main(arg):
    """
    main processing function.
    """

    uid = arg[0]
    value = arg[1]

    print('worker (id: {}) started at {}'.format(uid, time.time()))

    print('id: {}    value: {}'.format(uid, value))


    # assign parameters via setter function look up
    #ui.setters[para_name]
    # run nfa solver and get results

    # save results to disk
    results = []

    print('worker (id: {}) finished at {}'.format(uid, time.time()))
    return results


def init(para_name):
    """
    performs initial set up and disk io to load meta data.
    returns packed list of arguments for mapping to main
    """

    # get parameters dataframe for name lookup
    paras = ui.meta['parameters']

    # filter dataframe by user (cli) selection and return series
    para = paras.loc[ paras['name'] == para_name ].iloc[0]

    # form packed argument list
    uids = np.arange(1,POOL_NUM_WORKERS+1)

    # create array of linearly spaced alpha values (bounded by x_lb and x_ub)
    alphas = np.linspace(para['x_lb'], para['x_ub'], POOL_NUM_WORKERS)

    # scale alpha values
    values = st7macros.scale_para(para, alphas)

    # pack uids and assignment values to argument list
    args = list(zip(uids,values))

    return args


if __name__ == '__main__':

    # define __spec__ to be able to run the multiprocessing module in ipython shell
    __spec__ = "ModuleSpec(name='builtins', loader=<class '_frozen_importlib.BuiltinImporter'>)"

    # show main start time
    t0 = time.time()
    print('sensitivity study starting at {}...'.format(t0))

    n = POOL_NUM_WORKERS
    para_name = sys.argv[1]

    args = init(para_name)

    # start st7 api
    #st7py.start()

    with Pool(n) as pool:
        results = pool.map(main,args)

    # release api
    #st7py.stop()

    print('sensitivity studies finished. total elapsed time: {}s'.format(time.time()-t0))
