# QCM Algorithmes

### Q1]
On considère la fonction suivante :

```python
def f(t,i):
    im=i
    m=t[i]
    for k in range(i+1,len(t)):
        if t[k]<m:
            im,m=k,t[k]
    return im
```
Que renvoie f([ 7, 3, 1, 8, 19, 9, 3, 5 ], 0) ?

* [ ] 1
* [ ] 2
* [ ] 3
* [ ] 4

### Q2]

Combien d'échanges effecute la fonction Python suivante pour trier un tableau de 10 éléments au pire des cas ?


```python
def tri(tab):
    for i in range(1,len(tab)):
        for j in range(len(tab)-i):
            if tab[j]>tab[j+1]:
                tab[j],tab[j+1]=tab[j+1],tab[j]
```

* [ ]  45. 
* [ ]  100. 
* [ ]  10
* [ ]  55


### Q3]

Avec un algorithme de recherche par dichotomie, combien d'étapes sont nécessaires pour déterminer que 35 est présent dans le tableau [1,7,12,16,18,20,24,28,35,43,69] ?


* [ ]  2 étapes.
* [ ]  1 étape.
* [ ]  9 étapes.
* [ ]  11 étapes.

### Q4]

Dans le quadrillage ci-dessous, 14 points sont dessinés, dont 7 de la classe C1, avec des ronds noirs, et 7 de la classe C2, avec des losanges.

![](assets/quadrillage.png) 

On introduit un nouveau point A, dont on cherche la classe à l'aide d'un algorithme des k plus proches voisins pour la distance géométrique habituelle, en faisant varier la valeur de k parmi 1,3,5.
Quelle est la bonne réponse (sous la forme d'un triplet de classes pour le triplet (1,3,5) des valeurs de k) ?

* [ ]  C1, C2, C3. 
* [ ]  C2, C1, C2.
* [ ]  C2, C2, C2.
* [ ]  C2, C1, C1.

<hr>
<hr>

# Réponses et explications

### Q1]
On considère la fonction suivante :

```python
def f(t,i):
    im=i
    m=t[i]
    for k in range(i+1,len(t)):
        if t[k]<m:
            im,m=k,t[k]
    return im
```
Que renvoie f([ 7, 3, 1, 8, 19, 9, 3, 5 ], 0) ?

* [ ] 1
* [x] 2
* [ ] 3
* [ ] 4

La fonction f admet comme paramètres une liste t et un entier i qui tient lieu d'indice dans la liste.  
On garde en mémoire la valeur de i avec une nouvelle variable im.  
m est la valeur que prend la liste en position d'indide i.  
On fait varier une variable k de i+1 à len(t)-1 : si on trouve dans la liste, au delà de l'indice i, une valeur inférieure à m, celle qu'elle prend en l'indice i, on assigne à la variable im la valeur de cet indice k.  
La fonction renvoie la valeur de im mais attention, <u>une fois la boucle terminée !</u>

Dans le cas présent, i=0 et t[0]=7 ; on cherche donc à partir de l'indice k=1 une valeur dans la liste inférieure à 7, on trouve 3 et donc im=1 et m=3, puis on <u>continue</u> à augmenter k qui vaut maintenant 2, on trouve que 1 est inférieur à 3, donc im=2 et m=1, puis on continue à augmenter k mais aucune des valeurs qui suit 8, 19... n'est inférieure à 1 donc la boucle est finalement terminée et im garde sa valeur 2 qui est renvoyée.

Pour en être convaincu en pratique, ajouter f([ 7, 3, 1, 8, 19, 9, 3, 5 ], 0) au programme dans Thonny, activer le mode debug, faire 'step over F6' une fois, puis 'step into F7' autant de fois que nécessaire pour voir le déroulé du programme et l'évolution des variables.

### Q2]

Combien d'échanges effectue la fonction Python suivante pour trier un tableau de 10 éléments au pire des cas ?


```python
def tri(tab):
    for i in range(1,len(tab)):
        for j in range(len(tab)-i):
            if tab[j]>tab[j+1]:
                tab[j],tab[j+1]=tab[j+1],tab[j]
    return tab
```

* [x]  45
* [ ]  100
* [ ]  10
* [ ]  55

Le programme commence à partir du début de la liste en permutant à chaque fois le nouvel élément considéré avec le premier auquel il est supérieur ; le nombre de permutations dans le pire des cas où la liste des 10 éléments est initalement triée dans l'ordre décroissant est égal à 1+2+.......9 = 45.

Pour en être convaincus, observons les évolutions de la liste t=[10,9,8,7,6,5,4,3,2,1] la plus défavorable avec le debugger.

t=[10,9,8,7,6,5,4,3,2,1]	i=1		j=0.  
t=[9,10,8,7,6,5,4,3,2,1]	i=1		j=1.   
t=[9,8,10,7,6,5,4,3,2,1]	i=1		j=2.     
t=[9,8,7,10,6,5,4,3,2,1]	i=1		j=3.   
....................................    
t=[9,8,7,6,5,4,3,2,1,10]	i=1		j=8. 

t=[9,8,7,6,5,4,3,2,1,10]	i=2		j=0.   
t=[8,9,7,6,5,4,3,2,1,10]	i=2		j=1.    
t=[8,7,9,6,5,4,3,2,1,10]	i=2		j=2.   
t=[8,7,6,9,5,4,3,2,1,10]	i=2		j=3.   
....................................    
t=[8,7,6,5,4,3,2,1,9,10]	i=2		j=7     
....................................   
....................................    
t=[2,1,3,4,5,6,7,8,9,10]	i=9		j=1.    
t=[1,2,3,4,5,6,7,8,9,10]	i=9		j=0.   

On voit qu'à chaque fois la plus grande valeur remonte, c'est ce qu'on appelle le tri bulle.    
i = 1 ; j=0 à 8 : 9 permutations pour la remontée du 10.   
i = 2 ; j=0 à 7 : 8 permutations pour la remontée du 9.   
i = 3 ; j=0 à 6 : 7 permutations pour la remontée du 8.   
................................     
i = 8 ; j=0 à 1 : 2 permutations pour la remontée du 3.   
i = 9 ; j=0 à 0 : 1 permutation pour la remontée du 2.    

Au total : 9+8+.....1=45 permutations.    

On peut aussi introduire un compteur de permutation dans le programme pour le vérifier.

```python
def tri(tab):
    compte=0
    for i in range(1,len(tab)):
        for j in range(len(tab)-i):
            if tab[j]>tab[j+1]:
                tab[j],tab[j+1]=tab[j+1],tab[j]
                compte+=1
    return compte
 >>> tri([10,9,8,7,6,5,4,3,2,1])
45   
```
  
### Q3]

Avec un algorithme de recherche par dichotomie, combien d'étapes sont nécessaires pour déterminer que 35 est présent dans le tableau [1,7,12,16,18,20,24,28,35,43,69] ?


* [ ]  1 étape.
* [x]  2 étapes.
* [ ]  9 étapes.
* [ ]  11 étapes.

Notons l'évolution des variables g et d au fur et à mesure de l'avancement de l'algorithme :

étape 1 : g=0 d=11 m=5 35>t[5]=20  
étape 2 : g=5 d=11 m=8 t[8]=35

Attention ici, le piège est de faire 1+69//2=35 et de répondre 1 étape, mais on travaille avec les indices de position et non avec les valeurs !

On peut placer un compteur dans l'algorithme de dichotomie.

```python
def dichotomie(x,liste):
    g=0
    d=len(liste)
    compteur=0
    etapes=""
    while d-g>1:
        k=(g+d)//2        
        compteur +=1
        if x<liste[k]:
            d=k
            etapes+="["+str(liste[g])+","+str(liste[d-1])+"]"
            if x==liste[d]:
                return("La valeur "+str(x)+" a été trouvée dans la liste en position "+str(d)+" en "+str(compteur)+" étapes :"+etapes)
        else:
            g=k
            etapes+="["+str(liste[g])+","+str(liste[d-1])+"]"
            if x==liste[g]:
                return("La valeur "+str(x)+" a été trouvée dans la liste en position "+str(g)+" en "+str(compteur)+" étapes :"+etapes)
    return("La valeur n'est pas dans la liste")

>>> print(dichotomie(35,[1,7,12,16,18,20,24,28,35,43,69]))
La valeur 35 a été trouvée dans la liste en position 8 en 2 étapes :[20,69][35,69]
```
### Q4]

Dans le quadrillage ci-dessous, 14 points sont dessinés, dont 7 de la classe C1, avec des ronds noirs, et 7 de la classe C2, avec des losanges.

![](assets/quadrillage.png) 

On introduit un nouveau point A, dont on cherche la classe à l'aide d'un algorithme des k plus proches voisins pour la distance géométrique habituelle, en faisant varier la valeur de k parmi 1,3,5.
Quelle est la bonne réponse (sous la forme d'un triplet de classes pour le triplet (1,3,5) des valeurs de k) ?

* [ ]  C1, C2, C3. 
* [ ]  C2, C1, C2.
* [ ]  C2, C2, C2.
* [x]  C2, C1, C1.

En considérant 1 seul voisin qui est un losange, A a de grande chance d'être un losange lui-même de la classe C2.
En considérant les 3 plus proches voisins, on trouve 1 losange et 2 ronds, A a de grande chance d'être lui-même un rond de la classe C1.
En considérant les 5 plus proches voisins, on trouve 2 losanges et 3 ronds, A a de grande chance d'être lui-même un rond de la classe C1.
