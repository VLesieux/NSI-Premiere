f=open("small_performances.csv","r")#la fonction open renvoie une valeur affectée à la variable f ; "r" signifie read lecture ; on peut préciser l'encodage pour éviter les problèmes d'accent
champs=f.readline().rstrip().split(";")
lignes=f.readlines()#on observe l'utilisation du pluriel lines
table_performances=[]
for ligne in lignes:
    liste=ligne.rstrip().split(';')
    table_performances.append(liste)
f.close()

f=open("small_inscrits.csv","r")#la fonction open renvoie une valeur affectée à la variable f ; "r" signifie read lecture ; on peut préciser l'encodage pour éviter les problèmes d'accent
champs=f.readline().rstrip().split(";")
lignes=f.readlines()#on observe l'utilisation du pluriel lines
table_inscrits=[]
for ligne in lignes:
    liste=ligne.rstrip().split(';')
    table_inscrits.append(liste)
numero=1
for element in table_inscrits:
    element.append(numero)
    numero+=1   
f.close()

for element1 in table_inscrits:
    for element2 in table_performances:
        if element1[4]==int(element2[0]):
            element1+=[element2[1],element2[2],element2[3]]
            
for element in table_inscrits:
    if len(element)==5:
        element+=['100','100','100']
# 
#         
def calcul_temps(donnee):
    """
    Renvoie le temps en seconde
    >>> calcul_temps(['Sidney', 'Robert', 'M', '21/7/1970', 1, '1', '8', '55'])
    4135
    """
    return int(donnee[5])*3600+int(donnee[6])*60+int(donnee[7])
# 
table_inscrits=sorted(table_inscrits, key=lambda element: calcul_temps(element))
# 
# 
for element in table_inscrits:
    if element[5] =='100' and element[6] =='100' and element[7] =='100':
        print(f"[{element[4]}]: {element[0]} {element[1]} ({element[2]} {element[3]})=> None")          
    else:
        print(f"[{element[4]}]: {element[0]} {element[1]} ({element[2]} {element[3]})=> {element[5]}h {element[6]}mn {element[7]}s")
   
    
if __name__ == '__main__':
    import doctest
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS, verbose=True)
    