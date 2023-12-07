fichier=open("small_inscrits.csv","r",encoding='UTF8')
champs1=fichier.readline().rstrip().split(";")
lignes=fichier.readlines()
table_inscrits=[]
numero=0
for ligne in lignes:
    numero+=1
    liste=ligne.rstrip().split(';')
    table_inscrits.append(tuple([str(numero)]+liste))
fichier.close()
champs1=['bib_num']+champs1
print(champs1)
print(table_inscrits)


fichier=open("small_performances.csv","r",encoding='UTF8')
champs2=fichier.readline().rstrip().split(";")
lignes=fichier.readlines()
table_performances=[]
for ligne in lignes:
    liste=ligne.rstrip().split(';')
    table_performances.append(tuple(liste))
fichier.close()
print(champs2)


participants_course=[]

for element in table_performances:
    participants_course.append(element[0])
    
for i in range(len(table_inscrits)):
    if str(i+1) not in participants_course:
        table_performances.append((str(i+1),'1000','1000','1000'))
print(table_performances)
    

def temps(heure,minute,seconde):
    """
    Convertit en seconde
    param : heure : str
    param : minute : str
    param : seconde : str
    >>> temps('1', '21', '23')
    4883
    """
    resultat=int(heure)*3600+int(minute)*60+int(seconde)
    return resultat

def affichage_temps(valeur):
    """
    Convertit un temps en seconde en h, min, s
    param : valeur : int
    >>> affichage_temps(4883)
    '1h 21mn 23s'
    """
    heures=valeur//3600
    minutes=(valeur%3600)//60
    secondes=(valeur%3600)%60
    return str(heures)+"h "+str(minutes)+"mn "+str(secondes)+"s"

table_performances_secondes=[(donnee[0],temps(donnee[1],donnee[2],donnee[3])) for donnee in table_performances]
print(table_performances_secondes)


tableau_fusion=[]

for element1 in table_inscrits:
    for element2 in table_performances_secondes:
        if element1[0]==element2[0]:
            tableau_fusion.append((element1[0],element1[1],element1[2],element1[3],element1[4],element2[1]))

tableau_fusion=sorted(tableau_fusion, key=lambda element:element[5])
print(tableau_fusion)

for element in tableau_fusion:
    
    if element[5]==3661000:
        print(f"[{element[0]}]: {element[1]} {element[2]} ({element[3]} -{element[4]})=> None")         
    else:
        print(f"[{element[0]}]: {element[1]} {element[2]} ({element[3]} -{element[4]})=> {affichage_temps(element[5])}") 


if __name__ == '__main__':
    import doctest
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS, verbose=False)