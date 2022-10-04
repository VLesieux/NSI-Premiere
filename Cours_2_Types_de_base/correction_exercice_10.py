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
    for caractere in code[::-1]:
        if caractere in liste:
            resultat+=(liste.index(caractere)+10)*16**i
        else:
            resultat+=int(caractere)*16**i
        i+=1
    return resultat

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose = True) 
