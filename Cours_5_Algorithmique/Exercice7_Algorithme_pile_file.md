
***Notions de pile et de file en algorithmique***



On donne le code pour vérifier les doctest.

```python    
if __name__ == '__main__':
    import doctest
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS, verbose=True)
```

**1) Notion de pile** :

Une pile est une structure de données qui donne accès en priorité aux dernières données ajoutées. Ainsi la dernière information ajoutée sera la première à sortir. Autrement dit, on ne peut accéder qu'à l'objet situé au  sommet de la pile.
Le rangement des assiettes convient à cette description. En effet l'ordre dans lequel les assiettes sont dépilées est l'inverse de celui dans lequel elles ont été empilées, puisque seule l'assiette supérieure est accessible.
Une pile est ainsi une liste remplie sur le principe du "dernier arrivé, premier sorti", abrégé en **LIFO**, de l'anglais "Last In First Out".

Exemples d'applications pratiques : 

    1. La gestion de l'historique de navigation dans un navigateur web. Lorsque vous naviguez sur internet, les pages web que vous visitez sont empilées dans un ordre spécifique, vous permettant de retourner à des pages précédemment visitées en utilisant le bouton "Retour" de votre navigateur.

    2. La résolution d'expressions mathématiques en notation polonaise inversée (RPN). Cette méthode utilise une pile pour stocker les opérandes et effectuer les opérations en utilisant des opérateurs comme des "pop" et des "push" pour manipuler les données sur la pile.

    3. La gestion de la mémoire d'un ordinateur. Les systèmes d'exploitation utilisent des piles pour stocker les adresses de retour des appels de fonction lors de l'exécution de programmes. Cela permet de retourner automatiquement à l'emplacement d'où la fonction a été appelée une fois que celle-ci a été exécutée.

    4. La gestion des appels récursifs : Pour chaque appel récursif on stocke les informations de l'appel en cours dans la pile pour pouvoir y revenir à la fin de l'appel.

    5. La résolution d'algorithme de parcours de graphe : Pour chaque noeud visité on stocke les informations pour pouvoir y revenir si besoin et continuer l'exploration.

Deux opérations élémentaires sont nécessaires pour réaliser cette structure.

EMPILER(P,x) qui correspond à l'insertion de la donnée x au sommet de la pile P si celle-ci n'est pas pleine.   

DEPILER(P) qui retire la dernière donnée de P et la retourne si la pile n'est pas vide.

Afin de représenter une pile capable de contenir n éléments à l'aide d'un tableau de type `list`, on se propose de procéder ainsi : 

- la première case du tableau d'indice 0 contient **l'indice** du prochain élément à insérer dans la pile

- les cases suivantes du tableau (d'indices 1 à n) contiennent les éléments de la pile ou sont vides. La dernière case non vide du tableau est le sommet de la pile.

<img src="assets/pile.jpeg">

Le schéma ci-dessus donne la représentation d'une pile capable de contenir n=5 éléments à l'aide d'un tableau.

```python 
def creer_pile(Nombre_de_place):
    """
    créer une pile pouvant accueillir nombre de places
    >>> creer_pile(5)
    [1, None, None, None, None, None]
    """
	pass


def empiler(P, x):
    """
    insère la donnée x au sommet de la pile P
    sinon renvoie 'pile pleine'
    param : P : list
    param : x : int
    return : list
    >>> empiler([1, None, None, None, None, None], 8)
    [2, 8, None, None, None, None]
    >>> empiler([2, 8, None, None, None, None], 3)
    [3, 8, 3, None, None, None]
    >>> empiler([3, 8, 3, None, None, None], 5)
    [4, 8, 3, 5, None, None]
    >>> empiler([4, 8, 3, 5, None, None], 9)
    [5, 8, 3, 5, 9, None]
    >>> empiler([5, 8, 3, 5, 9, None], 7)
    [6, 8, 3, 5, 9, 7]
    >>> empiler([6, 8, 3, 5, 9, 7], 4)
    'pile pleine'
    >>> empiler([3, 8, 3, None, None, None], 7)
    [4, 8, 3, 7, None, None]
    """
	pass


def depiler(P):
    """
    modifie la valeur dans la case 0 et retourne la pile si elle n'est pas vide
    param : P : list
    return : list ou str
    >>> depiler([4, 8, 3, 5, None, None])
    [3, 8, 3, None, None, None]
    >>> depiler([1, None, None, None, None, None])
    'pile vide'
    >>> depiler([1, ')', None, None, None, None])
    'pile vide'
    >>> depiler([1, '(', None, None, None, None])
    'pile vide'
    """
	pass
```    

**Application 1** :

Voici un exemple d'utilisation des fonctions EMPILER et DEPILER dans le contexte de la gestion de l'historique de navigation dans un navigateur web :

```python 
# Initialisation de la pile pour stocker l'historique de navigation
historique = []

# Lorsque l'utilisateur accède à une nouvelle page web
url = "https://www.example.com"
EMPILER(historique, url)

# Lorsque l'utilisateur clique sur le bouton "Retour"
url_precedente = DEPILER(historique)
```   

**Application 2** :

On cherche à réaliser une fonction capable de dire si une expression mathématique est erronée ou non du point de vue du parenthésage en utilisant une pile.

On transforme pour cela à l'aide de `transforme_en_liste(E)` l'équation E en une liste de parenthèses ouvrantes ou fermantes. 

```python 
def transforme_en_liste(E):
    """
    transforme une expression mathématique en liste de parenthèses
    >>> transforme_en_liste('4*(3+5))')
    ['(', ')', ')']
    >>> transforme_en_liste('3+4*5')
    []
    """
	pass
```   
 
Puis, dans la fonction `verifier(E)`, on forme une pile pouvant accueillir au maximum tous ces caractères.  
On parcourt la liste des parenthèses.  

Lorsqu'on trouve une parenthèse ouvrante, on empile cette parenthèse ouvrante.  
Lorsqu'on trouve une parenthèse fermante, on dépile si P[0]>1, sinon on empile une parenthèse fermante.

À la fin, si P[0]=1, l'équation est correcte du point de vue du parenthésage, sinon elle est incorrecte.

<img src="assets/schema_pile.png">

```python 
def verifier(E):
    """
    renvoie True si l'expression E est cohérente du point de vue du parenthésage
    sinon False
    >>> verifier('4*(3+5))')
    False
    >>> verifier('4*(3+(5*7)+9)')
    True
    >>> verifier('4*(3+((5*7)+9)')
    False
    >>> verifier('')
    True
    >>> verifier('(()())')
    True
    >>> verifier(')(3+5)')
    False
    """
	pass
 ```

**2) Notion de file** : Une file est une structure de données linéaire dans laquelle les insertions se font à une extrémité appelée queue et les suppressions à l’autre extrémité appelée tête.

Elle suit le principe **FIFO** (First In First Out) :
le premier élément entré est le premier élément sorti.

Les opérations principales sur une file sont :
	•	enfiler : ajouter un élément en queue de la file ;
	•	défiler : retirer l’élément en tête de la file.

Indication : utiliser la méthode `pop()` des listes :

```python 

>>> liste=[2,5,9]
>>> liste.pop(1)
5
>>> liste
[2, 9]

```


```python 

def creer_file():
    """
    Crée une file vide.

    >>> f = creer_file()
    >>> f
    []
    """
    pass


def enfiler(f, x):
    """
    Ajoute un élément à la fin de la file.

    >>> f = creer_file()
    >>> enfiler(f, 10)
    >>> enfiler(f, 20)
    >>> f
    [10, 20]
    """
    pass


def defiler(f):
    """
    Retire et retourne le premier élément de la file.

    >>> f = creer_file()
    >>> enfiler(f, 10)
    >>> enfiler(f, 20)
    >>> defiler(f)
    10
    >>> f
    [20]
    """
	pass
 ```

**Application au parcours d'un graphe orienté**


<img width='200px' height='200px' src="assets/graphe2.png">

```python 
def plus_court_chemin(graphe, depart):
    """
    Parcours en largeur d'un graphe.

    >>> graphe = {
    ... 'A':['B','C'],
    ... 'B':['D'],
    ... 'C':['D'],
    ... 'D':[]
    ... }
    >>> plus_court_chemin(graphe,'A')
    ['A', 'B', 'C', 'D']
    """
	pass
 ```