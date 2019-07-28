# Programmation en Python : généralités

Quelques éléments historiques : le langage Python a été créé en 1989 par le développeur néerlandais Guido van Rossum né en 1956 à Haarlem près d'Amsterdam. Il a fait ses études de mathématiques à l’université d'Amsterdam, obtenant son master en 1982. Il fit partie des développeurs du langage ABC (successeur du BASIC). En 1989, profitant d’une semaine de vacances durant les fêtes de Noël, il utilise son ordinateur personnel pour écrire la première version du langage. Fan de la série télévisée _Monty Python's Flying Circus_ créée par la BBC, il décide avec humour de baptiser ce projet Python. En 1991 sort la première version publique du langage. En 2002, il a reçu le prix pour le développement du logiciel libre décerné par la FSF (Free Sofware Foundation) pour récompenser son travail. Fin 2005, il a été engagé par Google pour travailler sur Python. En décembre 2012, il quitte Google pour rejoindre Dropbox. Le 12 juillet 2018, il annonce son retrait en tant que Benevolent Dictator for Life du projet Python.   

Un programme est composé de **séquences** : des **instructions** exécutées les unes après les autres dans l'ordre où elles sont écrites, de définitions de **variables** et de **fonctions**, d'**instructions conditionnelles**, de **bloucles**, utilisant des **expressions**, en particulier des **appels de fonctions**.


## Variables ; affectation ; expression ; instruction 

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
>>> chaine+" plat"#ajout de chaînes à la suite l'une de l'autre : concaténation
'poisson plat'
>>> len(chaine)#longueur de la chaîne de caractères
7
```


- les **types composés** : `tuple` : p-uplet, `list` : liste ou tableau et `dict` : dictionnaire. De nombreuses opérations peuvent être exécutés sur ces types composés. 


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

On prendra soin de respecter l'**indentation**, élément important de la **syntaxe** de Python, qui est un décalage vers la droite qui permet d'identifier un **bloc** d'instructions.

Exemples :

```Python
#Une seule alternative

if n%2==0:##ici notation double égal pour distinguer l'instruction conditionnelle de l'affectation
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


