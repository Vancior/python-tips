from Cython.Distutils import build_ext
from distutils.core import setup, Extension

import numpy as np

setup(
    cmdclass={'build_ext': build_ext},
    ext_modules=[Extension('ck2_utils', sources=[
                           '_ck2_utils.pyx', '_ck2_utils.c'], include_dirs=[np.get_include()])]
)
