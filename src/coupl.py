import torch
import numpy as np
import json
import sys
import cgcCALC

device_ = "cpu"
print(torch.get_num_threads())
def kron2(argv):
    # kroenker product function 
    # makeing multiple product symultaneously togather
    #  
    b = torch.kron(argv[0],argv[1])
    for i in argv[2:]:
        b = torch.kron(b,i)
    return b

a = torch.tensor([[0,1.0],[0,0]])
#anhilation = \sigma_x + i*\sigma_y
#
astr = torch.tensor([[0,0],[1.0,0]])
#creation = \sigma_x - i*\sigma_y
#
s = torch.tensor([[1,0],[0,-1.0]])
# antisymmetry operator = 2*\sigma_z
# 
i = torch.tensor([[1.0,0],[0,1]])
# identity matrix
n = astr*a

c_a1 = torch.kron(astr,i) #creation  operator for alpha electron
c_b1 = torch.kron(s,astr) #creation operator for beta electron
z = torch.kron(s,s)  # Create Occupide sites
I = torch.kron(i,i)  # Create Un Occupied sites

jsonFile = json.load(open(sys.argv[1]))
K_nelec = jsonFile["ket"]["spin"][0]
K_finalS = jsonFile["ket"]["spin"][1]
K_Spathway = jsonFile["ket"]["spin"][2]
K_finalM = jsonFile["ket"]["spin"][3] + K_finalS
        #
B_nelec = jsonFile["bra"]["spin"][0]
B_finalS = jsonFile["bra"]["spin"][1]
B_Spathway = jsonFile["bra"]["spin"][2]
B_finalM = jsonFile["bra"]["spin"][3] + B_finalS
ket = jsonFile["ket"]["orb"]
bra = jsonFile["bra"]["orb"]

print("Selected Spatial Orbitals for Kra")
    
print(ket)
    
print("Selected Spatial Orbitals for Bra")
    
print(bra)
    
PrintP = False
spK = cgcCALC.SpinFunc(K_nelec ,
    K_finalS ,
    K_Spathway ,
    K_finalM )
    
spB = cgcCALC.SpinFunc(B_nelec ,
    B_finalS ,
    B_Spathway ,
    B_finalM )
    
    
ab = ["a","b"]
ab2 = ["\u2191","\u2193"]
Bcg = np.array([spB.CG])
Kcg = np.array([spK.CG])
    
CGMat = np.matmul(Bcg.T,Kcg)
numOfDeterminantsB = len(spB.CG)
numOfDeterminantsK = len(spK.CG)

ketStates = []
print("Printing Spin Configuration of Ket")
for i in range(numOfDeterminantsK):
    ks =[]
    print(Kcg[0][i], end=" ")
    for j in range(K_nelec):
        ks.append("%s_%s"%(ket[j],ab[spK.spin[i*K_nelec + j]]))
        print(ab2[spK.spin[i*K_nelec + j]], end="")
            #print("%s_%s"%(ket[j],ab[spK.spin[i*K_nelec + j]]), end=" ")
    ketStates.append(ks)
    print()
print()
print()
BraStates = []
print("Printing Spin Configuration of Bra")
for i in range(numOfDeterminantsB):
    bs = []
    print(Bcg[0][i], end=" ")
    for j in range(B_nelec):
        bs.append("%s_%s"%(bra[j],ab[spB.spin[i*K_nelec + j]]))
        print(ab2[spB.spin[i*K_nelec + j]], end="")
            #print("%s_%s"%(bra[j],ab[spB.spin[i*K_nelec + j]]), end=" ")
    BraStates.append(bs)
    print()
print()
print()
    
print("-----------------------------")
print("Printing Bra")
for i in range(len(BraStates)):
    print(Bcg[0][i], end=" ")
    print(BraStates[i])
print("Printing Ket")
for i in range(len(ketStates)):
    print(Kcg[0][i], end=" ")
    print(ketStates[i])
    
    
oper1 = []
for i in range(max(K_nelec,B_nelec)):
    operi_a = []
    operi_b = []
    for j in range(max(K_nelec,B_nelec)):
        if(j < i):
            operi_a.append(z)
            operi_b.append(z)
        if(j == i):
            operi_a.append(c_a1)
            operi_b.append(c_b1)
        if(j > i):
            operi_a.append(I)
            operi_b.append(I)
    oper1.append(operi_a)
    oper1.append(operi_b)

print(len(oper1))
tn = []
for i in range(len(oper1)):
    b1 = kron2(oper1[i])
    print(b1.size())
    tn.append(b1)

oper1 = tn
print(oper1[0].dtype)

numberMat1 = {}
sm = []
for i in range(int(len(oper1)/2)):
    if(i%2 == 0):
        numberMat1["h_%d_%s"%(int(i/2)+1, ab[0])]=[oper1[2*i + 0],2*i]
        numberMat1["h_%d_%s"%(int(i/2)+1, ab[1])]=[oper1[2*i + 1],2*i + 1]
        sm.append("h_%d_%s"%(int(i/2)+1, ab[0]))
        sm.append("h_%d_%s"%(int(i/2)+1, ab[1]))
    else:
        numberMat1["l_%d_%s"%(int(i/2)+1, ab[0])]=[oper1[2*i + 0],2*i]
        numberMat1["l_%d_%s"%(int(i/2)+1, ab[1])]=[oper1[2*i + 1],2*i + 1]
        sm.append("l_%d_%s"%(int(i/2)+1, ab[0]))
        sm.append("l_%d_%s"%(int(i/2)+1, ab[1]))

detK = []
for i in range(len(ketStates)):
    dk = torch.eye(oper1[0].size()[0], device=device_)
    for j in range(len(ketStates[i])):
        print("%2d %2d"%(i,j))
        sk = numberMat1[ketStates[i][j]][0]
        dk = torch.mm(dk,sk)
    detK.append(dk)
print("Making Ket Operator")
detK = torch.stack(detK)

detB = []
for i in range(len(BraStates)):
    db = torch.eye(oper1[0].size()[0], device=device_)
    for j in range(len(BraStates[i])):
        print("%2d %2d"%(i,j))
        sk = numberMat1[BraStates[i][j]][0]
        db = torch.mm(db,sk)
    detB.append(db)
detB = torch.stack(detB)

alN = len(tn)
mlp = []
ml1 = []
for i in range(len(tn)):
    for j in range(len(tn)):
        for k in range(len(tn)):
            for l in range(len(tn)):
                twoI = torch.mm(
                        torch.mm(tn[k],tn[i]),
                        torch.mm(tn[j].T,tn[l].T)
                    )*((k+1)*(alN+1)*(alN+1)*(alN + 1) + (i+1)*(alN+1)*(alN+1)  + (j+1)*(alN+1) + (l+1))
                mp = []
                for mi in range(detK.size()[0]):
                    sl = []
                    for ni in range(detB.size()[0]):
                        ml = torch.mm(detB[ni].T,torch.mm(twoI,detK[mi]))
                        sl.append(ml[0,0])
                    sl = torch.stack(sl)
                    mp.append(sl)
                mp = torch.stack(mp)
                #print(mp)
                mlp.append(mp)
                print("%d %d %d %d"%(i,j,k,l))

                #clear()
        OneI = torch.mm(tn[i],tn[j].T)*( (i+1)*(alN+1)  + (j+1) )
        mp = []
        for mi in range(detK.size()[0]):
            sl = []
            for ni in range(detB.size()[0]):
                ml = torch.mm(detB[ni].T,torch.mm(OneI,detK[mi]))
                sl.append(ml[0,0])
            sl = torch.stack(sl)
        mp.append(sl)
        mp = torch.stack(mp)
        ml1.append(mp)
        print("%d %d"%(i,j))
        
mlp = torch.stack(mlp)
ml = mlp[(mlp != 0).nonzero(as_tuple= True)]
ls = torch.abs(ml)
lsi = ml<0
print(lsi)
print(alN + 1)
print(ml/9)
ln = ls%(alN + 1)
lm = ((ls-ln)/(alN + 1))%(alN + 1)
lo = ((ls - lm*(alN + 1) -ln)/((alN + 1)*(alN + 1)))%(alN + 1)
lp = ((ls- lo*(alN + 1)*(alN + 1) - lm*(alN + 1) -ln)/((alN + 1)*(alN + 1)*(alN + 1)))%(alN + 1)
lc2 = torch.stack([ln,lm,lo,lp])
print(lc2)
ml1 = torch.stack(ml1)
mli1 = ml1[(ml1 != 0).nonzero(as_tuple= True)]
ls1 = torch.abs(mli1)
ln1 = ls1%(alN + 1)
lm1 = ((ls1-ln1)/(alN + 1))%(alN + 1)
lc1 = torch.stack([lm1,ln1])
print(lc1)
exit()
