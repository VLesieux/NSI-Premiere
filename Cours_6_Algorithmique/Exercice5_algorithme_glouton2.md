

On donne le code pour vérifier les docstrings des fonctions à écrire.

```Python
if __name__ == '__main__':
    import doctest
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS, verbose=True)
```

On suppose que l'on a une liste d'activités  chacune associée à un créneau horaire défini par une heure de début et une heure de fin.

Deux activités sont compatibles si leurs créneaux horaires ne se recouvrent pas.

On souhaite sélectionner un nombre maximal d'activités toutes compatibles entre elles.

1. On se donne des activités 'A','B','C','D','E' avec les créneaux suivant : 8h-13h, 12h-17h, 9h-11h, 14h-16h, 11h-12h. Quel est le nombre maximal d'activités que l'on peut concilier sur une journée ?

<img width=500px height=300px src="assets/schema.png">

2. On se propose d'appliquer une stratégie gloutonne pour sélectionner des activités en commençant par le début de journée ; pour cela on choisit l'activité **dont l'heure de fin arrive le plus tôt** (parmi les activités dont l'heure de début est bien postérieure aux créneaux des activités déjà choisies). Appliquer cette stratégie pour donner la liste des activités choisies pour une journée débutant à 8h et finissant à 18h.


3. On suppose avoir n activités numérotées de 0 à n-1 et deux tableaux `debuts` et `fins` de taille n tels que `debut[i]` et `fin[i]` correspondent respectivement à l'heure du début et à l'heure de fin de l'activité numéro i.  

a. Écrire une fonction `prochaine(horaires_debut,horaires_fin,h)` qui sélectionne parmi les activités dont l'heure de début n'est pas antérieures à `h` une activité s'arrêtant le plus tôt. On demandera également à la fonction de renvoyer 'Impossible' s'il n'y a aucun créneau compatible. 

```Python
debuts=[8,12,9,14,11]
fins=[13,17,11,16,12]
activites=['A','B','C','D','E']

def prochaine(horaires_debut,horaires_fin,h):
    """
    Renvoie l'indice de la séance qui commence après h et qui se termine le plus tôt dans la journée
    param : horaires_debut : list
    param : horaires_fin : list
    return : int
    >>> prochaine(debuts,fins,12)
    3
    >>> prochaine(debuts,fins,17)
    'Impossible'
    """
```
      
b. En déduire une fonction `selection(debut,fin,horaires_debut,horaires_fin)` qui sélectionne autant d'activités que possible en suivant la stratégie gloutonne. La fonction affiche la liste des activités sélectionnées.

```Python
def selection(debut,fin,horaires_debut,horaires_fin):
    """
    Renvoie la liste des noms des activités selon l'algorithme glouton
    param : debut : int
    param : fin : int
    return : list
    >>> selection(8,18,debuts,fins)
    ['C', 'E', 'D']
    >>> selection(11,16,debuts,fins)
    ['E', 'D']
    """
```