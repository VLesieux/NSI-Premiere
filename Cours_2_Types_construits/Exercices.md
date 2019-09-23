# Exercices types construits : tuples, listes et dictionnaires

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

L'instruction tuple(sorted((a,b,c))) renvoie un triplet contenant les valeurs des nombres a,b,c rangées dans l'ordre croissant. Compléter la fonction maxi qui renvoie le plus grand des trois nombres a,b,c.

```Python
def maxi(a,b,c):
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
On suppose avoir reçu une photo prise sur un smartphone par une personne en vacances. On regarde dans les propriétés les coordonnées GPS au moment de la prise de vue. Écrire une fonction prenant en paramètres un couple de coordonnées GPS et le dictionnaire construit, et renvoyant le nom du lieu correspondant. On tolère une précision au dix-millième de degré.
Par exemple si les coordonnées sont [(11.61135,43.14775)], la fonction doit nous renvoyer "Djibouti".

__Indications__ : 
1) l'idée est de faire un parcours des clés du dictionnaire, comparer les coordonnées du site avec chacune des clés du dictionnaire en élargissant l'égalité avec un encadrement
2) penser à comparer la valeur absolue (avec abs()) de la différence des coordonnées fois 10000

## Exercice 6

Écrire une fonction _stat_ qui prend en paramètre un texte et renvoie un dictionnaire dont les clés sont les différentes lettres du texte et les valeurs le nombre d'occurences de chaque lettre. On suppose le texte écrit en lettres capitales non accentuées. Le texte peut contenir des espaces ou des caractères de ponctuation qu'il ne faudra pas comptabiliser.  
On utilisera la méthode _get_ des dictionnaires qui évite les signalements d'erreur.

Exemple: #non signalement d'erreur avec la méthode get

```Python
>>> dictionnaire={"A":2,"B":3}
>>> dictionnaire["A"]
2
>>> dictionnaire.get("A")
2
>>> dictionnaire["C"]
Traceback (most recent call last):
  File "<pyshell>", line 1, in <module>
KeyError: 'C'
>>> dictionnaire.get("C")
#Pas d'ereur signalée
```

__Indications__ : parcourir les lettres du textes, créer le nouvel item (lettre:1) dans le dictionnaire statistiques s'il n'existe pas encore ou augmenter de 1 la valeur de l'item si celui-ci existe déjà.

## Exercice 7

On suppose que l'on dispose d'un traducteur anglais-français et la question est de mesurer l'intérêt d'une représentation par un dictionnaire {"yes":"oui","no":"non",...} plutôt que par une liste de listes [["yes","oui"],["no","non"],...]. Nous allons donc compter le temps de recherche d'un élément. Pour traduire "yes", on doit trouver dans le dictionnaire la valeur correspondant à la clé "yes" et dans la liste de listes la valeur du deuxième élément d'une sous-liste dont le premier élément a pour valeur "yes".
1. Écrire une fonction _recherche1_ qui prend en paramètres une liste de listes et une variable k et renvoie le deuxième élément de la sous-liste dont le premier élément a la valeur de k.
2. Écrire une fonction _recherche2_ qui prend en paramètres un dictionnaire et une variable k et renvoie la valeur correspondant à la clé k. Utiliser la méthode get de l'objet dictionnaire qui renvoie directement la valeur associée à la clé (cf.exercice précédent).
3. Pour la recherche qui doit être effectuée sur un grand ensemble, nous simplifions nos objets. Construire une liste dont les éléments sont de la forme [i,i] pour i allant de 0 à 10<sup>6</sup>-1. Mélanger cette liste avec la fonction `shuffle` du module `random`. Créer alors le dictionnaire correspondant à l'aide de la fonction `dict`.

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





