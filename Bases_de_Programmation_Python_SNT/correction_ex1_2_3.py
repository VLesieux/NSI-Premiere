############Exercice 1####################

def prix(n):
    """
    Renvoie le prix à payer pour un achat de n ramettes de papier
    param : n: int
    return : float
    C.U : aucune
    >>> prix(100)
    345.0
    """
    if n<=50:
        return 3.68*n
    else:
        return 3.68*50+3.22*(n-50)
    
#nombre=int(input("nombre de lots de ramettes de papier achetés ? "))
#
#print("Il vous en reviendra "+str(prix(nombre))+"€")

############Exercice 2####################

def abo1(n):
    """
    Affiche s'il est avantageux de prendre le pass
    return : float
    C.U : aucune
    >>> abo1(2)
    'Ne prenez pas le pass, il est désavantageux ; vous payez 17.4€ sans le pass au lieu de 26.0€ avec le pass'
    >>> abo1(8)
    'Prenez le pass, il est avantageux ; vous payez 59.0€ avec le pass au lieu de 69.6€ sans le pass'
    """
    prix_sans_abonnement=n*8.70
    prix_avec_abonnement=15+n*5.50
    difference=prix_avec_abonnement-prix_sans_abonnement
    if difference<0:
        return 'Prenez le pass, il est avantageux ; vous payez '+str(prix_avec_abonnement)+'€ avec le pass'+' au lieu de '+str(prix_sans_abonnement)+'€ sans le pass'
    else:
        return 'Ne prenez pas le pass, il est désavantageux ; vous payez '+str(prix_sans_abonnement)+'€'+' sans le pass au lieu de '+str(prix_avec_abonnement)+'€ avec le pass'
        

#nombre=int(input("combien de séances de cinéma allez-vous prendre ? "))
#print(abo1(nombre))

def abo2(n):
    """
    Renvoie un tuple prix_sans_abonnement,prix_avec_abonnement
    param : n : int
    return : tuple (float,float)
    C.U : aucune
    >>> abo2(2)
    (17.4, 26.0)
    >>> abo2(8)
    (69.6, 59.0)
    """    
    prix_sans_abonnement=n*8.70
    prix_avec_abonnement=15+n*5.50
    return prix_sans_abonnement,prix_avec_abonnement
        

#nombre=int(input("combien de séances de cinéma allez-vous prendre ? "))
#abo2(nombre)

############Exercice 3####################

def avantage():
    """
    Renvoie le nombre de séances à partir duquel le pass devient avantageux
    param: none
    return : int
    C.U : aucune
    >>> avantage()
    5
    """ 
    n=0
    while abo2(n)[0]<abo2(n)[1]:
        n+=1
    return n

print('Prendre le pass devient avantageux à partir de '+str(avantage())+' séances.')
    
    
##############################################################
if __name__ == '__main__':
  import doctest
  doctest.testmod(verbose=True)