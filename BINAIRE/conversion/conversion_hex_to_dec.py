######################## HEX 2 DEC #################################

def hex_to_dec(hexa):
    # Renvoie le nombre décimal correspondant au nombre hexadécimal sous forme de chaîne de caractères
    assert type(hexa) is str, 'Le nombre en binaire doit être donné sous forme de chaïne de caractères'
    valeursHexa={'0': 0, '1': 1, '2': 1, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15, 'G': 16}

    