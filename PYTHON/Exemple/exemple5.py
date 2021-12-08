n=int(input("Entrez 1, 2 ou 3 (0 pour sortir) : "))
while n!=0:
    if n==1:
        print("Vous avez entré le chiffre 1. Vous aimez l'unicité.")
    elif n==2:
        print("Vous avez choisi le chiffre 2. Vous aimez les paires.")
    elif n==3:
        print("Vous avez préféré le chiffre 3.")
    else:
        print("On vous a demandé de taper 1, 2 ou 3 !!! (ou 0)...")
    n=int(input("Entrez 1, 2 ou 3 (0 pour sortir) : "))
print("Le programme est terminé.")
