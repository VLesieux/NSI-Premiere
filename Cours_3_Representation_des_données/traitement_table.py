#f=open("Tableau_capitales.csv","r")
#table=[ligne.rstrip().split(';') for ligne in f]
##str.rstrip() supprime les espaces
##str.split(';') renvoie une liste en utilisant ; comme séparateur
#f.close()
#print(table)
#
#
#f=open("Tableau_capitales.csv","r")
#table=[tuple(ligne.rstrip().split(';')) for ligne in f]
##str.rstrip() supprime les espaces
##str.split(';') renvoie une liste en utilisant ; comme séparateur
#f.close()
#print(table)


f=open("Tableau_capitales.csv","r")
champs=f.readline().rstrip().split(";")#lecture de la première ligne
lignes=f.readlines()
table=[]
for ligne in lignes:
    liste=ligne.rstrip().split(';')
    liste[2]=float(liste[2])
    liste[3]=int(liste[3])
    table.append(tuple(liste))
f.close()
#print(table)

def sans_doublons(table,indice):
    rep=[table[0]]
    for ligne in table:
        if ligne[indice] != rep[-1][indice]:
            rep.append(ligne)
    return rep

def ajout(table1,table2,indice):
    rep=table1+table2
    return sans_doublons(rep,indice)


from copy import deepcopy
def fusion(table1,i1,table2,i2):
    rep=deepcopy(table1)#on fait une copie profonde de table1
    for ligne1 in rep:
        for ligne2 in table2:
            if ligne1[i1]==ligne2[i2]:
                for i in range(len(ligne2)):#parcours des champs de table2
                    if i !=i2:
                        ligne1.append(ligne2[i])
    return rep

#champs=deepcopy(champs1)
#for i in range(len(champs2)):
#    if i!=i2:#i2 est l'indice du champ 'Nom' dans champs2
#        champs.append(champs2[i])
        
#indices=[champs.index('Nom'),champs.index('Continent'),champs.index('Population')]         
##[0, 1, 3]
#rep=[]
#for ligne in table:
#    if ligne[indices[2]]>5000000 and ligne[indices[1]]=="Europe":
#        rep.append(ligne[indices[0]])
#print(rep)



def sans_doublons(table,indice):
    rep=[table[0]]
    for i in range(1,len(table)):
        test=True
        ligne=table[i]
        valeur=ligne[indice]
        for j in range(len(rep)):
            if rep[j][indice]==valeur:
                test=False
                break
        if test:
            rep.append(ligne)
    return rep

indices=[champs.index('Nom'),champs.index('Population')]         

tri=sorted(table,key=lambda ligne:ligne[indices[1]], reverse=True)
print(tri)


dictionnaire={"DK":1300}
dictionnaire[(2,6)]=23


m=[3*[0] for i in range(3)]
for i in range(3):
    m[i][i]=i+1
    m[0][i]=m[0][i]+i+1
    m[i][2]=m[i][2]+i+1
#    print(m)
    
d={"if":"si","yes":"oui","no":"non"} 
for c in d:
    print(d[c])
