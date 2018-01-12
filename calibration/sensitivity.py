from settings import *
import st7py as st7
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

    returns freqs, shapes, and 
    """

    uid, apply_fcn, value = arg

    print('worker (id: {}) started at {}'.format(uid, time.time()))

    # initialize st7api
    st7.start()

    # create instance of model
    model = st7.Model(filename=ST7_FILE,
                      scratch=ST7_SCRATCH,
                      uid=uid)

    # open model and get element totals
    model.open()
    totals = model.totals()

    # use dynamic setter function to set corresponding value in model
    apply_fcn(uid,value)

    # create nfa result and result log file names based on uid number
    nfa_file, nfa_log = st7.macros.gen_result_name(model.filename, uid, '.NFA', '.NFL')

    # create instance of nfa solver object
    nfa = st7.NFA(uid = uid,
                    filename = nfa_file,
                    logname = nfa_log,
                    fcase = NFA_FCASE,
                    nsm = NFA_NSM,
                    nmodes = NFA_NMODES)

    # run solver
    nfa.run(disp=True)

    # get modal results
    #  note - we're explicitely passing node indices for shape results atm
    freqs = nfa.getFrequencies()
    shapes = nfa.getModeShapes(np.arange(1,totals['Nodes']+1))

    # close model and release api
    model.close()
    st7.stop()

    print('worker (id: {}) finished at {}'.format(uid, time.time()))
    return freqs, shapes, value


def init(para_name):
    """
    performs initial set up and disk io to load meta data.
    returns packed list of arguments for mapping to main threaded function.
    """

    # get parameters dataframe and filter user (cli) selected by name (first).
    # returns a series.
    paras = ui.meta['parameters']
    para = paras.loc[ paras['name'] == para_name ].iloc[0]

    # create array of linearly spaced alpha values (bounded by x_lb and x_ub)
    alphas = np.linspace(para['x_lb'], para['x_ub'], POOL_NUM_WORKERS)

    # scale alpha values
    values = st7.macros.scale_para(para, alphas)

    # pack setter functions, uids and assignment values to argument list
    # each element in argument list is an array of length 3 -> [uid, (set_fcn,), (value,)]
    args = list(zip(np.arange(1,POOL_NUM_WORKERS+1),
                    itertools.repeat(ui.setters[para_name],POOL_NUM_WORKERS),
                    values))

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

    with Pool(n) as pool:
        results = pool.map(main,args)

    print('sensitivity studies finished. total elapsed time: {}s'.format(time.time()-t0))
