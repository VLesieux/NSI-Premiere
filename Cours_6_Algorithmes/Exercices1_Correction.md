

```python
debut_horaire=[8,12,9,14,11]
fin_horaire=[13,17,11,16,12]

def minimal(liste):#recherche du minimum d'une liste 
    minimum=liste[0]
    for i in range(len(liste)):
        if liste[i]<minimum:
            minimum=liste[i]
    return minimum



def prochaine(h):#recherche du créneau horaire postérieur à h de plus courte durée
    possibles=[]
    duree=[]
    for i in sorted(debut_horaire):
        if i>h:
            possibles.append((i,fin_horaire[debut_horaire.index(i)]))
            duree.append(fin_horaire[debut_horaire.index(i)]-i)
    if duree:
        return possibles[duree.index(minimal(duree))]
    else:
        return None
    
    
            
def selection(debut,fin):#donne la liste des créneaux horaires de plus courte durée qui se succèdent
    liste=[]
    while debut<=fin:
        if prochaine(debut):
            liste.append(prochaine(debut))
            debut=prochaine(debut)[1]
        else:
            return liste
```

