# Créé par herve, le 10/10/2021 en Python 3.7
#********************************************
#************* exemple_tab1******************
#********************************************

#******** liste vide*******************
liste=[]

#******** liste remplie ***************
liste1=[1,2,5,8]
liste2=["Paul","Jacques","Justin","Pierre"]

#******** lecture d'une liste *********
print(liste1[0])
print(liste1[3])

#****** lecture en dehors de la liste ***
"""print(liste1[4])"""
# affichage d'une erreur

#******* ajouter une donnée à la liste ***
liste1.append(14)
print(liste1)

#***** Parcourir une liste **************
for i in range(len(liste1)):
	print("indice",i,"->",liste1[i])

#******** Modifier une valeur *********
liste1[3]=19
print(liste1)

#********Supprimer une valeur *********
del liste1[2]
print(liste1)

