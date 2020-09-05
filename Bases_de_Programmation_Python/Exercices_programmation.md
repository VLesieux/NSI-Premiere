## Exercices de programmation (révisions 2de SNT)

Il est demandé d'écrire les docstring pour toutes les fonctions en utilisant les résultats escomptés en sortie

```Python
if __name__ == '__main__':
  import doctest
  doctest.testmod(verbose=True)
```

### Exercice 1

Une entreprise fournit des ramettes de papier à prix dégressif en fonction du nombre de lots achetés : les 50 premiers lots sont vendus 3,68€, au-delà chaque lot est vendu 3,22€. Écrire une fonction `prix(n)` qui lorsqu'on saisit le nombre `n` de lots achetés retourne (avec un return) le prix à payer puis procéder à l'affichage (avec un print) du résultat.

```Python
>>> %Run exercices_programmation_snt.py
nombre de lots de ramettes de papier achetés ? 100
Il vous en reviendra 345.0€
```

### Exercice 2

Un cinéma propose un pass mensuel à 15€ permettant d'obtenir une réduction sur le prix des séances : sans réduction la séance est à 8,70€, alors qu'avec le pass la séance est à 5,50€. 
Sans résoudre mathématiquement le problème, écrire une première fonction `abo1(n)` qui renvoie (avec un return) une chaîne de caractères et qui permet d'afficher (avec dans un deuxième temps un print) s'il est avantageux de prendre le pass ou non en fonction du nombre ` n` de séances dans le mois ; la fonction affiche également sur la même ligne le prix total à payer et l'avantage que représente ce choix.

```Python
>>> %Run exercices_programmation_snt.py
combien de séances de cinéma allez-vous prendre ? 2
Ne prenez pas le pass, il est désavantageux ; vous payez 17.4€ sans le pass au lieu de 26.0€ avec le pass
>>> %Run exercices_programmation_snt.py
combien de séances de cinéma allez-vous prendre ? 8
Prenez le pass, il est avantageux ; vous payez 59.0€ avec le pass au lieu de 69.6€ sans le pass
```
Écrire maintenant une deuxième fonction `abo2(n)` qui renvoie cette fois deux informations numériques sous la forme d'un tuple, la première information étant le prix sans abonnement, la seconde le prix avec abonnement.

```Python
>>> abo2(2)
(17.4, 26.0)
>>> abo2(8)
(69.6, 59.0)
```

### Exercice 3

On suppose que l'on dispose de la fonction `abo2(n)` précédente ; écrire une fonction `avantage()` qui utilise cette fonction et qui renvoie le nombre de séances à partir duquel le pass devient avantageux.

```Python
>>> %Run correction_exercices_programmation_snt.py
Prendre le pass devient avantageux à partir de 5 séances.
```

### Exercice 4

Soit l'algorithme ci-dessous écrit en langage naturel :

	a ← -1
	b ← 2
	Pour i allant de 1 à 4
	a ← b-a+i
	b ← 2a+1
	Fin Pour

Prévoir "à la main" les valeurs de a et de b ; retrouver le résultat en programmant l'algorithme.

### Exercice 5

Que fait la fonction `cherche` définie ci-dessous ?

```Python
def cherche(L):
    longueur=len(L)
    m=L[0]
    for i in range(1,longueur):
        if L[i]>m:
            m=L[i]
    return m
```

### Exercice 6

Modifier le programme précédent afin que la valeur renvoyée soit un couple contenant le plus petit et le plus grand élément d'une liste non vide.

```Python
>>> %Run exercices_programmation_snt.py
>>> recherche_min_max([2,8,19,4,1])
(1, 19)
```

### Exercice 7

Que fait la fonction div définie ci-dessous ? Que renvoie div(28) ?
Dans un premier temps, répondre sans exécuter le programme.

```Python
def div(n):
    L=[]
    for i in range(1,n+1):
        if n%i==0:
            L.append(i)
    return L
```

### Exercice 8

Que fait la fonction Inconnue définie ci-dessous ?
Dans un premier temps, répondre sans exécuter le programme.

```Python
def Inconnue(char,chaine):
    c=0
    for caractere in chaine:
        if caractere==char:
            c=c+1
    return c
```

### Exercice 9

Écrire une fonction `concat` telle que `concat(L1,L2)` concatène les listes L1 et L2, c'est-à-dire renvoie une liste des éléments L1 et L2 mis bout à bout.

On proposera deux façons de procéder certes moins efficaces que la fonction ci-dessous :

```Python
def concat(L1,L2):
    return L1+L2
>>> concat([2,8,4],[3,9])
[2, 8, 4, 3, 9]
```
mais présentant un intérêt pédagogique.


### Exercice 10

La suite de Fibonacci se construit comme ceci : les deux premiers termes valent 1, puis chaque terme est la somme des deux précédents.
F(1)=1
F(2)=1
F(3)=2
F(4)=3
F(5)=5
F(6)=8....

Proposer un fonction `Fibo(n)` permettant de déterminer le n-ième terme de la suite de Fibonacci.

```Python
>>> Fibo(38)
39088169
```

### Exercice 11

<img src="Assets/nombre_or.png"> 

Comme l'affirme cet extrait de wikipédia à propos du nombre d'or, il existe une relation entre le nombre d'or et la suite de Fibonacci étudiée précédemment. Ce nombre est en effet la valeur du rapport F(n+1)/F(n) quand n est très grand (ou encore la limite du quotient des termes consécutifs de la suite de Fibonacci). Proposer une fonction qui permet d'approcher la valeur du nombre d'or donnée dans le document à 10<sup>-10</sup> près.

```Python
>>> nombre_or()
(25, 1.6180339886704431)
```

On sera amené à utiliser la fonction `abs()` qui donne la valeur absolue d'un nombre.
```Python
>>> abs(-10)
10
>>> abs(10)
10
```

### Exercice 12

Écrire une fonction  `lancers ` telle que `lancer(n)` simule n lancers d'un dé équilibré à 6 faces et renvoie le résultat sous forme de liste.

```Python
>>> lancers(4)
[2, 1, 4, 5]
>>> lancers(4)
[6, 1, 1, 1]
>>> lancers(4)
[4, 4, 6, 2]
>>> lancers(4)
[2, 5, 6, 1]
```

### Exercice 13

Écrire une fonction `piece` telle que `piece(n)` simule n lancers d'une pièce équilibrée et renvoie la fréquence des "piles" observés.

```Python
>>> pieces(400)
0.47
>>> pieces(4000)
0.49975
```
### Exercice 14

Écrire une fonction `truquee` telle que `truquee(n,p)` simule n lancers d'une pièce truquée, dont la probabilité de faire "piles" vaut p, et renvoie la fréquence des "piles" observées.

Indication : random() génère un nombre compris entre [0,1[ ; random()+0.6 génère un nombre compris entre [0.6,1.6[ ; int(random()+0.6) génère un nombre qui vaut 0 pour tous les nombres compris dans l'intervalle [0.6,1[ d'étendue 0.4 et 1 pour tous les nombres compris entre [1,1.6[ d'étendue 0.6 ; on a donc 60% de chance d'avoir 1 et 40% de chance d'avoir 0.
La fonction int() donne en effet la partie entière du nombre.

```Python
>>> int(0.8)
0
>>> int(1.5)
1
>>> truquee(100,0.6)
0.65
>>> truquee(1000,0.6)
0.587
>>> truquee(10000,0.6)
0.6067
>>> truquee(100000,0.6)
0.60069
```

### Exercice 15

Que fait la fonction `trace` définie ci-dessous ?
Dans un premier temps, répondre sans exécuter le programme.

```Python
from turtle import *
def trace(n,larg):
    reset()
    for i in range(1,n+1):
        left(90)
        forward(larg*i)
        left(90)
        forward(larg*i)
```

### Exercice 16

Écrire un programme qui permet de tracer des triangles en spirales.


<img src="Assets/spirales_triangles.png" width="200" height="200"> 
