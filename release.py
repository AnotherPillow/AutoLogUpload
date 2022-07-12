import shutil
import py_compile
import os
#check if dist/src/ exists and if not, create it
if not os.path.exists("dist/src"):
    os.makedirs("dist/src")
    print("created dist/src")
#check if version.txt exists and if not, create it
if not os.path.exists("version.txt"):
    with open("version.txt","w") as f:
        f.write("1.0.0")
    print("created version.txt")

def compile_py():
    py_compile.compile('upload.py') #compiles single file named file.py
    print("compiled upload...")
    py_compile.compile('smapi.py') #compiles single file named file.py
    print("compiled smapi...")
def copy():
    print("copying...")
    #copy smapi.bat to dist/
    # shutil.copy("smapi.bat","dist/src/smapi.bat")
    # print("copied smapi.bat")
    #copy upload.py to dist/
    shutil.copy("__pycache__/upload.cpython-38.pyc","dist/src/upload.pyc")
    print("copied upload.pyc")
    #copy smapi.py to dist/
    shutil.copy("__pycache__/smapi.cpython-38.pyc","dist/src/smapi.pyc")
    print("copied smapi.pyc")
    shutil.copy("AutoLogUpload.bat","dist/AutoLogUpload.bat")
    print("copied AutoLogUpload.bat")
# compile_exe()
def zip(version):
    #archive dist/ to dist.zip
    shutil.make_archive("dist","zip","dist")
    print("created archive")
    shutil.move("dist.zip","dist/{0}.zip".format(version))
def version():
    #open version.txt and read the version number
    with open("version.txt","r") as f:
        version = f.read()
    return version

compile_py()
copy()
zip(version())