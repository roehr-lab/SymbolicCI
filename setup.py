from setuptools import setup, find_packages
from pybind11.setup_helpers import Pybind11Extension,build_ext
from setuptools.command.install import install
from pathlib import Path
def get_project_root() -> Path:
    return Path(__file__).parent.parent

projectPath = get_project_root()
print(projectPath)
module2 = [
    Pybind11Extension(
        "cgcCALC",
        ["%s/SymbolicCI/%s"%(projectPath,'src/getCGC.cpp'),
        "%s/SymbolicCI/%s"%(projectPath,'src/cgc.cpp'),
        "%s/SymbolicCI/%s"%(projectPath,'src/latex.cpp'),
        "%s/SymbolicCI/%s"%(projectPath,'src/layout.cpp'),
        "%s/SymbolicCI/%s"%(projectPath,'src/utilities.cpp'),],  # Sort source files for reproducibility
        include_dirs = ['/usr/local/include',
                                    '/usr/include',
                                    "%s/SymbolicCI/%s"%(projectPath,'include')],
                    #
    ),
]

setup(name='SymbolicCI',
        version='1.0',
        description='Python Distribution Utilities',
        author='Anurag Singh',
        author_email='anuragsingh291293@gmail.com',
        url='https://github.com/darkcoordinate',
        requires=[
            'numpy',
            'sympy',
            'torch',
            'pybind11',
            'npyscreen',
            'pathos',
        ],

        cmdclass={"build_ext": build_ext},
        #packages=["cgcCALC"],
        scripts=["%s/SymbolicCI/%s"%(projectPath,"src/SymbolicCI-Coupling.py"),],
        ext_modules = module2
    )

