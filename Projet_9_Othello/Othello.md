# Jeux à deux joueurs

## Les jeux à deux joueurs

Jeux bien connus, [Othello](https://fr.wikipedia.org/wiki/Othello_%28jeu%29), les échecs, les dames,  [Tic-tac-toe](https://fr.wikipedia.org/wiki/Tic-tac-toe), le [puissance 4](https://fr.wikipedia.org/wiki/Puissance_4),  [le jeu de Nim](https://fr.wikipedia.org/wiki/Jeux_de_Nim) et  bien d'autres, ont pour point commun d'être des "*jeux à deux joueurs au tour par tour*". Ils ont aussi en commun d'être des jeux  *à connaissance parfaite*, car, à tout moment, les deux joueurs possèdent exactement la même connaissance de l'état du jeu. De plus ils ne font pas intervenir le hasard. Ce sont ces jeux que nous allons étudier.

Ces jeux ont des points communs. Ainsi pour chacun, une partie est à tout moment caractérisée par le  *joueur courant*(le prochain qui doit jouer) et par un état du jeu, que nous appellerons  *situation courante*. Il s'agit par exemple

- de la configuration des pièces sur l'échiquier aux échecs,
- du nombre de cailloux restant à prendre dans le jeu de Nim
- etc ...

De plus, ces jeux partagent un mécanisme de déroulement des parties communes. Ce sont uniquement les  *règles du jeu* différentes d'un jeu à l'autre qui font la différence, pas la mécanique du jeu. Celle-ci se base principalement sur le fait que les joueurs jouent alternativement des "coups de jeu" en fonction de ce qui est autorisé par les règles du jeu. Ces différents coups font évoluer le jeu de situation en situation, jusqu'à ce que l'on atteigne une situation de fin de partie. Le déroulement d'une partie peut donc être décrit ainsi :

**Déroulement des jeux à deux joueurs**

1. installer le jeu, c'est-à-dire créer la  *situation courante* initiale
2. déterminer le premier  *joueur courant*
3. si le jeu n'est pas fini
   - si le  *joueur courant* peut jouer dans la  *situation courante*
     - le  *joueur courant* joue  
       
       c'est-à-dire qu'il choisit un coup possible parmi les coups autorisés dans la  *situation courante* du jeu. Chaque coup de jeu amène le jeu dans une nouvelle situation. Donc choisir un coup de jeu (= jouer) revient à choisir la prochaine  *situation courante* parmi toutes celles possibles.  
    	 - mettre à jour la  *situation courante*suite au choix du joueur
   - sinon
     - ne rien faire (la  *situation courante*ne change pas)
   - l'autre joueur devient le  *joueur courant*
   - recommencer en 3.
4. sinon le jeu est fini  
   
   afficher le résultat (le joueur vainqueur ou partie nulle)

Ce mécanisme de jeu nous fournit un algorithme permettant de jouer aux jeux à deux joueurs qui nous concernent. Cet algorithme est le même pour tous ces jeux. Les variations sont dues uniquement aux règles du jeu. Une analyse de cet algorithme doit permettre d'identifier les fonctions qu'il est nécessaire de définir pour n'importe quel jeu à deux joueurs afin de pouvoir y jouer grâce à cet algorithme.

Une des premières tâches que vous devez réaliser est donc cette analyse afin de produire  **l'interface** des jeux à deux joueurs.

**Programme `main.py` des jeux à deux joueurs**:

```python
def jouer():
    config = jeu.creer_config_init()
    joueur_courant = jeu.choisir_premier_joueur()
    jeu.afficher_config(config)

    while not jeu.est_jeu_fini(config):
        if jeu.est_coup_possible(config, joueur_courant) :
            coup = jeu.coup_joueur(config, joueur_courant)
            config = jeu.incrementer_config(config,coup,joueur_courant)
            jeu.afficher_config(config)
        joueur_courant = jeu.incrementer_joueur(joueur_courant)
    jeu.afficher_fin(config,joueur_courant)


if __name__ == "__main__":
    jouer()    
```

## Travail à réaliser

Par binôme il faut mettre en œuvre un module qui permette:

* de jouer aux jeux à deux joueurs avec le jeu de l'Othello en utilisant un import dans le programme`main.py.`

* Il faudra définir dans le module la mise en œuvre du jeu Othello en utilisant la ressouce ci-dessous.

* À l'issue de cette phase on doit pouvoir jouer au jeu dans une version  *humain contre humain*par des saisies au clavier du coup joué.

* On peut aussi envisager de faire des parties  *humain contre aléatoire*, le deuxième joueur étant géré par le programme qui joue aléatoirement.

## Présentation du jeu

#### Objectif:

Othello se joue à 2, sur un plateau unicolore de 64 cases (8 sur 8), avec des pions bicolores, noirs d'un côté et blancs de l'autre. Le but du jeu est d'avoir plus de pions de sa couleur que l'adversaire à la fin de la partie, celle-ci s'achevant lorsque aucun des deux joueurs ne peut plus jouer de coup légal, généralement lorsque les 64 cases sont occupées. Au début de la partie, la position de départ est indiquée ci-contre. Les noirs commencent.

![jeu](imgs/othello1.png)

***situation de départ***==>

#### Règles:

Chacun à son tour, les joueurs vont poser un pion de leur couleur sur une case vide, adjacente à un pion adverse. Chaque pion posé doit obligatoirement encadrer un ou plusieurs pions adverses avec un autre pion de sa couleur, déjà placé.  Il retourne alors le ou les pions adverse(s) qu'il vient d'encadrer. Les pions ne sont ni retirés de l'othellier, ni déplacés d'une case à l'autre.  

On peut encadrer des pions adverses dans les huit directions et plusieurs pions peuvent être encadrés dans chaque direction.

![img](imgs/othello2.png)

Par exemple, le joueur Noir a joué en c6. Il retourne alors les pions b6, b5, d7, c5 et c4. Il n'y a pas de réaction en chaîne : les pions retournés ne peuvent pas servir à en retourner d'autres lors du même tour de jeu. Si un joueur ne possède aucun coup permettant le retournement de pions adverses, celui-ci passe son tour et c'est à l'adversaire de jouer.

![img](imgs/othello3.png)

Vous pouvez visiter le lien suivant [http://www.lecomptoirdesjeux.com/regle-reversi.htm](http://www.lecomptoirdesjeux.com/regle-reversi.htm) pour plus d'informations sur les règles du jeu

## Programmation du jeu

#### Représentaion du plateau de jeu

Le plateau sera représenté par une grille qui sera techniquement une liste de liste de nombres entiers. Les nombres entiers réprésentent:

* une case vide du plateau

* une case avec un pion NOIR

* une case avec un pion BLANC

Exemple de liste:

```python
[[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 2, 1, 0, 0, 0, 0],
[0, 0, 0, 0, 1, 2, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
```

Cette liste représente le plateau de début de partie avec uniquement deux pions blancs et deux pions noirs en diagonal au centre (situation de départ).

***Travail à faire***

* Réaliser une fonction `creer_config_init` qui ne prend pas de paramètres et qui renvoie une liste de liste correspondant a la configuration de départ du jeu.

* Réaliser une fonction `afficher_config` qui ne prend en paramètre la liste de liste représentant la configuratuion jeu.  Cette fonction affiche le plateau dans le shell:

```python
    1  2  3  4  5  6  7  8  
1   ·  ·  ·  ·  ·  ·  ·  ·  
2   ·  ·  ·  ·  ·  ·  ·  ·  
3   ·  ·  ·  ·  ·  ·  ·  ·  
4   ·  ·  ·  ◎  ◉  ·  ·  ·  
5   ·  ·  ·  ◉  ◎  ·  ·  ·  
6   ·  ·  ·  ·  ·  ·  ·  ·  
7   ·  ·  ·  ·  ·  ·  ·  ·  
8   ·  ·  ·  ·  ·  ·  ·  · 
```

#### Gestion des joueurs

* Réaliser une fonction `incrementer_joueur` qui prend en paramètre une variable joueur qui représente le joureur courant. La fonction retourne cette même variable joueur après avoir switcher:

```python
>>> incrementer_joueur(JOUEUR_NOIR)
2
>>> incrementer_joueur(JOUEUR_BLANC)
1
```

Dans cet exemple `JOUEUR_NOIR=1` et `JOUEUR_BLANC=2`. La fonction bascule de JOUEUR_NOIR à JOUEUR_BLANC sur la première ligne. Puis l'inverse sur la deuxième ligne.

#### Gestion et validité des coups

Pour pouvoir jouer il faut savoir, dans un premier temps, si le joueur courant peut placer un pion de sa couleur sur le plateau. 

---

***Travail à faire***

* Réalier une fonction `test_dir_valide`qui prend en paramètre la configuration du jeu, les coordonnées de la "case à tester", une liste de directions possibles et le joueur courant. Cette fonction renvoie `True`si le joueur courant peu jouer sur la "case à tester"  et `False` dans le cas contraire:

```python
>>> config = creer_config_init()
>>> test_dir_valide(config,(3,3),Direction(0,-1),JOUEUR_BLANC)
False

>>> config = creer_config_init()
>>> test_dir_valide(config,(3,4),Direction(1,0),JOUEUR_NOIR)
True
```

Le premier teste **valide** qu'un **pion blanc** peut être placé sur la case de coordonnées **(3,3) **et qu'il pourra retourner un ou des pions noirs dans la direction des **y <0** (vers le haut du plateau).

Le deuxième teste **ne valide pas** qu'un **pion noir** placé sur la case **(3,4)** retournera des ou un pion blanc dans la direction **x>0** (vers la droite du plateau).

---

* Réaliser une fonction `est_coup_possible` qui,prend en paramètre la configuration du jeu et le joueur courant. Cette fonction renvoie vrai si le joueur courant peu jouer et faux dans le cas contraire:

```python
>>> config = creer_config_init()
>>> est_coup_possible(config,NOIR)
True

>>> config = [[NOIR for _ in range(10)] for _ in range(10)]
>>> est_coup_possible(config,BLANC)
False
```

Le premier test renvoie `True` car la configuration est le plateur de début de partie. Le deuxième test renvoie `False` car la configuration du jeux est un plateau rempli de pions noir.

***Remarque: l'utilisation de la fonction `test_dir_valide` est recommandé.***

Afin de pouvoir stopper le jeu, il nous faut savoir si les joueurs peuvent encore jouer.

* Réaliser une fonction `est_jeu_fini` qui prend en paramètre la configuration du jeu. Cette fonction renvoie `False` si un des deux joueurs peut jouer et `True` dans le cas contraire.

```python
>>> config = creer_config_init()
>>> est_jeu_fini(config)
False

>>> config = [[NOIR for _ in range(10)] for _ in range(10)]
>>> est_jeu_fini(config)
True
```

---

Il faut a présent que les deux joueurs puissent saisir les coordonnées des coups qu'il souhaite jouer. Le format le plus simple serait une saisie de coordonnées x y sous la forme `23` pour` x=2` et `y=3`.

---

***Travail à faire***

* Réaliser une fonction `verif_coup_valide` qui prend en paramètre la configuration du jeu, les coordonnées de la case à tester et le joueur courant. Cette fonction renvoie True si le coup est valide et False dans le cas contraire:

```python
>>> s = creer_config_init()
>>> verif_coup_valide(s,(3,4),JOUEUR_NOIR)
True

>>> s = creer_config_init()
>>> verif_coup_valide(s,(3,4),JOUEUR_BLANC)
False
```

Le premier test donne True car il est possible de placer un pion noir sur le plateau de départ à la case (3,4) ==> le pion blanc en (4,4) sera retourné.

Le deuxime test donne False car il n'est pas possible de placer un pion blanc en (3,4) car il n'y a pas de possibilité de retournement.

* Réaliser une fonction `coup_joueur` qui prend en paramètre la configuration du jeu et le joueur courant. Elle renvoie une variable `coup`qui contient les coordonnées de la case ou le joueur désire placer son pion. Une vérification de la validité du coup sera faite, si le coup n'est pas valable le joueur est invité a saisire de nouvelles valeurs au clavier:

```python
>>> config = creer_config_init()
>>> coup_joueur(config,JOUEUR_NOIR)
Aux joueur pions NOIR de jouer...
Donner les coordonnées de la case choisie pour jouer au format xy
```

La fonction attend la saisie de valeurs au clavier.

Il faut pour terminer actualiser la configuration du jeu suit au coup du joueur courant.

* Réaliser une fonction `incrementer_config` qui prend en paramètre la configuration du jeu, les coordonnées de la case à jouer etle joueur courant. Cette fonction modifie la configuration du jeu en ajoutant le nouveau pion et en retournant le ou les pions de couleur opposée:

```python
>>> s = creer_config_init()
>>> incrementer_config(s,(3,4),JOUEUR_NOIR)
[[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
[0, 0, 0, 0, 1, 2, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
```

Le test montre le nouveau pion noir en (3,4) ainsi que le retournement du pion en (4,4) qui était blanc à l'état initial du plateau .

#### Test du jeu dans le module main.py

Afin de tester le bon fonctionnement de votre jeu d'Othello, il faut au préalable configurer correctement le module `main`.

* Compléter le fichier `main.py` en important toutes les fonctions de votre module `othello` sous le nom jeu:

```python
???

def jouer():
 config = jeu.creer_config_init()
 joueur_courant = jeu.choisir_premier_joueur()
 jeu.afficher_config(config)
  while not jeu.est_jeu_fini(config):
 if jeu.est_coup_possible(config, joueur_courant) :
 coup = jeu.coup_joueur(config, joueur_courant)
 config = jeu.incrementer_config(config,coup,joueur_courant)
 jeu.afficher_config(config)
 joueur_courant = jeu.incrementer_joueur(joueur_courant)
 jeu.afficher_fin(config,joueur_courant)
  if __name__ == "__main__":
 jouer()
```

* Tester le bon fonctionnement.

* Que ce passe t-il en fin de partie?

* Quelle fonction manque t-il dans votre module?

* Réaliser cette fonction, et tester de nouveau votre jeu.

#### Amélioration du jeu

Nous allons a présent modifier notre module `othello`afin de pourvoir jouer contre l'ordinateur.

* Proposer une modification de la fonction `coup_joueur`  en utilisant le module `random`.
