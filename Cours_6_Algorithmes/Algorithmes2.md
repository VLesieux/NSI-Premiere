![Programme officiel ](assets/bo.png)

# I. Les algorithmes de tri

## 1. Tri par sélection

<u>Principe</u> : On dispose de n données. On cherche la plus petite donnée et on la place en première position, puis on cherche la plus petite donnée parmi les données restantes et on la place en deuxième position et ainsi de suite.  
Si les données sont les éléments d'une liste `liste`, l'algorithme consiste donc à faire varier un indice i de 0 à n-2.   
Pour chaque valeur de i, on cherche dans la tranche `liste[i:n]` le plus petit élément et on l'échange avec `liste[i]`.  
On connaît déjà l'algorithme de recherche du minimum.  

```python
def minimum(liste):
    minimum=liste[0]
    for i in liste:
        if i<minimum:
            minimum=i
    return minimum
```

Pour obtenir l'algorithme du tri selection, il ne reste qu'à insérer cette partie dans une boucle où i varie de 0 à n-2 et pour chaque valeur de i faire l'échange de liste[i] avec minimum.

<u>Exemple</u> : 

Soit la liste [7,4,3,2,9,5] de longueur 6.   

Pour i égal 0, [2,4,3,7,9,5] ; permutation de 2 avec 7    
Pour i égal 1, [2,3,4,7,9,5] ; permutation de 4 avec 3   
Pour i égal 2, [2,3,4,7,9,5] ; pas de permutation   
Pour i égal 3, [2,3,4,5,9,7] ; permutation de 5 avec 7   
Pour i égal 4=6-2, [2,3,4,5,7,9] ; permutation de 9 avec 7   

Montrer que l'écriture de la fonction `tri_selection(liste)` répond à cet objectif.

```python
def tri_selection(liste):
    n=len(liste)
    for i in range(n-1):
        minimum=liste[i]
        for j in range(i+1,n):
            if liste[j]<minimum:
                minimum=liste[j]
                i_minimum=j#on repère l'indice j pour la permutation
        liste[i],liste[i_minimum]=minimum,liste[i]
    return liste
```

<u>Terminaison</u> : dans la mesure où les boucles utilisées sont deux boucles inconditionnelles imbriquées, il n'y a pas de problème de terminaison.

<u>Correction</u>  : L'invariant est le suivant : "pour chaque i, la liste est une permutation de la liste initiale, la liste `liste[0:i+1]` est triée et tous les éléments de la liste `liste[i+1:n]` sont supérieurs à tous les éléments de la liste `liste[0:i+1]`."

Après le premier passage dans la boucle, pour i égal à 0, la liste `liste[0:1]` ne contient qu'un élément qui est le minimum de la liste, inférieur à tous les éléments de la liste. La propriété est donc vraie pour i=0.

Supposons la propriété vraie pour i=k,  on a donc la liste `liste[0:k+1]` triée et tous les éléments de la liste `liste[k+1:n]` sont supérieurs à tous les éléments de la liste `liste[0:k+1]`. Au passage suivant, le minimum de la liste `liste[k+1:n]` est placé en position k+1, cette valeur est supérieure à toutes les valeurs de la liste `liste[0:k+1]` et inférieure à toutes les valeurs de la liste `liste[k+2:n]` ; la propriété est donc bien vraie à l'ordre k+1.

La propriété est vraie au dernier passage pour i égal à n-2. À ce moment-là, la liste `liste[0:n-1]` est triée et l'élément n-1, dernier de la liste, est supérieur à tous les éléments de la liste `liste[0:n-1]` donc la liste `liste[0:n]` est triée.

<u>Coût</u> : Nous sommes dans le cas de deux boucles imbriquées. 
```python
    for i in range(n-1):
            .....................
        for j in range(i+1,n):
                ....................
```
Pour chaque valeur de i, j prend des valeurs de i+1 à n-1 soit n-i-1 valeurs. Et pour chaque valeur de j, une unique comparaison est effectuée. Donc pour chaque valeur de i, nous avons n-i-1 comparaisons. Au total, nous avons donc : (n-1)+(n-2)+....+2+1=n×(n+1)/2 comparaisons, donc un <u>coût quadratique</u> de l'ordre de n<sup>2</sup> comparaisons quelque soit la liste de longueur n, même si celle-ci est triée ! Le tri par sélection a l'avantage d'être facile à programmer mais il n'est pas recommandé si la liste contient plus de 10000 éléments.

## 2. Tri par insertion

<u>Principe</u> : On dispose de n données et on procède par étapes. À chaque étape, on suppose que les k premières données sont triées, et on insère une donnée supplémentaires à la bonne place parmi ces k données déjà triées.   
Si les données sont les éléments d'une liste, l'algorithme consiste donc à faire varier un indice i de 0 à n-2. Pour chaque valeur de i, on cherche dans la liste `liste[0:i+1]` à quelle place doit être inséré l'élément liste[i+1] qu'on appelle clé. Pour cela, on compare la clé successivement aux données précédentes, en commençant par la donnée d'indice i puis en remontant dans la liste jusqu'à trouver la bonne place, c'est-à-dire entre deux données successives, l'une étant plus petite et l'autre étant plus grande que la clé. Si la clé est plus petite que toutes les données précédentes, elle se place en premier. Pour ce faire, on décale d'une place vers la droite les données plus grandes que la clé après chaque comparaison.


```python
def tri_insertion(liste):
    for i in range(len(liste)-1):
        k=i+1#l'indice de la clé
        cle=liste[k]
        while k>0 and cle<liste[k-1]:
            liste[k]=liste[k-1]#décalage d'une place vers la droite
            k=k-1#on remonte dans la liste 
        liste[k]=cle
```

<u>Terminaison</u> : La boucle externe est une boucle for dont le nombre de passages est fini. La boucle interne est une boucle while conditionnée par les valeurs de k qui constituent une suite décroissante de i+1 à 1, soit au plus i+1 passages.

<u>Correction</u>  : Nous utilisons l'invariant de boucle : "pour chaque i, la liste est une permutation de la liste initiale et la liste `liste[0:i+2]` est triée."  
Après le premier passage dans la boucle, pour i égal à 0, l'élément `liste[0]` et la clé d'indice 1 sont rangés dans l'ordre. Donc la liste `liste[0:2]` est triée.  
Si après un passage pour i égal à un k quelconque, la liste `liste[0:k+2]` est triée, alors au passage suivant l'élément `liste[k+2]` est inséré à la bonne place parmi les éléments de la liste `liste[0:k+2]` ou reste à sa place. Donc la liste `liste[0:k+3]` est triée. La propriété est donc vraie pour i égal à k+1. La propriété est encore vraie après le dernier passage, pour i égal à n-2. À ce moment, la liste `liste[0:n]`, c'est-à-dire la liste, est triée.

<u>Coût</u> : Si la liste est déjà triée dans l'ordre croissant, pour chaque valeur de i, k prend la valeur de i+1 et il n'y a qu'une seule comparaison, le test `cle<liste[k-1]`. La variable i prenant n-1 valeurs, cela fait un total de n-1 comparaisons. Le coût de l'algorithme est donc de n.  
Si dans le pire des cas où les éléments de la liste sont rangés dans l'ordre décroissant, alors pour chaque valeur de i, k prend les valeurs de i+1 à 1 soit i+1 valeurs et donc i+1 comparaisons. Au total nous avons 1+2+...(n-2)+(n-1) comparaisons soit n×(n-1)/2, le coût est de l'ordre de n<sup>2</sup> comparaisons. En conclusion, cet algorithme de tri s'avère efficace sur une liste déjà presque triée. 

## 2. Tri en Python

Avec Python, nous disposons de la fonction `sorted(liste)` qui prend en argument la liste et renvoie la liste triée sans modification de la liste initiale. Nous disposons également de la méthode sort() des objets liste qui trie la liste à laquelle elle s'applique.

```python
liste=[4,1,3,2]
liste2=sorted(liste)
print(liste2)
print(liste)
liste.sort()
print(liste)
```

L'algorithme de tri utilisé par la méthode `sort` et la fonction `sorted` s'appelle `timsort`, du nom de son inventeur Tim Peters en 2002. C'est un tri performant, dérivé d'un tri fusion, qui utilise l'algorithme du tri par insertion sur des parties presque triées.

# II. L'algorithme des plus proches voisins

# III. Les algorithmes gloutons

