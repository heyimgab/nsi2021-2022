#****************************************************
#**************** exemple_tab3 **********************
#*********** Création par compréhension *************
#****************************************************

#******** Création d'une liste avec une boucle ******
liste=[]
for n in range(1,11):
    liste=liste+[n]
print("liste = ",liste)

#******* Création de la même liste plus simplement ****
tab1=[n for n in range(1,11)]
print("tab1 =",tab1)

#*** Création de la liste en appliquant une fonction ***
tab2=[2*n for n in range(1,11)]
print("tab2 =",tab2)

#*** Création de la liste en appliquant une fonction
#*** et en réalisant un test dans la liste initiale
tab3=[n for n in range(1,21) if n%2==0]
print("tab3 =",tab3)

#*** Même chose à partir d'une liste déjà créé *******
t=[1,4,8,5,7,12]
tab4=[x for x in t if x%2==0]
print("tab4 =",tab4)






