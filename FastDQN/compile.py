from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

import numpy

ext = Extension("c_FastDQN", ["c_FastDQN.pyx"],
                include_dirs=[numpy.get_include()],
                extra_compile_args=["-O3"])

setup(ext_modules=[ext],
      cmdclass={'build_ext': build_ext})