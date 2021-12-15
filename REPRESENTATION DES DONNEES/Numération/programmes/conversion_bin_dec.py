# Créé par herve, le 07/11/2021 en Python 3.7
#**********************************************************
# Conversion d'un nombre binaire en décimal sur python
#**********************************************************
#*******************Version 1 *****************************
# Code à compléter
def bin_to_dec(binaire):
    ''' renvoie le nombre décimal valeur du nombre binaire founi en argument sous forme de chaine de caractères'''
    assert type(binaire) is str, 'le nombre en binaire doit être donné sous forme de chaîne de caractère'
    for chiffre in binaire:
        assert (chiffre=='0' or chiffre=='1'), 'l argument doit être composé que de 0 ou 1'

    decimal=0
    nbChiffres=len(binaire)
    for i in range(nbChiffres):
        if binaire[nbChiffres-i-1]=="1":
            decimal =decimal+2**i                      # compléter ici le code
                                         # écrire une condition qui additionne 2 puissance i à decimal
                                         # si le chiffre dans binaire vaut 1 (attention au sens de lecture de binaire)
    return decimal

#************************************************************
#******************** Version 2 *****************************
def bin_to_dec2(binaire):
    ''' renvoie le nombre décimal valeur du nombre binaire founi en argument sous forme de chaine de caractères'''
    decimal=0
    for bit in binaire:
        decimal=decimal*2+int(bit)
    return decimal



#*************************************************************
#************************* TEST ******************************
print("1ère version :",bin_to_dec('11111111'))
print("2ième version :",bin_to_dec2('1111'))


#************************************************************
#****************** Version native python *******************

print("fonction native int(nbre,base) :",int('1111',2))


