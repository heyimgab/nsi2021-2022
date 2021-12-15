# Créé par herve, le 09/11/2021 en Python 3.7

# Conversion d'un nombre décimal en binaire en complement à 2
def dec_to_bin(decimal):
    ''' renvoie le nombre binaire correspondant à décimal, sous forme de chaine de caractères'''
    assert (type(decimal) is int), 'l argument de la fonction doit être un nombre entier'
    binaire=''
    while (decimal)!=0:
        reste=str(decimal%2)
        binaire=reste+binaire
        decimal=decimal//2
    return (binaire)

def complementA2(decimal,nBits):
    '''renvoie le complement à 2 codé sur nBits(sous forme de chaine de caractères) de l'entier relatif decimal '''



assert (complementA2(-61,8)=='11000011'),'erreur d encodage avec -61'
assert (complementA2(23,8)=='00010111'),'erreur d encodage avec 23'
