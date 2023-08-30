import matplotlib.pyplot as plt
import numpy as np
import torch 
import sys

def bothMat(s,F,eri):
    hm = 0
    hn = 1
    ho = 2
    lm = 3
    ln = 4
    lo = 5
    f = np.sqrt(1.5)
    bo =1.0
    s[0,1]   =  0
    s[0,2]   =  0
    s[0,3]   =  F[lm,ln]*bo
    s[0,4]   =  0
    s[0,5]   = -F[hm,ho]*bo
    s[0,6]   = -F[hm,hn]*bo
    s[0,7]   =  0
    s[0,8]   =  F[lm,lo]*bo
    s[0,9]   =  0
    s[0,10]  =  0
    s[0,11]  =  0

    s[1,2]   =  0 
    s[1,3]   = -F[hn,hm]*bo
    s[1,4]   =  F[ln,lo]*bo
    s[1,5]   =  0
    s[1,6]   =  F[ln,lm]*bo
    s[1,7]   = -F[hn,ho]*bo
    s[1,8]   =  0
    s[1,9]   =  0
    s[1,10]  =  0
    s[1,11]  =  0 

    s[2,3]   =   0    
    s[2,4]   = - F[ho,hn]*bo
    s[2,5]   =   F[lo,lm]*bo
    s[2,6]   =   0   
    s[2,7]   =   F[lo,ln]*bo
    s[2,8]   =   -F[ho,hm]*bo
    s[2,9]   =   0   
    s[2,10]  =   0 
    s[2,11]  =   0 

    s[3,4]   =   0
    s[3,5]   =   0
    s[3,6]   =   0
    s[3,7]   = - F[hm,ho]*bo
    s[3,8]   =   F[ln,lo]*bo
    s[3,9]   =   F[lm,hn]*f
    s[3,10]  =   0
    s[3,11]  =   0

    s[4,5]   =  0 
    s[4,6]   =  F[lo,lm]*bo
    s[4,7]   =  0 
    s[4,8]   = -F[hn,hm]*bo
    s[4,9]   =  0 
    s[4,10]  =  F[ln,ho]*f
    s[4,11]  =  0 

    s[5,6]   =- F[ho,hn]*bo
    s[5,7]   =  F[lm,ln]*bo
    s[5,8]   =  0  
    s[5,9]   =  0  
    s[5,10]  =  0  
    s[5,11]  =  F[lo,hm]*f

    s[6,7]   =   0
    s[6,8]   =   0
    s[6,9]   =   F[ln,hm] * f
    s[6,10]  =   0
    s[6,11]  =   0

    s[7,8]   =   0
    s[7,9]   =   0
    s[7,10]  =   F[lo,hn] * f
    s[7,11]  =   0

    s[8,9]   =   0
    s[8,10]  =   0
    s[8,11]  =   F[lm,ho] * f

    s[9,10]  =   0
    s[9,11]  =   0

    s[10,11] =   0

    f= np.sqrt(1.5)
    bo = 1.0
    s[0,1]    +=  (-eri[hm,hn,ln,lm] + 2*eri[hm,lm,ln,hn])*bo
    s[0,2]    +=  (-eri[hm,ho,lo,lm] + 2*eri[hm,lm,lo,ho])*bo
    s[0,3]    +=  (-eri[hm,hm,lm,ln] + 2*eri[hm,lm,ln,hm])*bo # 
    s[0,4]    +=  (-eri[hm,hn,lo,lm] + 2*eri[hm,lm,lo,hn])*bo #
    s[0,5]    +=  (-eri[hm,ho,lm,lm] + 2*eri[hm,lm,lm,ho])*bo #
    s[0,6]    +=  (-eri[hm,hn,lm,lm] + 2*eri[hm,lm,lm,hn])*bo #
    s[0,7]    +=  (-eri[hm,ho,ln,lm] + 2*eri[hm,lm,ln,ho])*bo #
    s[0,8]    +=  (-eri[hm,hm,lm,lo] + 2*eri[hm,lm,lo,hm])*bo #
    s[0,9]    += (-eri[hm,lm,hn,hm] +   eri[ln,lm,hn,ln])*f
    s[0,10]   +=  0
    s[0,11]   += (-eri[hm,lm,ho,hm] +   eri[lo,lm,ho,lo])*f

    s[1,2]    +=   (-eri[hn,ho,lo,ln] + 2*eri[hn,ln,lo,ho])*bo #
    s[1,3]    +=   (-eri[hn,hm,ln,ln] + 2*eri[hn,ln,ln,hm])*bo #
    s[1,4]    +=   (-eri[hn,hn,ln,lo] + 2*eri[hn,ln,lo,hn])*bo #
    s[1,5]    +=   (-eri[hn,ho,lm,ln] + 2*eri[hn,ln,lm,ho])*bo #
    s[1,6]    +=   (-eri[hn,hn,ln,lm] + 2*eri[hn,ln,lm,hn])*bo #
    s[1,7]    +=   (-eri[hn,ho,ln,ln] + 2*eri[hn,ln,ln,ho])*bo 
    s[1,8]    +=   (-eri[hn,hm,lo,ln] + 2*eri[hn,ln,lo,hm])*bo
    s[1,9]    +=  (-eri[hn,ln,hm,hn] +   eri[lm,ln,hm,lm])*f
    s[1,10]   +=  (-eri[hn,ln,ho,hn] +   eri[lo,ln,ho,lo])*f
    s[1,11]   +=   0 

    s[2,3]    +=   (-eri[ho,hm,ln,lo] + 2*eri[ho,lo,ln,hm] )*bo
    s[2,4]    +=   (-eri[ho,hn,lo,lo] + 2*eri[ho,lo,lo,hn] )*bo
    s[2,5]    +=   (-eri[ho,ho,lo,lm] + 2*eri[ho,lo,lm,ho] )*bo
    s[2,6]    +=   (-eri[ho,hn,lm,lo] + 2*eri[ho,lo,lm,hn])*bo
    s[2,7]    +=   (-eri[ho,ho,lo,ln] + 2*eri[ho,lo,ln,ho] )*bo
    s[2,8]    +=   (-eri[ho,hm,lo,lo] + 2*eri[ho,lo,lo,hm] )*bo
    s[2,9]    +=   0
    s[2,10]   +=  ( -eri[ho,lo,hn,ho] +   eri[ln,lo,hn,ln])*f
    s[2,11]   +=  ( -eri[ho,lo,hm,ho] +   eri[lm,lo,hm,lm])*f

    s[3,4]    +=   (-eri[hm,hn,lo,ln] + 2*eri[hm,ln,lo,hn])*bo
    s[3,5]    +=   (-eri[hm,ho,lm,ln] + 2*eri[hm,ln,lm,ho])*bo
    s[3,6]    +=   (-eri[hm,hn,ln,lm] + 2*eri[hm,lm,ln,hn])*bo
    s[3,7]    +=   (-eri[hm,ho,ln,ln] + 2*eri[hm,ln,ln,ho] )*bo
    s[3,8]    +=   (-eri[hm,hm,lo,ln] + 2*eri[hm,ln,lo,hm] )*bo
    s[3,9]    +=  ( eri[hm,lm,ln,ln] -   eri[lm,hn,hm,lm] )*f
    s[3,10]   +=  (-eri[hm,ho,hn,lo] )*f
    s[3,11]   +=  (eri[ho,lm,ln,lo] )*f

    s[4,5]    +=   (-eri[hn,ho,lm,lo] + 2*eri[hn,lo,lm,ho])*bo
    s[4,6]    +=   (-eri[hn,hn,lm,lo] + 2*eri[hn,lo,lm,hn] )*bo
    s[4,7]    +=   (-eri[hn,ho,lo,ln] + 2*eri[hn,ln,lo,ho])*bo
    s[4,8]    +=   (-eri[hn,hm,lo,lo] + 2*eri[hn,lo,lo,hm] )*bo
    s[4,9]    += (  eri[hm,ln,lo,lm] )*f
    s[4,10]   += ( -eri[ln,ho,hn,ln] +   eri[hn,ln,lo,lo] ) *f
    s[4,11]   += ( -eri[hm,hn,ho,lm] ) *f

    s[5,6]    +=   (-eri[ho,hn,lm,lm] + 2*eri[ho,lm,lm,hn] )*bo
    s[5,7]    +=   (-eri[ho,ho,ln,lm] + 2*eri[ho,lm,ln,ho] )*bo
    s[5,8]    +=   (-eri[ho,hm,lm,lo] + 2*eri[ho,lo,lm,hm])*bo
    s[5,9]    +=  (-eri[hn,ho,hm,ln] )*f
    s[5,10]   +=  (eri[hn,lo,lm,ln] )*f
    s[5,11]   +=  ( eri[ho,lo,lm,lm] - eri[lo,hm,ho,lo] )*f

    s[6,7]    +=   (-eri[hn,ho,ln,lm] + 2*eri[hn,lm,ln,ho])*bo
    s[6,8]    +=   (-eri[hn,hm,lo,lm] + 2*eri[hn,lm,lo,hm])*bo
    s[6,9]    +=  ( -eri[ln,hm,hn,ln] +   eri[hn,ln,lm,lm] )*f
    s[6,10]   +=  ( eri[ho,ln,lm,lo] )*f
    s[6,11]   +=  ( -eri[ho,hn,hm,lo] )*f

    s[7,8]    +=   (-eri[hm,hn,lm,lo] + 2*eri[hm,lo,lm,hn])*bo
    s[7,9]    +=  ( -eri[hm,ho,hn,lm] )*f
    s[7,10]   +=  ( eri[ho,lo,ln,ln] -   eri[lo,hn,ho,lo])*f
    s[7,11]   +=  ( eri[hm,lo,ln,lm] )*f

    s[8,9]    +=  (eri[hn,lm,lo,ln] )*f
    s[8,10]   +=  (-eri[hn,hm,ho,ln] )*f
    s[8,11]   +=  (eri[hm,lm,lo,lo] -   eri[lm,ho,hm,lm] )*f

    s[9,10]   +=   2*eri[hm,ho,lo,lm]
    s[9,11]   +=   2*eri[hn,ho,lo,ln]

    s[10,11]  +=   2*eri[hm,hn,ln,lm]
    return s



def ETT(s,F,eri):
    hm = 0
    hn = 1
    ho = 2
    lm = 3
    ln = 4
    lo = 5
    #print(S1En)
    #groundEn = 2*hcr[hm,hm] + 2*hcr[hn,hn] + 2*hcr[ho,ho] + grounEri
    #groundTT = hcr[hm,hm] + hcr[hn,hn] + hcr[lm,lm] + hcr[ln,ln] + 2*hcr[ho,ho] #+ groundTTeri
    #CAEn = 2.0*hcr[hm,hm] + 1.0*hcr[hn,hn] + 2.0*hcr[ho,ho] + 1.0*hcr[lm,lm] + CAeri
    #S1En = 2.0*hcr[hn,hn] + 2.0*hcr[ho,ho] + 1.0*hcr[lm,lm] + 1.0*hcr[hm,hm] + S1eri 
    s[0,0] =  2.0*F[hn,hn] + 2.0*F[ho,ho] + F[lm,lm] + F[hm,hm] -1.0*eri[hm,hm,lm,lm] + 2.0*eri[hm,lm,lm,hm]#- groundEn#F[lm,lm]-F[hm,hm] - hcr[ho,ho] + hcr[ln,ln] + hcr[lo,lo] 
    s[1,1] =  2.0*F[hm,hm] + 2.0*F[ho,ho] + F[ln,ln] + F[hn,hn]-1.0*eri[hn,hn,ln,ln] + 2.0*eri[hn,ln,ln,hn] #- groundEn#groundEn#F[lm,lm]-F[hn,hn] - hcr[ho,ho] + hcr[lm,lm] + hcr[lo,lo] 
    s[2,2] = 2.0*F[hn,hn] + 2.0*F[hm,hm] + F[lo,lo] + F[ho,ho]-1.0*eri[ho,ho,lo,lo] + 2.0*eri[ho,lo,lo,ho] #- groundEn#groundEn#F[lm,lm]-F[ho,ho] - hcr[hn,hn] + hcr[lm,lm] + hcr[ln,ln] 
    
    s[3,3] = 2.0*F[hn,hn] + 2.0*F[ho,ho] + F[hm,hm] + F[ln,ln] -1.0*eri[hm,hm,ln,ln] + 2.0*eri[hm,ln,hm,ln] #- groundEn#F[lm,lm]-F[hm,hm] - hcr[ho,ho] + hcr[ln,ln] + hcr[lo,lo] 
    s[4,4] = 2.0*F[hm,hm] + 2.0*F[ho,ho] + F[hn,hn] + F[lo,lo] -1.0*eri[hn,hn,lo,lo] + 2.0*eri[hn,lo,hn,lo]# - groundEn#groundEn#F[lm,lm]-F[hn,hn] - hcr[ho,ho] + hcr[lm,lm] + hcr[lo,lo] 
    s[5,5] = 2.0*F[hn,hn] + 2.0*F[hm,hm] + F[ho,ho] + F[lm,lm] -1.0*eri[ho,ho,lm,lm] + 2.0*eri[ho,lm,ho,lm]# - groundEn#groundEn#F[lm,lm]-F[ho,ho] - hcr[hn,hn] + hcr[lm,lm] + hcr[ln,ln] 
    s[6,6] = 2.0*F[hm,hm] + 2.0*F[ho,ho] + F[hn,hn] + F[lm,lm] -1.0*eri[hn,hn,lm,lm] + 2.0*eri[hn,lm,hn,lm]# - groundEn#F[lm,lm]-F[hm,hm] - hcr[ho,ho] + hcr[ln,ln] + hcr[lo,lo] 
    s[7,7] = 2.0*F[hm,hm] + 2.0*F[hn,hn] + F[ho,ho] + F[ln,ln] -1.0*eri[ho,ho,ln,ln] + 2.0*eri[ho,ln,ho,ln]# - groundEn#groundEn#F[lm,lm]-F[hn,hn] - hcr[ho,ho] + hcr[lm,lm] + hcr[lo,lo] 
    s[8,8] = 2.0*F[hn,hn] + 2.0*F[ho,ho] + F[hm,hm] + F[lo,lo] -1.0*eri[hm,hm,lo,lo] + 2.0*eri[hm,lo,hm,lo]# - groundEn#groundEn#F[lm,lm]-F[ho,ho] - hcr[hn,hn] + hcr[lm,lm] + hcr[ln,ln] 

    s[9,9]  = 2.0*F[ho,ho] + F[lm,lm] + F[hm,hm] + F[ln,ln] + F[hn,hn] -1.0*eri[hm,hm,lm,lm] -1.0*eri[hn,hn,ln,ln] 
    s[10,10]= 2.0*F[hm,hm] + F[ln,ln] + F[hn,hn] + F[lo,lo] + F[ho,ho] -1.0*eri[hn,hn,ln,ln] -1.0*eri[ho,ho,lo,lo] 
    s[11,11]= 2.0*F[hn,hn] + F[lm,lm] + F[hm,hm] + F[lo,lo] + F[ho,ho] -1.0*eri[ho,ho,lo,lo] -1.0*eri[hm,hm,lm,lm] 

    
    #s[9,9]  = 2.0*F[ho,ho] + F[hm,hm] + F[hm,hm] + F[hn,hn] + F[hn,hn] + 0.5 *eri[hm,hn,hn,hm] - 1.0 *eri[hm,lm,lm,hm] + 0.5 *eri[hm,ln,ln,hm]  + 0.5* eri[hn,lm,lm,hn]  - 1.0* eri[hn,ln,ln,hn]  + 0.5* eri[lm,ln,ln,lm]
    #s[10,10]= 2.0*F[hm,hm] + F[hn,hn] + F[hn,hn] + F[ho,ho] + F[ho,ho] + 0.5 *eri[hn,ho,ho,hn] - 1.0 *eri[hn,ln,ln,hn] + 0.5 *eri[hn,lo,lo,hn]  + 0.5* eri[ho,ln,ln,ho]  - 1.0* eri[ho,lo,lo,ho]  + 0.5* eri[ln,lo,lo,ln]
    #s[11,11]= 2.0*F[hn,hn] + F[hm,hm] + F[hm,hm] + F[ho,ho] + F[ho,ho] + 0.5 *eri[hm,ho,ho,hm] - 1.0 *eri[hm,lm,lm,hm] + 0.5 *eri[hm,lo,lo,hm]  + 0.5* eri[ho,lm,lm,ho]  - 1.0* eri[ho,lo,lo,ho]  + 0.5* eri[lm,lo,lo,lm]

    #print(F[lm,lm] -F[hm,hm])
    #print(F[ln,ln]-F[hn,hn])
    #print(groundTT)
    #print(groundEn)
    return s

def plot_fct(del_X=0.0,del_Y=0.0, color="ocean_r"):
    vbs = del_X
    mvs = del_Y
    col = color
    v = del_X
    mvi = del_Y
    f = np.sqrt(1.5)
    hm = 0
    hn = 1
    ho = 2
    lm = 3
    ln = 4
    lo = 5

    bo = 1.0
    
    orb = torch.load("Orb%f_%f.pt"%(v,mvi))
    fron = torch.load("frontier%f_%f.pt"%(v,mvi))
    fock = torch.load("Fock%f_%f.pt"%(v,mvi))
    eri = torch.load("eri1_%f_%f.pt"%(v,mvi))
#hcore = torch.load("Hcore%f_%f.pt"%(v,mvi))
    F= fron.T.mm(fock).mm(fron)
#h = fron.T.mm(hcore).mm(fron)
    s = torch.zeros(12,12)
    s = bothMat(s,F,eri)
    s = ETT(s,F,eri)
    sdt = s
#plt.show()
    groundEn = 2*F[hm,hm] + 2*F[hn,hn] + 2*F[ho,ho]
    bd =torch.zeros(13,13)
    bd[1:,1:] =s
    #bd =torch.zeros(10,10)
    #bd[1:,1:] =s[:9,:9]

    bd[0,0] = groundEn
    bd[0,1] = F[lm,hm]
    bd[0,2] = F[ln,hn]
    bd[0,3] = F[lo,ho]
    bd[0,4] = F[ln,hm]
    bd[0,5] = F[lo,hn]
    bd[0,6] = F[lm,ho]
    bd[0,7] = F[lm,hn]
    bd[0,8] = F[ln,ho]
    bd[0,9] = F[lo,hm]
    bd[0,10] = np.sqrt(1.5)*eri[hm,lm,hn,ln]
    bd[0,11] = np.sqrt(1.5)*eri[hn,ln,ho,lo]
    bd[0,12] = np.sqrt(1.5)*eri[hm,lm,ho,lo]
    
    ab,ac =torch.symeig(bd,eigenvectors=True, upper=True)
    kb = ab*27.2114
    return kb, torch.diagonal(bd)
    
i = int(sys.argv[1])
j = int(sys.argv[2])
ssa,ssb = plot_fct(i*0.1,j*0.1)

plot =[]
plot2 = []
for i in range(41):
    sbp = []
    sap = []
    for j in range(41):
        print(" %d %d"%(i,j))
        ssa,ssb = plot_fct(i*0.1,j*0.1)
        sbp.append(ssa)
        sap.append(ssb)
    plot.append(torch.stack(sbp))
    plot2.append(torch.stack(sap))
    
    
sp = torch.stack(plot)
sp2 = torch.stack(plot2)

print(sp.size())
torch.save(sp,"energy.pt")
torch.save(sp2,"energyD.pt")
