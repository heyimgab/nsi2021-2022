# Exercice 3, tables de multiplications du 2 et 'user-defined'
# Table de multiplication de 2

for i in range( 0, 20 ):
    print( i, " * 2 =", 2 * i )

# Table de multiplication user-defined

nb = int(input("Entrez un entier: "))
for j in range(0,10):
    print(j,"*",nb,"=",nb*j)
