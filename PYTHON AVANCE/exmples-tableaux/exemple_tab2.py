#******************************************
#********** exemple_tab2 ******************
#******************************************

#On crée un tableau de 7 cases contenant des 0
tabTemp=[0.0]*7
somme=0
for i in range(0,7):
    tabTemp[i]=float(input("Saisir la température du jour "+str(i+1)+": "))
    somme=somme+tabTemp[i]
moyenne=somme/7
print("Voici le tableau des températures",tabTemp)
print("La moyenne est de",moyenne,"degrés")




