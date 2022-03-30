"""
Fonction estTrie(tableau)
	trie=Vrai
	Pour i allant de 0 à longueur(tableau)-2 faire
		Si (tableau[i]>tableau[i+1]) alors
			trie=Faux
		Fin Si
	Fin Pour
	retourner trie
"""

def estTrie(tableau):
    pass

#tests
"""assert(estTrie([1,1,2,3,5,6,7])==True),"Test tableau trié"
assert(estTrie([1,2,6,3,7,8])==False),"Test tableau non tiré"
"""

"""
Procédure triParSelection1 (tableau)
	n=longueur(tableau)
	Pour i allant de n-1 à 0 avec un pas de -1 faire
		indiceMaxi=0
		Pour k allant de 0 à i faire
			Si (tableau[k]>tableau[indiceMaxi]) alors
				indiceMaxi=k
			Fin Si
		Fin Pour
		temp=tableau[i]
		tableau[i]=tableau[indiceMaxi]
		tableau[indiceMaxi]=temp
	Fin Pour
"""
def triParSelection1(tableau):
    n=len(tableau)
    for i in range(n-1, -1, -1):
        indiceMaxi=0
        for k in range(1, i+1):
            if tableau[k]>tableau[indiceMaxi]:
                indiceMaxi=k
        temp=tableau[i]
        tableau[i]=tableau[indiceMaxi]
        tableau[indiceMaxi]=temp
    

"""
Procédure triParSelection2(tableau)
	n=longueur(tableau)
	Pour i allant de 0 à n-1 faire
		indiceMaxi=0
		Pour k allant de 0 à n-1-i faire
			Si (tableau[k]>tableau[indiceMaxi]) alors
				indiceMaxi=k
			Fin Si
		Fin Pour
		temp=tableau[n-1-i]
		tableau[n-1-i]=tableau[indiceMaxi]
		tableau[indiceMaxi]=temp
	Fin Pour
"""

def triParSelection2(tableau):
    pass

"""
Procédure triParSelection3(tableau)
"""
def triParSelection3(tableau):
    pass

""" Tri à Bulles
Procédure triABulles (tableau)
	n=longueur(tableau)
	Pour i allant de 0 à n-2 faire
		Pour k allant de 0 à n-2-i faire
			Si tableau[k]>tableau[k+1] alors
				temp=tableau[k]
				tableau[k]=tableau[k+1]
				tableau[k+1]=temp
			Fin Si
		Fin Pour
	Fin Pour
"""
def triABulles(tableau):
    n=len(tableau)
    for i in range(0, n-2):
        for k in range(0, n-2-i):
            if tableau[k]>tableau[k+1]:
                temp = tableau[k]
                tableau[k]=tableau[k+1]
                tableau[k+1]=temp
            
    pass

"""
Procédure triParInsertion(tableau)
	n=longueur(tableau)
	Pour i allant de 1 à n-1 faire
		k=i
		Tant que tableau[k]<tableau[k-1] et k>0 faire
			temp=tableau[k]
			tableau[k]=tableau[k-1]
			tableau[k-1]=temp
			k=k-1
		Fin tant que
	Fin Pour
"""

def triParInsertion(tableau):
    pass
            
#Tests
tab=[3,7,1,9,6,0,5,3,7]
print("Tableau non trié",tab)
triParSelection1(tab)
print("Tableau trié",tab)

