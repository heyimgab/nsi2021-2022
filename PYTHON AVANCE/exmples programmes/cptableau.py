#################### COPIE TABLEAU ############################

## Ce code ne permet pas de copier le tableau, A et B pointent vers la même place en mémoire
## Pour une copie distincte, on pourra utiliser B=A[:]
## B = A[1:] copie du tableau amputée du premier élément
## B = A[:-1] copie du tableau amputee du dernier élément
## B = A[::-1] copie du tableau en ordre inverse 

def copie():
    A = [1,2,3]
    B = A
    B[0]=5
    print("liste B ",B)
    print("Liste A ",A)
