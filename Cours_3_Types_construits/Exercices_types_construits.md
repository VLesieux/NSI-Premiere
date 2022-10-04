# Exercices types construits : tuples, listes et dictionnaires

Pour les différents exercices, lorsqu'une fonction est demandée, produire la documentation de la fonction avec un ou plusieurs tests de votre choix à vérifier.

```Python
if __name__ == '__main__':
  import doctest
  doctest.testmod(verbose=True)
```

## Exercice 1

Écrire une fonction _separe_ qui prend en argument un tuple _t_ composé d'entiers et renvoie deux listes : la première liste _pairs_ contient les nombres pairs et la seconde _impairs_ les nombres impairs.

__Indications__ : 
1) revoir dans le cours sur les tuples le moyen de parcourir les éléments d'un tuple
2) revoir le moyen de tester la parité d'un nombre
3) revoir le moyen d'ajouter un élément à une liste

## Exercice 2

Écrire une fonction _produit_ qui prend en paramètres une liste de nombres appelée _nombres_ et un entier naturel appelé _n_ non nul et qui renvoie une liste obtenue en multipliant chaque élément de la liste _nombres_ par _n_. On proposera différentes écritures du programme.

__Indications__ : 
1) Réaliser une première écriture en passant par la création d'une liste vierge _nouvelle_liste_ que l'on complète au fur et à mesure du parcours de la liste _nombres_
2) Proposer une deuxième méthode beaucoup plus efficace en créant une liste par compréhension qui répond à la demande (revoir les exemples du cours), et la renvoyer directement sans avoir à créer de liste intermédiaire 

## Exercice 3

Voici une fonction mystère :
```Python
def mystere(liste1,liste2):
    liste=[]
    i,j=0,0
    while i<len(liste1) and j<len(liste2):
        if liste1[i]<liste2[j]:
            liste.append(liste1[i])
            i=i+1
        else:
            liste.append(liste2[j])
            j=j+1
    return liste
```
On appelle cette fonction avec l'instruction mystere([2,5,6,8],[1,4,7,8,9]). Quel est le résultat renvoyé ?   
Le trouver avec un crayon avant de tester sur machine.


## Exercice 4

L'instruction tuple(sorted(t)) renvoie le tuple ordonné dans l'ordre croissant. Compléter la fonction maxi qui renvoie le maximum d'une suite de valeurs données dans un tuple.

```Python
def maxi(t):
    return ...
```

## Exercice 5

On construit un dictionnaire ayant pour clés des couples contenant les coordonnées GPS de villes (Latitude et Longitude) et pour valeur les noms des villes correspondantes. On trouve les coordonnées sur Internet par exemple. Les données sont sous forme décimale en degré.      

```Python
positions={}
positions[(48.853585,2.301490)]="Paris"
positions[(11.611358,43.147752)]="Djibouti"
positions[(43.70000,7.250000)]="Nice"
```
On suppose avoir reçu une photo prise sur un smartphone par une personne en vacances. On regarde dans les propriétés les coordonnées GPS au moment de la prise de vue. Écrire une fonction _renvoie_position_ prenant en paramètres un couple de coordonnées GPS et le dictionnaire _positions_ que nous avons construit, et renvoyant le nom du lieu correspondant. On tolère une précision au dix-millième de degré.
Par exemple si les coordonnées sont (11.61135,43.14775), la fonction doit nous renvoyer "Djibouti", mais si les coordonnées sont (11.61135,43.14798), la fonction doit nous renvoyer "Position inconnue".

__Indications__ : 

1) l'idée est de faire un parcours des clés du dictionnaire (revoir la procédure dans le cours), comparer les coordonnées du site avec chacune des clés du dictionnaire en élargissant l'égalité avec un encadrement

2) penser à comparer la valeur absolue (avec abs()) de la différence des coordonnées multipliée par 10000 pour retourner ensuite la valeur associée à la clé (revoir la procédure dans le cours).

```Python
def renvoie_position(position,dictionnaire):
    """
    Renvoie la ville à partir de position avec une précision au dix-millième de degré
    param : position : tuple
    param : dictionnaire : dict
    return : str
    >>> renvoie_position((11.611377,43.147762),positions)
    'Djibouti'
    >>> renvoie_position((11.611368,43.14798),positions)
    'Position inconnue'
    """
```

## Exercice 6

Écrire une fonction _stat_ qui prend en paramètre un texte et renvoie un dictionnaire _statistiques_ dont les clés sont les différentes lettres du texte et les valeurs le nombre d'occurrences de chaque lettre dans le texte. Le texte peut contenir des espaces ou des caractères de ponctuation qui ne devront pas être comptabilisés dans le dictionnaire fourni par la fonction.

__Indications__ : parcourir les lettres du textes, créer s'il n'existe pas encore le nouvel item (lettre:1) dans le dictionnaire statistiques, ou augmenter de 1 sa valeur si l'item existe déjà.

```Python
def stat(texte):
    """
    Renvoie les nombres d'occurence de chaque lettre du texte sous forme de dictionnaire
    param : string
    return : dict
    >>> stat("ceci est un texte")
    {'c': 2, 'e': 4, 'i': 1, 's': 1, 't': 3, 'u': 1, 'n': 1, 'x': 1}
    """
```

## Exercice 7

On suppose que l'on dispose d'un traducteur anglais-français et la question est de mesurer l'intérêt d'une représentation par un dictionnaire {"yes":"oui","no":"non",...} plutôt que par une liste de listes [["yes","oui"],["no","non"],...]. Nous allons donc compter le temps de recherche d'un élément. Pour traduire "yes", on doit trouver dans le dictionnaire la valeur correspondant à la clé "yes" et dans la liste de listes la valeur du deuxième élément d'une sous-liste dont le premier élément a pour valeur "yes". 

1) Écrire une fonction _recherche1_ qui prend en paramètres une liste de listes et une variable k qui pourrait être "yes" et qui renvoie le deuxième élément de la sous-liste dont le premier élément a la valeur de k et qui serait "oui" dans ce cas.

```Python
dictionnaire_a_f={"yes":"oui","no":"non"}
liste_a_f=[["yes","oui"],["no","non"]]

def recherche1(liste_voca,k):
    """
    Renvoie l'élément[1] de liste dont element[0]=k
    param : liste_a_f : list
    param : k : str
    return : str
    >>> recherche1(liste_a_f,"no")
    'non'
    """
```


2) Écrire une fonction _recherche2_ qui prend en paramètres un dictionnaire et une variable k et renvoie la valeur correspondant à la clé k.

```Python
def recherche2(dictionnaire_voca,k):
    """
    Renvoie la clé associée à la valeur k
    param : dictionnaire_voca : dict
    param : k : str
    return : str
    >>> recherche2(dictionnaire_a_f,"no")
    'non'
    """
```

3) Pour la recherche qui doit être effectuée sur un grand ensemble, nous simplifions nos objets. Construire par compréhension une liste de listes dont les éléments sont de la forme [i,i] pour i allant de 0 à 10<sup>6</sup>-1. Mélanger cette liste avec la fonction `shuffle` du module `random`. Créer alors le dictionnaire correspondant à l'aide de la fonction `dict`.

```Python
>>> from random import shuffle
>>> liste=[1,2,3,4]
>>> shuffle(liste)#ne pas écrire liste=shuffle(liste)
>>> liste
[3, 4, 1, 2]
```

```Python
>>> liste=[[5,5],[7,7]]
>>> dictionnaire=dict(liste)
>>> dictionnaire
{5: 5, 7: 7}
```

4) Tester les fonctions de recherche sur la liste et le dictionnaire en utilisant pour le paramètre k une valeur quelconque. Pour les tests, utiliser la fonction `time` du module `time`. 

```Python
from time import time
st=time()
#écrire ici le programme dont on veux mesurer la durée d'exécution
print(time()-st)
```

5) Pour gagner une ligne de code, on peut améliorer la fonction _recherche2_ en utilisant la méthode get associée au dictionnaire qui renvoie la valeur d'une clé et ne retourne pas d'erreur si la clé est introuvable. Créer la fonction _recherche3_ et comparer son efficacité avec les fonctions précédentes.


## Exercice 8

Au scrable, les valeurs des pièces sont les suivantes:  

    1 point : E , A , I , N , O , R , S , T , U , L    
    2 points : D , M , G    
    3 points : B , C , P    
    4 points : F , H , V    
    8 points : J , Q    
    10 points : K , W , X , Y, Z    

On suppose qu'un joueur s'apprête à réaliser un mot sur un emplacement où la sixième lettre compte triple, il a plusieurs mots possibles à son actif.

On cherche à écrire une fonction capable de renvoyer à partir d'un tuple de mots possibles un dictionnaire associant une valeur en points à chacun des mots de ce tuple en plaçant les mots dans l'ordre décroissant des points.   


Indications :

1) Créer un dictionnaire associant une valeur à un tuple de lettres.

2) Créer une première fonction appelée _points_ retournant la valeur en points d'un mot entré en paramètre

```Python
def points(mot):
    """
    Renvoie la valeur d'un mot dont la sixième lettre compte triple
    param : mot : str
    return : int
    >>> points('CASSER')
    10
    >>> points('RESSAC')
    14
    >>> points('ECRASES')
    13
    """
```

3) Utiliser les méthodes `sort()` et `reverse()` des listes dans une nouvelle fonction `classement_mots`; il s'agira en effet de créer une liste contenant les valeurs des mots, puis d'ordonner et de renverser cette liste. On sera ensuite amené à créer un nouveau dictionnaire initialement vide que l'on remplira avec des mots (les clés) qui ont pour valeur les valeurs de cette dernière liste.

Exemple :

```Python
>>> liste=[1,8,9,3]
>>> liste.sort()
>>> liste
[1, 3, 8, 9]
>>> liste.reverse()
>>> liste
[9, 8, 3, 1]
```

```Python
def classement_mots(possibles):
    """
    Renvoie un dictionnaire associant mot et valeur avec les valeurs rangées dans l'ordre décroissant
    param : possibles : tuple
    return : dict
    >>> classement_mots(("CASSER","RESSAC","ECRASES"))
    {'RESSAC': 14, 'ECRASES': 13, 'CASSER': 10}
    """
```

### Exercice 9

Soit un ensemble de points :

A : (-2,4) ; B : (1,-2) ; C : (3,7) ; D : (5,-3)

que l'on présente sous la forme d'un dictionnaire de points

```Python
dictionnaire_points={"A": (-2,4), "B": (1,-2), "C": (3,7), "D": (5,-3)}
```

1. Écrire une fonction `calcul_distance` qui calcule la distance entre deux points.

```Python
def distance_entre_deux_points(point1,point2):
    """
    Renvoie la distance entre point1 et point2
    param : point1 : tuple
    param : point2 : tuple
    return : float
    >>> distance_entre_deux_points((1,1),(4,5))
    5.0
    """
```

2. Écrire une fonction `calcul_distance_totale` qui calcule la longueur totale du chemin : AB + BC + CD et qui peut s'appliquer à n'importe quelle série de points fournie sous la forme d'un dictionnaire.

```Python
def calcul_distance_totale(dictionnaire):
    """
    Renvoie la distance totale pour une série de points fournie dans un dictionnaire
    param : dictionnaire : dict
    return : float
    >>> calcul_distance_totale(dictionnaire_points)
    26.125787416977825
    """
```

### Exercice 10

Un fabricant décide de créer des tee-shirts dont la taille peut être : XS, S, M, L, XL, XXL.

À chaque taille son prix : il adopte le principe suivant : 8 € pour la taille XS et il ajoute 2 € en passant à la taille supérieure, jusqu'au XXL.

1. Proposer une écriture en compréhension permettant d'obtenir un dictionnaire que l'on appelera `marchandises` :

```Python
{'XS': '8 €', 'S': '10 €', 'M': '12 €', 'L': '14 €', 'XL': '16 €', 'XXL': '18 €'}
```

Indication : créer une liste `tailles`

```Python
tailles=['XS', 'S', 'M', 'L', 'XL', 'XXL']
```

2. Ce même fabricant décide de changer sa façon de fixer les prix de vente des tee-shirts. Ceux dont la taille est XS sont toujours à 8 €, mais cette fois-ci, pour passer d'une taille à la suivante, il ajoute au prix de la taille inférieure la moitié de sa racine carrée (prendre la racine carrée d'un nombre, c'est l'élever à la puissance 1/2=0.5).

Par exemple, pour obtenir le prix des tailles S, il fait : 8 + 0.5*8**0.5 = 9.41.

Proposer une écriture en compréhension permettant d'obtenir pour le dictionnaire `marchandises`:

```Python
{'XS': '8 €', 'S': '9.41 €', 'M': '10.94 €', 'L': '12.59 €', 'XL': '14.36 €', 'XXL': '16.25 €'}

```

Remarque : pour arrondir à deux décimales

```Python
>>> round(9.414213562373096,2)
9.41
```

Indication : créer une liste `prix` où chacun des prix pour chaque taille est initialement à 0

```Python
prix=[0]*len(tailles)
```

puis affecter le premier prix de la liste à 8,
puis faire le calcul des prix des autres tailles par compréhension ;
affecter ces prix aux tailles dans le dictionnaire `marchandises`.

3. Un magasin fait une commande à un grossiste en précisant ses quantités de tee-shirts par taille sous la forme :

```Python
quantites={'XS': 200, 'S': 350 , 'M': 125 , 'L': 370 , 'XL': 50 , 'XXL': 50}
```

Calculer le prix de revient de cette commande.

Indication : travailler avec les nombres, retirer les '€'.




