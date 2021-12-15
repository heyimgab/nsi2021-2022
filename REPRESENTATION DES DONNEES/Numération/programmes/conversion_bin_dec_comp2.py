# Créé par herve, le 09/11/2021 en Python 3.7
def décodage(binaire):
    ''' renvoie le nombre décimal correspondant au nombre binaire signé founi en argument sous forme de chaine de caractères'''
    assert type(binaire) is str, 'le nombre en binaire doit être donné sous forme de chaîne de caractère'
    for chiffre in binaire:
        assert (chiffre=='0' or chiffre=='1'), 'l argument doit être composé que de 0 ou 1'
    # complété ici



# algorithme de conversion pour binaire non signé
def bin_to_dec(binaire):
    ''' renvoie le nombre décimal valeur du nombre binaire founi en argument sous forme de chaine de caractères'''
    decimal=0
    for bit in binaire:
        decimal=decimal*2+int(bit)
    return decimal

assert decodage('10101010')==-86, 'erreur de decodage avec 10101010'
assert decodage('00101010')==42, 'erreur de decodage avec 00101010'

