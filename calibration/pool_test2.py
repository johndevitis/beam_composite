from multiprocessing import Pool
import time
import numpy as np
from itertools
import pandas as pd

# load meta data from excel file as a pandas dataframe
paras = pd.read_excel('analysis1.xls', sheet_name='parameters')
# filter by user selection and convert dataframe to series
#para = df.loc[ df['name'] == 'para_name' ].iloc[0]


def main(paras):
    """
    main calibration function
    """

    uid = paras[0]
    x = paras[1]

    print('worker (id: {}) started at {}'.format(uid, time.time()))
    print(x)

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
        results = pool.map(main, list(zip(list(paras.index),paras['name'], paras['x_ub'])))

    print('calibration finished. total elapsed time: {}s'.format(time.time()-t0))
