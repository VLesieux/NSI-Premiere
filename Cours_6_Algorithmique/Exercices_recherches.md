## Exercices sur les algorithmes de recherche

L'instruction `random.randrange(n)` du module random effectue un tirage aléatoire d'un entier compris entre 0 inclus et n exclu.

1. Construire une liste par compréhension de 10**6 éléments en effectuant autant de tirages aléatoires. Visualiser la liste en affichant les variables dans Thonny.
2. Écrire une fonction qui recherche la présence d'un entier quelconque dans la liste, elle renvoie True s'il est présent, False sinon.
3. Écrire une fonction qui recherche à nouveau la présence d'un entier quelconque dans la liste, mais cette fois-ci par dichotomie. Ne pas oublier de trier la liste au préalable.
4. Grâce à la fonction time du module time, on peut lancer un chronomètre : `t0=time.time()` puis `t1=time.time()` avant et après une instruction pour mesurer la durée d'exécution d'une fonction. Comparer, sur une même liste initialement triée, la durée de la recherche de manière séquentielle à la durée de la recherche par dichotomie.

