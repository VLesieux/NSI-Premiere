def minimum_selection(indice, liste,comparaison):
    minimum=liste[indice]
    for i in range(indice,len(liste)):
        if comparaison(liste[i],minimum):
            minimum=liste[i]
    return liste.index(minimum)



def classement(liste,comparaison):
    for i in range(len(liste)):
        j=minimum_selection(i,liste,comparaison)
        liste[i],liste[j]=liste[j],liste[i]        
    return liste

def comparaison_croissant(a,b):
    if a<b:
        return True
    else:
        return False
    
def comparaison_decroissant(a,b):
    if a>b:
        return True
    else:
        return False

print(classement(["c","f","d","a","h"],comparaison_croissant))

print(classement([9,1,4,8,23],comparaison_decroissant))    