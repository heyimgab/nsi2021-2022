prenom=input("Entrez votre prénom : ")
age=int(input("Entrez votre âge : "))
taille=int(input("Entrez votre taille (en cm) : "))

print("Bonjour",prenom,". Vous avez",age,"ans et vous mesurez",taille,"cm.")

poids=float(input("Entrez votre poids (en kg) : "))
taille=taille/100
imc=poids/taille**2
print("Votre IMC est de ",imc)

if imc<18.5:
    print("Vous êtes en Insuffisance pondérale.")
elif imc<25:
    print("Vous avez un poids normal.")
elif imc<30:
    print("Vous êtes en surpoids.")
else:
    print("Vous êtes obèse.")
