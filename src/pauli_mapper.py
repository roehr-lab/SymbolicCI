import sys
sys.path.insert(0,'/home/anurag/sq2/SlowQuant/')
import numpy as np
from qiskit.quantum_info import SparsePauliOp
from qiskit.circuit import ParameterVector
from functools import *


from slowquant.unitary_coupled_cluster.operators import Epq, hamiltonian_0i_0a
from slowquant.molecularintegrals.integralfunctions import (
    one_electron_integral_transform,
    two_electron_integral_transform,
)
from slowquant.unitary_coupled_cluster.fermionic_operator import *

# Define same circuit
I = np.array([[1, 0],
              [0, 1]], dtype=complex)

X = np.array([[0, 1],
              [1, 0]], dtype=complex)

Y = np.array([[0, -1j],
              [1j, 0]], dtype=complex)

Z = np.array([[1, 0],
              [0, -1]], dtype=complex)

S = (X- 1.0j*Y)*0.5
S_ = (X + 1.0j*Y)*0.5
Sa = np.kron(S,I)
Sb = np.kron(Z,S)
II = np.kron(I,I)
ZZ = np.kron(Z,Z)
S1a = np.kron(Sa,II)
S2a = np.kron(ZZ,Sa)
S1b = np.kron(Sb,II)
S2b = np.kron(ZZ,Sb)

np.max(np.abs(S1b.T@S1a))


S1a_ = "SIII"
S1b_ = "ZSII"
S2a_ = "ZZSI"
S2b_ = "ZZZS"

g = [S1a_, S1b_, S2a_, S2b_]

mat = []
for i in range(len(g)):
    ind = g[i].index("S")
    sn = list(g[i])
    sn[i] = 'X'
    P1 = "".join(sn)
    sn[i] = 'Y'
    P2 = "".join(sn)
    mat.append(SparsePauliOp([P1,P2],np.array([0.5,-0.5j])))


print(mat)


gp = []
for i in range(len(mat)):
    for j in range(len(mat)):
        gp.append(mat[i]@mat[j].adjoint())
        
        
        
from pyscf import gto, scf 
atm = '''
C        0.0000000000    0.0000000000   -0.0000000000;
O        1.1369739059    0.0000000000   -0.0000000000;
O       -1.1369739059   -0.0000000000    0.0000000000;
'''

mol = gto.M(
    atom=atm,
    #charge= 2,
    charge= 0,
    spin = 0,
    verbose=2,
    unit="Angstrom",
    basis= "def2-svp"
)

mf = scf.RHF(mol)
print(mol.nelec)
mf.max_cycle = 300
mf.kernel()

print(mol.nelec)
print(mf.e_tot - mf.energy_nuc())

c_mo = mf.mo_coeff
h_ao = mol.intor("int1e_kin") + mol.intor("int1e_nuc")
g_ao = mol.intor("int2e")


mf = scf.RHF(mol, )
mf.max_cycle=300
print(mf)
mf.kernel()

hcore = mol.intor("int1e_kin") + mol.intor("int1e_nuc")
eri_ao = mol.intor("int2e_sph")
print(eri_ao.shape)
print(mf.mo_coeff.shape)
print(mol.nelec)
print(mf.mo_occ)
mo_occa = (mf.mo_occ > 0).astype(np.double)
mo_occb = (mf.mo_occ == 2).astype(np.double)
print(mo_occa)
print(mo_occb)
ncas = 2
nclosed = sum(mol.nelec)//2 - ncas//2
print(nclosed)

nvirt = len(mo_occa) -(nclosed + ncas)
core_coeff = mf.mo_coeff[:, :nclosed]
active_coeff = mf.mo_coeff[:, nclosed: nclosed + ncas]
virtual_coeff = mf.mo_coeff[:, nclosed + ncas:]




print(mol.energy_nuc())
print(core_coeff.shape)
print(active_coeff.shape)
print(virtual_coeff.shape)

mo_occa = (mf.mo_occ > 0).astype(np.double)
mo_occb = (mf.mo_occ == 2).astype(np.double)

print(mo_occa)
print(mo_occb)


core_dm = np.dot(core_coeff, core_coeff.conj().T) 
corevhf = mf.get_veff(mf.mol, core_dm)
corevhf = [corevhf]
#print(corevhf.shape)
energy_core = 0# mol.energy_nuc()
energy_core += np.einsum('ij,ji', core_dm, hcore)
energy_core += np.einsum('ij,ji', core_dm, hcore)
energy_core += np.einsum('ij,ji', core_dm, corevhf[0])
energy_core += np.einsum('ij,ji', core_dm, corevhf[0])
print("print all core")
print(energy_core)
dm_core = core_coeff.dot(core_coeff.T)
dm_active_a = np.dot(active_coeff*mo_occa[nclosed: nclosed + ncas], active_coeff.T)
dm_active_b = np.dot(active_coeff*mo_occb[nclosed: nclosed + ncas], active_coeff.T)

print(mo_occa[nclosed: nclosed + ncas])
print(mo_occb[nclosed: nclosed + ncas])


vj_core_1 = np.einsum("ijkl,kl-> ij", eri_ao, dm_core)
vk_core_1 = np.einsum("ikjl,kl-> ij", eri_ao, dm_core)

vhf_core = vj_core_1 + vj_core_1 - vk_core_1

h1eff = reduce(np.dot, (active_coeff.conj().T, hcore+vhf_core, active_coeff))
eris1 = np.einsum("ip,jq,ijkl,kr,ls->pqrs", active_coeff.conj(), active_coeff, 
                                 eri_ao, active_coeff.conj(), active_coeff)
print(h1eff)
#eri = mol.intor("int2e")
#eri1 = ao2mo.outcore.full_iofree(mol, active_coeff)
#eris1 = ao2mo.addons.restore(1, eri1, 2)
print(eris1)
print(h1eff)

h1eff_spin = np.zeros((4,4))
eris1_spin = np.zeros((4,4,4,4))

for i in range(h1eff_spin.shape[0]):
    for j in range(h1eff_spin.shape[1]):
        h1eff_spin[i,j] = h1eff[i//2,j//2]

for i in range(eris1_spin.shape[0]):
    for j in range(eris1_spin.shape[1]):
        for k in range(eris1_spin.shape[2]):
            for l in range(eris1_spin.shape[3]):
                eris1_spin[i,j,k,l] = eris1[i//2,j//2,k//2,l//2] 
                
                
gp = []
for i in range(len(mat)):
    for j in range(len(mat)):
        gp.append(mat[i]@mat[j].adjoint()*h1eff[i//2,j//2])
        
print(gp)

spl1 = sum(gp)
sl = list(spl1.paulis)
sl2 = list(spl1.coeffs)

idx = 0
while(True):
    idxs = []
    for i in range(len(sl)):
        if(sl[i] == sl[idx]):
            idxs.append(i)
    print(len(sl))
    print(idxs)
    for i in range(len(idxs)-1,0, -1):
        print(i)
        print(idxs[i])
        sl.pop(idxs[i])
        sl2[idxs[0]] += sl2[idxs[i]]
        sl2.pop(idxs[i])
    print(len(sl))
    if(len(sl)-1 == idx):
        break
    else:
        idx += 1


for i in range(len(sl2)-1, 0, -1):
    if(abs(sl2[i]) < 1e-8):
        sl.pop(i)
        sl2.pop(i)

print(sl2)
print(sl)
bl = SparsePauliOp(sl,sl2)
print(bl)
print(bl.to_matrix())
blm =bl.to_matrix()


EIP = []
for i in range(len(mat)):
    for j in range(len(mat)):
        for k in range(len(mat)):
            for l in range(len(mat)):
                if((i%2) == (l%2)):
                    if((j%2) == (k%2)):
                        EIP.append(mat[i]@mat[j]@mat[k].adjoint()@mat[l].adjoint()*eris1[i//2,l//2,j//2,k//2]) # pysicst to chemist notaion
                
print(EIP)


spl1 = sum(EIP)
sl = list(spl1.paulis)
sl2 = list(spl1.coeffs)

idx = 0
while(True):
    idxs = []
    for i in range(len(sl)):
        if(sl[i] == sl[idx]):
            idxs.append(i)
    print(len(sl))
    print(idxs)
    for i in range(len(idxs)-1,0, -1):
        print(i)
        print(idxs[i])
        sl.pop(idxs[i])
        sl2[idxs[0]] += sl2[idxs[i]]
        sl2.pop(idxs[i])
    print(len(sl))
    if(len(sl)-1 == idx):
        break
    else:
        idx += 1


for i in range(len(sl2)-1, 0, -1):
    if(abs(sl2[i]) < 1e-8):
        sl.pop(i)
        sl2.pop(i)

print(sl2)
print(sl)
kl = SparsePauliOp(sl,sl2)
print(kl)
print(kl.to_matrix())
klm = kl.to_matrix()

alm = blm + 0.5*klm

print(alm)



ag0 = np.array([[1.0,0.0]])
ag1 = np.array([[0.0,1.0]])
adg = reduce(np.kron, [ag0,ag0, ag0, ag0])
mlp  = S1b@S1a@adg.T
mlp2  = S1a@S1b@adg.T


nk = mlp.T@alm@mlp
print(alm@mlp)
print(energy_core)
print(nk)
import math as mt

print(energy_core + nk)
