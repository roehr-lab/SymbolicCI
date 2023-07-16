#!/usr/bin/env python
import os
import random # for random data generation
from multiprocessing import Pool
#import matplotlib.pyplot as plt
import numpy as np
from sympy import Symbol, Matrix, symbols,UnevaluatedExpr,expand
import sympy
import os
import torch
import cgcCALC

import npyscreen




from sympy.physics.quantum import Dagger,Bra,Ket
import numpy as np
print(os.cpu_count())
"""
https://doi.org/10.1002/qua.24898
https://arxiv.org/abs/1412.5829
https://doi.org/10.1142/S021797921345029X
https://tensornetwork.org/mps/
 This code is based on these papers 
"""
class MatrixOperator(Matrix):           
    #this operator is made to 
    def __init__(self,*argv):
        super(Matrix,self).__init__()
        self.spin = None

class Network(list):
    def __init__(self,*argv):
        super(list,self).__init__()
        
    def sum(self):                      # add  the array and make a complete expression
        bb = self[0]*0
        for i in range(len(self)):
            bb += self[i]
        return bb

def kron2(argv):
    # kroenker product function 
    # makeing multiple product symultaneously togather
    #  
    b = np.kron(argv[0],argv[1])
    for i in argv[2:]:
        b = np.kron(b,i)
    return MatrixOperator(b)

def comb_(a,b):                                 # returns product of two state and it's complex conjegate
    # this combines the two matrix
    return a*b,a.T * Dagger(b)

def spinChainCombine(spin, orb):
    totalVar = Network([])
    totalVar_ = Network([])
    v,v_ = comb_(spin[0],Ket("%s_a"%(orb)))
    v.spin = "a"
    v_.spin = "a"
    totalVar.append(v)
    totalVar_.append(v_)
    v,v_ = comb_(spin[1],Ket("%s_b"%(orb)))
    v.spin = "b"
    v_.spin = "b"
    
    totalVar.append(v)
    totalVar_.append(v_)
    
    return totalVar, totalVar_


a = MatrixOperator([[0,1],[0,0]])
#anhilation = \sigma_x + i*\sigma_y
#
astr = MatrixOperator([[0,0],[1,0]])
#creation = \sigma_x - i*\sigma_y
#
s = MatrixOperator([[1,0],[0,-1]])
# antisymmetry operator = 2*\sigma_z
# 
i = MatrixOperator([[1,0],[0,1]])
# identity matrix
n = astr*a

c_a1 = np.kron(astr,i) #creation  operator for alpha electron
c_b1 = np.kron(s,astr) #creation operator for beta electron
z = np.kron(s,s)  # Create Occupide sites
I = np.kron(i,i)  # Create Un Occupied sites


class myEmployeeForm(npyscreen.Form):
    def afterEditing(self):
        if(self.name == '<BRAspin|'):
            s = "%s : %s\n"%(self.numElectron.name,self.numElectron.value)
            s = "%s%s : %s\n"%(s,self.finalS.name,self.finalS.value)
            s = "%s%s : %s\n"%(s,self.Spathway.name,self.Spathway.value)
            s = "%s%s : %s\n"%(s,self.finalM.name,self.finalM.value)
            npyscreen.notify_confirm(s)
            #npyscreen.notify_wait(str(self.parentApp.options))
            self.parentApp.NEXT_ACTIVE_FORM = "ORB1"
        else:
            s = "%s : %s\n"%(self.numElectron.name,self.numElectron.value)
            s = "%s%s : %s\n"%(s,self.finalS.name,self.finalS.value)
            s = "%s%s : %s\n"%(s,self.Spathway.name,self.Spathway.value)
            s = "%s%s : %s\n"%(s,self.finalM.name,self.finalM.value)
            npyscreen.notify_confirm(s)
            
            orb_choice = []
            for i in range(int(self.numElectron.value)):
                if(i%2 == 0):
                    orb_choice.append("h_%d"%(int(i/2)+1))
                else:
                    orb_choice.append("l_%d"%(int(i/2)+1))
            self.parentApp.setOption(orb_choice,int(self.numElectron.value))
            npyscreen.notify_confirm(str(self.parentApp.options))
            
            
            self.parentApp.NEXT_ACTIVE_FORM = "SPIN2"
        #self.parentApp.NEXT_ACTIVE_FORM = None

    def create(self):
        t3 = self.add(npyscreen.BoxTitle, name="Spin Configutation for %s :"%(self.name), max_height=10,
                        scroll_exit = True,
                        contained_widget_arguments={
                                'color': "WARNING", 
                                'widgets_inherit_color': True,},
                        values = ["Hi there", 
                            "First we generate the spin configuration in Bra side", 
                            "Write the number of electron in the system", 
                            "Write the final multiplicity you need",
                            "Write the index of the pathway of S^2. Please refer to https://roehr-lab.github.io/im1.html",
                            "Write the final S_z value"]
                        )
        self.numElectron  = self.add(npyscreen.TitleText,width = 50,value = "4", name='Number Of Electrons')
        self.finalS       = self.add(npyscreen.TitleText,width = 50,value = "0", name='Final S')
        self.Spathway     = self.add(npyscreen.TitleText,width = 50,value = "1", name='Pathway Of S')
        self.finalM       = self.add(npyscreen.TitleText,width = 50,value = "0", name='Final M')
    
        
    def setOption(self, op):
        self.options = op

        
class myEmployeeForm2(npyscreen.Form):
     
    def afterEditing(self):
        pk  = self.Orbitals
        orb_choice = self.parentApp.options
       
        if(self.name == '<BRA|'):
            bra = [orb_choice[i.value[0]]  for i in pk]
            sp = "|Ket > = \n        "
            for i in bra:
                sp = "%s | %s >"%(sp,i)
            npyscreen.notify_confirm(sp)
            self.parentApp.NEXT_ACTIVE_FORM = None
        else:
            bra = [orb_choice[i.value[0]]  for i in pk]
            sp = "<Bra| = \n        "
            for i in bra:
                sp = "%s < %s |"%(sp,i)
            npyscreen.notify_confirm(sp)
            self.parentApp.NEXT_ACTIVE_FORM = "ORB2"

    def beforeEditing(self):
        #npyscreen.notify_wait("Before call")
        #npyscreen.notify_wait(str(self.parentApp.options))
        t3 = self.add(npyscreen.BoxTitle, name="Spatial orbital for %s :"%(self.name), max_height=10,
                        scroll_exit = True,
                        contained_widget_arguments={
                                'color': "WARNING", 
                                'widgets_inherit_color': True,},
                        values = [
                            "Now we assign spatial orbtials to each electrons",
                            "Select the orbital for each electrons"
                        ]
                        )
        self.Orbitals = []
        for i in range(self.parentApp.nelec):   
            pl = self.add(npyscreen.TitleSelectOne, scroll_exit=True, max_height=len(self.parentApp.options), name='Electron %d'%(i),value='0', values = self.parentApp.options,width= 50, rely= 15+ i*5)
            self.Orbitals.append(pl)
        
            
    def create(self):
        pass
        
class MyApplication(npyscreen.NPSAppManaged):
    def onStart(self):
        self.addForm('MAIN', myEmployeeForm, name='New Employee')
        self.cp = 4
       # A real application might define more forms here.......

class MyApplication2(npyscreen.NPSAppManaged):
    def onStart(self):
        self.options = None
        self.nelec = 0
        self.addForm('MAIN', myEmployeeForm, name='|KETspin>')
        self.addForm('SPIN2', myEmployeeForm, name='<BRAspin|')
        self.addForm('ORB1', myEmployeeForm2, name='|KET>')
        self.addForm('ORB2', myEmployeeForm2, name='<BRA|')
    
    def setOption(self,op, elec):
        self.options = op
        self.nelec = elec


if __name__ == '__main__':
    #TestApp2 = MyApplication2()
    #TestApp2.run()
    #K_nelec = int(TestApp2._Forms["MAIN"].numElectron.value)
    #K_finalS = int(TestApp2._Forms["MAIN"].finalS.value)
    #K_Spathway = int(TestApp2._Forms["MAIN"].Spathway.value)
    #K_finalM = int(TestApp2._Forms["MAIN"].finalM.value) + K_finalS
    #
    #B_nelec = int(TestApp2._Forms["SPIN2"].numElectron.value)
    #B_finalS = int(TestApp2._Forms["SPIN2"].finalS.value)
    #B_Spathway = int(TestApp2._Forms["SPIN2"].Spathway.value)
    #B_finalM = int(TestApp2._Forms["SPIN2"].finalM.value) + B_finalS
    #
    #orb_choice = TestApp2.options
    #slk =  TestApp2._Forms["ORB1"].Orbitals
    #ket = [orb_choice[i.value[0]]  for i in slk]
    #slb =  TestApp2._Forms["ORB2"].Orbitals
    #bra = [orb_choice[i.value[0]]  for i in slb]
    K_nelec = 4
    K_finalS = 1
    K_Spathway = 1
    K_finalM = 1
    
    B_nelec = 4
    B_finalS = 1
    B_Spathway = 0
    B_finalM = 1
    
    print("Selected Spatial Orbitals for Kra")
    ket = ["h_1","l_1","h_2","l_2"]
    print(ket)
    
    print("Selected Spatial Orbitals for Bra")
    bra = ["h_1","l_1","h_2","l_2"]
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


    print("Generating Operators")
    with Pool() as pool:
        result = pool.map(kron2,oper1)
    oper1 = result
    
    



    numberMat = []
    for i in range(int(len(oper1)/2)):
        if(i%2 == 0):
            numberMat.append(spinChainCombine([oper1[i*2],oper1[i*2 + 1]],"h_%d"%(int(i/2)+1)))
        else:
            numberMat.append(spinChainCombine([oper1[i*2],oper1[i*2 + 1]],"l_%d"%(int(i/2)+1)))
        
        
    matC = []
    matA = []
    for i in numberMat:
        for j in i[0]:
            matC.append(j)
        for j in i[1]:
            matA.append(j)

    numberMat1 = {}
    sm = []
    for i in range(int(len(oper1)/2)):
        if(i%2 == 0):
            numberMat1["h_%d_%s"%(int(i/2)+1, ab[0])]=[oper1[2*i + 0],matC[2*i + 0],matA[2*i + 0],2*i]
            numberMat1["h_%d_%s"%(int(i/2)+1, ab[1])]=[oper1[2*i + 1],matC[2*i + 1],matA[2*i + 1],2*i + 1]
            sm.append("h_%d_%s"%(int(i/2)+1, ab[0]))
            sm.append("h_%d_%s"%(int(i/2)+1, ab[1]))
        else:
            numberMat1["l_%d_%s"%(int(i/2)+1, ab[0])]=[oper1[2*i + 0],matC[2*i + 0],matA[2*i + 0],2*i]
            numberMat1["l_%d_%s"%(int(i/2)+1, ab[1])]=[oper1[2*i + 1],matC[2*i + 1],matA[2*i + 1],2*i + 1]
            sm.append("l_%d_%s"%(int(i/2)+1, ab[0]))
            sm.append("l_%d_%s"%(int(i/2)+1, ab[1]))

    print("Making Ket Operator")
    detK = []
    for i in range(len(ketStates)):
        dk = np.eye(matC[0].shape[0])
        for j in range(len(ketStates[i])):
            print("%2d %2d"%(i,j), end="\r")
            sk = np.array(numberMat1[ketStates[i][j]][0], dtype=np.float32)
            dk = np.matmul(dk,sk)
        detK.append(dk)
    print("Making Ket Operator")
    detB = []
    for i in range(len(BraStates)):
        db = np.eye(matC[0].shape[0])
        for j in range(len(BraStates[i])):
            print("%2d %2d"%(i,j), end="\r")
            sk = np.array(numberMat1[BraStates[i][j]][0], dtype=np.float32)
            db = np.matmul(db,sk)
        detB.append(db)

    

    def multithreaded_DensityOperators(rankOfMatrix, bra,ket):
        print("Loop")
        OnePD = np.zeros_like(ab1[0])
        TwoPD =  np.zeros_like(ab1[0])
        ThreePD = np.zeros_like(ab1[0])
        for a,i in  enumerate(l1):
            for b,j in  enumerate(l1_):
                OnePD += i*j
                if(rankOfMatrix > 1):
                    for c,k in  enumerate(l1):
                        for d,l in  enumerate(l1_):
                            if(l.spin == k.spin):
                                if(j.spin == i.spin):
                                    TwoPD +=UnevaluatedExpr(k*i*j*l)
                            if( rankOfMatrix > 2):
                                for e,o in  enumerate(l1):
                                    for f,p in  enumerate(l1_):
                                        print("%d %d %d %d %d %d"%(a,b,c,d,e,f),end="\r")
                                        if(p.spin == o.spin):
                                            if(k.spin == l.spin):
                                                if(i.spin ==  j.spin):
                                                    ThreePD += o*k*i*j*l*p
                            else:
                                print("%d %d %d %d"%(a,b,c,d), end="\r")
                else:
                    print(" %d %d"%(a,b), end="\r")
        return OnePD, TwoPD, ThreePD  
    

#OnePD, TwoPD, ThreePD   = multithreaded_DensityOperators(2,l1_,l1)




    from pathos.pools import ProcessPool 
    AllowSpinOrbitCoupling =False
    def Calulcate_OnePD(a,b):
        i = matC[a]
        j = matA[b]
        TwoPD =  np.zeros_like(matC[0])
        ThreePD = np.zeros_like(matC[0])
        rankOfMatrix = 2
        for c,k in  enumerate(matC):
            for d,l in  enumerate(matA):
                if((j.spin == i.spin) or AllowSpinOrbitCoupling):
                    if((l.spin == k.spin) or AllowSpinOrbitCoupling):
                        mat2 = k*i*j*l
                        TwoPD += mat2
                        print("%2d %2d %2d %2d"%(a,b,c,d), end="\r")
                        if( rankOfMatrix > 2):
                            for e,o in  enumerate(matC):
                                for f,p in  enumerate(matA):
                                    print("%d %d %d %d %d %d"%(a,b,c,d,e,f),end="\r")
                                    if(o.spin ==  p.spin):
                                        mat3 = o*mat2*p
                                        ThreePD += mat3
        return matC[a]*matA[b] , TwoPD, ThreePD
    
    def symetry(a):
        mp = torch.zeros_like(a)
        pb =torch.tensor([   
            [0, 1, 2, 3],         # first 4 index holds the value of index correspond to electron wave function. Later 3 index "4 5 6" are same through out.                                                       
            [1, 0, 3, 2],                      # these are indexes of bra term ket term and coefficients
            [0, 3, 2, 1],
            [3, 0, 1, 2],
            [2, 1, 0, 3],
            [1, 2, 3, 0],
            [2, 3, 0, 1],
            [3, 2, 1, 0] ])
        ma = a[0]
        kb = None
        kb2 = torch.zeros(len(a))+1
        for i in range(100):
            s = torch.stack([ma for i in range( len(pb))])
            am = torch.tensor([[i,i,i,i] for i in range(len(pb))])
            indx = []
            for i in range(len(pb)):
                a2 = (((a- s[am,pb][i]) !=0).sum(1) == 0)
                indx.append(a2)
            s2 = torch.stack(indx)
            kb = (s2.sum(0) != 0)
            kb2 = torch.logical_and((s2.sum(0) == 0) ,kb2)
            idx = kb.nonzero(as_tuple=True)
            idx2 = kb2.nonzero(as_tuple=True)
            mp[idx] = ma
            if(len(kb2.nonzero()) > 0):
                ma = a[idx2][0]
            else:
                break
        return mp
    
    print("Making One and Two electron Integral Operator")
    sib = []
    for i in range(2*K_nelec):
        s = [i for j in range(len(matC))]
        s2  = [j for j in range(len(matA))]
        with ProcessPool() as pool:
            b = pool.map(Calulcate_OnePD, s,s2)
        sib.append(b)
    
    OnePD = np.zeros_like(matC[0])
    TwoPD =  np.zeros_like(matC[0])
    ThreePD = np.zeros_like(matC[0])
    for i in range(len(sib)):
        for j in range(len(sib[i])):
            print("%d %d"%(i,j), end="\r")
            OnePD += sib[i][j][0]
            TwoPD += sib[i][j][1]
        #ThreePD += sib[i][j][2]
    print("Generating Coupling  Expression ")   
    lp1 = []
    lp2 = []
    nrm = []
    #print(CGMat)
    for i in range(len(detK)):
        lp1i = []
        lp2i = []
        nrmi = []
        for j in range(len(detB)):
            print("%d %d"%(i,j), end="\r")
            ki = Matrix(detK[i])
            bi = Matrix(detB[j].T)
            OneI = bi*OnePD*ki
            TwoI = bi*TwoPD*ki
            nrmib = bi*ki
            lp1i.append(expand(OneI[0,0]))
            lp2i.append(expand(TwoI[0,0]))
            nrmi.append(nrmib[0,0]*float(CGMat[j,i]))
        lp1.append(lp1i)
        lp2.append(lp2i)
        nrm.append(nrmi)

    print(nrm)
    nrmK = []
    for i in range(len(detK)):
        ki = detK[i]
        bi = detK[i].T
        nrmib = np.matmul(bi,ki)
        nrmK.append(nrmib[0,0]*float(Kcg[0][i]*Kcg[0][i]))
    
    nrmB = []
    for i in range(len(detB)):
        ki = detB[i]
        bi = detB[i].T
        nrmib = np.matmul(bi,ki)
        nrmB.append(nrmib[0,0]*float(Bcg[0][i]*Bcg[0][i]))
    print(CGMat)
    print(nrmB)
    print(nrmK)
    
    nrmK = torch.tensor(nrmK)
    nrmB = torch.tensor(nrmB)
    print("Nromalisation")
    
    print(nrm)        
    l1 = 0
    l2 = 0
    n0 = 0
    for i in range(len(lp1)):
        for j in range(len(lp1[i])):
            #print(i,j,end= " ")
            #print(CGMat[j,i])
            l1 += CGMat[j,i]*lp1[i][j]
            l2 += CGMat[j,i]*lp2[i][j]
    l = expand(l2)
    print()
    print("################################")
    print("Two electron Integrals")
    print("################################")
    twoI_tensor = []
    twoI_C = []
    for i in l.args:
        cp = 1
        var = ""
        sp = []
        twoIc = []
        for j in i.args:
            
            if(type(j) is sympy.Float):
                print(cgcCALC.decimalToFraction(j),end= "  <")
                cp *= j
            else:
                var = "%s%s|"%(var,str(j.args[0]))
                sp.append(str(j.args[0])[:3])
                print(str(j.args[0]), end= " ")
                twoIc.append(numberMat1[str(j.args[0])][3])
        print(">")
        twoIc = np.array(twoIc)

        twoI_tensor.append(np.take(twoIc,[0,1,3,2]))
        twoI_C.append(cp)
        sk = np.array(sp)
        sk = np.take(sk,[0,1,3,2])
        
    twoI_tensor = torch.tensor(twoI_tensor)
    #twoI_tensor = symetry(twoI_tensor.clone())
    t2I = 0
    smb = []
    for i in range(len(twoI_tensor)):
        var = "<%s %s | %s %s >"%(
            sm[twoI_tensor[i,0]],
            sm[twoI_tensor[i,1]],
            sm[twoI_tensor[i,2]],
            sm[twoI_tensor[i,3]]
        )
        smb.append([
            sm[twoI_tensor[i,0]],
            sm[twoI_tensor[i,1]],
            sm[twoI_tensor[i,2]],
            sm[twoI_tensor[i,3]]
        ])
        #print(twoI_C[i])
        t2I += Symbol(var)*twoI_C[i]
    #print()
    #print("##############################################")
    #print("Symmetrised Spin adapted Two Electron Integral")
    #print("##############################################")
    #for i in t2I.args:
    #    print(i)
    
    print()
    print("################################")
    print("Spin Free Two electron integral")
    print("################################")
   
    l = t2I
    t2I = 0
    for i in range(len(l.args)):
        cp = 1
        var = ""
        sp = []
        twoIc = []
        for j in l.args[i].args:
           
            if(type(j) is sympy.Float):
                #print(cgcCALC.decimalToFraction(j),end= " |")
                #print(j,end= " ")
                cp *= j
        var = "<%s %s | %s %s >"%(smb[i][0][:3],smb[i][1][:3],smb[i][2][:3],smb[i][3][:3])
        t2I += Symbol(var)*cp
        #print(Symbol(var)*cp)
     #print(t2I)
    for i in t2I.args:
        for j in i.args:
            if(type(j) is sympy.Float):
                print(cgcCALC.decimalToFraction(j),end= " ")
            else:
                print(j,end=" ")
        print()
    print()
    print("################################")
    print("One electron Integral")
    print("################################")
    oe1= expand(l1)
    #print(oe1)
    

    
    for i in oe1.args:
        cp = 1
        for j in i.args:
            if(type(j) is sympy.Float):
                print(cgcCALC.decimalToFraction(j),end= " ")
                cp *= j
            else:
                print(str(j),end=" ")
        print()

        
    
    
    print("program Ends here")
