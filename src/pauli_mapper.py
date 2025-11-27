
# TODO make it qiskit compatible


def pauli_op(a, b):
    if(a== "X" and  b=="Y"):
        return "Z" , 1.0j
    if(a== "Y" and  b=="X"):
        return "Z" , -1.0j
    if(a== "X" and  b=="Z"):
        return "Y" , -1.0j
    if(a== "Z" and  b=="X"):
        return "Y" , 1.0j
    if(a== "Y" and  b=="Z"):
        return "Z" , 1.0j
    if(a== "Z" and  b=="Y"):
        return "X" , -1.0j
    
    if(a== "X" and  b=="X"):
        return "I" , 1.0
    if(a== "Y" and  b=="Y"):
        return "I" , 1.0
    if(a== "Z" and  b=="Z"):
        return "I" , 1.0
    
    
    if(a== "I" and  b=="X"):
        return "X" , 1.0
    if(a== "I" and  b=="Y"):
        return "Y" , 1.0
    if(a== "I" and  b=="Z"):
        return "Z" , 1.0
    
    if(a== "X" and  b=="I"):
        return "X" , 1.0
    if(a== "Y" and  b=="I"):
        return "Y" , 1.0
    if(a== "Z" and  b=="I"):
        return "Z" , 1.0
    
    if(a== "I" and  b=="I"):
        return "I" , 1.0
    
    
    
