import numpy as np
from qiskit.quantum_info import SparsePauliOp
from qiskit.circuit import ParameterVector
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
print(gp)
s = SparsePauliOp(["ZZZY", "ZZZX"],np.array([+0.5j,0.5]))
sum( gp[-1][0], gp[-1][3]  )



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
