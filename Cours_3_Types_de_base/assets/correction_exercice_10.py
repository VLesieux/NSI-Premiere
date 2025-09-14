#Pour convertir un nombre décimal, écrit en base 10, en nombre hexadécimal, écrit en base 16,
#il faut réaliser une succession de divisions par 16,
#le quotient devenant à chaque fois le nouveau dividende,
#aussi longtemps que le quotient est strictement positif ;
#le code hexadécimal obtenu est formé par les restes de ces divisions, écrit dans l'ordre du dernier au premier,
#en remplaçant les valeurs 10, 11, 12, 13, 14, 15 par les caractères A, B, C, D, E, F.

def conversion_decimal_hexadecimal(n):
    """
    Renvoie la conversion en hexadécimal d'un nombre décimal
    param : n : int
    return : str
    >>> conversion_decimal_hexadecimal(1807)
    '70F'
    """
    resultat=""
    liste=["A","B","C","D","E","F"]
    while n>0:
        reste=n%16
        if reste<10:
            resultat=str(reste)+resultat
        else:
            resultat=str(liste[reste-10])
        n=n//16
    return resultat

#Pour convertir un code hexadécimal en nombre décimal, il faut additionner
#les résultats des produits (valeur du code * puissance de 16),
#en augmentant d'une unité la puissance de droite à gauche,
#en commençant par la puissance 0.


def conversion_hexadecimal_decimal(code):
    """
    convertit un entier n en base b
    param : code: str
    return : int
    exemples:
    >>> conversion_hexadecimal_decimal('70F')
    1807
    """
    resultat=0
    i=0
    liste=["A","B","C","D","E","F"]
    for caractere in code[::-1]:#on renverse la chaîne de caractère pour lire celle-ci dans l'ordre croissant des puissances de 16
        if caractere in liste:
            resultat+=(liste.index(caractere)+10)*16**i
        else:
            resultat+=int(caractere)*16**i
        i+=1
    return resultat

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose = True) 
