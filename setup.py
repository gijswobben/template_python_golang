import os
import sys

from setuptools import setup, find_packages


os.chdir(os.path.dirname(sys.argv[0]) or ".")

setup(
    name="test_py_go",
    version="0.0",
    description="PyBindGen example",
    author="xxx",
    author_email="yyy@zz",
    packages=find_packages(),
    cffi_modules=["./builder.py:ffibuilder"],
    install_requires=["cffi>=1.0.0"],
)
