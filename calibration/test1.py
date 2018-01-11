import sys

import pandas as pd



if __name__ == '__main__':

    df = pd.read_excel('analysis1.xls', sheet_name='parameters')

    for idx, row in df[df['name'] == sys.argv[1]].iterrows():
        print('idx: {}     row: {}'.format(idx,row))
