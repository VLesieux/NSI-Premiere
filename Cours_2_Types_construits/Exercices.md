# Exercices types construits : tuples, listes et dictionnaires: [solutions](https://drive.google.com/file/d/1nN06LUbrYFkH-8MNdgX5bdKNj6zC8faw/view?usp=sharing)

## Exercice 1

Écrire une fonction _separe_ qui prend en argument un n-uplet _t_ composé d'entiers et renvoie deux listes : la première liste _pairs_ contient les nombres pairs et la seconde _impairs_ les nombres impairs.

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

## Exercice 6

Écrire une fonction _stat_ qui prend en paramètre un texte et renvoie un dictionnaire _statistiques_ dont les clés sont les différentes lettres du texte et les valeurs le nombre d'occurences de chaque lettre dans le texte. Le texte peut contenir des espaces ou des caractères de ponctuation qui ne devront pas être comptabilisés dans le dictionnaire fourni par la fonction.

__Indications__ : parcourir les lettres du textes, créer s'il n'existe pas encore le nouvel item (lettre:1) dans le dictionnaire statistiques, ou augmenter de 1 sa valeur si l'item existe déjà.

## Exercice 7

On suppose que l'on dispose d'un traducteur anglais-français et la question est de mesurer l'intérêt d'une représentation par un dictionnaire {"yes":"oui","no":"non",...} plutôt que par une liste de listes [["yes","oui"],["no","non"],...]. Nous allons donc compter le temps de recherche d'un élément. Pour traduire "yes", on doit trouver dans le dictionnaire la valeur correspondant à la clé "yes" et dans la liste de listes la valeur du deuxième élément d'une sous-liste dont le premier élément a pour valeur "yes".
1. Écrire une fonction _recherche1_ qui prend en paramètres une liste de listes et une variable k qui pourrait être "yes" et qui renvoie le deuxième élément de la sous-liste dont le premier élément a la valeur de k et qui serait "oui" dans ce cas.
2. Écrire une fonction _recherche2_ qui prend en paramètres un dictionnaire et une variable k et renvoie la valeur correspondant à la clé k.
3. Pour la recherche qui doit être effectuée sur un grand ensemble, nous simplifions nos objets. Construire par compréhension une liste de listes dont les éléments sont de la forme [i,i] pour i allant de 0 à 10<sup>6</sup>-1. Mélanger cette liste avec la fonction `shuffle` du module `random`. Créer alors le dictionnaire correspondant à l'aide de la fonction `dict`.

```Python
>>> from random import shuffle
>>> liste=[1,2,3,4]
>>> shuffle(liste)
>>> liste
[3, 4, 1, 2]
```

4. Tester les fonctions de recherche sur la liste et le dictionnaire en utilisant pour le paramètre k les valeurs de 0 à 49. Pour les tests, utiliser la fonction `time` du module `time`. 

```Python
from time import time
st=time()
#écrire ici le programme dont on veux mesurer la durée d'exécution
print(time()-st)
```

5. Pour gagner une ligne de code, on peut améliorer la fonction _recherche2_ en utilisant la méthode get associée au dictionnaire qui renvoie la valeur d'une clé et ne retourne pas d'erreur si la clé est introuvable. Créer la fonction _recherche3_ et comparer son efficacité avec les fonctions précédentes.


## Exercice 8

Au scrable, les valeurs des pièces sont les suivantes:  
    1 point : E , A , I , N , O , R , S , T , U , L    
    2 points : D , M , G    
    3 points : B , C , P    
    4 points : F , H , V    
    8 points : J , Q    
    10 points : K , W , X , Y, Z    
Un joueur s'apprête à placer un mot sur un emplacement où la sixième lettre compte triple, il a plusieurs mots possibles.
Écrire une fonction capable de renvoyer à partir d'un tuple de mots un dictionnaire associant une valeur en points à chacun des mots en rangeant ces mots dans l'ordre décroissant des points.   

Par exemple:
```Python
>>> classement_mots(("CASSER","RESSAC","ECRASES"))
{'RESSAC': 14, 'ECRASES': 11, 'CASSER': 10}
```

Écrire les doc_test des fonctions réalisées pour atteindre cet objectif.

Indications :

1) Créer une première fonction donnant la valeur en points d'un mot
2) Utiliser les méthodes sort() et reverse() des listes dans la fonction classement_mots





