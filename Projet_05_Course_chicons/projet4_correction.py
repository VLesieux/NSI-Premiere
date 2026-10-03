f=open("small_inscrits.csv","r")#la fonction open renvoie une valeur affectée à la variable f ; "r" signifie read lecture ; on peut préciser l'encodage pour éviter les problèmes d'accent
table1=[ligne.rstrip().split(';') for ligne in f]#construction d'une liste par compréhension ; l'écriture condensée ligne.rstrip().split(';') permet de faire agir les deux méthodes successivement d'abord rstrip() puis split(';')
f.close()
# print(table1)


del table1[0]
numero=1
for ligne in table1:
    ligne+=[str(numero)]
    numero+=1
descripteurs_table1=['Prenoms', 'Noms', 'Sexes', 'Date naiss.', 'bib_num']

f=open("small_performances.csv","r")#la fonction open renvoie une valeur affectée à la variable f ; "r" signifie read lecture ; on peut préciser l'encodage pour éviter les problèmes d'accent
table2=[ligne.rstrip().split(';') for ligne in f]#construction d'une liste par compréhension ; l'écriture condensée ligne.rstrip().split(';') permet de faire agir les deux méthodes successivement d'abord rstrip() puis split(';')
f.close()
# print(table1)
descripteurs_table2=['bib_num', 'hours', 'minutes', 'seconds']

for ligne1 in table1:
    for ligne2 in table2:
        if ligne1[4]==ligne2[0]:
            ligne1+=[ligne2[1], ligne2[2], ligne2[3]]
for ligne in table1:
    if len(ligne)==5:
        ligne+=['100', '100', '100']
        
def calcule_temps(heures, minutes, secondes):
    return int(heures)*3600+ int(minutes)*60+ int(secondes)
resultat=sorted(table1,key=lambda element:calcule_temps(element[5],element[6],element[7]))

for ligne in resultat:
    if ligne[5]!='100':
        print(f"[{ligne[4]}]: {ligne[0]}, {ligne[1]} ({ligne[2]}) {ligne[3]}=> {ligne[5]}h {ligne[6]}mn {ligne[7]}s")
    else:
        print(f"[{ligne[4]}]: {ligne[0]}, {ligne[1]} ({ligne[2]}) {ligne[3]}=> none")

        
    
    
