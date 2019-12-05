```python

import src.Competitor as Competitor
import Time

def read_competitors(text):
    """
    lit un fichier csv et retourne un dictionnaire dont les clés sont les numéros de brassard
    et les valeurs les tuples contenant les informations sur les compétiteurs
    """
    try: 
        f=open(text,"r")
        champs=f.readline().rstrip().split(";")
        lignes=f.readlines()
        dictionnaire={}
        brassard=0
        for ligne in lignes:
            brassard+=1
            liste=ligne.rstrip().split(';')
            dictionnaire[brassard]=Competitor.create(liste[0],liste[1],liste[2],liste[3],brassard)
        f.close()
        return(dictionnaire)
    except FileNotFoundError:
        print("Votre fichier n'est pas un csv lisible")
        
#print(read_competitors("mat_course_chicon/data/small_inscrits.csv"))

def affichage(competiteurs):
    texte=""
    for i in competiteurs:
        print(Competitor.to_string(competiteurs[i]))
    return texte

#print(affichage(read_competitors("data/small_inscrits.csv")))

```
