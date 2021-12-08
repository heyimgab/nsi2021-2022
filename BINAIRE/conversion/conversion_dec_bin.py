########################## DECIMAL 2 BINARY ##################################
def dec_to_bin(decimal):
    
    # Renvoie le nombre binaire en chaine de ccaractère du décimal fourni en argument
    assert type(decimal) is int, 'Le nombre doit être un entier '

    binaire = ''
    while decimal != 0:
        reste = decimal % 2
        decimal = decimal // 2
        binaire = str(reste) + binaire
    return binaire

print("conversion 1: ",dec_to_bin(345))