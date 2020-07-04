import os
import glob
import numpy as np

_mydir = os.path.dirname(os.path.realpath(__file__))

def list_files():
    d = dict()
    d['train'] = glob.glob(os.path.join(_mydir, 'trainex/data/*.dat'))
    d['valid'] = glob.glob(os.path.join(_mydir, 'validex/data/*.dat'))
    return d
