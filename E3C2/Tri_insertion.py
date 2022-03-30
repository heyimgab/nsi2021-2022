#*****************************************************************************
#****** NSI ************ E3C2 **************** H. Kesseler *******************
#*****************************************************************************
#***************************** Tri insertion *********************************
#*****************************************************************************

import random

def tri_insertion(L):
    n = len(L)
    if L==[]:         # Compléter la condition pour gérer le cas de la liste vide
        return L
    for j in range(1,n):          ## Boucle sur toute la liste
        e = L[j]                  ## e sera la valeur dans la case j de la liste
        i = j-1                   ## i sera l'index de la case juste avant j
        ## On remonte la liste triée L[0,j-1] tant que la valeur L[i] est
        ## plus grande que la valeur e
        while  i >= 0 and L[i] > e:
            L[i+1]=L[i]           ## On décale la valeur L[i] vers la droite
            i = i-1               # Compléter pour décrémenter i
        L[i+1] = e   # Compléter pour mettre la valeur L[j] dans la case libre L[i+1]
    return L

#******************************************************************************
#************* Vérification du fonctionnement de la fonction Tri **************
liste = []
for k in range(20):
    liste.append(random.randint(-10,40))
print(liste)
liste_triee = tri_insertion(liste)
print(liste_triee)