from datetime import* # Importation du module datetime

dateactuelle=date.today() # On récupère la date du jour
print(dateactuelle)
print(type(dateactuelle)) # Le type de cette date est spécifique
jourActuel=dateactuelle.day # On récupère le jour
moisActuel=dateactuelle.month # le mois
anneeActuelle=dateactuelle.year # et l'année

print(type(jourActuel)) # On vérifie le type de la variable jourActuel pour pouvoir la manipuler par la suite.

print("Nous sommes le",jourActuel,moisActuel,anneeActuelle)

datetime



