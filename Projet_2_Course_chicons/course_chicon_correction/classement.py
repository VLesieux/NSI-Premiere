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

#print(classement(["c","f","d","a","h"],comparaison_croissant))
#
#print(classement([9,1,4,8,23],comparaison_decroissant))

def classement_nom_famille(dictionnaire):
    liste_nom=[]
    for i in dictionnaire:
        liste_nom.append(dictionnaire[i]['last_name'])
    liste_nom=tri_perso.classement(liste_nom,tri_perso.comparaison_croissant)
    new={}
    for j in liste_nom:
        for i in dictionnaire:
            if dictionnaire[i]['last_name']==j:
                new[i]=dictionnaire[i]
    return new