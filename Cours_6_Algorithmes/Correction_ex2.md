
## Rappels

### 1. Tri par sélection

Soit une liste de longueur n.  
On considère que jusqu'à l'indice i-1 la liste est déjà triée et qu'il nous reste encore à trier de i à n.

L'algorithme consiste à sélectionner le minimum de la partie non triée situé admettons à l'indice m et de placer ce minimum à la suite de la partie triée en position i en faisant une permutation des éléments situés en positions i et m.

L'algorithme nécessite donc la recherche du minimum et l'écriture d'une permutation ou échange.

On rappelle l'algorithme du recherche de minimum qui est présent dans la fonction tri_selection

```python
def minimal(liste):
    minimum=liste[0]
    for i in range(len(liste)):
        if liste[i]<minimum:
            minimum=liste[i]
    return minimum
```
D'où l'algorithme complet :

```python
def echange(t,i,j):
    temp=t[i]
    t[i]=t[j]
    t[j]=temp

def tri_selection(t):
    for i in range(len(t)-1):
        m=i#on suppose que jusque i la liste est triée
        for j in range(i+1,len(t)):#recherche du minimum entre i+1 et n
            if t[j]<t[m]:#si on trouve en j un élément plus petit qu'en i
                m=j
        echange(t,i,m)
    return t
```
```python   
>>> tri_selection([3,12,9,1,7])
[1, 3, 7, 9, 12]
```

### 2. Tri par insertion

Soit une liste de longueur n. 
On considère que jusqu'à l'indice i-1 la liste est triée et qu'il nous reste encore à trier de i à n.

L'algorithme consiste à insérer correctement l'élément i dans la partie triée en décalant vers la droite tous les éléments qui le suivent.

L'algorithme nécessite l'écriture de l'insertion et du décalage vers la droite.

```python
def insere(t,i,v):
#insertion dans la liste t supposée triée de l'élément de valeur v en position i
    j=i
#on mémorise la variable i à travers la variable j pour ne pas modifier i
    while j>0 and t[j-1]>v:
        t[j]=t[j-1]
#on décale vers la droite tous les éléments de valeur supérieure à v en faisant décroître j
        j=j-1
#on parcourt pour cela de droite à gauche pour trouver le bon emplacement où insérer la valeur v
    t[j]=v
    
def tri_insertion(t):
    for i in range(1,len(t)):
        insere(t,i,t[i])
    return t
```
```   
>>> tri_insertion([3,12,9,1,7])
[1, 3, 7, 9, 12]
```

## Application 1 : Ordre lexicographique

