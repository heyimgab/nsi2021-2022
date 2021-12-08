# Exercice 4, températures.

somme = 0
for i in range(1,8):
 temperature = float(input("Saisir la température n°"+str(i)+" : "))
 somme = somme + temperature

 print("Température moyenne: ",somme/7)
