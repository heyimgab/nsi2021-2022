#################  EXERCICE 7  ################# 


#   ███████╗██╗  ██╗    ███████╗ ██████╗ ██╗   ██╗
#   ██╔════╝╚██╗██╔╝    ╚════██║ ██╔══██╗╚██╗ ██╔╝
#   █████╗   ╚███╔╝         ██╔╝ ██████╔╝ ╚████╔╝ 
#   ██╔══╝   ██╔██╗        ██╔╝  ██╔═══╝   ╚██╔╝  
#   ███████╗██╔╝ ██╗       ██║██╗██║        ██║   
#   ╚══════╝╚═╝  ╚═╝       ╚═╝╚═╝╚═╝        ╚═╝   
                                              
#################  TABLEAUX  ################# 

combinaisons=[[0,0],[0,1],[1,0],[1,1]]

#################  FONCTIONS  ################# 

def OU(a, b):
    if a==1 or b==1:
        return 1
    else:
        return 0

def ET(a, b):
    if a==1 and b==1:
        return 1 
    elif a==1 and b==0:
        return 0
    elif a==0 and b==1:
        return 0
    elif a==0 and b==0:
        return 0

def NAND(a, b):                                     # def NAND2(a, b):
    if a==1 and b==1:                               #     if a==1 and b==1:
        return 0                                    #         return 0
    elif a==1 and b==0:                             #     else:
        return 1                                    #         return 1
    elif a==0 and b==1:
        return 1
    elif a==0 and b==0:
        return 1

def NOR(a, b):                                      # def NOR2(a, b):
    if a==0 and b==0:                               #     if a==0 and b==0:
        return 1                                    #        return 1
    elif a==0 and b==1:                               #     else:
        return 0                                    #        return 0
    elif a==1 and b==0:
        return 0
    elif a==1 and b==1:
        return 0

def XOR(a, b):
    if a==0 and b==1:
        return 1
    elif a==1 and b==0:
        return 1
    else:
        return 0

def table():
    return 0

################# USER INPUT ################# 

a=input("Donner le premier argument :")
assert (a=="1" or a=="0", "Argument invalide")
a=int(a)

b=input("Donner le deuxieme argument :")
assert (b=="1" or b=="0", "Argument invalide")
b=int(b)

