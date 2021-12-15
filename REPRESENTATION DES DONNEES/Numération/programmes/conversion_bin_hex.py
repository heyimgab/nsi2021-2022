# Créé par herve, le 07/11/2021 en Python 3.7
# Fonction de conversion d'un nombre codé en binaire vers sa codée en hexadécimal
from math import ceil
def bin_to_hex(binaire):
    ''' renvoie le nombre hexadecimal correspondant à l'argument binaire, (arguement et sortie sous forme de chaine de caractères)'''
    assert type(binaire) is str, 'le nombre binaire doit être donnée sous forme de chaîne de caractère'
    for chiffre in binaire:
        assert (chiffre=='0' or chiffre=='1'), 'l argument doit être composé que de 0 ou 1'

    hexa=''
    # calcul du nombre de paquets de 4 bits dans binaire
    nbPaquets=ceil(len(binaire)/4) # ceil -> arrondi supérieur
    # on compléte le nombre binaire pour avoir des paquets de 4 complétés
    nbZeros=4*nbPaquets-len(binaire)
    binaire='0'*nbZeros+binaire

    chiffresHexa={0:'0',1:'1',2:'2',3:'3',4:'4',5:'5',6:'6',7:'7',8:'8',9:'9',10:'A',11:'B',12:'C',13:'D',14:'E',15:'F'}
    for i in range (nbPaquets):
        hexa+=chiffresHexa[int(binaire[4*i:4*(i+1)],2)]
    return (hexa)

print("conversion de binaire vers hexadécimal de 10110110 : ",bin_to_hex('10110110'))
