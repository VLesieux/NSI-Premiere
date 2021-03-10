## Exercices sur les algorithmes de recherche

#### Exercice 1 : Recherche de l'indice d'une valeur dans un tableau

[Sujet Bac Terminale exercice 1](https://github.com/VLesieux/NSI-Terminale/blob/master/Banque_Sujets_2021/21_NSI_01/21-NSI-01.pdf)

#### Exercice 2 : Recherche d'un minimum pour une fonction donnée

[Sujet Bac Terminale exercice 2](https://github.com/VLesieux/NSI-Terminale/blob/master/Banque_Sujets_2021/21_NSI_01/21-NSI-01.pdf)

#### Exercice 3 : Recherche d'une moyenne

[Sujet Bac Terminale exercice 1](https://github.com/VLesieux/NSI-Terminale/blob/master/Banque_Sujets_2021/21_NSI_02/21-NSI-02.pdf)

#### Exercice 4 : Recherche par dichotomie

L'instruction `random.randrange(n)` du module random effectue un tirage aléatoire d'un entier compris entre 0 inclus et n exclu.

1. Construire une liste par compréhension de 10**6 éléments en effectuant autant de tirages aléatoires. Visualiser la liste en affichant les variables dans Thonny.
2. Écrire une fonction qui recherche la présence d'un entier quelconque dans la liste, elle renvoie True s'il est présent, False sinon.
3. Écrire une fonction qui recherche à nouveau la présence d'un entier quelconque dans la liste, mais cette fois-ci par dichotomie. Ne pas oublier de trier la liste au préalable.
4. Grâce à la fonction time du module time, on peut lancer un chronomètre : `t0=time.time()` puis `t1=time.time()` avant et après une instruction pour mesurer la durée d'exécution d'une fonction. Comparer, sur une même liste initialement triée, la durée de la recherche de manière séquentielle à la durée de la recherche par dichotomie.

Résultat obtenu:

```python
True
durée recherche séquentielle 0.0003178119659423828
True
durée recherche par dichotomie 0.00013518333435058594
```