# Programmation en Python : généralités

Quelques éléments d'histoire : le langage Python a été créé en 1989 par le développeur néerlandais Guido van Rossum né en 1956 à Haarlem près d'Amsterdam. Il a fait ses études de mathématiques à l’université d'Amsterdam, obtenant son master en 1982. Il fit partie des développeurs du langage ABC (successeur du BASIC). En 1989, profitant d’une semaine de vacances durant les fêtes de Noël, il utilise son ordinateur personnel pour écrire la première version du langage. Fan de la série télévisée _Monty Python's Flying Circus_ créée par la BBC, il décide avec humour de baptiser ce projet Python. En **1991** sort la première version publique du langage. En 2002, il a reçu le prix pour le développement du logiciel libre décerné par la FSF (Free Sofware Foundation) pour récompenser son travail. Fin 2005, il a été engagé par Google pour travailler sur Python. En décembre 2012, il quitte Google pour rejoindre Dropbox. Le 12 juillet 2018, il annonce son retrait en tant que Benevolent Dictator for Life du projet Python.   

Un programme est composé de **séquences** : des **instructions** exécutées les unes après les autres dans l'ordre où elles sont écrites, de définitions de **variables** et de **fonctions**, d'**instructions conditionnelles**, de **bloucles conditionnelles**  ou **non conditionnelles**, utilisant des **expressions**, en particulier des **appels de fonctions**.   
Une instruction est une commande que doit exécuter la machine tandis qu'une expression est un valeur renvoyée généralement par une fonction suite à une combinaison d'opérations.


## Variables ; affectation

Les **données** utilisées par les programmes sont stockées dans des **variables**, ce qui se fait en réalisant une **affectation** en utilisant l'**opérateur d'affectation** `=` . 

Exemple :

```Python
# On affecte aux variables x, y et z des valeurs de données
>>> x=3
>>> y=4
>>> z=x+y
# x+y est ici une expression, sa valeur est le fruit d'une combinaison des variables x et y. 
>>> z
7
```

On peut aussi réaliser des **affectations multiples** pour remplacer une **séquence d'instructions** par une instruction unique.

```Python
>>> x,y,z=3,4,x+y
# Une instruction unique en remplace trois
>>> z
7
```

En fait chaque variable possède un nom ou identificateur et possède une **adresse en mémoire** donnée ici en décimal que l'on peut obtenir grâce à `id(object)`.

```Python
>>> id(x)
4460309648
>>> id(y)
4460309680
>>> id(z)
4460309776
```

## Types 

Le type d'une variable est l'ensemble des valeurs qui peuvent être affectées à cette variable.

On distingue :   
- les **types simples** : `int` (les nombres entiers), `bool` (les valeurs booléennes True ou False), `float` (nombres réels), `str` (abréviation de string ou chaîne de caractères écrite entre des guillemets " " ou des apostrophes ' '), `None` qui n'a pas de valeur


Opérations sur les types simples

```Python
>>> 1+2#addition
3
>>> 1-2#soustraction
-1
>>> 1*2#multiplication
2
>>> 1/2#division
0.5
>>> 1//2#division entière : renvoit le quotient entier de la division
0
>>> 1%2#reste de la division
1

#existence de raccourcis d'écriture
>>> x=5
>>> x+=1
>>> x
6
>>> x*=2
>>> x
12

#opérations sur les chaînes de caractères
>>> chaine="poisson"
>>> chaine[1]#une chaîne est indicée à partir de 0 de gauche à droite
'o'
>>> chaine[-2]#on peut indicer de droite à gauche avec des indices négatifs
'o'
>>> chaine[2:4]#on réalise une découpe la chaîne (slice) entre 2 inclus et 4 non inclus
'is'
>>> chaine+" plat"#ajout de chaînes à la suite l'une de l'autre : concaténation à l'aide de l'opérateur +
#l'opérateur - ne s'applique pas sur les chaînes de caractères
'poisson plat'
>>> len(chaine)#longueur de la chaîne de caractères
7
>>> chaine*2
'poissonpoisson'
```


- les **types composés** : `tuple` : p-uplet, `list` : liste ou tableau et `dict` : dictionnaire. De nombreuses opérations peuvent être exécutées sur ces types composés. 


Présentation rapide des types composés

```Python
>>> p_uplet=(1,"a")# les tuples sont des éléments séparés par des virgules entre des parenthèses
>>> len(p_uplet)#pour obtenir la longueur du tuple
2
>>> p_uplet[0]#les tuples sont indicés, le premier indice est 0
1
>>> p_uplet[1]
'a'
>>> p_uplet[1]='b'
Traceback (most recent call last):
  File "<pyshell>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment#les tuples sont immutables, on ne peut pas changer la valeur d'un élément
>>> p_uplet[2]='c'
Traceback (most recent call last):
  File "<pyshell>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment#les tuples sont immutables, on ne peut pas ajouter un élément
____________________________________

>>> liste=[1,"a"]# les listes sont des éléments séparés par des virgules entre des crochets
>>> len(liste)#la longueur de la liste
2
>>> liste[0]
1
>>> liste[1]
'a'
>>> liste[1]="b"
>>> liste
[1, 'b']#les listes sont mutables
>>> liste[2]="c"
Traceback (most recent call last):
  File "<pyshell>", line 1, in <module>
IndexError: list assignment index out of range#une erreur qui signifie qu'on ne peut pas accéder à un élément en dehors de la taille de la liste
>>> liste.append("c")#on utilise la méthode append pour ajouter un élément à la liste
>>> liste
[1, 'b', 'c']
>>> nouvelle_liste=[liste,'d']#une liste peut contenir une liste
>>> nouvelle_liste
[[1, 'b', 'c'], 'd']
>>> nouvelle_liste[0][1]#pour accéder à l'élément d'indice 1 de l'élément d'indice 0 de nouvelle_liste
'b'
>>> nouvelle_liste.pop()#renvoie le dernier élément de la liste et le supprime 
'd'
>>> nouvelle_liste
[[1, 'b', 'c']]
>>> 'b' in nouvelle_liste#pour savoir si un élément est dans une liste
False
>>> 'b' in nouvelle_liste[0]
True
>>> nouvelle_liste[0].index('b')#renvoie l'indice de position d'un élément dans une liste
1
____________________________________

>>> frequence={"do4":523.25,"la3":440}#dictionnaire clé-valeur : clé=nom de la note, valeur=fréquence en Hz à l'intérieur d'une accolade
>>> frequence["do4"]#on cherche la valeur associée à la clé
523.25
>>> frequence["mi4"]=659.26#ajout d'un couple clé-valeur au dictionnaire
>>> frequence
{'do4': 523.25, 'la3': 440, 'mi4': 659.26}
>>> len(frequence)#longueur du dictionnaire
3
```

## Instructions conditionnelles

On prendra soin de respecter l'**indentation**, élément important de la **syntaxe** de Python, qui est un décalage vers la droite qui permet d'identifier un **bloc** d'instructions. On utilise l'instruction conditionnelle `if`.

Exemples :

```Python
#Une seule alternative

if n%2==0:##ici la notation double égal représente une expression booléenne qui renvoie True ou False
    print("n est pair")
else:
    print("n est impair")

#Plusieurs alternatives

if age<10:
    print("enfant")
elif age>=10 and age<=18:
    print("adolescent")
elif age>19 and age<=70:
    print("adulte")
else:#else est toujours suivi immédiatement de deux points
    print("personne agée")
```

## Boucles conditionnelles et boucles non conditionnelles

Exemple de bloucle conditionnelle avec `while`:

```Python
i=0
while i<3:
    print("valeur de i :",i)
    i+=1
>>> 
valeur de i : 0
valeur de i : 1
valeur de i : 2
```

Exemple de bloucle non conditionnelle avec `for i in range(n)` qui produit **n** tours de boucle :

```Python
for i in range(3):#i prend 3 valeurs entières successives à partir de 0 jusque 2, 3 étant exclu
    print("valeur de i :",i)
>>> 
valeur de i : 0
valeur de i : 1
valeur de i : 2

for i in range(2,15,2):# i commence à 2 inclus jusque 15 exclu (attention !!) par pas de 2
    print("valeur de i :",i)
>>> 
valeur de i : 2
valeur de i : 4
valeur de i : 6
valeur de i : 8
valeur de i : 10
valeur de i : 12
valeur de i : 14
```

## Fonctions 

Exemple de fonction : 

```Python
def tranche_age(age):
    """
    cette fonction associe un qualificatif à une personne connaissant son âge
    : param age : int
    : return : string
    : CU: age est un nombre
    : Exemples :
    >>> tranche_age(13.5)
    'adolescent'
    >>> tranche_age(48)
    'adulte'
    """
    qualificatif=''
    if age<10:
        qualificatif='enfant'
    elif age>=10 and age<=18:
        qualificatif='adolescent'
    elif age>19 and age<=70:
        qualificatif='adulte'
    else:
        qualificatif='personne agée'
    return qualificatif
```
La partie entre les triples guillements est la **documentation** de la fonction ; elle permet d'avoir des informations sur une fonction que l'on peut retrouver dans le shell avec la fonction help. On y placera la **spécification** de la fonction, en précisant la nature des paramètres, ce que retourne la fonction, les conditions d'utilisation, on fournira également un ou plusieurs exemples.

```Python
>>> help(tranche_age)
Help on function tranche_age in module __main__:

tranche_age(age)
    cette fonction associe un qualificatif à une personne connaissant son âge
    : param age : int
    : return : string
    : CU: age est un nombre
    : Exemples :
    >>> tranche_age(13.5)
    'adolescent'
    >>> tranche_age(48)
    'adulte'
```

## Modules et bibliothèques

Exemple : On réalise un programme appelé max_deux_nombres.py dans lequel on a défini une fonction maximum_deux_nombres.

```Python
def maximum_deux_nombres(a,b):
    if a>b:
        return a
    else:
        return b
```

On réalise un deuxième programme max_trois_nombres.py qui importe le programme précédent comme module.  
On observe que pour utiliser la fonction définie dans le module, on l'appelle de la façon suivante : module.fonction

```Python
import max_deux_nombres

def maximum_trois_nombres(a,b,c):
    if max_deux_nombres.maximum_deux_nombres(a,b)<c:
        return c
    else:
        return max_deux_nombres.maximum_deux_nombres(a,b)
```
Une autre façon de procéder est la suivante ; on peut importer uniquement la fonction du module qui nous intéresse :

```Python
from max_deux_nombres import maximum_deux_nombres 

def maximum_trois_nombres(a,b,c):
    if maximum_deux_nombres(a,b)<c:
        return c
    else:
        return maximum_deux_nombres(a,b)
```
Les modules `math`, `random`, `turtle` sont des modules communément utilisés présents dans la bibliothèque standard de Python.  

Pour connaître le contenu du module math par exemple, utiliser `dir`(module) puis `help`(fonction) après avoir importé le module avec `import`(module) :

```Python
>>> import math
>>> dir(math)
['__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'ceil', 'copysign', 'cos', 'cosh', 'degrees', 'e', 'erf', 'erfc', 'exp', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 'pi', 'pow', 'radians', 'remainder', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'tau', 'trunc']

>>> help(math.floor)
Help on built-in function floor in module math:

floor(x, /)
    Return the floor of x as an Integral.
    
    This is the largest integer <= x. #L'expression math.floor(x) renvoie ainsi la partie entière de x
```
```Python
>>> import random
>>> dir(random)
['BPF', 'LOG4', 'NV_MAGICCONST', 'RECIP_BPF', 'Random', 'SG_MAGICCONST', 'SystemRandom', 'TWOPI', '_BuiltinMethodType', '_MethodType', '_Sequence', '_Set', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '_acos', '_bisect', '_ceil', '_cos', '_e', '_exp', '_inst', '_itertools', '_log', '_os', '_pi', '_random', '_sha512', '_sin', '_sqrt', '_test', '_test_generator', '_urandom', '_warn', 'betavariate', 'choice', 'choices', 'expovariate', 'gammavariate', 'gauss', 'getrandbits', 'getstate', 'lognormvariate', 'normalvariate', 'paretovariate', 'randint', 'random', 'randrange', 'sample', 'seed', 'setstate', 'shuffle', 'triangular', 'uniform', 'vonmisesvariate', 'weibullvariate']
>>> help(random.randint)
Help on method randint in module random:

randint(a, b) method of random.Random instance
    Return random integer in range [a, b], including both end points.
```

La bibliothèque Matplotlib est utilisée pour dessiner des courbes à partir de deux listes, les abscisses et les ordonnées. Elle contient le module pyplot à cet effet.

```Python
import matplotlib.pyplot as plt

def f(x):
    return x**2

x=[i*0.01 for i in range(101)]
y=[f(u) for u in x]
plt.plot(x,y)
plt.grid()
plt.show()
```
