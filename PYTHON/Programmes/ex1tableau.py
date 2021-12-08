n=int(input("Entrez le nombre d'élèves :"))
tableau = []*n
notes = []
for i in range(0,n):
    notes[i]=float(input("Saisir les notes de l'élève "+str(i+1)+": "))
    print("Elève ",n+1, " : ",i)

