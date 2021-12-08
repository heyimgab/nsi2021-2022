# Exercice 5

# Création de la fonction checkFeb pour vérifier le nombre de jours en février.

def checkFeb():
    if mois == 2 and jour >= 28:
        print("Nous sommes en février. Ce jour ne peut pas exister.")
        quit()
    return


# Requête de la date à l'utilisateur

jour = int(input("Entrez le jour :"))
if jour > 31:
    print("Ce jour n'existe pas")
    quit()
elif jour < 1:
    print("Ce jour n'existe pas")
    quit()

mois = int(input("Entrez le mois :"))
checkFeb()
if mois > 12:
    print("Ce mois n'existe pas")
    quit()
elif mois < 1:
    print("Ce mois n'existe pas")
    quit()

annee1 = int(input("Entrez l'année :"))
annee2 = str(annee1)
if len(annee2) > 4:
    print("Le format de l'année est invalide.")
    quit()

print("Nous sommes le ",jour,"/",mois,"/",annee2,".")
