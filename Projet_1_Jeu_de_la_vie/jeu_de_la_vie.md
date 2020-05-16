# Jeu de la vie

Le jeu de la vie est une modélisation simpliste de la vie de cellules dans
l'espace. Dans le cadre de cet exercice l'espace sera une grille rectangulaire
dont chaque case peut contenir au plus une cellule. Chaque case contiendra
donc soit 0 soit 1 cellule. Les cellules peuvent émerger ou mourir selon des
critères précis à réévaluer à chaque nouvelle génération :
1. Une cellule émergera dans une case qui possède exactement trois voisines
   avec une cellule.
2. Une cellule disparaît de sa case si elle est entourée par strictement moins
   de deux cellules vivantes ou strictement plus de trois cellules vivantes.
3. Les autres cases restent dans leur état.

Les voisines prises en compte sont toutes les cases situées immédiatement à
gauche, à droite, en haut, en bas ou sur les quatre diagonales, si elles existent.
Une case a donc au plus 8 voisines, moins si elle se situe sur un bord de la grille.

## Représentation d'une grille

Du point de vue technique une grille du jeu de la vie sera représentée par une
liste de listes de nombre entiers. Chaque nombre entier représente le nombre
de cellules vivantes dans une case de la grille (0 ou 1).
Par exemple la liste :
```
[ [0, 1, 0], [1, 0, 0] ]
```
représente une grille de jeu de 6 cases, 3 cases en largeur et 2 cases en
hauteur. Sur la première ligne seule la deuxième case possède une cellule, 
tandis que sur la deuxième ligne, seule la première case en possède une.


### Construction d'une grille vide

Réalisez une fonction `creer_grille` qui prend en paramètre le nombre de cases
horizontalement, puis verticalement et qui renvoie une liste de listes
correspondant à une grille du jeu de la vie aux dimensions souhaitées, ne
contenant aucune cellule.

```
>>> creer_grille(3, 2)
[[0, 0, 0], [0, 0, 0]]
```

### Dimensions d'une grille

Réalisez une fonction `hauteur_grille` qui prend en paramètre une grille de
jeu de la vie et qui renvoie le nombre de cases verticalement.

```
>>> hauteur_grille(creer_grille(3, 2))
2
```

Réalisez une fonction `largeur_grille` qui prend en paramètre une grille de
jeu de la vie et qui renvoie le nombre de cases horizontalement.
``` 
>>> largeur_grille(creer_grille(3, 2))
3
```

### Initialisation d'une grille

La grille créée par la fonction `creer_grille` ne contient aucune cellule.
Réalisez une fonction `creer_grille_aleatoire` qui prend en paramètre les
dimensions horizontales et verticales de la grille et une probabilité *p*, qui
est la probabilité pour une case de la grille d'avoir une cellule.

```
>>> creer_grille_aleatoire(3, 2, 1)
[[1, 1, 1], [1, 1, 1]
>>> creer_grille_aleatoire(3, 2, 0)
[[0, 0, 0], [0, 0, 0]]
>>> creer_grille_aleatoire(3, 2, 0.5)
[[1, 0, 1], [0, 0, 1]]
```

### Voisins d'une case

Réalisez une fonction `voisins_case` qui prend en paramètre une grille de jeu
de la vie ainsi que les coordonnées en abscisse et en ordonnée de la case (la
coordonnée 0,0 étant la case en haut à gauche).  La fonction renvoie une liste
contenant la valeur des cases voisines de la case donnée en paramètre.
Le nombre de valeurs retournées dans la liste correspond au nombre de voisines de la case (au plus huit, 
moins quand elle se trouve sur un bord de la grille).
L'ordre dans lequel les valeurs sont renvoyées n'est pas spécifié.  Cependant
dans l'exemple ci-dessous les valeurs des cases voisines sont renvoyées ligne par ligne, de gauche
à droite.

Pour les exemples qui suivent (jusqu'à la fin de l'énoncé), nous considérons
définie une variable grille :
```
grille = [[0, 1, 0], [1, 0, 0], [1, 1, 1]]
```

```
>>> voisins_case(grille, 1, 1)
[0, 1, 0, 1, 0, 1, 1, 1]
>>> voisins_case(grille, 2, 2)
[0, 0, 1]
>>> voisins_case(grille, 0, 2)
[1, 0, 1]

```

### Nombre de cellules dans le voisinage

Réalisez une fonction `nb_cellules_voisins` qui prend en paramètre une grille
ainsi que les coordonnées d'une case et qui renvoie le nombre de cellules dans
les cases voisines de la case passée en paramètre.

```
>>> nb_cellules_voisins(grille, 1, 1)
5
>>> nb_cellules_voisins(grille, 2, 2)
1
```

## Afficher une grille

Visualiser une grille sous forme de listes de listes n'est pas aisé.  Nous
allons donc réaliser une procédure `afficher_grille` dont le rôle sera
d'afficher de manière plus claire une grille du jeu de la vie qui lui est
passée en paramètre.  Les cases vides seront affichées avec un tiret bas (`_`)
et les cases contenant une cellule seront affichées avec un o majuscule
(`O`). Le contenu des cases sera séparé par une espace. Chaque ligne de la grille
sera affichée sur une ligne distincte.

C'est la **seule** fonction ou procédure qui pourra utiliser un `print`.

```
>>> afficher_grille(grille)
_ O _
O _ _
O O O
>>> afficher_grille(creer_grille(3, 2))
_ _ _
_ _ _
```


## Évolution d'un jeu de la vie
### Génération suivante

Nous allons maintenant réaliser une fonction qui, à partir d'une grille passée
en paramètre, calcule la grille de la génération suivante et la retourne.  La
nouvelle génération est calculée à partir des critères d'émergence ou de mort
des cellules indiqués au début de l'énoncé.
Dans le jeu de la vie, on considère que la nouvelle génération apparaît spontanément dans toutes les cellules au même moment.

```
>>> generation_suivante(grille)
[[0, 0, 0], [1, 0, 1], [1, 1, 0]]
>>> generation_suivante([[0, 0, 0], [1, 0, 1], [1, 1, 0]])
[[0, 0, 0], [1, 0, 0], [1, 1, 0]]
>>> generation_suivante([[0, 0, 0], [1, 0, 0], [1, 1, 0]])
[[0, 0, 0], [1, 1, 0], [1, 1, 0]]
```

### Évolution au fil de n générations

Nous allons réaliser une procédure `evolution_n_generations` qui prend en
paramètre une grille et un entier naturel `n` et qui va afficher l'évolution
de la grille au fil de `n` générations.  Afin de mieux visualiser l'évolution
nous ferons une pause d'une seconde entre chaque génération.  La fonction
`sleep` du module `time` vous permettra de faire une telle pause (allez voir
la documentation de cette fonction pour savoir comment l'utiliser).

<!-- Ajouter la contrainte que la grille ne doit pas être vide ? -->

### Motifs récurrents

Quelques motifs récurrents peuvent être obtenus à partir de grilles
particulières.

Par exemple, un oscillateur à deux états peut être obtenu avec cette grille :
```
[[0, 0, 1, 0], [1, 0, 0, 1], [1, 0, 0, 1], [0, 1, 0, 0]]
```

Le planeur est un motif qui se déplace jusqu'à disparaître de la grille. Voici
une grille permettant d'obtenir un planeur qui se répète toutes les quatre
générations en s'étant déplacé d'une case vers le bas et d'une case vers 
la droite à chaque génération :
```
[[0, 1, 0, 0, 0], [0, 0, 1, 0, 0], [1, 1, 1, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
```

# Ressources additionnelles

Vous trouverez des motifs plus complexes sur la [page Wikipedia du jeu de la
vie](https://fr.wikipedia.org/wiki/Jeu_de_la_vie#Structures), en particulier
dans sa [version
anglophone](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life#Examples_of_patterns).
Cette [vidéo didactique](https://www.youtube.com/watch?v=S-W0NX97DB0) de David Louapre présente le jeu de la vie et des structures complexes.
