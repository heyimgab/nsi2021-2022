# Créé par herve, le 10/10/2021 en Python 3.7
#*************** exemple_tab4 *****************
#********* tableau à deux dimensions **********
#**********************************************

#************* création du tableau ************
tableau = []
for ligne in range(5):
    nvLigne = []
    for colonne in range(5):
        nvLigne.append((ligne, colonne))
    tableau.append(nvLigne)
for ligne in tableau:
    print(ligne)

#************ accéder à une valeur *************
print(tableau[4][2])
