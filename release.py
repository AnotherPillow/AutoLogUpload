from distutils.core import setup
import py2exe
import shutil
import py_compile
import os

def compile_exe():
    setup(console=['smapi.py'])
def compile_py():
    py_compile.compile('upload.py') #compiles single file named file.py
def copy():
    #copy smapi.bat to dist/
    shutil.copy("smapi.bat","dist/smapi.bat")
    #copy upload.py to dist/
    shutil.copy("__pycache__/upload.cpython-38.pyc","dist/upload.pyc")
compile_exe()
compile_py()
copy()