## QCM Thème F : Langages et programmation ##
 [Vidéo de la correction](https://www.youtube.com/watch?v=qfq7Of0a0yk&feature=youtu.be)

### Question 1 ###

On exécute le script suivant.

```Python
n = 6
s = 0
while n >= 0:
    s = s + n
    n = n -1
```

a. [ ] 0     
b. [ ] 6     
c. [ ] 15   
d. [ ] 21   


### Question 2 ###

La documentation de la bibliothèque random de Python précise que `random.randint(a,b)` renvoie un entier aléatoire N tel que a ≤ N ≤ b.
Afin d’obtenir un entier choisi aléatoirement dans l’ensemble {-4 ; -2 ; 0 ; 2 ; 4}, après avoir importé la librairie random de Python, on peut utiliser l’instruction :

a. [ ] random.randint(0,8)/2.      
b. [ ] random.randint(0,8)/2 - 4.    
c. [ ] random.randint(0,4)*2 - 2.  
d. [ ] (random.randint(0,4) - 2) * 2 


### Question 3 ###

On définit la fonction suivante :

```Python
def f(x,y):
    x = x + y
    y = x - y
    x = x - y
    return (x,y)
```
Quel est la valeur renvoyée par l'appel f(2019,2020) ?

a. [ ] 2019,2019.     
b. [ ] 2019,2020.     
c. [ ] 2020,2019.  
d. [ ] 2020,2020.  

### Question 4 ###

T est un tableau de nombres entiers non vide. Que représente la valeur de s renvoyée par cette fonction ?

```Python
def mystere(T):
    s = 0
    for k in T:
        if k % 2 == 0:
            s = s+k
    return s
```

a. [ ] la somme des valeurs du tableau T.  
b. [ ] la somme des valeurs positives du tableau T.       
c. [ ] la somme des valeurs impaires du tableau.  
d. [ ] la somme des valeurs paires du tableau T


### Question 5 ###

On exécute le script suivant :

```Python
def calcul(a,b):
    a = a + 2
    b = b + 5
    c = a + b
    return c
a,b = 3,5
calcul(a,b)
```

À la fin de cette exécution :

a. [ ] a vaut 3, b vaut 5 et c vaut 15.  
b. [ ] a vaut 3, b vaut 5 et c n'est pas défini    
c. [ ] a vaut 5, b vaut 10 et c vaut 15.    
d. [ ] a vaut 5, b vaut 10 et c n'est pas défini

### Question 6 ###

Ce programme ne renvoie pas toujours ses trois arguments dans l’ordre croissant. Parmi les tests suivants, lequel va permettre de détecter l’erreur ?

```Python
def ranger(a, b, c):
    if a > b :
        a, b = b, a
    if b > c:
        b, c = c, b
    return a, b, c
```

a. [ ] ranger(1,2,3).  
b. [ ] ranger(3,4,1).             
c. [ ] ranger(1,3,2).  
d. [ ] ranger(4,2,3). 

### Question 7 ###

On considère le code suivant :

```Python
if x < 4:
    x = x + 3
else:
    x = x - 3
```

Quelle construction élémentaire peut-on identifier ?

a. [ ] une boucle non bornée.  
b. [ ] une structure conditionnelle.   
c. [ ] une boucle bornée.   
d. [ ] un appel de fonction

### Question 8 ###

On considère la fonction suivante :
```Python
def comparaison(a,b):
    if a < b:
        return a
    else:
        return b
print(comparaison(3,7))
```
Quel est le type de la valeur renvoyée par l'appel comparaison(6,5) ?

a. [ ] un booléen (vrai/faux).   
b. [ ] un nombre entier.    
c. [ ] un nombre flottant.  
d. [ ] une chaîne de caractères

### Question 9 ###

La fonction `ajoute(n,p)` codée ci-dessous en Python doit calculer la somme de tous les entiers compris entre n et p (n et p compris).
Par exemple, ajoute(2,4) doit renvoyer 2+3+4 = 9.

```Python
def ajoute(n,p):
    somme = 0
    for i in range(.........): # ligne à modifier
        somme = somme + i
    return somme
```
Quelle est la bonne écriture de la ligne marquée à modifier ?

a. [ ] for i in range(n,1,p):    
b. [ ] for i in range(n,p):   
c. [ ] for i in range(n,p+1):   
d. [ ] for i in range(n-1,p):   

### Question 10 ###

On a défini une liste L de nombres entiers.
Quelle est la valeur de la variable m à la fin de l'exécution du script suivant ?

```Python
m = L[0]
for j in range(len(L)):
    if m < L[j]:
        m = L[j]
```

a. [ ] la moyenne de la liste L.   
b. [ ] le minimum de la liste L.   
c. [ ] le maximum de la liste L.   
d. [ ] la longueur de la liste L. 
