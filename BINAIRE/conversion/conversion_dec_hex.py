# Créé par herve, le 07/11/2021 en Python 3.7
# Fonction de conversion décimal vers hexadécimal par divisions successives
def dec_to_hex(decimal):
    ''' renvoie le nombre binaire correspondant à décimal, sous forme de chaine de caractères'''
    assert (type(decimal) is int), 'l argument de la fonction doit être un nombre entier'

    chiffresHexa=['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
    hexa=''
    while decimal>0:
        # à Compléter
    return hexa

print('conversion en hexadécimal de 9350 :',dec_to_hex(9355))
print('avec la fonction native hex :',hex(9355))
