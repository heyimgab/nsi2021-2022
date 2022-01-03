################# TABLEAU A DEUX DIMENSIONS ####################

tab = [[22,36,15,11],[-48,13,-12,48],[25,-16,-71,32]]

## Ici tab[1][0] vaut -48

## Création d'un tableau à deux dimensions avec append

tableau = []
for ligne in range(5):
    nvLigne= []
    for colonne in range(5):
        nvLigne.append((ligne,colonne))
    tableau.append(nvLigne)
for ligne in tableau:
    print(ligne)


## Afficher un tableau à deux DIMENSIONS

for i in range(len(tab)):
    print(tab[i])

## Afficher le tableau à deux dimensions mais sans les crochets 

for i in range(len(tab)):
    for j in range(len(tab[0])):
        print(tab[i][j],end= " ")
    print()

