import ctypes

_dll = ctypes.CDLL('./dummy.so')

_foobar = _dll.foobar
_foobar.argtypes = [ctypes.c_int]
_foobar.restype = None

def foobar(x):
    _foobar(x)

if __name__ == '__main__':
    foobar(1234)