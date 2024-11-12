# Exercices types construits : tuples, listes et dictionnaires

Pour les différents exercices, lorsqu'une fonction est demandée, produire la documentation de la fonction avec un ou plusieurs tests de votre choix à vérifier.

```Python
if __name__ == '__main__':
  import doctest
  doctest.testmod(verbose=True)
```

## Exercice 1

Écrire une fonction _separe_ qui prend en argument un tuple _t_ composé d'entiers et renvoie deux listes : la première liste _pairs_ contient les nombres pairs et la seconde _impairs_ les nombres impairs.

```Python
def separe(t):
    """
    Renvoie une liste de nbre pairs et une liste de nbre impaires
    param : t : tuple
    return : tuple
    >>> separe((5,8,2,9,6))
    ([8, 2, 6], [5, 9])
    """
```

__Indications__ : 
1) revoir dans le cours sur les tuples les deux moyens de parcourir les éléments d'un tuple
2) revoir le moyen de tester la parité d'un nombre
3) revoir le moyen d'ajouter un élément à une liste

## Exercice 2

Écrire une fonction _produit_ qui prend en paramètres une liste de nombres appelée _nombres_ et un entier naturel appelé _n_ non nul et qui renvoie une liste obtenue en multipliant chaque valeur de la liste _nombres_ par _n_. On proposera différentes écritures du programme.

```Python
def produit(nombres,n):
    """
    Renvoie la liste obtenue en multipliant par n toutes les valeurs de nombres
    param : nombres : list
    param : n: int
    return : list
    >>> produit([3,7,4],2)
    [6, 14, 8]
    """
```
    
__Indications__ : 
1) Réaliser une première écriture en passant par la création d'une liste vierge _nouvelle_liste_ que l'on complète au fur et à mesure du parcours de la liste _nombres_.
2) Proposer une deuxième méthode, beaucoup plus efficace, en créant une liste par compréhension qui répond à la demande (voir les exemples du cours), et la renvoyer directement sans avoir à créer de liste intermédiaire 

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
Le trouver d'abord avec un crayon avant de le tester sur la machine.   
Vérifier également l'évolution des variables liste1,liste2,liste avec le debugger.


## Exercice 4

L'instruction `tuple(sorted(t))` renvoie le tuple ordonné dans l'ordre croissant.   
Écrire une fonction `maxi` qui renvoie, en une seule ligne, le maximum d'une suite de valeurs données dans un tuple en utilisant cette instruction.

```Python
def maxi(valeurs):
    """
    Renvoie le maximum d'une liste valeurs
    param : valeurs : tuple
    return : int
    >>> maxi((7,18,9,2))
    18
```

## Exercice 5

On construit un dictionnaire ayant pour clés des couples contenant les coordonnées GPS de villes (Latitude et Longitude) et pour valeur les noms des villes correspondantes. On trouve les coordonnées sur Internet par exemple. Les données sont fournies sous forme décimale en degré.      

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

Écrire une fonction _stat_ qui prend en paramètre un texte et renvoie un dictionnaire _statistiques_ dont les clés sont les différentes lettres du texte et les valeurs le nombre d'occurrences de chaque lettre dans le texte (nombre de fois où la lettre apparaît dans le texte). Le texte peut contenir des espaces ou des caractères de ponctuation qui ne devront pas être comptabilisés dans le dictionnaire fourni par la fonction.

__Indications__ : parcourir les lettres du textes, créer, s'il n'existe pas encore, le nouvel item (lettre:1) dans le dictionnaire _statistiques_, ou augmenter de 1 sa valeur si l'item existe déjà.

Utiliser la méthode `get` des dictionnaires pour ne pas bloquer le programme en cas d'absence d'une clé.

```Python
>>> frequences={"do4":523.25,"la3":440}
>>> frequences["mi5"]
Traceback (most recent call last):
  File "<pyshell>", line 1, in <module>
KeyError: 'mi5'
>>> frequences.get('mi5')
>>> #pas de message d'erreur
```

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


2) Écrire une fonction _recherche2_ qui prend en paramètres un dictionnaire et une variable k et renvoie la valeur correspondant à la clé k si elle est présente dans le dictionnaire et ne fait rien sinon (sans le message KeyError).

```Python
def recherche2(dictionnaire_voca,k):
    """
    Renvoie la clé associée à la valeur k
    param : dictionnaire_voca : dict
    param : k : str
    return : str
    >>> recherche2(dictionnaire_a_f,"no")
    'non'
    >>> recherche2(dictionnaire_a_f,"inconnu")
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

## Exercice 8

Au scrable français, les valeurs des pièces sont les suivantes:  

    1 point : E , A , I , N , O , R , S , T , U , L    
    2 points : D , M , G    
    3 points : B , C , P    
    4 points : F , H , V    
    8 points : J , Q    
    10 points : K , W , X , Y, Z    

On suppose qu'un joueur s'apprête à réaliser un mot sur un emplacement où la sixième lettre compte triple, il a plusieurs mots possibles à son actif avec les mêmes lettres et cherche à connaître le meilleur choix.

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
    11
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
    Renvoie un dictionnaire avec les valeurs des possibles dans l'ordre décroissant
    param : possibles : tuple
    return : int
    >>> classement_mots(("CASSER","RESSAC","ECRASES"))
    {'RESSAC': 14, 'ECRASES': 11, 'CASSER': 10}
    """
```

### Exercice 9

Soit un ensemble de points :

A : (-2,4) ; B : (1,-2) ; C : (3,7) ; D : (5,-3)

que l'on présente sous la forme d'un dictionnaire de points associant le nom d'un point (clé) au tuple (valeur) correspondant à ses coordonnées dans un repère orthonormé.

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


Remarque : une première méthode consistera à créer une nouvelle liste appelée `coordonnees` en y ajoutant avec `append` les coordonnées des points en parcourant les items du dictionnaire, une deuxième méthode consistera à utiliser `list(dictionnaire.values())` puis à itérer sur celle-ci.


3. En déduire une fonction `calcul_distance_polygone` qui calcule la longueur totale du chemin : AB + BC + CD + DA, ou périmètre du polygone, et qui peut s'appliquer à n'importe quelle série de points fournie sous la forme d'un dictionnaire.


```Python
def calcul_distance_polygone(dictionnaire):
    """
    Renvoie la longueur du polygone formée par une série de points donnée par dictionnaire
    param : dictionnaire : dict
    return : float
    >>> calcul_distance_polygone({"A":(3,0),"B":(3,3),"C":(0,3),"D":(0,0)})
    12.0
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


### Exercice 11

Un carré de côté n est dit magique si les sommes des nombres de chaque rangée, les sommes des nombres de chaque colonne et les sommes de chaque diagonale principale (première et deuxième diagonale) sont égales à une valeur commune.

Par exemple, vérifier avec un crayon que le carré [[2,7,6],[9,5,1],[4,3,8]] est bien magique.

Dans un premier temps, compléter la fonction <i>valeur_commune</i> ci-dessous ; on réalisera le parcours des éléments de la liste en les comparant à la première valeur de celle-ci.

```Python
############################### À faire 1. ##################################
def valeur_commune(liste):
    """
    Renvoie la valeur commune de la liste sinon renvoie False
    param : liste : list
    return : int ou bool
    >>> valeur_commune([4,4,4,4])
    4
    >>> valeur_commune([4,4,3,4])
    False    
    """
	pass
```

Proposer une seconde version de la fonction utilisant la fonction all().

Rappel :

```Python
>>> all([True,True,True])
True
>>> all([True,False,True])
False
```


```Python
############################### À faire 2. ##################################
def valeur_commune_version2(liste):
    """
    Renvoie la valeur commune de la liste sinon renvoie False
    param : liste : list
    return : int ou bool
    >>> valeur_commune_version2([4,4,4,4])
    4
    >>> valeur_commune_version2([4,4,3,4])
    False    
    """
	pass
```

Compléter maintenant les 4 fonctions suivantes ; on utilisera la fonction sum() qui s'appliquera sur 4 listes écrites par compréhension.


Rappel : 

```Python
>>> sum([3,2,4])
9
```

```Python
############################### À faire 3. ##################################
def somme_rangees(carre):
    """
    Renvoie la somme des valeurs des différentes rangées
    param : carre
    return : int
    >>> somme_rangees([[2,5,3],[3,2,1],[2,2,1]])
    [10, 6, 5]
    """
	pass


############################### À faire 4. ##################################
def somme_colonnes(carre):
    """
    Renvoie la somme des valeurs des différentes colonnes
    param : carre
    return : int
    >>> somme_colonnes([[2,5,3],[3,2,1],[2,2,1]])
    [7, 9, 5]
    """
	pass

############################### À faire 5. ##################################

def somme_premiere_diagonale(carre):
    """
    Renvoie la somme des valeurs de la première diagonale
    param : carre
    return : int
    >>> somme_premiere_diagonale([[2,5,3],[3,2,1],[2,2,1]])
    5
    """
	pass

############################### À faire 6. ##################################

def somme_deuxieme_diagonale(carre):
    """
    Renvoie la somme des valeurs de la deuxième diagonale
    param : carre
    return : int
    >>> somme_deuxieme_diagonale([[2,5,3],[3,2,1],[2,2,1]])
    7
    """
	pass
```

Utiliser ces quatre fonctions ainsi que la fonction <i>valeur_commune</i> pour compléter la fonction <i>est_magique</i>

```Python
############################### À faire 7. ##################################
def est_magique(carre):
    """
    Renvoie la valeur commune des sommes selon rangées,colonnes, et les deux diagonales si le carre est magique, False sinon
    param : carre : list
    return : bool
    >>> est_magique([[2,7,6],[9,5,1],[4,3,8]])
    15
    >>> est_magique([[4,5,11,14],[15,10,8,1],[6,3,13,12],[9,16,2,7]])
    34
    >>> est_magique([[4,2,11,14],[15,10,8,1],[6,3,13,12],[9,16,2,7]])
    False
    """
```
############################### À faire 8 (bonus) ##################################

Écrire un programme qui vous donnera une liste formée de 5 carrés magiques différents (formés de nombres compris entre 1 et 3).
On pourra obtenir ceci :

[[[2, 3, 1], [1, 2, 3], [3, 1, 2]], [[2, 1, 3], [3, 2, 1], [1, 3, 2]], [[1, 1, 1], [1, 1, 1], [1, 1, 1]], [[1, 3, 2], [3, 2, 1], [2, 1, 3]], [[3, 1, 2], [1, 2, 3], [2, 3, 1]]]

