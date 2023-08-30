#localising the system
#calulating the one particle and two particle density matrix
import unittest
import numpy
from pyscf import gto, scf
from pyscf.lo import boys, edmiston, pipek
from pyscf import ao2mo
import numpy as np
from  numpy import matmul as mm
import torch
import matplotlib.pyplot as plt
import ase.io as asi
import sys
from pyscf import lib
lib.num_threads(40)
print(lib.num_threads())
basis = '6-31g'
mol = gto.Mole()
stack = float(sys.argv[2])
stacky = float(sys.argv[3])
ab = asi.read(sys.argv[1])
atm = ""
monSize = len(ab.symbols)
print(len(ab.symbols))
for mi in range(3):
    for i in range(len(ab.symbols)):
#    print("%s %f %f %f"%(ab.symbols[i],ab.positions[i][0],ab.positions[i][1],ab.positions[i][2]))
        atm = "%s%s %f %f %f\n"%(atm,ab.symbols[i],ab.positions[i][0] + stack*mi ,ab.positions[i][1] + stacky*mi, ab.positions[i][2]+3.4*mi)

print(atm)
#exit()
mol.atom= atm
mol.basis = basis
mol.symmetry = 0
mol.verbose = 4
mol.build()
mf = scf.RHF(mol)
hcore = torch.tensor(mf.get_hcore())
torch.save(hcore,"Hcore%f_%f.pt"%(stack,stacky))
#cd print(hcore)
print(hcore.shape)
#exit()
lib.num_threads(40)
mf = mf.run()
print(mol.nao_nr())



def lowdinOperators(Overlap):
    """
    This function gives both square root and inverse square too of the given hessian matrix
    """
    lma, lma_v = torch.symeig(Overlap, eigenvectors= True, upper=True)
    X_e = torch.sqrt(lma.abs())*torch.eye(lma.size(-1))
    Xinv_e = torch.sqrt(torch.where(lma.abs() > 1e-6, 1/lma.abs(),0.0))*torch.eye(lma.size(-1))
    print()
    return lma_v.mm(X_e).mm(lma_v.t()), lma_v.mm(Xinv_e).mm(lma_v.t())
bp = mf.get_ovlp()
sqr_s, insqr_s = lowdinOperators(torch.tensor(bp))
moCoeff = torch.tensor(mf.mo_coeff)
print(mf.mo_occ < 0.5)

numberOfFragments = 3
numberOfAtomsInEachFragments = [monSize,monSize,monSize]
atomList = mol.atom.split("\n")
atomOffset = 0
frag = []
allOccupideOrbital = int(mol.nelectron/2)
moOrthoOccupide = sqr_s.mm(moCoeff)[:,:allOccupideOrbital]
moOrthoUnOccupid = sqr_s.mm(moCoeff)[:,allOccupideOrbital:]

monoHf = []

monHam = torch.zeros_like(moCoeff)
front = torch.zeros_like(monHam)
moOff = 0
for i in range(numberOfFragments):
    b = ""
    for j in range(numberOfAtomsInEachFragments[i]):
        b = "%s\n%s"%(b,atomList[atomOffset + j])
    mol2 = gto.Mole()
    mol2.atom = b
    mol2.basis = basis
    mol2.symmetry = 0
    mol2.verbose = 4
    mol2.build()
    frag.append(mol2)
    nOrb = mol2.nao_nr()
    nocc = int(mol2.nelectron/2)
    print("Printing Number of proces")
    print(lib.num_threads())
    print("Printing again")
    print(lib.num_threads(40))
    monoHf.append(scf.RHF(mol2).run())
    print(nOrb)
    print(nocc)
    print(monoHf[i].mo_coeff.shape)
    monHam[moOff: moOff+ nOrb,moOff: moOff+ nOrb,] = torch.tensor(monoHf[i].mo_coeff)
    homo = monHam[:,moOff+ nocc - 1]
    lumo = monHam[:,moOff+ nocc]
    front[:,i] = homo
    front[:,numberOfFragments + i] = lumo
    moOff += nOrb
    atomOffset += numberOfAtomsInEachFragments[i]

fc = torch.tensor(mf.get_fock())
nufron = front[:,:numberOfFragments*2] 
import tempfile
from pyscf.tools.molden import *
mol.stdout= open("fl2_%f_%f.molden"%(stack,stacky),"w")

sp = header(mol, mol.stdout)
print(order_ao_index(mol))
print(orbital_coeff(mol, mol.stdout, front))

fockMat = nufron.T.mm(fc).mm(nufron)
torch.save(fc,"Fock%f_%f.pt"%(stack,stacky))
torch.save(monHam,"Orb%f_%f.pt"%(stack,stacky))
torch.save(nufron, "frontier%f_%f.pt"%(stack,stacky))
print("Re setting the number of threads")
print(lib.num_threads(40))
mo1 = nufron
eri1 = ao2mo.outcore.full_iofree(mol, mo1.detach().numpy())
print(eri1.shape)
eris1 = ao2mo.addons.restore(1, eri1, numberOfFragments*2)
print(eris1.shape)
s = torch.tensor(eris1)
torch.save(s,"eri1_%f_%f.pt"%(stack,stacky))
