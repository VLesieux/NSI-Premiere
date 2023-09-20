# Exercices : Représentation des données 

## Exercice 1

Les nombres sont écrits en binaire.
1. Calculer la somme 100110 + 001101 en posant l'addition.
2. Traduire le calcul en décimal.
3. Vérifier dans la console en utilisant la notation en base 2 : 0b......

## Exercice 2

1. Déterminer à la main l'écriture hexadécimale (en base 16) du nombre qui s'écrit 172 en base dix.
2. Donner l'écriture binaire du mot hexadécimal B3.
3. Vérifier dans la console en utilisant la notation en base 16 : 0x...... puis bin()

## Exercice 3

Compléter les fonctions suivantes

```Python
def conversion_decimal_binaire(n):
    """
    (1) Donne la représentation binaire du nombre entier décimal n
    param : n : int
    return : str
    >>> conversion_decimal_binaire(18)
    '10010'
    >>> conversion_decimal_binaire(141)
    '10001101'
    """
	pass        

def conversion_binaire_decimal(mot):
    """
    (2) Donne la valeur décimale d'un mot binaire
    param : n : int
    return : str
    >>> conversion_binaire_decimal('110011')
    51
    >>> conversion_binaire_decimal('1010101')
    85
    """
	pass 

def conversion_decimal_hexadecimal(n):
    """
    (3) Donne la représentation hexadécimale d'un nombre décimal n
    param : n : int
    return : str
    >>> conversion_decimal_hexadecimal(18)
    '12'
    >>> conversion_decimal_hexadecimal(141)
    '8d'
    """
	pass 


def conversion_hexadecimal_decimal(mot):
    """
    (4) Donne la valeur décimale d'un mot hexadécimal
    param : mot : str
    return : int
    >>> conversion_hexadecimal_decimal('ae')
    174
    >>> conversion_hexadecimal_decimal('34a')
    842
    """
	pass 

def conversion_binaire_hexadecimal(mot):
    """
    (5) Donne la représentation hexadécimale d'un mot binaire
    param: str
    return : str
    >>> conversion_binaire_hexadecimal('101101001')
    '169'
    >>> conversion_binaire_hexadecimal('110111')
    '37'
    """
	pass 

def conversion_hexadecimal_binaire(mot):
    """
    (6) Donne la représentation binaire d'un mot hexadécimal
    param: str
    return : str
    >>> conversion_hexadecimal_binaire('169')
    '101101001'
    >>> conversion_hexadecimal_binaire('37')
    '110111'
    """
    pass 
    

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose = True) 
```

**Indications:**

(1) Écrire l'algorithme de divisions successives par 2 aussi longtemps que le quotient est strictement positif ; on ne connaît pas le nombre de tour de boucle, mais on peut écrire une boucle conditionnelle en utilisant `while`.    

(2) Les bits du mot binaire sont à multiplier par les puissances de 2 croissantes de droite à gauche à partir de 0 ; on fera un boucle `for` en passant en revue les caractères du mot binaire. Penser à transformer une chaîne de caractères formée de nombres en nombre avec `int()`.   

(3) Réutiliser (1) en introduisant `liste_remplaçant=["a","b","c","d","e"]`.  

(4) Réutiliser (2) en introduisant `liste_remplaçant=["a","b","c","d","e"]` et utiliser liste_remplaçant.index() pour trouver l'indice de position du caractère dans cette liste ; il suffira de lui ajouter 10 pour trouver la valeur décimale de ce caractère si le caractère appartient à cette liste.

(5) Rajouter au préalable des 0 au début du mot pour qu'il puisse être découpé en parties de 4 bits ; convertir chaque partie (utiliser slice[ : ]) en décimal, puis en binaire.    

(6) Utiliser `conversion_decimal_binaire(conversion_hexadecimal_decimal(mot))`


## Exercice 4

1. Comment code-t-on le nombre 9 sur 5 bits ?
2. Comment code-t-on le nombre -15 sur 5 bits ? Réaliser les deux méthodes et vérifier.
3. Comment se code - 56 sur le nombre de bit nécessaire à sa représentation ?

## Exercice 5

Écrire le nombre 3,625 en binaire.
Proposer deux méthodes :  
- une méthode utilisant la décomposition en puissances négatives de 2.  
- une méthode utilisant le décalage à gauche suite à la multiplication par 2

## Exercice 6

Les flottants sont codés suivant la norme IEEE 754 sur 64 bits, soit 1 bit pour le signe, 11 bits pour l'exposant décalé et 52 bits pour la mantisse tronquée (cf.cours).
1. Comment est codé le nombre - 4.5 ?  
2. Quel est le nombre réel codé par 1011 1111 1110 1000 0000 ... 0000 ?

Pour vérifier, utiliser le [convertisseur](https://www.binaryconvert.com/result_double.html?decimal=050048)


## Exercice 7

Lors du premier conflit États-Unis/Irak en 1991, les américains disposaient d'antimissiles *patriot* pour intercepter les missiles irakiens *scud*. Les *patriot* disposaient d'une horloge interne émettant un signal tous les 0.1 seconde. Le temps écoulé était obtenu en multipliant 0.1 par le nombre de signaux d'horloge reçus. 

Le microcontroleur de l'antimissile *patriot* stocke la valeur 1/10 en ne conservant que 23 bits pour la partie décimale (codage en virgule fixe).

On observe que :

```Python
0.1=1.6*0.0625 soit :  
0.1=1.6*2^(-4) ou :  
0.1=1*2^(-4)+(0.5+0.1)*2^(-4) ou :  
0.1=1*2^(-4)+(2^(-1)+0.1)*2^(-4) ou :  
0.1=1*2^(-4)+2^(-5)+0.1*2^(-4) ou :  
en remplaçant le 0.1 du membre de droite par l'expression trouvée :

0.1=1*2^(-4)+2^(-5)+[1*2^(-4)+2^(-5)+0.1*2^(-4)]*2^(-4)

soit : 

0.1=1*2^(-4)+1*2^(-5)+1*2^(-8)+1*2^(-9)+0.1*2^(-8)

```
et on peut recommencer, on a affaire à une **écriture infinie et périodique**.

Ainsi: 0.1<sub>10</sub>=0.000110011001100110011001100110...<sub>2</sub>

1. Quelle est, en base 10, la valeur exacte qui est effectivement codée à la place de 1/10 ?
3. Quelle est l'erreur approximative commise sur la représentation de 1/10 ?
4. En tenant compte de cette erreur, quel est le décalage d'horloge du *patriot* par rapport à l'heure locale au bout de 100 h ?
5. Sachant que le missile se déplace à une vitesse d'environ 1676 m.s<sup>-1</sup>, à quelle erreur de position en mètre correspond le décalage d'horloge après 100h de fonctionnemt.
6. Conclure, sachant que pour atteindre sa cible, un *patriot* doit l'approcher à moins de 500 m.


## Exercice 8

Vérifier, à l'aide d'une table de vérités, l'égalité suivante entre expressions booléennes : 

`a xor b = (a and not(b)) or (not(a) and b)`.

Rappel : XOR is a binary operation, it stands for "exclusive or", that is to say the resulting bit evaluates to one if **only exactly one** of the bits is set to 1.

This is its function table:

a | b | a xor b
--|---|------
0 | 0 | 0
0 | 1 | 1
1 | 0 | 1
1 | 1 | 0


## Exercice 9

Comparer les résultats renvoyés par les trois fonctions suivantes, où x et y sont de type quelconque, sans les programmer en machine :
```python
def compare1(x,y):
    if x and y :
        return True
    else:
        return False
    
def compare2(x,y):
    return x and y

def compare3(x,y):
    return not(not x or not y)
```

## Exercice 10

Les [couleurs](http://vfsilesieux.free.fr/colours.html) sont souvent exprimées en code hexadécimal. 
Par exemple la couleur verte pomme peut être codée par #C7E180 ; les codes C7, E1 et 80 représentent respectivement les valeurs hexadécimales des niveaux de rouge, de vert et de bleu. L'écriture binaire en 3 octets est aussi possible :
11000111 11100001 10000000 ; ce qui correspond aux niveaux : 199, 225, 128.


Montrer que l'on peut utiliser le masque 0xFF pour extraire le niveau de bleu selon :

```python
>>> code=0xC7E180
>>> mask=0xFF
>>> hex(code & mask)
'0x80'
```
Montrer que l'on peut extraire le niveau de rouge selon :

```python
>>> code=0xC7E180
>>> mask=0xFF<<8
>>> hex((code & mask)>>8)
'0xe1'
```

Montrer comment extraire le niveau de vert avec ce masque.

