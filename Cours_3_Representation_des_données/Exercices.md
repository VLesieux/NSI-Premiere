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


## Exercice 5 : codage d'un entier relatif en binaire sur p bits

Écrire une fonction _conversion_relatif(a,p)_ qui prend en paramètres un entier relatif a exprimé en base dix et un entier naturel non nul p et renvoie le codage de a sur p bits. Le résultat renvoyé est de type str.     
Par exemple, sur p=6 bits, la fonction doit renvoyer '010010' si a=18 et '101110' si a= - 18.

Indications :
- Faire une fonction conversion_entier(a,p) puis une fonction conversion_entier_relatif(a,p)
- Ajouter ensuite les conditions pour une écriture sur p bits

## Exercice 6

Vérifier, à l'aide d'une table de vérités, l'égalité : a xor b = (a and not(b)) or (not(a) and b).


## Exercice 7

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

## Exercice 8

Écrire le nombre 3,625 en binaire.

## Exercice 9

Les flottants sont codés suivant la norme IEEE 754 sur 64 bits, soit 1 bit pour le signe, 11 bits pour l'exposant décalé et 52 bits pour la mantisse tronquée (cf.cours).
1. Comment est codé le nombre - 4.5 ?
2. Quel est le nombre réel codé par 1011 1111 1110 1000 0000 ... 0000 ?

## Exercice 10 : codage d'un flottant suivant la norme IEEE 754

Écrire une fonction _codage_ (accompagnée de sa docstring) qui détermine et renvoie le codage binaire d'un flottant exprimé en base dix. L'entrée en paramètre est de type float et la sortie de type str. On utilise le codage sur 64 bits de la norme IEEE 754.   
Voici les différentes étapes :
1. Le paramètre de la fonction, de typle float, représente un nombre x.
2. Le signe de x est déterminé et stocké dans une variable s='0' ou s='1' puis x est changé en |x|
3. Calcul de l'exposant et de la mantisse. Pour cela, si x≥2, effectuer des divisions successives par 2, si x<1 effectuer des multiplications successives par 2, en remplaçant à chaque fois la valeur de x par le résultat obtenu, et dans les deux cas jusqu'à obtenir un nombre x tel que 1≤x<2. L'exposant est alors, au signe près, le nombre de divisions ou de multiplications effectuées et la mantisse est le nombre x final.
4. Calcul de l'exposant décalé qui est codé en binaire sur 11 bits (voir l'exercice 5). Le résultat est stocké dans une chaîne e.
5. Calcul de la mantisse tronquée x=x-1 qui doit être écrite en binaire sur 52 bits et stockée dans une chaîne m. Pour cela, multiplier x par 2 ; si x≥1, ajouter '1' à m et retrancher 1 à x, sinon ajouter '0' à m ; reproduire ce schéma 52 fois.
6. La chaîne concaténée s+e+m est renvoyée.

Par exemple, codons le réel - 0,375. On note que 0,375=1,5×2<sup>-2</sup>. On réalise donc la concaténation de '1' pour le signe, du code de -2 + 1023 = 1021 soit '011 1111 1101', la mantisse 1,5 s'écrit 1,1 en binaire et on ne garde que la partie décimale 1 et on complète avec des 0. Au final, le codage de - 0,375 est 1 011 1111 1101 1000.......0

Exemples:
```  
>>>codage(1.025)
00111111100000110011001100110011
>>>codage(-11.0252)
11000001001100000110011100111000
```  

## Exercice 11 

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


