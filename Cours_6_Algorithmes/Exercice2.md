## Exercices sur les algorithmes de tri
### Rappels

1. Rappeler le principe du tri par sélection et essayer de retrouver l'algorithme de ce tri par vous-même.
2. De même pour le tri par insertion.

### Application 1 : Ordre lexicographique

L'objectif est d'écrire un programme qui trie une liste de mots et les range suivant l'ordre lexicographique (ordre des dictionnaires).

1. Écrire une fonction ordre_alphabet qui prend en arguments deux caractères alphabétiques c1 et c2 et renvoie -1 si c1 est avant c2, 1 si c2 est avant c1 et 0 si c1 = c2. On pourra utiliser la méthode index qui renvoie l'indice d'un élément dans une chaîne de caractères.
2. Écrire une fonction ordre_lexicographique qui prend en arguments deux mots m1 et m2 et renvoie -1 si m1 est avant m2, 0 si m1 et m2 sont identiques et 1 si m1 est après m2.
3. Écrire une fonction tri_lexicographique qui prend en argument une liste de mots et trie cette liste, en utilisant le tri par sélection.

### Application 2 : Trier des points

On dispose de points dans un plan muni d'un repère orthonormé d'origine O. Ces points possèdent un couple de coordonnées représenté par la liste [x,y].  
On se propose de trier ces points en fonction de leur distance à O, de la plus petite à la plus grande.

Indications: 

- écrire une fonction distance qui prend en paramètre une liste de deux nombres, nommée point, qui représente les coordonnées d'un point du plan
- écrire une fonction compare qui prend en paramètre deux listes p1 et p2 représentant deux points P1 et P2 et qui renvoie -1 si P1 est plus proche de O que P2, 1 si P2 est plus proche de O que P1, et 0 si les deux points sont équidistants
- écrire une fonction tri_points qui prend en paramètre une liste de points et qui trie cette liste suivant la distance à O, en utilisant le tri par insertion.






