# Exercices : représentation des données 

## Exercice 1

Les nombres sont écrits en binaire.
1. Calculer la somme 100110 + 001101 en posant l'addition.
2. Traduire le calcul en décimal.
3. Vérifier dans la console en utilisant la notation en base 2 : 0b......

## Exercice 2

1. Déterminer à la main l'écriture hexadécimale (en base 16) du nombre qui s'écrit 172 en base dix.
2. Donner l'écriture binaire du mot hexadécimal 'B3'.
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
    (2) Donne la représentation binaire du nombre entier décimal n
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
    (3) Donne la représentation hexadécimale du nombre entier décimal n
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
    (4) Donne la valeur décimale du mot hexadécimal
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
(2) Les bits du mot binaire sont à multiplier par les puissances de 2 croissantes de droite à gauche à partir de 0 ; on fera un boucle `for` en passant en revue les caractères du mot binaire.  
(3) Réutiliser (1) en introduisant `liste_remplaçant=["a","b","c","d","e"]`.
(4) Réutiliser (2) en introduisant `liste_remplaçant=["a","b","c","d","e"]` et utiliser liste_remplaçant.index() pour trouver l'indice de position du caractère dans cette liste.  
(5) Rajouter au préalable des 0 au début du mot pour qu'il puisse être découpé en parties de 4 ; convertir chaque partie (utiliser slice[ : ]) en décimal, puis en binaire.  
(6) Utiliser `conversion_decimal_binaire(conversion_hexadecimal_decimal(mot))`







## Exercice 4

1. Comment code-t-on le nombre 9 sur 5 bits ?
2. Comment code-t-on le nombre -15 sur 5 bits ? Réaliser les deux méthodes et vérifier.
3. Si on utilise p bits pour coder les entiers relatifs, combien de nombres peut-on coder et lesquels ?
4. Comment se code - 56 sur le nombre de bit nécessaire à sa représentation ?

## Exercice 5

Écrire le nombre 3,625 en binaire.
Proposer deux méthodes :
- une méthode utilisant la décomposition en puissances négatives de 2
- une méthode utilisant le décalage à gauche suite à la multiplication par 2

## Exercice 6

Les flottants sont codés suivant la norme IEEE 754 sur 64 bits, soit 1 bit pour le signe, 11 bits pour l'exposant décalé et 52 bits pour la mantisse tronquée (cf.cours).
1. Comment est codé le nombre - 4.5 ?
2. Quel est le nombre réel codé par 1011 1111 1110 1000 0000 ... 0000 ?

Pour vérifier, utiliser le [convertisseur](https://www.binaryconvert.com/result_double.html?decimal=050048)
## Exercice 7

Vérifier, à l'aide d'une table de vérités, l'égalité suivante entre expressions booléennes : 

`a xor b = (a and not(b)) or (not(a) and b)`.

Rappel : XOR is a binary operation, it stands for "exclusive or", that is to say the resulting bit evaluates to one if **only exactly one** of the bits is set.

This is its function table:

a | b | a xor b
--|---|------
0 | 0 | 0
0 | 1 | 1
1 | 0 | 1
1 | 1 | 0


## Exercice 8

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

## Exercice 9 

On considère le code python suivant qui permet de créer un fichier HTML pour obtenir une page contenant les caractères "ééé".

```python
f=open('page.html','w')##ouverture du fichier
ch="""<!DOCTYPE html>
<html>
    <head>
    <meta charset="utf-8"/>
    </head>
    <body>
    ééé
    </body>
</html>"""
f.write(ch)##écriture du fichier
f.close()##fermeture du fichier 
```

Voir l'effet en modifiant l'encodage de la page html utf-8 ou ISO-8859-1.

## Exercice 10

Compléter le code suivant :

**Indications** :

```python
>>> str(10)#on transforme le nombre en chaîne de caractères
'10'
>>> int('10')#on transforme la chaîne de caractères en nombre entier
10
>>> "A"+str(2)#on concatène les chaînes de caractères pour obtenir une plus longue chaîne
'A2'
>>> liste=["A","B","C","D","E","F"]
>>> len(liste)#donne la longueur de liste
6
>>> liste[2]#on prend l'élement en position 2; les indices de position commencent à 0 jusque len(liste)-1.
'C'
>>> liste.index("D")#on demande l'indice de position de l'élément dans la liste (ou dans le tuple ou dans la chaîne)
3
>>> "E" in liste#permet de savoir si un caractère est dans une liste
True
>>> code="70F"
>>> code.index("F")#une chaîne de caractère fonctionne comme un tuple
2
>>> "F" in code#une chaîne de caractère fonctionne comme un tuple
True
>>> code[::-1]#on retourne la chaîne de caractères
'F07'
>>> for caractere in code:#on parcourt les éléments de la chaîne de caractères
    print(caractere)#on les affiche
    
7
0
F
```

 ```python
 def conversion_decimal_hexadecimal(n):
    """
    Renvoie la conversion en hexadécimal d'un nombre décimal
    param : n : int
    return : str
    >>> conversion_decimal_hexadecimal(1807)
    '70F'
    """
    resultat=""
    liste=["A","B","C","D","E","F"]


def conversion_hexadecimal_decimal(code):
    """
    Renvoie la conversion en décimal du code hexadécimal
    param : code : str
    return : int
    >>> conversion_hexadecimal_decimal('70F')
    1807
    """
    resultat=0
    i=0
    liste=["A","B","C","D","E","F"]


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose = True)  
```

