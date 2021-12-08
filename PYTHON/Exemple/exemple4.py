from random import*

rep=False
a=randrange(1,101)
b=randrange(1,101)

while rep==False:
    resultat=int(input(str(a)+"*"+str(b)+"=?"))
    if resultat==a*b:
        rep=True
print("Bravo, vous avez trouvé la bonne réponse.")
