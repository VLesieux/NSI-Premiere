# WA-TOR : Mise en place du projet

## Attendus du programme

![programmes ](programme1.png)   
![programmes ](programme2.png)   

## Première partie : représentation et affichage de la grille 

### Introduction : choix de la structure de données

La grille du jeu sera représentée par une _**liste de listes**_ contenant une structure de données liée à la nature de la case : mer, thon ou requin.

La représentation choisie pour une case sera un _**tuple**_ de forme _(n,g,e)_ où 
- **n** désigne la nature de la case : 0 pour la mer, 1 pour un thon, 2 pour un requin
- **g** désigne le temps de gestation de l'espèce : 0 si n vaut 0
- **e** désigne l'énergie de l'espèce : 0 si n vaut 0    

Les tuples représentant les cases seront placés dans un tableau à deux dimensions.    
Par exemple, la grille de jeu suivante :   ```[[(0,0,0),(0,0,0),(0,0,0)],[(1,2,0),(2,5,3),(1,2,0)]]  ``` est constituée de deux lignes (deux cases en hauteur) et de trois colonnes (trois cases en largeur) : la première ligne est vide et ne contient que la mer, la deuxième contient dans l'ordre un thon de temps de gestation 2, d'énergie 0 ; un requin de temps de gestation 5 et d'énergie 3 ; un thon de temps de gestation 2 et d'énergie 0.

On rappelle que les tuples (type tuple) et les listes (type list) sont des structures _**indicées**_. Les opérations que l'on peut effectuer sur eux sont similaires si ce n'est que les tuples ne sont pas modifiables : on dit de ces derniers qu'ils sont _**immuables**_.

```python
>>> tuple=("a",3,8)
>>> tuple[1]
3
>>> tuple[1]=4
Traceback (most recent call last):
  File "<pyshell>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
>>> liste=["a",3,8]
>>> liste[1]
3
>>> liste[1]=4
>>> liste
['a', 4, 8]
```  

Par ailleurs tuples et listes sont des _**itérables**_, c'est-à-dire qu'on peut les parcourir à l'aide d'une boucle ```for```.

```python
>>> tuple=("a",3,8)
>>> for i in tuple:
    print(i)
a
3
8
>>> liste=["a",3,8]
>>> for i in liste:
    print(i)    
a
3
8
``` 
Ce qui s'avère plus pratique et plus efficace que de faire :

```python
>>> for i in range(len(tuple)):
    print(tuple[i])    
a
3
8
>>> for i in range(len(liste)):
    print(liste[i])   
a
3
8
``` 

Ici la liste l étant à deux dimensions ou liste de liste, on utilisera la _**notation ```l[i][j] ```**_ pour accéder à la liste située en position j dans la ième liste de l, la numérotation des indices commençant à 0.

Exemple :

```python
>>>liste=[[(0,0,0),(0,0,0),(0,0,0)],[(1,2,0),(2,5,3),(1,2,0)]]
>>> liste[1][1]
(2, 5, 3)
```  

Puisqu'on trouvera un tuple dans une case, on utilisera la _**notation ```l[i][j][k] ```**_ pour accéder à la kième information du tuple.

Exemple :

```python
>>>liste=[[(0,0,0),(0,0,0),(0,0,0)],[(1,2,0),(2,5,3),(1,2,0)]]
>>> liste[1][1][2]
3
``` 

### Première étape : représentation de la grille

Réaliser une fonction ```creer_grille``` qui prend en _**paramètres**_ :
- le nombre de cases horizontalement ou largeur
- le nombre de cases verticalement ou hauteur

qui **_renvoie_** une liste de listes correspondant à une grille aux dimensions souhaitées, ne contenant dans un premier temps que de la mer.

On proposera deux approches :   
	- la première utilisant la **méthode** ```append``` associée aux listes et utilisant deux boucles successives   
	- la deuxième utilisant un **tableau donné en compréhension**    

##### Première méthode : utilisation de listes et de boucles

1. Utilisation de la méthode ```append``` des listes (une **méthode** est une fonction associée à un **objet**, ici l'objet liste, qui s'écrit sous la forme ```objet.methode```)
```python
>>> liste=[]
>>> liste.append((0,0,0))
>>> liste
[(0, 0, 0)]
```  
2. Utilisation de la _**boucle bornée**_ ```for```:   observer l'_**indentation**_

```python
def fonction_boucle(nombre_de_tours):
    liste=[]
    for i in range(nombre_de_tours):
        liste.append("a")
    return liste
```  
```python
>>> fonction_boucle(5)
['a', 'a', 'a', 'a', 'a']
```  
3. Utilisation d'une _**docstring**_ et tester avec _**doctest**_ : 

[Pour en savoir plus, consultez la documentation en ligne de Python](https://docs.python.org/3/library/doctest.html) ou [cette page de l'université de Lille](http://www.fil.univ-lille1.fr/~L1S2API/CoursTP/tp_doctest.html)

Réaliser une telle chaîne de documentation permet:   
- à l’utilisateur de la fonction de savoir   
		-	à quoi peut servir la fonction ;    
		-	comment il peut l’utiliser ;    
		-	quelles conditions il doit respecter pour l’utiliser (CU).    
- au programmeur de la fonction de préciser   
		- le nombre et la nature de ses paramètres ;    
		- la relation entre la valeur renvoyée et celle du ou des paramètres ;    
		- ses idées avec quelques exemples.   
 
 (Tout cela bien entendu à condition que cette documentation soit rédigée avant la réalisation du programme et non le contraire)

```python
def fonction_boucle(nombre_de_tours):
    """
    :param nombre_de_tours: (int) représente le nombre de répétition de la boucle
    :return: (list)  une liste de "a" de longueur égale au nombre de tours
    :CU : nombre_de_tours entier strictement positif
    :Exemples:

     >>> fonction_boucle(5)
     ['a', 'a', 'a', 'a', 'a']

    """    
    liste=[]
    for i in range(nombre_de_tours):
        liste.append("a")
    return liste

fonction_boucle(5)

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose = True)  

``` 

Remarque : pour que les tests soient validés, séparer dans vos exemples de résultat attendu, les items d'un tableau ou d'un tuple par une virgule suivie d'une espace. Par exemple écrire (1, 2, 0) au lieu de (1,2,0).

```python
Trying:
    fonction_boucle(5)
Expecting:
    ['a', 'a', 'a', 'a', 'a']
ok
1 items had no tests:
    __main__
1 items passed all tests:
   1 tests in __main__.fonction_boucle
1 tests in 2 items.
1 passed and 0 failed.
Test passed.

``` 
La fonction testmod du _**module**_ doctest est allée chercher dans la docstring de la fonction l'exemple (reconnaissable à la présence des triples chevrons >>>), et a vérifié que la fonction documentée satisfaisait bien cet exemple. Il n’y a eu aucun échec (failed=0).

> **À vous de jouer n°1** : _écrire la fonction ```creer_grille``` utilisant la première méthode avec son docstring !_

##### Deuxième méthode : utilisation des listes en compréhension

On veut créer une nouvelle liste appelée new_list à partir d'une première appelée list en faisant subir à chaque item de cette première une fonction appelée function.

La syntaxe d'une _**liste en compréhension**_ est ainsi :    
 ```new_list = [function(item) for item in list if condition(item)]```

Exemple : 

```python
>>> liste1=["a","b","a"]
>>> liste2=[x*2 for x in liste1 if x!="b"]
>>> liste2
['aa', 'aa']
``` 

Ici, on peut créer la grille de façon rapide et efficace avec une liste en compréhension.   
Par exemple, pour créer une grille de largeur 2 et de hauteur 3.

```python
>>> print([[(0, 0, 0) for _ in range(2)] for _ in range(3)])
[[(0, 0, 0), (0, 0, 0)], [(0, 0, 0), (0, 0, 0)], [(0, 0, 0), (0, 0, 0)]]
``` 

> **À vous de jouer n°2** : _écrire la fonction ```creer_grille``` utilisant la deuxième méthode avec sa docstring !_


### Deuxième étape : sélection des cases de la grille  


Afin de remplir la grille aléatoirement nous aurons besoin de sélectionner une case de la grille de façon aléatoire.  
Réaliser une fonction appelée ```selection_case``` prenant en paramètres le nombre total de cases horizontales nb_cases_h et le nombre total de cases verticales nb_cases_v de la grille et renvoyant un tuple de la forme (x,y) où x désigne l'abscisse de la case (x=0 au début d'une ligne) et y l'ordonnée d'une case (on commencera à y=0 et y augmente de 1 lorsqu'on passe à la ligne suivante) choisie de façon aléatoire.
La case de coordonnées (0,0) sera donc la première de la grille.  

<img src="fig1.png"/>

Par exemple :
```python
>>> selection_case(3,3)
(0, 2)
>>> selection_case(4,4)
(2, 2)
``` 
Exceptionnellement, ces exemples aux résultats aléatoires ne seront pas placés dans la docstring pour éviter les erreurs.
Déclarer également dans votre code deux _**variables globales**_ notées H et V représentant respectivement le nombre de cases horizontales et verticales. Vous initialiserez pour l'instant ces valeurs à 4. Elles nous seront utiles pour la suite.  

Remarque importante : une variable dite _**globale**_ par exemple v_globale déclarée dans le code en dehors des fonctions est connue dans la totalité du code même dans les fonctions. Une variable dite _**locale**_ n'a quant à elle plus de valeur en dehors de la fonction.  

Exemple :
```python
b=5#variable globale

def fonction(x):
    b=0#variable locale
    return b

fonction(5)
print("Appel à une variable locale : ", fonction(5))
print("Appel à une variable globale : ", b)

>>>Appel à une variable locale :  0
Appel à une variable globale :  5
```

Indication : on importe le module ```random``` et la méthode ```randrange``` correspondante en écrivant : ```from random import randrange```.

Ce qui donne par exemple :
```python
>>> randrange(8)
6
```

> **À vous de jouer n°3** : _écrire la fonction ```selection_case``` avec sa docstring !_

### Troisième étape : initialisation des cases 

Le jeu nécessite très régulièrement de permettre la naissance ou la mort d'un poisson, on se propose donc de réaliser une fonction ```init_case``` qui prend en paramètre la _nature_ de la case à générer (mer, thon ou requin) et qui retourne le tuple correspondant aux valeurs initiales des paramètres de gestation et d'énergie correspondant à cette nature.
Déclarer préalablement dans votre code quatre variables globales notées G_THON, G_REQUIN, E_THON et E_REQUIN  en leur affectant leurs valeurs initiales respectives 2, 5, 0, 3 conformément à la règle du jeu.   
Puis réaliser la fonction ```init_case``` qui utilisera ces variables globales.
Par ailleurs, dans l'écriture du code, il est toujours préférable de n'écrire qu'un seul ```return``` final.

```python
>>> init_case(0)
(0, 0, 0)
>>> init_case(1)
(1, 2, 0)
>>> init_case(2)
(2, 5, 3)
```

> **À vous de jouer n°4** : _écrire la fonction ```init_case``` avec sa docstring !_

### Quatrième étape : placement aléatoire des poissons dans la grille   

Réaliser maintenant une fonction appelée ```placement_espece``` prenant en paramètres une _grille_ (en pratique, une liste à deux dimensions définie plus haut), la _nature_ de l'espèce (thon ou requin) à placer aléatoirement et le nombre de poissons _nb_poissons_ de cette nature. Cette fonction retournera la grille correspondante. Dans cette fonction, vous utiliserez les fonctions précédentes ```selection_case``` et ```init_case```.   
Remarque : comme la fonction ```selection_case``` admet comme paramètres la largeur et la hauteur de la grille, on se demandera comment relier ces deux paramètres au seul paramètre grille.

Par exemple : 
```python
>>> placement_espece(creer_grille(3,2),2,4)
[[(2, 5, 3), (0, 0, 0), (2, 5, 3)], [(2, 5, 3), (2, 5, 3), (0, 0, 0)]]
```

Indications : 

1) L'idée est de placer des poissons aléatoirement uniquement dans des cases qui contiennent de la mer.   
2) Au vu de la structure de la grille, s'interroger sur la façon d'atteindre la nature de la case (mer, thon ou requin) située à l'abscisse x et à l'ordonnée y de la grille. Ce point est important pour la suite.
3) On pourra créer une variable locale intermédiaire nommée case telle que x=case[0] et y=case[1].
4) On utilisera une boucle ```while``` pour faire le décompte du nombre d'espèces ajoutées.
5) On pourra éventuellement utiliser l'opérateur ```not in``` pour tester l'appartenance d'une valeur à une liste établie.

Par exemple : 
```python
>>> 5 not in [2,6,8]
True
```

> **À vous de jouer n°5** : _écrire la fonction ```placement_espece``` avec sa docstring !_

### Cinquième étape : initialisation de la grille   

Réaliser une fonction ```denombre_espece``` qui admet comme paramètre la grille et la nature de l'espèce, et qui retourne le nombre d'espèces dans la grille.

Par exemple : 

```python
>>> denombre_espece(placement_espece(creer_grille(3,2),2,4),2)
4
```

Indication :   
Utiliser le caractère _**itérable**_ des listes.

> **À vous de jouer n°6** : _écrire la fonction ```denombre_espece``` avec sa docstring !_


Il s'agit maintenant de placer des poissons dans la grille en respectant un pourcentage donné des espèces. Réaliser une fonction ```init_grille``` qui admet comme paramètres les pourcentages initiaux de chacune des espèces _p_thons_ puis _p_requins_ ainsi que le nombre de cases horizontales _nb_cases_h_ et le nombre de cases verticales _nb_cases_v_ de la grille. La fonction retournera une grille.

Par exemple:
```python
>>> denombre_espece(init_grille(0.5,0.5,2,2), 1)
2
>>> denombre_espece(init_grille(0.5,0.5,2,2), 2)
2
```

Par la suite, on choisira des pourcentages initiaux adaptés pour ces deux espèces : par exemple 30 % pour les thons et 10 % pour les requins.
On déclarera donc deux nouvelles variables globales notées P_THON et P_REQUIN en leur affectant les valeurs adaptées.

### Sixième étape : affichage de la grille  

La visualisation d'une grille sous la forme d'un affichage en 2 dimensions nous permettra d'appréhender plus facilement le déplacement des différentes espèces.
Réaliser une _**procédure**_ appelée ```afficher_grille``` dont le rôle sera de visualiser la grille passée en paramètre. On utilisera la fonction ```print(chaîne de caractères)```.
Les cases de la mer seront affichées avec un tiret bas _ , les cases occupées par les thons seront affichées avec un T majuscule et celles des requins par un R majuscule. Le contenu des cases sera séparé par un espace. Chaque ligne sera affichée sur une ligne distincte.

Exemples :
```python
>>> afficher_grille(creer_grille(3,2))
 _  _  _ 

 _  _  _ 


>>> afficher_grille(init_grille(0.5,0.5,4,4))

 R  R  T  T 

 R  T  T  R 

 R  R  R  T 

 T  T  T  R 
```

Indications :  

1) Utiliser le processus dit de _**concaténation**_ des chaînes de caractères. Par exemple :
```python
>>> "Py"+"thon"
'Python'
```
2) Forcer le passage à la ligne avec ```"\n"```. 

> **À vous de jouer n°7** : _écrire la fonction ```afficher_grille``` avec sa docstring !_



## Deuxième partie : gestion de l'environnement   

L'interaction entre les proies et les prédateurs ainsi que les déplacements dans la mer nécessitent lorsqu'une case a été choisie aléatoirement au début d'un tour du jeu de connaître l'environnement proche de celle-ci.

### Première étape : trouver les cases voisines  

Réaliser une fonction ```cases_voisines``` prenant comme paramètres :
- les coordonnées de la case sous la forme du tuple (x,y)
- le nombre de cases présentes dans la grille horizontalement
- le nombre de cases présentes dans la grille verticalement   

Cette fonction doit retourner une liste de 4 coordonnées sous forme de 4 tuples (x,y) des cases voisines selon les 4 directions particulières : une au NORD, une à l'OUEST, une à l'EST et enfin une au SUD. Il sera de plus nécessaire de réfléchir aux coordonnées des voisines d'une case située sur le bord de la grille dans la mesure où l'environnement est torique.

Par exemple : 

```python
>>> cases_voisines((1,1),2,2)
[(1, 0), (0, 1), (0, 1), (1, 0)]
>>> cases_voisines((1,1),3,3)
[(1, 0), (0, 1), (2, 1), (1, 2)]
>>> cases_voisines((2,0),3,3)
[(2, 2), (1, 0), (0, 0), (2, 1)]
```

Indication : l'opérateur modulo % qui renvoie le reste de la division peut s'avérer utile ici.

Par exemple :
```python
>>> 4%3
1
```

> **À vous de jouer n°8** : _écrire la fonction ```cases_voisines``` avec sa docstring !_

### Deuxième étape : rechercher un type de case parmi les voisines

Lors de leurs déplacements respectifs, les thons et les requins cherchent aléatoirement des cases mer ou thon parmi leurs voisins. Réaliser une fonction ```recherche_case``` acceptant 3 paramètres : 
- une liste de coordonnées de 4 cases
- une grille
- la nature de la case recherchée   

Cette fonction retournera les coordonnées sous la forme de tuple (x,y) d'une case tirée au sort parmi celles répondant au critère de recherche sinon False.

Exemple : 

```python
>>> grille=[
    [(1, 2, 0), (0, 0, 0), (0, 0, 0)],
    [(1, 2, 0), (2, 5, 3), (0, 0, 0)],
    [(0, 0, 0), (1, 2, 0), (0, 0, 0)]
    ]
>>> afficher_grille(grille)
 T  _  _ 

 T  R  _ 

 _  T  _ 

>>> recherche_case(cases_voisines((1,1),3,3),grille,1)
(0, 1)
>>> recherche_case(cases_voisines((1,1),3,3),grille,1)
(1, 2)
```

> **À vous de jouer n°9** : _écrire la fonction ```recherche_case``` avec sa docstring !_

### Troisième étape : actions liées aux espèces

#### Action commune : gérer la durée de gestation

Réaliser une fonction ```evol_gestation``` acceptant deux paramètres : les coordonnées d'une case et une grille.  
La fonction retournera la durée de gestation de l'espèce diminuée d'une unité.

Par exemple avec la même grille que précedemment :

```python
>>> evol_gestation((0,0),grille)
1
>>> evol_gestation((1,1),grille)
4
```

> **À vous de jouer n°10** : _écrire la fonction ```evol_gestation``` avec sa docstring !_


#### Action commune : se déplacer vers la mer   

Lorsque c'est le tour d'un thon il cherche à se déplacer vers une mer voisine, c'est aussi vrai pour un requin s'il n'y a pas de thon à proximité. On cherche donc à écrire une fonction qui traduit un comportement commun aux deux espèces.

Réaliser une fonction ```deplace_vers_mer``` acceptant comme paramètres :
- la nature de l'espèce
- la case initiale sur laquelle se trouve l'espèce
- la case de mer vers laquelle se déplace l'espèce
- la grille
- la durée de gestation de l'espèce
- l'énergie de l'espèce : on pourra utiliser une valeur 0 par défaut pour ce paramètre.    

Cette fonction devra gérer les reproductions éventuelles des espèces, les réinitialisations des gestations et les cases redevenant des mers. Elle retourne la grille ayant évolué en conséquence.   
La fonction ne s'occupe pas de la mise à jour du temps de gestation ou de l'énergie et on suppose que cette mise à jour est faite préalablement au déplacement.


Exemples :
```python
>>> grille1 = [
[(1, 2, 0), (1, 2, 0), (0, 0, 0)],
[(0, 0, 0), (2, 5, 3), (0, 0, 0)]
]
>>> afficher_grille(grille1)

 T  T  _ 

 _  R  _ 


>>> deplace_vers_mer(1, (0, 0), (0, 1),grille1, 1)
[
[(0, 0, 0), (1, 2, 0), (0, 0, 0)],
[(1, 1, 0), (2, 5, 3), (0, 0, 0)]
]
>>> afficher_grille(grille1)

 _  T  _ 

 T  R  _ 

--------------------------------------------------------------

>>> grille2 = [
[(0, 0, 0), (0, 0, 0), (0, 0, 0)],
[(0, 0, 0), (2, 5, 3), (0, 0, 0)]
]
>>> afficher_grille(grille2)

 _  _  _ 

 _  R  _ 

>>> deplace_vers_mer(2, (1, 1), (2, 1), grille2, 4, 2)
[
[(0, 0, 0), (0, 0, 0), (0, 0, 0)],
[(0, 0, 0), (0, 0, 0), (2, 4, 2)]
]
>>> afficher_grille(grille2)

 _  _  _ 

 _  _  R 


--------------------------------------------------------------

>>> grille3 = [
[(0, 0, 0), (0, 0, 0), (0, 0, 0)],
[(0, 0, 0), (2, 1, 3), (0, 0, 0)]
]
>>> afficher_grille(grille3)
 _  _  _ 

 _  R  _ 

>>> deplace_vers_mer(2,(1, 1), (2, 1), grille3, 0, 2)
[
[(0, 0, 0), (0, 0, 0),
(0, 0, 0)], [(0, 0, 0),
(2, 5, 3), (2, 5, 2)]
]
>>> afficher_grille(grille3)
 _  _  _ 

 _  R  R 
```

Rappels : lorsqu'un thon a un temps de gestation nul, il engendre un nouveau thon là où il était et son temps de gestation est réinitialisé. Lorsqu'un requin a un temps de gestation nul, il engendre un nouveau requin là où il était, son temps de gestation est réinitialisé mais pas son niveau d'énergie.

Remarque : donner à un argument une valeur par défaut peut se comprendre sur un exemple : 
```python
def calcul(x,a,b=2):
    return a*x+b
>>> calcul(5,2,4)
14
>>> calcul(5,2)
12
```

> **À vous de jouer n°11** : _écrire la fonction ```deplace_vers_mer``` avec sa docstring !_


#### Actions propres aux thons   

Réaliser une fonction ```tour_thon``` qui traduira parfaitement les actions d'un thon situé sur un case de la grille en retournant une nouvelle grille donnant l'état de celle-ci à la fin de ce tour.

Cette fonction mettra en oeuvre les fonctions ```recherche_case```, ```cases_voisines```, ```evol_gestation```, ```deplace_vers_mer```. Elle prendra comme argument une case, une liste de cases (coordonnées des 4 cases voisines) et une grille.

Il faudra envisager le cas où il n'y a pas de case disponible pour le déplacement du thon, auquel cas il reste sur place. Son niveau de gestation se réinitialise s'il passe à zéro.

Exemple :
```python
>>> grille=[
[(0, 0, 0), (1, 2, 0), (0, 0, 0)],
[(1, 1, 0), (2, 5, 3), (0, 0, 0)]
]
>>> afficher_grille(grille)
 _  T  _ 

 T  R  _ 

>>> evol_gestation((0,1),grille)
0#le thon (0,1) va pouvoir se reproduire
>>> tour_thon((0,1),grille)
[
[(1, 2, 0), (1, 2, 0), (0, 0, 0)],
[(1, 2, 0), (2, 5, 3), (0, 0, 0)]
]
>>> afficher_grille(grille)
 T  T  _ 

 T  R  _ 
# il s'est déplacé en (0,0) et a engendré un nouveau thon à la place quittée
#les temps de gestation sont réinitialisés
>>> tour_thon((0,1),grille)
[
[(1, 2, 0), (1, 2, 0), (0, 0, 0)],
[(0, 0, 0), (2, 5, 3), (1, 1, 0)]
]
#le thon (0,1) s'est déplacé en (2,2) en utilisant le caractère torique de la mer
>>> afficher_grille(grille)
 T  T  _ 

 _  R  T 
```

> **À vous de jouer n°12** : écrire la fonction ```tour_thon``` avec sa docstring !_


#### Actions propres aux requins

##### Gestion de l'énergie

Réaliser une fonction  ```evol_energie``` acceptant deux paramètres : les coordonnées d'une case et une grille. La fonction retournera l'énergie de l'espèce diminuée d'une unité.

Exemple :
```python
>>> evol_energie((1, 1),[[(1, 2, 0), (1, 2, 0), (0, 0, 0)], [(0, 0, 0),(2, 5, 3), (0, 0, 0)]])
2
```
> **À vous de jouer n°13** : écrire la fonction ```evol_energie``` avec sa docstring !_

##### Chasser un thon  

Lors de son tour, le requin, après avoir perdu un temps de gestation et trouvé un thon parmi les cases voisines, mange le thon en se déplaçant sur cette case. Réaliser une fonction ```chasse_au_thon``` traduisant cette dernière action. Elle acceptera plusieurs paramètres :
- les coordonnées de la case de départ du requin
- les coordonnées de la case occupée par le thon
- la grille
- la durée de gestation

La fonction retournera la grille ayant évolué en conséquence (penser aux éventuelles naissances !).

Exemples : 

```python
>>> grille=[
[(1, 2, 0), (1, 2, 0), (0, 0, 0)],
[(0, 0, 0),(2, 5, 3), (0, 0, 0)]
]
>>> afficher_grille(grille)
 T  T  _ 

 _  R  _ 

>>> chasse_au_thon((1,1),(1,0),grille,5)
[
[(1, 2, 0), (2, 5, 3), (0, 0, 0)],
[(0, 0, 0), (0, 0, 0), (0, 0, 0)]
]
>>> afficher_grille(chasse_au_thon((1,1),(1,0),grille,5))
 T  R  _ 

 _  _  _ 

-----------------------------------------------------------------------------------

>>> grille=[
[(1, 2, 0), (1, 2, 0), (0, 0, 0)],
[(0, 0, 0),(2, 0, 3), (0, 0, 0)]
]
>>> afficher_grille(grille)
 T  T  _ 

 _  R  _ 

>>> chasse_au_thon((1,1),(1,0),grille,0)
[
[(1, 2, 0), (2, 5, 3), (0, 0, 0)],
[(0, 0, 0), (2, 5, 3), (0, 0, 0)]
]
>>> afficher_grille(chasse_au_thon((1,1),(1,0),grille,0))
 T  R  _ 

 _  R  _ 


```
> **À vous de jouer n°14** : écrire la fonction ```chasse_au_thon``` avec sa docstring !_


##### Tour du requin  

Réaliser une fonction ```tour_requin``` qui traduira parfaitement les actions d'un requin en retournant une grille donnant un état à la fin du tour.

La fonction met en oeuvre les fonctions  ```evol_gestation```, ```evol_energie```, ```recherche_case```, ```cases_voisines```. Elle accepte les paramètres case et grille et renvoie une grille mise à jour.

> **À vous de jouer n°15** : écrire la fonction ```evol_energie``` avec sa docstring !_


## Troisième partie : évolution des populations

### Évolution de la grille

Réaliser une fonction ```evol_population``` acceptant une grille comme paramètre. Cette fonction devra simuler le comportement du jeu en choissant tout d'abord une case aléatoirement de la grille puis en appelant éventuellement la fonction liée aux actions de la nature de la case sélectionnée. Elle retournera la grille ayant écvolué d'un pas de simulation.

> **À vous de jouer n°16** : écrire la fonction ```evol_population``` avec sa docstring !_


### Simulation pas à pas

Réaliser une fonction ```simulation``` qui accepte comme paramètres :
- une grille
- un nombre de pas de simulations
- un nombre de pas au bout duquel un affichage de la grille est réalisé

Cette fonction utilisera la fonction ```evol_population```.  
Si on veut avoir un affichage de l'évolution de la mer, il peut être pertinent de ne pas afficher toutes les étapes mais une étape tous les 10 par exemple et de faire une pause après chaque affichage grâce au module time et sa fonction sleep:
```python
import time
time.sleep(0.1) # pause de 0,1 seconde
```

### Construction de la courbe

On ajoute à la simulation des listes qui comptabilisent à chaque pas les nombres de requins et de thons. Utilisez pour cela la fonction ```denombre_espece```.   
Ces listes peuvent être utilisées pour dessiner les courbes des évolutions de population.
On utilise pour cela le module ```pylab```.

Exemple : 
```python
import pylab
data_x=[0,1,2,3]
data_y=[0,3,6,9]
pylab.plot(data_x,data_y)
pylab.title('courbe des points de coordonnées (x,y)')
pylab.xlabel('Axe des abscisses')
pylab.ylabel('Axe des ordonnées')
pylab.grid()
```





