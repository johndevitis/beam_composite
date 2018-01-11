import os
import ctypes
import numpy as np
import pandas as pd
from st7py import *
from settings import *
import st7macros


# load meta data from excel file as a pandas dataframe
meta = pd.read_excel(XLS_FILE, sheet_name=None)


def set_barrier_modulus(uid,value):
    print('Setting {}...'.format(value))


def set_deck_modulus(uid,value):
    print('Setting {}...'.format(value))


def set_deck_density(uid,value):
    print('Setting {}...'.format(value))


def set_deck_thickness(uid,value):
    print('Settings {}...'.format(value))


def set_deck_height(uid,value):
    print('Setting {}...'.format(value))


def set_kx_ends(uid,value):
    # get near and far node indices from node_stiffness sheet
    df = meta['node_stiffness']
    # filter nodal indices based on 'near' and 'far' node names
    df = df[ (df['name']=='near') | (df['name']=='far') ]
    # apply longitudinal spring value to each node
    for _, row in df.iterrows():
        st7macros.set_node_stiffness(uid, node=row['id'], fcase=row['fcase'],
            value=[value,0,0,0,0,0])


def set_kx_mid(uid,value):
    # get near and far node indices from node_stiffness sheet
    df = meta['node_stiffness']
    # filter nodal indices based on 'near' and 'far' node names
    df = df[ df['name']=='mid' ]


def set_steel_modulus(uid,value):
    print('Setting {}...'.format(value))


def set_diaphragm_modulus(uid,value):
    print('Setting {}...'.format(value))


setters = {'barrier_modulus': set_barrier_modulus,
           'deck_modulus': set_deck_modulus,
           'deck_density': set_deck_density,
           'deck_thickness': set_deck_thickness,
           'deck_height': set_deck_height,
           'kx_ends': set_kx_ends,
           'kx_mid': set_kx_mid,
           'steel_modulus': set_steel_modulus,
           'diaphragm_modulus': set_diaphragm_modulus}



def sensitivity():
    f, df, paras = assignment_functions()
    # loop included parameters
    for idx, para in paras.iterrows():
        # get array of alphas based on lower and upper bounds
        alphas = np.linspace(para['x_lb'], para['x_ub'], PARALLEL_NUM_WORKERS)
        # scale alpha values (scale_para broadcasts here, i.e. works for scalar and array of alphas)
        values = scale_para(para, alphas)




def run_nfa(uid):
    # load St7API
    start()

    # open st7 model from st7py Model class instance
    model = Model(filename = ST7_FILE, scratch = ST7_SCRATCH, uid = uid)
    model.open()

    # get total number of elements
    tots = model.totals()

    # run NFA solver using model filename and uid to name files
    nfa_file, nfa_log = gen_result_name(model.filename, uid,'.NFA','.NFL')
    nfa = NFA(uid = uid,
              filename = nfa_file,
              logname = nfa_log,
              fcase = NFA_FCASE,
              nsm = NFA_NSM,
              nmodes = NFA_NMODES)

    # run  nfa solver
    nfa.run(disp=True)

    freqs = nfa.getFrequencies()
    shapes = nfa.getModeShapes(nodes=np.arange(1,1334))

    # close model file and unload St7API
    model.close()
    stop()

    return freqs, shapes




def calibrate():
    pass



def main(uid):


    # load xls file w/ meta data
    paras = pd.read_excel(XLS_FILE, sheet_name='parameters')
