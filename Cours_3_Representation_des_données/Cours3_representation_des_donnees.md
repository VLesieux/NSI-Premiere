# Thème A : types de base

## Un peu d'histoire

Pour représenter l'information dans la machine, on utilise le code binaire formé des bits (binary digit) 0 et 1. Ces codes correspondent aux états ouvert ou fermé des interrupteurs utilisés dans les circuits électroniques. 
Une variable qui a deux états 0 ou 1, ou, False ou True, est également appelée **booléenne** en hommage au britannique **George Boole** qui a créé au XIX<sup>e</sup> siècle l'algèbre, fondement de la logique booléenne utilisée en mathématique, philosophie et informatique.  
<img width="150" src="assets/Boole.png" /><img width="150" src="assets/Atanasov.png" /><img width="150" src="assets/Atansov_Berry_computer.png" /><img width="250" src="assets/Eniac.png" />. 

À la fin des années 1930, **Djon Atanasov**, physicien, mathématicien et ingénieur américain d'origine Bulgare, travaillait avec son étudiant Clifford Berry sur la construction d'un calculateur électronique (sans programme enregistré). Atanasov avait compris que la solution du fonctionnement était le binaire. L'**ABC** (Atanasov Berry Computer) entra en service à la fin **1939**, il pouvait effectuer une opération toutes les 15 secondes et pesait plus de 300 kilos.   
Pendant ce temps, la construction de l'**ENIAC** avait commencé ; Eckert et Mauchly, concepteurs et constructeurs, vont breveté leur invention d'un ordinateur en **1945**. Un procès aura lieu dans les années 1970, Atanasov affirmant que l'ENIAC avait été construit sur la base de ses idées. Une cour des États-Unis finira par invalider le brevet d'Eckert et Mauchly, tombé alors dans le domaine public, et attribuera ainsi l'invention du premier ordinateur électronique à Atanasov.

## Les attendus du programme

![Programme officiel ](assets/bo1.png)

## Écriture d'un entier positif en base b≥2

> Attendu : passer d'une base à une autre
>
> Commentaire : les bases 2, 10 et 16 sont privilégiées

Il faut toujours indiquer la base dans laquelle un nombre est exprimé (sauf,
par usage et commodité, en base 10) :   
1010<sub>2</sub> = 10 = A<sub>16</sub>

**Note** : la base par défaut dans du code Python est la base 10. Mais, avec certaines notations, il est
possible d'utiliser d'autres bases.

```python 	
>>> 10 == 0b1010 == 0xA 
True
```

Toutes ces représentations correspondent au même nombre dix.   
Mais peu importe la représentation donnée en entrée, en interne toutes les données sont en
binaire.

> Écrire en base cinq le nombre qui s'écrit 175 en base dix

Algorithme de conversion d'un entier en base b≥2 :

```python
Entrée : b la base de numération, n est un entier naturel.
Sortie : x0 , x1 ,. . . xp−1 les différents chiffres de l’écriture de n en base b.

m := n
i := 0
tant que m ≥ b faire
 r := m (mod b)
 m := m ÷ b
 xi := chiffre correspondant à r
 i := i + 1
fin tant que
xi := chiffre correspondant à m
renvoyer x0 , x1, . . . , xi.

```

> Exemple : Comment parmi quatre propositions de code binaire 11 1100 1101 ; 11 1110 0101 ; 10 0111 1001; 10 1111 1001 retenir celle qui correspond à 761 ?

On voit que le bit de poids le plus fort est commun aux quatre propositions : 1 qui représente la puissance de 9 car 2<sup>9</sup>=2x2<sup>8</sup>==2x256=512.
Ainsi 761=512+249. Puis 249=1x128+121=1x2<sup>7</sup>+1x2<sup>6</sup>+..
On attend donc le début 1011... seule la dermière proposition est donc cohérente et peut être retenue sans avoir à poursuivre le travail de décomposition.

```python
>>> bin(761)
'0b1011111001'
```


### Passage du binaire (base 2) à l'hexadécimacal (base 16), et inversement

La base 16 est fréquemment utilisée. Pourquoi ?   
16 a le bon goût d'être une puissance de 2 (2<sup>4</sup>) et ainsi **deux chiffres hexadécimaux suffisent pour décrire un octet de 8 bits**.   

Abordons le passage de la base 2 à la base 16 (et inversement).  
Quatre bits (2<sup>4</sup>=16 possibilités) correspondent à un chiffre hexadécimal (0 à 9 puis A à F soit 16 possibilités). 
On peut donc convertir un nombre de la base 2 à la base 16, sans passer par l'écriture décimale, en procédant par la formation de paquets de 4 bits. Si le nombre de bits n'est pas un multiple de 4, on peut toujours « ajouter » des 0 non significatifs avant le bit de poids fort.

> Exemple 1 : Recherchons l'écriture hexadécimale du nombre entier 157.

Une première méthode peut consister à réaliser la décomposition de l'entier en base 16.
Sachant que 16<sup>2</sup>=2<sup>8</sup>=256, et que 10x16=160, on cherche une décomposition en 9x16=144 ; ainsi 157=9x16<sup>1</sup>+13 et l'écriture hexadécimale de 157 est : 9D.

Une autre méthode peut consister à donner l'écriture binaire de 157 en réalisant des divisions successives par 2 aussi longtemps que le quotient est non nul et en remontant de bas en haut pour obtenir : 10011101 puis on fait des regroupements de 4 : 1001 qui correspond à 9 et 1101 qui correspond à 13 soit D.

```python
>>> hex(157)
'0x9d'
```

Application à voir : [le codage des couleurs](http://isnangellier.alwaysdata.net/php/colours.html) ; les couleurs sont codées en code RGB (Red Green Blue) avec chaque niveau de couleur codé sur 1 octet : soit 256 niveaux de 0 à 255 pour chaque couleur et un total de 256x256x256 couleurs soit 2<sup>24</sup>=16 777 216 couleurs possibles sur un écran.

> Exemple 2 : La couleur "vert impérial" est codée en écriture décimale par (0,86,27). Recherchons son codage hexadécimal.

86=5x16+6 est codé 56 en hexadécimal et 
27=1x16+11 est codé 1B en hexadécimal. 
Le codage hexadécimal de cette couleur est donc : (0,56,1B).

```python
>>> hex(0),hex(86),hex(27)
('0x0', '0x56', '0x1b')
```

> Exemple 3 : Exprimons la différence CBD-BAC en base 16.
  
On sait que la valeur décimale de A est 10, que la valeur décimale de B est 11, que la valeur décimale de C est 12 et que la valeur décimale de D est 13 ; ainsi la valeur décimale de CBD est 12×16<sup>2</sup>+11×16<sup>1</sup>+13×16<sup>0</sup> tandis que la valeur décimale de BAC est 11×16<sup>2</sup>+10×16<sup>1</sup>+12×16<sup>0</sup> ; la différence recherchée est donc égale à 1×16<sup>2</sup>+1×16<sup>1</sup>+1×16<sup>0</sup>, ce qui s'écrit 111 en base 16.  
La vérification en Python peut se faire ainsi : 
 
```python
>>> hex(0xCBD-0xBAC)
'0x111'
```

> Exemple 4 : Exprimons en base 16 la valeur de la somme des deux entiers positifs A7 et 84 écrits en base 16.

La valeur décimale de A7 est 10×16<sup>1</sup>+7×16<sup>0</sup> tandis que celle de 84 est 8×16<sup>1</sup>+4×16<sup>0</sup> ainsi la valeur décimale de la somme est 18×16<sup>1</sup>+11×16<sup>0</sup> or 18=1×16+2 donc la valeur décimale de la somme s'écrit 1×16<sup>2</sup>+2×16<sup>1</sup>+11×16<sup>0</sup> soit 12B en hexadécimal.  
La vérification en Python peut se faire ainsi : 
 
```python
>>> hex(0xA7+0x84)
'0x12b'
```



### Taille des données

**À noter** : 1ko c'est 1 000 octets, pas 1 024. Le préfixe kilo correspond
toujours à 1000, l'informatique ne fait pas exception (de même pour méga,
giga, téra, etc.). Il existe cependant les préfixes kibi (2<sup>10</sup>=1024), mébi
(2<sup>20</sup>), gibi (2<sup>30</sup>), tébi (2<sup>40</sup>), etc. qui sont respectivement abbréviés en
ki, Mi, Gi, Ti, etc.

# Représentation binaire (en base 2) d'un entier relatif

> Attendu : Évaluer le nombre de bits nécessaires à l’écriture en base 2 d’un
> entier, de la somme ou du produit de deux nombres entiers.  Utiliser le
> complément à 2.
>
> Commentaires : Il s’agit de décrire les tailles courantes des entiers (8,
> 16, 32 ou 64 bits).  Il est possible d’évoquer la représentation des entiers
> de taille arbitraire de Python.

## Taille d'un entier dans l'écriture en base 2

Le fait que l'entier soit relatif ne change finalement pas grand chose. Il
faut uniquement prendre en compte un bit en plus afin de stocker le signe.

En utilisant exactement *`n`* bits (avec un nième bit non nul) on peut représenter les entiers naturels de
*`2^{n-1}`* (1 suivie de 0) à *`2^n-1`* (que des 1).  Si on veut connaître le nombre de bits pour
représenter un entier donné, il faut utiliser la fonction inverse de 2^n soit *`log_2`*
(mais qui n'est pas présentée en 1è).
De ce fait un entier naturel *`n`* s'écrit sur *`log_2(n)+ 1`* bits.

D'un point de vue plus pratique les entiers naturels représentables sur 8, 16,
32 ou 64 bits sont donc ceux strictement inférieurs à 2<sup>8</sup>=256, 2<sup>16</sup> = 65 536, 2<sup>32</sup> =
4 294 967 296, 2<sup>64</sup> = 18 446 744 073 709 551 616.

> Exemple 1 : Recherchons le plus grand entier positif (non signé) représentable en binaire sur 2 octets (c'est-à-dire sur 16 bits).  

Écrit sur 16 bits, le plus grand entier s'écrit comme une succession du bit 1, sa valeur correspond au nombre de combinaisons possibles soit 2<sup>16</sup> auquel on retire le cas de 0 soit 2<sup>16</sup>-1. Une autre façon de procéder, que l'on donne pour son intérêt mathématique, est de calculer la somme des termes d'une suite géométrique de raison 2.  
S=1+2<sup>1</sup>+2<sup>2</sup>+...+2<sup>15</sup>.   
2×S=2+2<sup>2</sup>+2<sup>3</sup>+...+2<sup>16</sup>.  
En retranchant membre à membre la deuxième équation à la première, on obtient :  S=2<sup>16</sup>-1.

> Exemple 2 : Recherchons le nombre maximal de bits du produit de deux entiers positifs codés sur 8 bits. 

Pour répondre à cette question, commençons par le cas simple de la multiplication entre eux de deux entiers de deux bits 11×11 qui s'effectue comme à l'accoutumée (avec le même système de retenue) et on obtient : 1001 c'est à dire un nombre entier de 4 bits. On prédit ainsi que le nombre maximal de bits du produit de deux entiers positifs codés sur 8 bits est 2×8=16.

```python
>>> bin(255*255)
'0b1111111000000001'
```


> Exemple 3 : On ajoute trois chiffres 0 à droite de l'écriture binaire d'un entier N strictement positif ; montrons que cela revient à donner l'écriture binaire de 8×N.

En effet, pour un entier N qui s'écrit sur n bits :

N=a<sub>0</sub>×2<sup>0</sup>+.........+a<sub>n-1</sub>×2<sup>n-1</sup>.   
2×N=0×2<sup>0</sup>+a<sub>0</sub>×2<sup>1</sup>+.........+a<sub>n-1</sub>×2<sup>n</sup>. 

La multiplication par 2 a pour effet de placer un 0 à droite et de décaler tous les bits vers la gauche. Ajouter 3 chiffres 0 à droite consiste à faire 3 fois la multiplication par 2, c'est-à-dire la multiplication par 8. 
Par exemple : 

```python
>>> 0b1010
10
>>> 0b1010000
80
```


## Écriture en complément à 2 d'un entier négatif

Pour représenter un **nombre signé** on pense intuitivement qu'il suffit d'ajouter
un bit de signe. Mais cette représentation (appelée *signe-valeur absolue*) ne
permet pas d'additionner directement deux nombres.

Par exemple si le bit de poids fort est le bit de signe et qu'on représente
les entiers relatifs sur 3 bits et qu'on fait 2 + (-1). Cela donne, en
représentation signe-valeur absolue : 010 + 101 = 111. Or 111 en
représentation signe-valeur absolue correspond à -3, ce qui est incorrect.

À la place la représentation en complément à 2 est généralement préférée.
Soit *`n`* l'entier relatif à représenter sur *`p`* bits (avec *`|n| < 2^{p-1}`*):
- si *`n > 0`* : *`n`* est représenté en binaire sur *`p`* bits.
- sinon : le complément à 2 de *`-n`* est représenté sur *`p`* bits.

**Attention** C'est le bit de poids fort qui sert de bit de signe. Il est donc très
important de préciser le nombre de bits dans la représentation afin de savoir
quel bit est le bits de poids fort.

Le complément à 2 d'un entier positif *`N`* sur *`p`* bits est tel que la
somme de *`N`* et de son complément à 2 soit nulle sur *`p`* bits.
Il peut se calculer de deux méthodes :     


- **Première méthode** : On prend le complément de la représentation binaire de *`N`* et on lui ajoute 1    

- **Deuxième méthode** :  *`2^p-N`* qu'on représente en binaire sur *`p`* bits.

**Attention** *complément à 2* désigne à la fois l'opération mathématique de
conversion et une méthode de représentation des entiers relatifs (qui
n'implique pas forcément de calculer un complément à 2 !)

**Avec la représentation en complément à 2 sur *`p`* bits il est possible de
représenter tous les entiers compris entre *`-2^{p-1}`* jusqu'à *`2^{p-1}-1`*
(représentés respectivement par 10...0 et 01...1, la valeur -1 étant codée par une suite de 1).**

### Exemples

> Exemple 1 : On souhaite représenter 13 sur 5 bits dans la représentation en complément
à 2. 

On a 13 = 1101<sub>2</sub>. Donc dans la représentation en complément à 2 sur 5 bits
13 s'écrit : 01101.      


On souhaite maintenant représenter -13 sur 5 bits dans la représentation en complément
à 2.  On a toujours 13 = 1101<sub>2</sub>. Nous devons calculer le complément
à 2. Voyons avec les deux méthodes     


**Première méthode** : Le complément de 01101<sub>2</sub> est 10010<sub>2</sub>, auquel on ajoute 1. On obtient donc 10011<sub>2</sub>. La représentation de -13 en complément à 2 sur 5 bits est donc 10011.     

 
**Deuxième méthode** : *`2^5 - 13 = 32 - 13 = 19`* or 19 = 10011<sub>2</sub>. Donc la représentation de -13 en
   complément à 2 est 10011.

> Exemple 2 : Quel est le nombre entier relatif qui correspond à la représentation en
complément à 2 sur 5 bits suivante 11001 ?

Il s'agit d'un nombre négatif puisque le bit de poids fort est à 1.     
**Première méthode** :  On prend le complément et on lui ajoute 1 : 00111<sub>2</sub>, ce qui correspond à
   l'entier 7. L'entier représenté était donc -7    
**Deuxième méthode** : En binaire 11001<sub>2</sub> = 25 puis *`2^5-25 = 7`* donc l'entier représenté était -7.

Remarque : Si la représentation en complément à 2 est par exemple 01001, alors le nombre entier est
positif car le bit de poids fort est 0. Il suffit alors de convertir le nombre en
décimal pour connaître la valeur de l'entier, ici 9.

> Exemple 3 : Recherchons l'écriture binaire, en complément à deux sur 8 bits, de l'entier négatif -7.

La représentation binaire de 7 sur 8 bits est 00000111 ; le complément est 11111000 puis on ajoute 1 ainsi 11111001 est l'écriture en complément à deux sur 8 bits de l'entier négatif -7. On peut aussi, mais c'est plus long, calculer 2<sup>8</sup>-7 soit 256-7=249 puis écrire son écriture binaire et on retrouve 11111001.

### Représentation des entiers de taille arbitraire en Python

Dans un langage où les entiers sont de taille fixe, par exemple sur 32 bits,
ajouter 1 à *`2^{31}-1`* donnera un nombre négatif, et cela donnera
*`-2^{31}`* si les nombres sont représentés en complément à 2 sur 32 bits.

Il n'est pas possible d'illustrer cela sous Python, ou alors de manière très
détournée, car les entiers peuvent être arbitrairement grand (l'unique limite
étant la mémoire disponible sur la machine).

Pour information les nombres entiers en Python sont représentés comme une
suite de chiffres en base 2<sup>30</sup>. Plus [d'informations ici](https://rushter.com/blog/python-integer-implementation/).

# Représentation approximative des nombres réels : notion de nombre flottant 

> Attendu : Calculer sur quelques exemples la représentation de nombres
> réels : 0.1, 0.25 ou 1/3.
>
> Commentaire : 0.2 + 0.1 n’est pas égal à 0.3.  Il faut éviter de tester
> l’égalité de deux flottants.  Aucune connaissance précise de la norme
> IEEE-754 n’est exigible.


Un nombre flottant n de type `float` s'écrit sous la forme `n = (-1)^s × b^p × m`, où s vaut soit 0 soit 1 (le signe), b vaut soit 2 soit 10 (la base) et m, appelée la mantisse, dont on peut considérer qu'il s'agit d'un nombre entier.
Ce n'est pas tout à fait vrai dans la norme IEEE-754 mais, dans le cadre de cette norme, on peut néanmoins se ramener à ce cas-là.

L'intérêt d'une telle notation est qu'elle permet de représenter avec une même
précision aussi bien des très petits nombres que de très grands nombres.
Cependant on ne peut représenter que des nombres rationnels, mais pas tous.

Par exemple, en faisant le choix de la base 10,  *`b=10`* :
* *`0,1 = (-1)^0× 10^(-1)× 1`*
* *`0,25 = (-1)^0× 10^(-2)× 25`*
* *`1/3 = (-1)^0× 10^(-beaucoup)× 33333.....`*
* *`0,0000421 = (-1)^0× 10^(-7)× 421`*
* *`-421000 = (-1)^1× 10^(3)× 421`*

Mais lorsque la représentation se fait sur ordinateur, il est plus aisé d'avoir une base *`b=2`*.
En base 2 le nombre 1,110001<sub>2</sub> est *`1+1/2+1/4+1/64`*.
Voici quelques valeurs pour les puissances de 2 négatives :

| *`x`* | *`2^(-x)`*   |
|-------|--------------|
| 1     | 0.5          |
| 2     | 0.25         |
| 3     | 0.125        |
| 4     | 0.0625       |
| 5     | 0.03125      |
| 6     | 0.015625     |
| 7     | 0.0078125    |
| 8     | 0.00390625   |
| 9     | 0.001953125  |
| 10    | 0.0009765625 |

Dans ce cas, on a :

* *`0,25 = (-1)^0× 2^{-2}× 1`*    

* *`0,1 = (-1)^0× 2^{-4}× 1,6`*. Or `1,6 = 1+1/2+1/16+1/32+1/256+1/512+....`.     
  Ainsi, de la même manière qu'il n'est pas possible de représenter 1/3 de manière exacte avec *`b=10`*, on ne pourra pas
  représenter *`0,1`* de manière exacte avec *`b=2`*


**Attention :** Les calculs sur les nombres flottants ne sont donc pas
exacts. Il est parfois nécessaire d'approximer la valeur à représenter.  Il ne
faut **jamais** tester une égalité entre deux nombre flottants mais utiliser
une marge d'erreur relative.

**Attention :** Il ne faut pas se fier à l'affichage de Python (ou d'un autre
langage) qui n'affiche pas toutes les décimales stockées du nombre flottant.
On peut cependant accéder à plus de décimales en utilisant par exemple les
options de formattage de `format`. Attention aux yeux !
```python
>>> .1
0.1
>>> .25
0.25
>>> '{:.40f}'.format(.1)
'0.1000000000000000055511151231257827021182'
>>> '{:.40f}'.format(.2)
'0.2000000000000000111022302462515654042363'
>>> '{:.40f}'.format(.25)
'0.2500000000000000000000000000000000000000'
>>> '{:.40f}'.format(.3)
'0.2999999999999999888977697537484345957637'
>>> '{:.40f}'.format(.05)
'0.0500000000000000027755575615628913510591'
>>> .1 + .2 == .3
False
>>> .1 + .1 + .1 == .3
False
>>> .25 + .05 == .3
True
```

```python
>>> 0.2+0.1
0.30000000000000004
```

La **norme IEEE754** (notion présentée mais non exigible) définit précisément le codage des "nombres en virgule flottante". On représente un nombre par un signe s, une mantisse m et un exposant p dans la base b selon : 
`n = (-1)^s × b^p × m` avec m=1,... c'est-à-dire 1< m <=2.

Sur 64 bits, la règle est la suivante :
- un bit est réservé pour le signe, 0 pour le signe + et 1 pour le signe -
- 11 bits (2<sup>11</sup>=2048) pour l'exposant décalé e qui vaut p+1023 avec la condition -1022≤p≤1023, donc 1≤e≤2046 (les valeurs 0 et 2047 sont réservées pour coder par exemple -∞ ou +∞)
- 52 bits pour la mantisse tronquée qui vaut m'=m-1 avec la condition 1≤m<2.
Ces trois parties sont codées en binaire et concaténées pour former un nombre de 64 bits (1+11+52).

Par exemple, codons le réel - 0,375.
On note que 0,375=1,5×2<sup>-2</sup> ce qui permet d'avoir une mantisse comprise entre 1 et 2. On réalise donc la concaténation de '1' pour le signe, du code de -2 + 1023 = 1021 soit '011 1111 1101' sur 11 bits (on le trouve en faisant `bin(1021)`), la mantisse 1,5 s'écrit 1,1 en binaire et on ne garde que la partie décimale 1 et on complète avec cinquante et un 0.
Au final, le codage de - 0,375 est 1 011 1111 1101 1000.......0

Codons maintenant le réel 20. Il nous faut une mantisse comprise entre 1 et 2 et une puissance de 2.   
20=16×1,25=2<sup>4</sup>×1,25. On réalise donc la concaténantion de '0' pour le signe, du code de 4 + 1023 = 1027 soit '10000000011' sur 11 bits (on le trouve en faisant `bin(1027)`), la mantisse 1,25 s'écrit 1,01 en binaire et on ne garde que la partie décimale 01 et on complète avec cinquante 0.
Au final, le codage de 20 est 0100000000110100.....0


# Valeurs, opérateurs et expressions booléennes

> Attendu : Dresser la table d’une expression booléenne.
>
> Commentaires : Le ou exclusif (xor) est évoqué.  Quelques applications
> directes comme l’addition binaire sont présentées.  L’attention des élèves est
> attirée sur le caractère séquentiel de certains opérateurs booléens.


Table de vérité de ET (AND)

```python
>>> True and True
True
>>> True and False
False
>>> False and False
False
```

Table de vérité de OU (OR)

```python
>>> True or True
True
>>> True or False
True
>>> False or False
False
```



> Exemple 1 : 

```python
>>> True or (True and False)
True
```


Table d'une expression booléenne avec *`n`* variables : *`2^n`* cas à évaluer.

> Exemple 2 : recherchons la table de vérité de  *`(a ∨ b) ∧ c`* (∨ : OU ; ∧ : ET)


| a | b | c | *`(a ∨ b)`* | *`(a ∨ b) ∧ c`* |
|---|---|---|---------------|-------------------------|
| 0 | 0 | 0 | 0             | 0                       |
| 0 | 0 | 1 | 0             | 0                       |
| 0 | 1 | 0 | 1             | 0                       |
| 0 | 1 | 1 | 1             | 1                       |
| 1 | 0 | 0 | 1             | 0                       |
| 1 | 0 | 1 | 1             | 1                       |
| 1 | 1 | 0 | 1             | 0                       |
| 1 | 1 | 1 | 1             | 1                       |

 

### Exemples d'application

#### 1) L'opérateur ET 
Il permet par exemple de créer des masques afin de ne conserver que certains
bits d'une valeur.

#### 2) Parité d'un nombre

Un entier naturel pair *`n`* a son bit de poids faible à 0. Il suffit donc de
consulter ce bit pour connaître la parité du nombre.

`n ∧ 1` permet de ne conserver que le bit de poids faible (tous les autres bits sont mis à 0).
Si le résultat est 1 alors le nombre est impair, sinon le nombre est pair.

### 3) Signe d'un nombre représenté en complément à 2

On a vu que dans la représentation en complément à 2, le bit de poids fort
désigne le bit de signe.  Si on suppose un nombre entier *`n`* représenté sur
*`p`* bits, on peut isoler le bit de poids fort avec un ET également :`n
∧ (2^{p-1})`. Si le résultat est 0, le nombre est positif sinon il est
négatif.

### 4) Caractère séquentiel des expressions booléennes

Les expressions booléennes sont évaluées de manière paresseuses : dès que le résultat est connu l'évaluation est stoppée.

Par exemple avec `a ET b ET c`. Si `a` est faux, `b` et `c` ne sont même pas
évaluées puisque le résultat sera nécessairement faux.

L'ordre dans lequel les expressions sont écrites est donc important. Par
exemple il faut d'abord vérifier qu'une clé existe dans un dictionnaire pour
ensuite vérifier sa valeur.

Si `d` est un dictionnaire, on peut faire :
```python
if 'cle' in d and d['cle'] == 2:
```
Mais on **ne doit pas** faire (une exception sera levée dès que la clé n'existe pas) :
```python
if d['cle'] == 2 and 'cle' in d:
```

### 5) XOR

Le ou-exclusif ne pose généralement pas de problème car son interprétation
correspond à l'interprétation intuitive du OU en français « *resto chinois ou
italien* ? ».  Le résultat d'un ou-exclusif entre deux valeurs n'est vrai que
si exactement une des deux valeurs est vraie.

### 6) Et les opérateurs bit-à-bit ?

Les opérateurs bit-à-bit incluent les opérateurs booléens déjà mentionnés mais
également les décalages de bits.

- *Décalage à droite* : le décalage à droite de *`k`* positions d'un entier
*`n`*, noté *`n >> k`*, est l'entier dont l'écriture binaire est obtenue en
supprimant les *`k`* bits de poids faibles de l'écriture binaire de *`n`*.

Exemple :

```python
>>> 11 >> 2
2
```
En effet, 11 s'écrit en binaire 1011, le décalage vers la droite deux fois de suite donne 10 dont la valeur décimale vaut 2.

- *Décalage à gauche* : le décalage à gauche de *`k`* positions d'un entier
*`n`*, noté *`n\ll k`*, est l'entier dont l'écriture binaire est obtenue en
ajoutant *`k`* bits nuls à droite de l'écriture binaire de *`n`*.

Exemple :

```python
>>> 1<<2
4
```
En effet, 1 s'écrit en binaire 1, le décalage vers la gauche deux fois de suite donne 100 dont la valeur décimale vaut 4 ; la valeur décimale de départ a été multipliée par 2<sup>2</sup>.


En Python, décaler un nombre entier positif d'un bit vers la gauche revient à
le multiplier par 2, et ainsi le décaler de *`k`* bits, revient à le multiplier par
*`2^k`*.  
Si le nombre entier est représenté sur un nombre fixe de bits (ce
qui n'est pas le cas de Python), décaler de *`k`* bits vers la gauche va
également faire perdre les *`k`* bits qui étaient originellement de poids
fort.



Le décalage de bit aurait été utile dans l'exemple 3 de
détermination du bit de signe pour un entier n qui s'écrit sur p bits. Avec le
décalage à droite on peut faire *`n >> (p-1)`* et dans ce cas le
résultat est soit 0 soit 1 pour nous indiquer le signe.

# Représentation d'un texte en machine

> Attendu : Identifier l’intérêt des différents systèmes d’encodage.
> Convertir un fichier texte dans différents formats d’encodage.
>
> Commentaires : Aucune connaissance précise des normes d’encodage n’est
> exigible.

## Pourquoi différents encodages de caractères ?

### ASCII
Le code ASCII (*American Standard Code for Information Interchange*) est la première
norme largement utilisée pour encoder des caractères.  Comme son nom l'indique
cette norme est américaine et elle sert pour l'échange d'information dans cette langue ;  elle n'**inclue donc pas les lettres  
accentuées** mais comme le tableau ci-dessous l'indique, des chiffres, opérateurs mathématiques, caractères de
ponctuation ou de délimitation et certains caractères spéciaux.

Voici les caractères de la table ASCII (les 33 premiers, et le dernier, ne sont pas imprimables) :

|     | `0`     | `1`   | `2`   | `3`   | `4`   | `5`   | `6`   | `7`   | `8`   | `9`  | `A`   | `B`   | `C`  | `D`  | `E`  | `F`  |
|-----|---------|-------|-------|-------|-------|-------|-------|-------|-------|------|-------|-------|------|------|------|------|
| `0` | `NUL`   | `SOH` | `STX` | `ETX` | `EOT` | `ENQ` | `ACK` | `BEL` | `BS`  | `HT` | `LF`  | `VT`  | `FF` | `CR` | `SO` | `SI` |
| `1` | `DLE`   | `DC1` | `DC2` | `DC3` | `DC4` | `NAK` | `SYN` | `ETB` | `CAN` | `EM` | `SUB` | `ESC` | `FS` | `GS` | `RS` | `US` |
| `2` | `ESP`   | `!`   | `"`   | `#`   | `*`   | `%`   | `&`   | `'`   | `(`   | `)`  | `*`   | `+`   | `,`  | `-`  | `.`  | `/`  |
| `3` | `0`     | `1`   | `2`   | `3`   | `4`   | `5`   | `6`   | `7`   | `8`   | `9`  | `:`   | `;`   | `<`  | `=`  | `>`  | `?`  |
| `4` | `@`     | `A`   | `B`   | `C`   | `D`   | `E`   | `F`   | `G`   | `H`   | `I`  | `J`   | `K`   | `L`  | `M`  | `N`  | `O`  |
| `5` | `P`     | `Q`   | `R`   | `S`   | `T`   | `U`   | `V`   | `W`   | `X`   | `Y`  | `Z`   | `[`   | `\`  | `]`  | `^`  | `_`  |
| `6` | `accent grave ` | `a`   | `b`   | `c`   | `d`   | `e`   | `f`   | `g`   | `h`   | `i`  | `j`   | `k`   | `l`  | `m`  | `n`  | `o`  |
| `7` | `p`     | `q`   | `r`   | `s`   | `t`   | `u`   | `v`   | `w`   | `x`   | `y`  | `z`   | `{`   | `|`  | `}`  | `~`  | `DEL`|

128 caractères composent la table ASCII, ce qui permet de les représenter sur
7 bits (en pratique ils sont donnés sur 8 bits afin d'occuper un octet complet).

Pour obtenir le code ASCII d'un caractère et inversement : 

```python
>>> ord("k")
107
>>> chr(52)
'4'
```


### ISO-8859-1

Par la suite d'autres encodages ont vu le jour afin de pallier les limites de
l'ASCII.  L'ISO-8859-1 (aussi appelé *Latin-1*), pour l'Europe occidentale, a
vu le jour en 1986.  Celui-ci comble les manques pour la plupart des langues
d'Europe occidentale.  Pour le français il manque cependant le œ, le Œ et le Ÿ
et, bien entendu, le symbole €.  L'encodage en ISO-8859-1 utilise 8 bits, les
128 premières valeurs de l'ISO-8859-1 sont identiques à l'ASCII, ce qui assure
une compatibilité avec cet encodage.

Voici la table des caractères ISO-8859-1 :

![](assets/iso-8859-1.png)

### UTF-8

À nouveau le codage ISO-8859-1 (et les autres codages de la famille ISO-8859)
présentent des limites.  Dans les années 1990, le projet Unicode de codage
unifié de tous les alphabets est né. Différents codages sont utilisés pour
représenter des caractères Unicode (UTF-8, UTF-16, UTF-32\dots). Ici nous nous
concentrons sur l'UTF-8

Le codage UTF-8 est un codage de longueur variable. Certains caractères sont
codés sur un seul octet, ce sont les 128 caractères du codage ASCII.  Les
autres caractères peuvent être codés sur 2, 3 ou 4 octets.  Ainsi l'UTF-8
permet en théorie de représenter *`2^{21} = 2\,097\,152`* caractères
différents, en réalité un peu moins. Il y a actuellement environ une centaine
de milliers de caractères Unicode (incluant les [caractères des langues
vivantes ou
mortes](https://unicode.org/cldr/charts/latest/supplemental/languages_and_scripts.html)
et également de [nombreux emojis
indispensables](https://unicode.org/emoji/charts-12.0/full-emoji-list.html)
😇)

Les caractères en UTF-8 doivent avoir une forme particulière décrite dans la
table ci-dessous :

| Nbre octets codant | Format de la représentation binaire   |
|--------------------|---------------------------------------|
| 1                  | `0xxxxxxx`                            |
| 2                  | `110xxxxx 10xxxxxx`                   |
| 3                  | `1110xxxx 10xxxxxx 10xxxxxx`          |
| 4                  | `11110xxx 10xxxxxx 10xxxxxx 10xxxxxx` |

L'encodage UTF-8 est lui aussi compatible avec l'ASCII. En revanche ISO-8859-1
et UTF-8 sont incompatibles entre eux pouvant conduire à ce genre de problèmes :

![](assets/martine.jpg)

Aller plus loin : Plus d'informations sur ces différents aspects sont disponibles [dans chapitre 1 du polycopié du cours de Codage de l'information donné en L2 informatique](assets/poly.pdf).
