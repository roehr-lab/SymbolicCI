from setuptools import setup, find_packages
from pybind11.setup_helpers import Pybind11Extension,build_ext
from setuptools.command.install import install
from pathlib import Path
def get_project_root() -> Path:
    print(Path(__file__).absolute())
    return Path(__file__).parent.absolute()

projectPath = get_project_root()

print(projectPath)

module2 = [
    Pybind11Extension(
        "cgcCALC",
        ["%s/%s"%(projectPath,'src/getCGC.cpp'),
        "%s/%s"%(projectPath,'src/cgc.cpp'),
        "%s/%s"%(projectPath,'src/latex.cpp'),
        #"%s/%s"%(projectPath,'src/layout.cpp'),
        "%s/%s"%(projectPath,'src/utilities.cpp'),],  # Sort source files for reproducibility
        include_dirs = ['/usr/local/include',
                                    '/usr/include',
                                    "%s/%s"%(projectPath,'include')],
                    #
    ),
]

setup(name='SymbolicCI',
        version='1.0',
        description='Python Distribution Utilities',
        author='Anurag Singh',
        author_email='anuragsingh291293@gmail.com',
        url='https://github.com/darkcoordinate',
        install_requires=[
            'numpy',
            'sympy',
            'torch',
            'pybind11',
            'npyscreen',
            'pathos',
        ],

        cmdclass={"build_ext": build_ext},
        #packages=["cgcCALC"],
        scripts=["%s/%s"%(projectPath,"src/SymbolicCI-Coupling.py"),],
        ext_modules = module2
    )
