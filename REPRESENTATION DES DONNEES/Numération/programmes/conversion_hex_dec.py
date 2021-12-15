# Créé par herve, le 07/11/2021 en Python 3.7
# Conversion d'un nombre hexadécimal en décimal sur python

def hex_to_dec(hexa):
    '''renvoie le nombre décimal correspondant au nombre hexadécimal fourni en argument sous forme de chaîne de caractères'''
    assert type(hexa) is str, 'le nombre en binaire doit être donné sous forme de chaîne de caractère'
    valeursHexa=['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
    for chiffre in hexa:
        assert (chiffre in valeursHexa), 'l argument doit être composé de chiffres hexadécimaux'

    decimal=0
    nbChiffres=len(hexa)
    #A commpléter

print("valeur décimal de BAC : ", hex_to_dec('BAC'))

