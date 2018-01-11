from multiprocessing import Pool
import time
import numpy as np
import json
import string
import random

from sqlitedict import SqliteDict

db_file = './db-test.db'


d = SqliteDict(filename='./sqlitedict_pool.db',
                tablename='test-dict',
                flag='c',
                autocommit=True)


dj = SqliteDict(filename='./sqlitedict_pool.db',
                tablename='test-dict-json',
                flag='c',
                autocommit=True,
                encode=json.dumps,
                decode=json.loads)

d['cnt'] = 0
dj['cnt'] = 0


def main(uid):
    """
    main calibration function
    """
    print('worker (id: {}) started at {}'.format(uid, time.time()))

    d['cnt'] = d['cnt']+1
    dj['cnt'] = dj['cnt']+1
    dj['names'] = random.choice(string.ascii_letters)

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
