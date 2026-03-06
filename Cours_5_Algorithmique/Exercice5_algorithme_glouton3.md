Lors d'un festival de cinéma, plusieurs films sont projetés dans la même salle au cours de la journée.

Chaque film possède :

- une heure de début
- une heure de fin


Un spectateur souhaite voir le plus grand nombre possible de films, mais il ne peut évidemment pas regarder deux films en même temps.


Ainsi deux films sont compatibles si l'un commence après ou exactement à l'heure de fin de l'autre.

Dans une version améliorée, on peut tenir compte d'un temps de pause entre deux projections consécutives qui reste au choix du spectateur.

```Python
debuts=[9,10,11,12,13,15]
fins=[11,12,13,14,15,17]
films=["F1","F2","F3","F4","F5","F6"]



def prochain_film(horaires_debut,horaires_fin,h):
    """
    renvoie l'indice du film qui commence après h
    et qui se termine le plus tôt
    si incompatibilité renvoie "Impossible"
    >>> prochain_film(debuts,fins,11)
    2
    """
	
    
    
def selection_films(debut,fin,horaires_debut,horaires_fin):
    """
    renvoie la liste des films que l'on peut voir
    selon l'algorithme glouton
    >>> selection_films(9,18,debuts,fins)
    ['F1', 'F3', 'F5', 'F6']
    """
	
        

def selection_films_avec_pause(debut,fin,horaires_debut,horaires_fin,duree_pause):
    """
    renvoie la liste des films que l'on peut voir
    selon l'algorithme glouton avec un temps de pause entre deux films consécutifs
    >>> selection_films_avec_pause(9,18,debuts,fins,0.25)
    ['F1', 'F4', 'F6']
    """
	

def nombre_et_duree_totale_films_avec_pause(debut, fin, horaires_debut, horaires_fin,duree_pause):
    """
    renvoie le nombre maximal de films que l'on peut voir tenant compte de la durée de pause,
	ainsi que la durée totale devant un écran de cinéma
    >>> nombre_et_duree_totale_films_avec_pause(9,18,debuts,fins,0.25)
    (3, 6)
    """
	




    
if __name__ == '__main__':
    import doctest
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS, verbose=True)



```