# Exercices : représentation des données ; [solutions](https://drive.google.com/file/d/1COIunuivag_zynodW33Eq5amiWpHdFCc/view?usp=sharing)

## Exercice 1

Les nombres sont écrits en binaire.
1. Calculer la somme 100110 + 001101 en posant l'addition.
2. Traduire le calcul en décimal.
3. Véfier dans le Shell en utilisant la notation en base 2 : 0b......

## Exercice 2

1. Écrire en base cinq puis en base seize le nombre qui s'écrit 172 en base dix.
2. Le nombre B3 est écrit en base seize. Écrire ce nombre en base deux puis en base cinq.
3. Vérifier dans le Shell en utilisant l'instruction int(str, base) qui crée un nombre entier à partir de son écriture sous forme de string dans la base. La notation en base 16 est aussi : 0x....

## Exercice 3

Un nombre entier représenté par plusieurs octets est stocké en mémoire ou dans un fichier suivant un ordre qui s'appelle "l'endianness". Par exemple, le nombre qui s'écrit B35F en hexadécimal peut être stocké sous la forme B35F ou sous la forme 5FB3.
Dans le premier cas on parle d'orientation _big-endian_ et dans le deuxième cas d'orientation _little-endian_. Avec l'orientation _big-endian_, 08 00 correspond à 8×16<sup>2</sup>=2048 en décimal alors qu'avec l'orientation _little-endian_ 08 00 correspond à 8 en décimal.
Écrire une fonction qui prend en paramètres 2 octets écrits en hexadécimal (directement et non sous forme de string), représentés par deux entiers compris entre 0 et 255, et une chaîne de caractères "BE" ou "LE" et renvoie la valeur décimale du nombre représenté suivant l'encodage _big-endian_ (pour "BE") ou _little-endian_ (pour "LE").

## Exercice 4

On utilise 5 bits pour coder en binaire les entiers relatifs.

1. Comment code-t-on le nombre 9 ?
2. Comment code-t-on le nombre -10 ?
3. Si on utilise 5 bits pour coder les entiers relatifs, combien de nombres peut-on coder et lesquels ?

## Exercice 5

Écrire le nombre 3,625 en binaire.

## Exercice 6

Les flottants sont codés suivant la norme IEEE 754 sur 64 bits, soit 1 bit pour le signe, 11 bits pour l'exposant décalé et 52 bits pour la mantisse tronquée (cf.cours).
1. Comment est codé le nombre - 4.5 ?
2. Quel est le nombre réel codé par 1011 1111 1110 1000 0000 ... 0000 ?

## Exercice 7

Vérifier, à l'aide d'une table de vérités, l'égalité : a xor b = (a and not(b)) or (not(a) and b).


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


