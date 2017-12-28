from st7py import *
from St7API import *
from settings import *
import ctypes
import os



def set_beam_material_property(uid, propnums, value, propname='ipBeamModulus', disp=False):
    """sets a single modulus to single or multiple st7 property numbers. defaults to setting beam elastic modulus"""
    for prop in propnums:
        Double = ctypes.c_double*9
        Doubles = Double()
        chkErr(St7GetBeamMaterialData(uid,prop,Doubles))
        Doubles[propname] = value
        chkErr(St7SetBeamMaterialData(uid,prop,Doubles))
    [print('Beam Propnum: {}\tAssigned {} as {}'.format(x,propname,value)) for x in propnums if disp==True]


def set_plate_iso_material_property(uid, props, value, propname='ipPlateIsoModulus',disp=False):
    """sets desired material data to isotropic plates. defaults to modulus assignment"""
    for prop in props:
        Double = ctypes.c_double*8
        Doubles = Double()
        chkErr(St7GetPlateIsotropicMaterial(uid,prop,Doubles))
        Doubles[propname] = value
        chkErr(St7SetPlateIsotropicMaterial(uid,propnum,Doubles))
    [print('Plate Propnum: {}\tAssigned {} as {}'.format(x, propname, value)) for x in propnums if disp==True]


def set_plate_ortho_material_property_e(uid, propnums, value, disp=False):
    """ sets a value[0] and value[1] to ortho plate modulus 1 and 2 respectively for each prop in propnums"""
    for prop in propnums:
        Double = ctypes.c_double*18
        Doubles = Double()
        chkErr(St7GetPlateOrthotropicMaterial(uid,prop,Doubles))
        Doubles[ipPlateOrthoModulus1] = value[0]
        Doubles[ipPlateOrthoModulus2] = value[1]
        chkErr(St7SetPlateOrthotropicMaterial(uid,prop,Doubles))


def set_node_stiffness(uid,nodes,value):
    pass


def set_node_restraint(uid,nodeids,value):
    pass


def gen_result_name(base_name, uid,result_ext,log_ext):
    """ adds *_<uid>* to model file name for nfa results and log files"""
    result_file = os.path.splitext(base_name)[0] + '_{}'.format(uid) + result_ext.upper()
    log_file = os.path.splitext(base_name)[0] + '_{}'.format(uid) + log_ext.upper()
    return result_file, log_file


def main(uid):

    start()

    # open st7 model from st7py Model class instance
    model = Model(filename = ST7_FILE, scratch = ST7_SCRATCH, uid = uid)
    model.open()

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

    # close file
    model.close()


    stop()

    return freqs, shapes
