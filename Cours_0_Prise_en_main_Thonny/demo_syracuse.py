def syracuse(valeur):
    resultat=0
    if valeur%2==0:
        resultat=valeur//2
    else:
        resultat=3*valeur+1
    return resultat

def terme_syracuse(premier_terme,nb_termes):
    terme=premier_terme
    for i in range(nb_termes):
        terme=syracuse(terme)
    return terme

def atterrissage_syracuse(premier_terme):
    nb_termes=0
    terme=premier_terme
    while terme !=1:
        terme=syracuse(terme)
        nb_termes +=1
    return nb_termes
