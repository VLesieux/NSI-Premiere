## I. Tri par sélection

###### 1. Cours :
Rappeler sur un schéma le principe de ce tri.

###### 2. Exemple:
Montrer les différentes étapes du tri sur l'exemple : [3,4,1,7,2]

###### 3. Programmation :

```python
def echange(t,i,j):
    temp=t[i]
    t[i]=t[j]
    t[j]=temp

def tri_selection(t):
    for i in range(len(t)):
        m=i
        for j in range(i+1,len(t)):
            if t[j]<t[m]:
                m=j
        echange(t,i,m)
    return t
```

Expliquer le programme et proposer une amélioration de son écriture.

###### 4. Efficacité du tri
Prouver qu'elle est proportionnel à N<sup>2</sup>.
###### 5. Application :
En supposant que le tri par sélection prend à peu près 6,8 secondes pour trier 16 000 valeurs, calculer le temps qu'il faudrait pour trier un million des valeurs avec ce même tri par sélection.


## II. Tri par insertion

###### 1. Cours :
Rappeler sur un schéma le principe de ce tri.
###### 2. Exemple: 
Montrer les différentes étapes du tri sur l'exemple : [3,4,1,7,2]
###### 3. Programmation :

```python
def insere(t,i,v):
    j=i
    while j>0 and t[j-1]>v:
        t[j]=t[j-1]
        j=j-1
    t[j]=v
    
def tri_insertion(t):
    for i in range(1,len(t)):
        insere(t,i,t[i])
    return t
```

Expliquer le programme.

###### 4. Efficacité du tri
Prouver qu'elle est proportionnel à N<sup>2</sup> dans le pire des cas, c'est-à-dire quand le tableau se présente en ordre décroissant.
###### 5. Application :
En se servant du tri par insertion, écrire une fonction qui prend en argument un tableau d'entiers et renvoie la valeur la plus fréquente dans ce tableau. Indication : une fois le tableau trié, les valeurs égales se retrouvent côte à côte dans ce tableau et il devient facile de les compter. Une simple boucle et quelques variables suffisent. On désignera par v la valeur courante, c son nombre d'occurences, mv la valeur la plus courante, m son nombre d'occurences.


## III. Recherche dichotomique dans un tableau trié

###### 1.  Cours :
Rappeler sur un schéma le principe de cette recherche.
###### 2. Programmation :

```python
def recherche_dichotomique(t,v):
    g=0
    d=len(t)-1
    while g<=d:
        m=(g+d)//2
        if t[m]<v:
            g=m+1
        elif t[m]>v:
            d=m-1
        else:
            return m
    return None
```
Expliquer le programme. 

###### 3. Efficacité
Modifier le programme pour afficher le nombre total de tours de boucle effectués par l'algorithme. Lancer le programme sur des tableaux de tailles différentes (par exemple 100, 1000, etc) et observer les nombres de tours affichés. On pourra par exemple chercher la valeur 1 dans un tableau ne contenant que des valeurs 0, ce qui correspond au pire des cas.
###### 4. Exemple:
Combien de valeurs sont examinés lors de l'appel à recherche_dichotomique([0,1,1,2,3,5,8,13,21],7) ? On fera apparaître les valeurs de g, d et m.


## IV. Algorithme des k plus proches voisins

###### 1. Cours:
Rappeler le principe de cet algorithme

###### 2. Exemple: Couleur d'un fruit

On cherche à prédire la couleur d’un fruit en fonction de sa largeur L et de sa hauteur H. \
On dispose des données d’apprentissage suivantes :

| largeur | hauteur | couleur |
| ------- | ------- | ------- |
| 2       | 6       | red     |
| 5       | 6       | yellow  |
| 2       | 5       | orange  |
| 6       | 5       | purple  |
| 1       | 2       | red     |
| 4       | 2       | blue    |
| 2       | 1       | violet  |
| 6       | 1       | green   |

Ces données sont placées dans un repère L en abscisse, H en ordonnée), indiquez pour chaque point sa couleur.

![](assets/fruit-color.png)

L’objectif ici est d’étudier l’influence des voisins sur la propriété de couleur d’un fruit. 

Soit U le nouveau fruit de largeur L = 1, et de hauteur H = 4. 

1. Quelle est sa couleur si l'on considère 1 voisin ?
2. Quelle est sa couleur si l'on considère 3 voisins ?
3. Plutôt que le vote majoritaire, on voudrait considérer le vote des voisins pondérés par la distance. Chaque voisin vote selon un poids w inversement proportionnel au carré de sa distance  : w = 1/d<sup>2</sup>. On prend  3 voisins, quelle est la couleur de U ? Comparez vos résultats à ceux de la question 2.


## V. Algorithme glouton (cf. Voyageur de commerce)

###### 1. Cours:
Rappeler le principe d'un algorithme glouton.
###### 2. Programmation :
Expliquer le programme ci-dessous de rendu de monnaie

```python
euros=[1,2,5,10,20,50,100,200]

def monnaie(s):
    """
    combien de pièces faut-il pour obtenir la somme s
    """
    i=len(euros)-1
    liste=[]
    while s>0:
        if s>=euros[i]:
            liste.append(euros[i])
            s-=euros[i]
        else:
            i -=1
    return liste
```

###### 3. Application :

Supposons avoir une liste d'activités, chacune associée à un créneau horaire défini par une heure de début et une heure de fin. Deux activités sont compatibles si leurs créneaux horaires ne se recouvrent pas. On souhaite sélectionner un nombre maximal d'activités toutes compatibles entre elles. 

1. On se donne des activités avec les créneaux suivants : 8h-13h, 12h-17h, 9h-11h, 14h-16h, 11h-12h. Combien de ces activités peuvent-elles être conciliées sur une seule journée ?
	
2. On propose une stratégie gloutonne pour sélectionner des activités en commençant par le début de journée : choisir l'activité dont l'heure de fin arrive le plus tôt (parmi les activités dont l'heure de début est bien postérieure aux créneaux des activités déjà choisies). Appliquer cette stratégie à la situation précédente.

3. On suppose avoir n activités numérotées de 0 à n-1, et deux tableaux début et fin de taille n tels que debut_horaire[i] et fin_horaire[i] contiennent respectivement l'heure de début et l'heure de fin de l'activité numéro i. Écrire une fonction prochaine(h) qui sélectionne l'activité sous la forme d'un tuple de deux valeurs ou doublet dont l'heure de début n'est pas antérieure à h et qui s'arrête le plus tôt. On demandera à la fonction de renvoyer None s'il n'y a aucun créneau compatible.   
<u>Remarque</u> : On ne se permettra pas d'utiliser la fonction min associée à une liste qui renvoie la valeur minimale de celle-ci mais on s'efforcera d'écrire une fonction `minimale` qui renvoie cette valeur minimale.

<u>Indication 1</u>  : on pourra utiliser la méthode index(valeur) associée à une liste qui renvoie l'indice de la position de la valeur dans la liste.

```python
>>> liste=["A","B","C"]
>>> print(liste.index("B"))
1
```

<u>Indication 2</u>  : On peut utiliser une version ordonnée d'une liste sans pour autant modifier la liste de départ.

```python
>>> liste=[12,5,19,2]
>>> print(sorted(liste))
[2, 5, 12, 19]
>>> liste
[12, 5, 19, 2]
```

Exemple :

```python
>>> prochaine(7)
(11, 12)
```

4. En déduire une fonction selection(debut,fin) qui sélectionne autant d'activités que possible en suivant la stratégie gloutonne. On demandera à la fonction d'afficher la suite de ces activités sélectionnées.

Exemple : 

```python
>>> selection(10,16)
[(11, 12), (14, 16)]
```
