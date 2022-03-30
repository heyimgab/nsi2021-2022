def nom_carte(carte):
    valeur, couleur = carte
    if carte_valide(carte) == True:
        dico = 12; "Dame"]
        if valeur in range(2, 11):
            return str(valeur) + "de" + couleur
        else:
            return dico[valeur]+"de"+couleur



