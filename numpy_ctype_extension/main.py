import ctypes
import numpy as np
import os
import random
import scipy.sparse

_dll = ctypes.CDLL('./dummy.so')

_foobar = _dll.foobar
_foobar.argtypes = [ctypes.POINTER(ctypes.c_float), ctypes.c_int]
_foobar.restype = None

def foobar(x, y):
    _foobar(x, y)

if __name__ == '__main__':
    matrix = scipy.sparse.lil_matrix((100, 100), dtype=np.float32)
    for i in range(300):
        matrix[random.randint(0, 99), random.randint(0, 99)] = random.random()
    matrix = matrix.tocsr()
    foobar(matrix.data.ctypes.data_as(ctypes.POINTER(ctypes.c_float)), len(matrix.data))