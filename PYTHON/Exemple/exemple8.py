# Fonctions

def f(x):
    a=1
    b=2
    c=3
    return a*x*x+b*x+c

# Programme principal
a=int(input("Entrer le coefficient a du trinôme : "))
b=int(input("Entrer le coefficient b du trinôme : "))

c=int(input("Entrer le coefficient c du trinôme : "))

x=float(input("Entrer la valeur de x : "))
print("L'image de ",x,"vaut",f(x),".")

print("a = ",a," b = ",b," c = ",c)

