import ctypes
import numpy as np
import pandas as pd

from settings import *
import st7py as st7


# load meta data from excel file as a pandas dataframe
meta = pd.read_excel(XLS_FILE, sheet_name=None)


def set_barrier_modulus(uid,value):
    print('Setting...')


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
        st7.macros.set_node_stiffness(uid, node=row['id'], fcase=row['fcase'],
            value=[value,0,0,0,0,0])


def set_kx_mid(uid,value):
    # get near and far node indices from node_stiffness sheet
    df = meta['node_stiffness']
    # filter nodal indices based on 'near' and 'far' node names
    df = df[ df['name']=='mid' ]
    for _, row in df.iterrows():
        st7.macros.set_node_stiffness(uid, node=row['id'], fcase=row['fcase'],
            value=[value,0,0,0,0,0])


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
