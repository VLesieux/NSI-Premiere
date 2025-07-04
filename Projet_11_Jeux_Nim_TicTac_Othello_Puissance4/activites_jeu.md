## Réalisation d&#39;une IHM (Interface Homme Machine) commune à un ensemble de jeux.

**1. Introduction.**

Les jeux comme Othello, les échecs, les dames, Tic-tac-toe, le puissance 4, le jeu de Nim ont pour point commun d&#39;être des &quot; _jeux à deux joueurs au tour par tour_ &quot;.

Ces jeux partagent un mécanisme de déroulement des parties qui est commun. Ce sont uniquement les _règles du jeu_ qui différent.

**Déroulement des jeux à deux joueurs :**

1. Installer le jeu, c&#39;est-à-dire créer la _situation courante_ initiale.
2. Déterminer le premier _joueur courant_.
3. **Si le jeu n&#39;est pas fini**
  - si le _joueur courant_ peut jouer dans la _situation courante_, 
     - le _joueur courant_ joue, c&#39;est-à-dire qu&#39;il choisit un coup possible parmi les coups autorisés dans la _situation courante_ du jeu. Chaque coup de jeu amène le jeu dans une nouvelle situation. Donc choisir un coup de jeu (= jouer) revient à choisir la prochaine _situation courante_ parmi toutes celles possibles.
     - mettre à jour la _situation courante_ suite au choix du joueur
     - afficher celle-ci
  - sinon
     - ne rien faire (la _situation courante_ ne change pas)
     - l&#39;autre joueur devient le _joueur courant_
  - recommencer en 3.
4. Le jeu est fini, afficher le résultat de la partie : le nom du joueur vainqueur ou partie nulle.

  

**2. Exemple du jeu de Nim**. ([wikipédia](https://fr.wikipedia.org/wiki/Jeux_de_Nim))

Les règles du jeu sont simples :

- On dispose un tas d&#39;allumettes au milieu de la table.
- Les (deux) joueurs ramassent tour à tour 2 ou 3 allumettes. Celui qui prend les 2 ou 3 dernières allumettes a gagné.
- S&#39;il ne reste qu'une seule allumette, le jeu est nul.

Commençons par analyser le programme fourni : **jeu\_nim.py**

```python
def situation_init():
    """
    : création de la situation initiale du jeu
    : renvoie le nombre d'allumettes du tas
    : param : Rien
    : return : nb_allumettes
    Exemple:
    >>> situation_init()
    11
    """
    nb_allumettes=11
    return nb_allumettes

def choix_joueur(valeur_joueur,param_jeu):
    """
    : Demande au joueur d'effectuer un choix d'allumettes à enlever (2 ou 3)
    : param : bool(valeur_joueur) identification du joueur (True:I;False:II)
    : param : int(param_jeu) nombres d'allumettes
    : return : int(choix) choix du joueur
    Remarque: Ne pas faire de doctest sur des fonctions d'entrées /sorties
    """
    if valeur_joueur:
        joueur='I'
    else:
        joueur='II'
    #init choix jeu
    nb_enlev=0
    #Les joueurs doivent ramasser tour à tour 2 ou 3 allumettes
    while (nb_enlev!=2 and nb_enlev!=3):
        nb_enlev= int(input('JOUEUR {} : Choisir le nombre d\'allumettes à enlever : '.format(joueur)))

    choix=test_validite_choix(valeur_joueur,nb_enlev,param_jeu)
    return choix

def test_validite_choix(valeur_joueur,lechoix,tas):
    """
    : test de la validité du choix 2 ou 3 allumettes
    : param : bool(valeur_joueur) identification du joueur (True:I;False:II)
    : param lechoix: (int) valeur allumettes à supprimer
    : param tas: (int) le nombre d'allumettes presentes
    : return : int(choix) le choix validé ou non du joueur
    """
    correct=False
    if (((lechoix==2) &(tas>=2))|((lechoix==3) &(tas>=3))):
        correct=True
    else:
        lechoix=choix_joueur(valeur_joueur,tas)
        return lechoix
    if correct:
        return lechoix
    return None

def action_joueur(valeur_joueur,param_jeu):
    """
    : permet de connaitre le nombre d'allumettes à enlever
    : param : bool(valeur_joueur) identification du joueur (True:I;False:II)
    : return : int(choix) choix du joueur
    """
    lechoix=choix_joueur(valeur_joueur,param_jeu)
    return lechoix

def evolution_jeu(valeur_joueur,param_jeu,choix_joueur):
    """
    : permet de faire évoluer le jeu
    : param : int(param_jeu) nombres d'allumettes
    : param : bool(valeur_joueur) identification du joueur (True:I;False:II)
    : return : int(param_jeux) le nombres d'allumettes restantes
    Exemple:
    >>> evolution_jeu(True,11,2)
    9
    """
    param_jeu=param_jeu-choix_joueur
    return param_jeu

def aff_evolution_jeu(param_jeu):
    """
    : permet d'afficher le nombre d'allumettes restantes
    : param : int(param_jeu) nombres d'allumettes
    : return : None
    Exemple:
    >>> aff_evolution_jeu(9)
    Il reste 9 allumettes sur la table
    """
    print('Il reste {} allumettes sur la table'.format(param_jeu))
    return None

def etat_final(param_jeu):
    """
    : vérification si fin jeu
    : param : int(param_jeu) nombres d'allumettes
    : return : bool(fini),bool(per_gag)
    Exemple:
    >>> etat_final(0)
    (True, False)
    """
    per_gag=False
    #per_gag=True désigne le cas d'égalité
    #fini désigne l'état de la partie qui est finie ou non
    if ((param_jeu==0)|(param_jeu==1)):
        fini=True
        if param_jeu==1:
            per_gag=True
    else:
        fini=False
    return fini,per_gag

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)


```

2.1 Combien de fonctions composent le jeu de Nim ? Donner, par écrit, leurs noms et leurs rôles, indiquer les paramètres retournés ainsi que leur type (bool,int,str..).

2.2 Faire l&#39;analogie entre les fonctions du jeu de Nim et le déroulement des jeux à deux joueurs si cela est possible.

2.3 D&#39;après l&#39;analyse précédente, peut-on utiliser le jeu tel quel ? Si non, expliquer ce qui manque.

On décide de rendre le code opérationnel, pour cela il faut respecter l&#39;ordre de déroulement des jeux à deux joueurs.

2.4 Compléter le programme **interface_jeu.py** donné ci-dessous pour rendre le jeu opérationnel, tester le bon fonctionnement de votre solution.

```python
# coding: UTF-8

import jeu_nim as jeu #importation des fonctions du jeu Nim 

def aff_mess_vainqueur(valeur_joueur,per_gag):
    """
    : affichage du gagnant
    : param : bool(valeur_joueur)  identification du joueur (True:I;False:II)
    : param : bool(per_gag)  identification gagné ou égalité (True:gagné;False:égalité)
    : return : None
    Exemple:
    >>> aff_mess_vainqueur(True,False)
    Le joueur I a gagné
    """
    if valeur_joueur:
        joueur='I'
    else:
        joueur='II'      
        
    if per_gag:
        print('Egalité !!!!')
    else:
        if valeur_joueur:
            #gagné
            print('Le joueur {} a gagné'.format(joueur))
        else:
            #perdu
            print('Le joueur {} a gagné'.format(joueur))

    return None

param_jeu = jeu.situation_init()    #création de la situation courante initiale

valeur_joueur=False #Détermination du premier joueur courant

jeu.aff_evolution_jeu(param_jeu)    #Affichage de l'état du jeu

fini=False  #Initialisation de la situation du jeu

while not fini: # Voir le point 3 de l'introduction : si le jeu n'est pas fini

##############################

Cette partie est à compléter : 

5 à 7 lignes de code utilisant les fonctions définies dans jeu_nim.py, remarquer que certaines fonctions en appellent d'autres.

#################

aff_mess_vainqueur(vainqueur,per_gag)   # jeu fini et affichage du résultat.
# cette ligne de code sera réalisée lorsque la partie sera finie


```
Exemples de partie :

```python
Il reste 11 allumettes sur la table
JOUEUR II : Choisir le nombre d'allumettes à enlever : 2
Il reste 9 allumettes sur la table
JOUEUR I : Choisir le nombre d'allumettes à enlever : 3
Il reste 6 allumettes sur la table
JOUEUR II : Choisir le nombre d'allumettes à enlever : 3
Il reste 3 allumettes sur la table
JOUEUR I : Choisir le nombre d'allumettes à enlever : 3
Il reste 0 allumettes sur la table
Le joueur I a gagné
```
```python
Il reste 11 allumettes sur la table
JOUEUR II : Choisir le nombre d'allumettes à enlever : 2
Il reste 9 allumettes sur la table
JOUEUR I : Choisir le nombre d'allumettes à enlever : 2
Il reste 7 allumettes sur la table
JOUEUR II : Choisir le nombre d'allumettes à enlever : 2
Il reste 5 allumettes sur la table
JOUEUR I : Choisir le nombre d'allumettes à enlever : 2
Il reste 3 allumettes sur la table
JOUEUR II : Choisir le nombre d'allumettes à enlever : 3
Il reste 0 allumettes sur la table
Le joueur II a gagné
```
```python
Il reste 11 allumettes sur la table
JOUEUR II : Choisir le nombre d'allumettes à enlever : 2
Il reste 9 allumettes sur la table
JOUEUR I : Choisir le nombre d'allumettes à enlever : 2
Il reste 7 allumettes sur la table
JOUEUR II : Choisir le nombre d'allumettes à enlever : 3
Il reste 4 allumettes sur la table
JOUEUR I : Choisir le nombre d'allumettes à enlever : 3
Il reste 1 allumettes sur la table
Egalité !!!!
```

**Votre solution ayant été validée**, on vous demande de concevoir maintenant un nouveau jeu (tic tac toe) en vous inspirant du jeu Nim.

**Contraintes:**

- le programme principale doit être le même que celui définit pour le jeu Nim, où la chaîne de caractères &quot;jeu\_nim&quot; est remplacée par &quot;jeu\_tic\_tac&quot;.

- les fonctions du jeu &quot;jeu\_tic\_tac&quot;  devront être implémentées dans le fichier &quot;jeu\_tic\_tac.py&quot; fourni dans le dossier du projet.

- Quatre fonctions doivent permettre de tester l&#39;alignement de trois symboles identiques, horizontalement, verticalement ou en diagonale .

**3. Le jeu du Tic-tac-toe**. (**[wikipédia](https://fr.wikipedia.org/wiki/Tic-tac-toe)**)**

À partir de votre lecture sur wikipédia :

3.1 Donner l&#39;autre nom du jeu ?

3.2 Quel est l&#39;élément support du jeu ?

3.3 Quel est le but de ce jeu ?

3.4  Par convention, quel est le symbole utilisé par le joueur n°1, par le joueur n°2 ?

3.5 Comment en python peut-on représenter l&#39;élément support de ce jeu ?

3.6 Écrire en python, le code qui permet de créer le plateau de jeu vide (le vide sera représenté par le caractère « - ») et le tester.

3.7 À quelle situation du jeu, ce plateau vide correspond-t-il ?   Quelle était la fonction correspondant du jeu de Nim ?

3.8 Implémenter cette fonction pour le jeu Tic-Tac-Toe.

Tester son bon fonctionnement avec le doctest.

```python
>>> situation_init()
[['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
```

**Attention !**

Ne pas écrire : 
```python
return [['-']*3]*3
```
en effet: 
```python
>>> a=situation_init()
>>> a[1][1]='X'
>>> a
[['-', 'X', '-'], ['-', 'X', '-'], ['-', 'X', '-']]
```

3.9 Écrire la fonction &quot;test\_ligne&quot;  qui a pour résultat l&#39;état d&#39;une ligne (remplie ou pas remplie) dont le plateau de jeu est passé en paramètre.

Prévoir le test de cette fonction, commun pour les joueurs 1 et 2.

Tester son bon fonctionnement avec le doctest.

```python
>>> test_ligne([['-', 'X', '-'], ['X', 'X', 'X'], ['0', '-', '0']])
True
>>> test_ligne([['-', 'X', '-'], ['0', 'X', 'X'], ['0', '-', '0']])
False
```

3.10 Écrire la fonction &quot;test\_diagonale1&quot; (orientée vers le haut) qui a pour résultat l&#39;état d&#39;une diagonale (remplie, pas remplie) dont le plateau de jeu est passé en paramètre.

Prévoir le test de cette fonction, commun pour les joueurs 1 et 2.

Tester son bon fonctionnement avec le doctest.

```python
>>> test_diagonale1([['-', 'X', '-'], ['X', 'X', 'X'], ['0', '-', '0']])
False
>>> test_diagonale1([['-', 'X', '0'], ['0', '0', 'X'], ['0', '-', '0']])
True
```

3.11 Écrire la fonction &quot;test\_colonne&quot;  qui a pour résultat l&#39;état d&#39;une colonne (remplie, pas remplie) dont le plateau de jeu est passé en paramètre.

Prévoir le test de cette fonction pour les joueurs 1 et 2.

Tester son bon fonctionnement avec le doctest.

```python
>>> test_colonne([['0', 'X', '-'], ['0', 'X', 'X'], ['0', '-', '0']])
True
>>> test_colonne([['-', 'X', '-'], ['0', 'X', 'X'], ['0', '-', '0']])
False
```

3.12 Écrire la fonction &quot;test\_diagonale2&quot; (orientée vers le bas) qui a pour résultat l&#39;état d&#39;une diagonale (remplie, pas remplie) dont le plateau de jeu est passé en paramètre.

Prévoir le test de cette fonction pour les joueurs 1 et 2.

Tester son bon fonctionnement avec le doctest.

```python
>>> test_diagonale2([['-', 'X', '-'], ['X', 'X', 'X'], ['0', '-', '0']])
False
>>> test_diagonale2([['0', 'X', '0'], ['0', '0', 'X'], ['0', '-', '0']])
True
```

**Faire valider votre travail**


3.13 Écrire la fonction &quot;test\_jeu\_rempli&quot; qui a pour résultat l&#39;état du plateau de jeu (rempli, pas rempli) dont le plateau de jeu est passé en paramètre.

```python
>>> test_jeu_rempli([['-', 'X', '-'], ['X', 'X', 'X'], ['0', '-', '0']])
False
>>> test_jeu_rempli([['0', '0', 'X'], ['0', '0', 'X'], ['0', 'X', '0']])
True
```

Tester son bon fonctionnement avec le doctest.

3.14 Implémenter la fonction choix_joueur

```python
>>> choix_joueur(True,situation_init())
JOUEUR I : Choisir la position de votre pion par exemple 1,1 : 2,3
JOUEUR I : Choisir la position de votre pion par exemple 1,1 : 2,2
(2, 2)
```

3.15 Écrire la fonction &quot;action\_joueur&quot; qui a pour résultat le choix de jeu du joueur ; pour cette fonction, le joueur et  le paramètre du jeu sont passés en paramètres.

Pas de test de fonctionnement de test_validite_choix avec le doctest.


3.16 Écrire la fonction &quot; evolution\_jeu &quot; qui a pour résultat le paramètre du jeu ;  le paramètre du jeu et le choix du joueur sont passés en paramètres. Tester son bon fonctionnement.

```python
>>> evolution_jeu(True,[['0', '0', 'X'], ['0', '0', 'X'], ['0', 'X', '0']],(1,1))
[['0', '0', 'X'], ['0', 'X', 'X'], ['0', 'X', '0']]
```

Tester son bon fonctionnement avec le doctest.

3.17 Écrire la fonction &quot; aff\_evolution\_jeu&quot; qui affiche le plateau de jeu dont le plateau de jeu est passé en paramètre.

```python
    >>> aff_evolution_jeu([['0', '0', 'X'], ['0', '0', 'X'], ['0', 'X', '0']])
    [ 0 , 0 , X ]
    [ 0 , 0 , X ]
    [ 0 , X , 0 ]
```

Tester son bon fonctionnement avec le doctest.


3.18 Écrire la fonction &quot;etat\_final&quot; qui a pour résultats la fin du jeu et le résultat du jeu dont le paramètre du jeu est passé en paramètre.

```python
    >>> aff_evolution_jeu([['0', '0', 'X'], ['0', '0', 'X'], ['0', 'X', '0']])
    [ 0 , 0 , X ]
    [ 0 , 0 , X ]
    [ 0 , X , 0 ]
    >>> etat_final([['-', 'X', '-'], ['X', 'X', 'X'], ['0', '-', '0']])
    (True, False)
    >>> etat_final([['X', 'X', '0'], ['X', '0', 'X'], ['0', 'X', '0']])
    (True, False)
```

Tester le bon fonctionnement de l'ensemble en important le module jeu_tic_tac dans principal_jeu.

Pour cela,  on remplacera jeu_nim par jeu dans tout le code et à la place de import jeu_nim, on écrira import jeu_tic_tac as jeu.

**Faire valider votre travail**


**4. Amélioration facilitant le choix de l&#39;un ou l&#39;autre des jeux**

Maintenant que nos deux jeux fonctionnent, il serait intéressant de concevoir un programme permettant le choix de l&#39;un ou de l&#39;autre à l&#39;aide d&#39;une interface commune.

Rappel introduction:  ces jeux partagent un **mécanisme de déroulement** _des parties_  qui est **commun**. Ce sont uniquement les règles du jeu qui différent.

En vous aidant de l&#39;exemple simple suivant, modifier le programme principal du projet 8 afin que celui-ci propose, au lancement, un menu donnant le choix entre le jeu Nim ou le jeu Tic-tac-toe.

```python
#pasvoyelle.py
def categorie_lettre(c):
    """
    :Hypothese: len(c) ==1
    :param c:(str) chaine de caractères à tester
    :return: bool    renvoie True si pas voyelle
    exemple:
    >>> categorie_lettre("c")
    True
    >>> categorie_lettre("a")
    False
    """
    return c not in {'a', 'e', 'i', 'o', 'u', 'y'}

def nb_lettrecategorie(s):
    """
    :param s:(str) chaine de caractères à tester
    :return: (int)  renvoie le nombre de caractère qui ne sont pas des voyelles
    Exemples:
    >>> nb_lettrecategorie("")
    0
    >>> nb_lettrecategorie("abracadabra")
    6
    >>> nb_lettrecategorie("cqfd")
    4
    >>> nb_lettrecategorie("aaa")
    0
    """
    # compte : int
    compte = 0
    # c : str
    for c in s:
     if categorie_lettre(c):
        compte = compte +1
    return compte


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
```
```python
#voyelle.py
def categorie_lettre(c):
    """
    :Hypothese: len(c) ==1
    :param c:(str) chaine de caractères à tester
    :return: bool    renvoie True si pas voyelle
    exemple:
    >>> categorie_lettre("c")
    False
    >>> categorie_lettre("a")
    True
    """
    return c in {'a', 'e', 'i', 'o', 'u', 'y'}

def nb_lettrecategorie(s):
    """
    :param s:(str) chaine de caractères à tester
    :return: (int)  renvoie le nombre de caractère qui ne sont pas des voyelles
    Exemples:
    >>> nb_lettrecategorie("")
    0
    >>> nb_lettrecategorie("abracadabra")
    5
    >>> nb_lettrecategorie("cqfd")
    0
    >>> nb_lettrecategorie("aaa")
    3
    """
    # compte : int
    compte = 0
    # c : str
    for c in s:
     if categorie_lettre(c):
        compte = compte +1
    return compte


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)

```

```python
#prog-principal.py
import pasvoyelle as malib
import voyelle as malib

def categorie(chaine):
    """
    :param c:(str) chaine de caractères à tester
    :return: lettres_categorie (list) la liste des caractères de la catégorie dans la chaine
    """
    lettres_categorie=[]
    for lettre in chaine :
        if malib.categorie_lettre(lettre):
            lettres_categorie.append(lettre)
    return lettres_categorie

choix=int(input('Saisir le test a effectué : 1.voyelle  ou  2. pasvoyelle'))
#si 1 importer fichier fonctions voyelle
if choix==1:
    module = 'voyelle'
else:
    module='pasvoyelle'
    
malib=__import__(module)

chaine=str(input('Saisir la chaine a testée : '))
print(categorie(chaine))

```

**Faire valider votre travail qui devrait ressembler à ceci :**

```python

Choisir le jeu : 1.jeu_nim  ou  2. jeu_tic_tac : 1
Il reste 11 allumettes sur la table
JOUEUR II : Choisir le nombre d'allumettes à enlever : 2
Il reste 9 allumettes sur la table
JOUEUR I : Choisir le nombre d'allumettes à enlever : 
========================= RESTART =========================
Choisir le jeu : 1.jeu_nim  ou  2. jeu_tic_tac : 2
['-', '-', '-']
['-', '-', '-']
['-', '-', '-']
JOUEUR II :Choisir la position de votre pion par exemple 1,1 : 0,2
['-', '-', '0']
['-', '-', '-']
['-', '-', '-']
JOUEUR I :Choisir la position de votre pion par exemple 1,1 : 
```

******************************************************************************************

Réaliser maintenant le jeu d'Othello : [voir les règles du jeu](https://fr.wikipedia.org/wiki/Othello_(jeu)) en utilisant les mêmes fonctions de façon à pouvoir jouer à ce jeu avec la même interface que les jeux précédents.

Les fonctions vous sont données et sont à compléter pour que les tests fonctionnent.


```python

def situation_init():
    """
    : création de la situation initiale du jeu
    : renvoie le plateau initiale
    : param : Rien
    Exemple:
    """
    plateau=[
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 2, 1, 0, 0, 0],
    [0, 0, 0, 1, 2, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0]]
    return plateau


def aff_evolution_jeu(plateau):
    """
    : permet d'afficher le nombre d'allumettes restantes
    : param : int(param_jeu) nombres d'allumettes
    : return : None
    Exemple:
    >>> aff_evolution_jeu(situation_init())
      1 2 3 4 5 6 7 8
    1 · · · · · · · · 
    2 · · · · · · · · 
    3 · · · · · · · · 
    4 · · · □ ■ · · · 
    5 · · · ■ □ · · · 
    6 · · · · · · · · 
    7 · · · · · · · · 
    8 · · · · · · · · 
    """
	pass

import copy

def evolution_jeu(valeur_joueur,plateau,choix_joueur):
    """
    : permet de faire évoluer le jeu
    : param : bool(valeur_joueur) identification du joueur (True:I;False:II)
    : param : plateau : list
    : param : choix_joueur : tuple: 
    return : le nouveau plateau : list
    >>> aff_evolution_jeu(situation_init())
      1 2 3 4 5 6 7 8
    1 · · · · · · · ·
    2 · · · · · · · ·
    3 · · · · · · · ·
    4 · · · □ ■ · · ·
    5 · · · ■ □ · · ·
    6 · · · · · · · ·
    7 · · · · · · · ·
    8 · · · · · · · ·
    >>> aff_evolution_jeu(evolution_jeu(True,situation_init(),(4,6)))
      1 2 3 4 5 6 7 8
    1 · · · · · · · ·
    2 · · · · · · · ·
    3 · · · · · · · ·
    4 · · · □ □ □ · ·
    5 · · · ■ □ · · ·
    6 · · · · · · · ·
    7 · · · · · · · ·
    8 · · · · · · · ·
    >>> aff_evolution_jeu(evolution_jeu(False,situation_init(),(6,5)))
      1 2 3 4 5 6 7 8
    1 · · · · · · · ·
    2 · · · · · · · ·
    3 · · · · · · · ·
    4 · · · □ ■ · · ·
    5 · · · ■ ■ · · ·
    6 · · · · ■ · · ·
    7 · · · · · · · ·
    8 · · · · · · · ·
    >>> plateau_exemple=[[0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 3, 1, 0, 0, 0],[0, 0, 0, 3, 1, 3, 0, 0],[0, 0, 0, 3, 1, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0]]
    >>> aff_evolution_jeu(plateau_exemple)
      1 2 3 4 5 6 7 8
    1 · · · · · · · ·
    2 · · · · · · · ·
    3 · · · □ ■ · · ·
    4 · · · □ ■ □ · ·
    5 · · · □ ■ · · ·
    6 · · · · · · · ·
    7 · · · · · · · ·
    8 · · · · · · · ·
    >>> aff_evolution_jeu(evolution_jeu(True,plateau_exemple,(3,6)))
      1 2 3 4 5 6 7 8
    1 · · · · · · · ·
    2 · · · · · · · ·
    3 · · · □ □ □ · ·
    4 · · · □ □ □ · ·
    5 · · · □ ■ · · ·
    6 · · · · · · · ·
    7 · · · · · · · ·
    8 · · · · · · · ·
    >>> config=evolution_jeu(False,plateau_exemple,(2,5))
    >>> aff_evolution_jeu(config)
      1 2 3 4 5 6 7 8
    1 · · · · · · · ·
    2 · · · · ■ · · ·
    3 · · · □ ■ □ · ·
    4 · · · □ ■ □ · ·
    5 · · · □ ■ · · ·
    6 · · · · · · · ·
    7 · · · · · · · ·
    8 · · · · · · · ·
    >>> config1=[[0, 0, 3, 1, 1, 1, 0, 0],[0, 3, 3, 3, 1, 1, 0, 1],[0, 0, 3, 1, 3, 1, 3, 0],[0, 0, 3, 1, 1, 1, 3, 3],[0, 0, 3, 3, 1, 3, 0, 0],[1, 1, 1, 3, 3, 3, 1, 0],[1, 1, 1, 1, 3, 3, 0, 1],[3, 3, 3, 3, 3, 3, 0, 0]]
    >>> aff_evolution_jeu(config1)
      1 2 3 4 5 6 7 8
    1 · · □ ■ ■ ■ · ·
    2 · □ □ □ ■ ■ · ■
    3 · · □ ■ □ ■ □ ·
    4 · · □ ■ ■ ■ □ □
    5 · · □ □ ■ □ · ·
    6 ■ ■ ■ □ □ □ ■ ·
    7 ■ ■ ■ ■ □ □ · ■
    8 □ □ □ □ □ □ · ·
    >>> config2=evolution_jeu(True,config1,(1,7))
    >>> aff_evolution_jeu(config2)
      1 2 3 4 5 6 7 8
    1 · · □ □ □ □ □ ·
    2 · □ □ □ ■ □ · ■
    3 · · □ ■ □ ■ □ ·
    4 · · □ ■ ■ ■ □ □
    5 · · □ □ ■ □ · ·
    6 ■ ■ ■ □ □ □ ■ ·
    7 ■ ■ ■ ■ □ □ · ■
    8 □ □ □ □ □ □ · ·
    """
	pass


def compteur_pieces(valeur_joueur,param_jeu):
    """
    Compte le nombre de pièces du joueur
    param : valeur_joueur : bool
    param : param_jeu : list
    >>> aff_evolution_jeu(situation_init())
      1 2 3 4 5 6 7 8
    1 · · · · · · · ·
    2 · · · · · · · ·
    3 · · · · · · · ·
    4 · · · □ ■ · · ·
    5 · · · ■ □ · · ·
    6 · · · · · · · ·
    7 · · · · · · · ·
    8 · · · · · · · ·
    >>> compteur_pieces(True,situation_init())
    2
    >>> compteur_pieces(False,situation_init())
    2
    """

def test_jeu_rempli(param_jeu):
    """
    Renvoie True si le jeu est rempli sinon False
    """
	pass

def etat_final(param_jeu):
    """
    : vérification si fin jeu
    : param : int(param_jeu)
    : return : bool(fini),bool(per_gag)
    """
	pass

def test_validite_choix(valeur_joueur,le_choix,plateau):
    """
    : test de la validité de la position
    : param : bool(valeur_joueur) identification du joueur (True:I;False:II)
    : param le_choix: tuple
    : param plateau : la grille de jeu
    : return : le choix validé ou non du joueur
    >>> aff_evolution_jeu(situation_init())
      1 2 3 4 5 6 7 8
    1 · · · · · · · ·
    2 · · · · · · · ·
    3 · · · · · · · ·
    4 · · · □ ■ · · ·
    5 · · · ■ □ · · ·
    6 · · · · · · · ·
    7 · · · · · · · ·
    8 · · · · · · · ·
    >>> test_validite_choix(False,(4,6),situation_init())
    False
    >>> test_validite_choix(True,(10,10),situation_init())
    False
    >>> test_validite_choix(True,(3,5),situation_init())
    True
    >>> test_validite_choix(False,(6,5),situation_init())
    True
    """
	pass

def choix_joueur(valeur_joueur,param_jeu):
    """
    : Demande au joueur d'effectuer un choix de position
    : param : bool(valeur_joueur) identification du joueur (True:I;False:II)
    : param : param_jeu : list : la grille
    : return : choix du joueur
    Remarque: Ne pas faire de doctest sur des fonctions d'entrées /sorties
    """
	pass

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)

```

******************************************************************************************

Réaliser enfin le jeu de Puissance4 : [voir les règles du jeu](https://fr.wikipedia.org/wiki/Puissance_4) en utilisant les mêmes fonctions de façon à pouvoir jouer à ce jeu avec la même interface que les jeux précédents.

Les fonctions vous sont données et sont à compléter pour que les tests fonctionnent.


```python

def situation_init():
    """
    : création de la situation initiale du jeu
    : renvoie le plateau initiale
    : param : Rien
    Exemple:
    """
    plateau=[[0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0]]
	return plateau


def aff_evolution_jeu(param_jeu):
    """
    : affiche la configuration courante du jeu
    : param : list
    : return : str
    Exemple:
    >>> afficher_config(situation_init())
    1 2 3 4 5 6 7
    · · · · · · · 
    · · · · · · · 
    · · · · · · · 
    · · · · · · · 
    · · · · · · · 
    · · · · · · · 
    """
    print("1 2 3 4 5 6 7")
    numero=1
    for ligne in param_jeu:
        for element in ligne:
            if element==0:
                print('\u00B7',end=' ')
            if element==1:
                print('●',end=' ')
            if element==2:
                print('○',end=' ')
        numero +=1
        print()

def test_colonne(configuration,joueur):
    """
    Renvoie True si alignement selon colonne des jetons de joueur sinon False
    >>> config = [[0, 1, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0], [0, 2, 0, 0, 2, 0, 0], [0, 2, 0, 0, 2, 0, 0]]
    >>> aff_evolution_jeu(config)
    1 2 3 4 5 6 7
    · ● · · · · · 
    · ● · · · · · 
    · ● · · · · · 
    · ● · · · · · 
    · ○ · · ○ · · 
    · ○ · · ○ · · 
    >>> test_colonne(config)
    True
    >>> config1 = [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [2, 1, 0, 0, 0, 0, 0]]
    >>> aff_evolution_jeu(config1)
    1 2 3 4 5 6 7
    · · · · · · · 
    · · · · · · · 
    · · · · · · · 
    · · · · · · · 
    · · · · · · · 
    ○ ● · · · · · 
    >>> test_colonne(config1)
    False
    """
	pass

def test_ligne(configuration,joueur):
    """
    Renvoie True si alignement selon colonne des jetons de joueur sinon False
    >>> config = [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 2, 0, 0, 2, 0, 0], [0, 2, 1, 1, 1, 1, 0]]
    >>> aff_evolution_jeu(config)
    1 2 3 4 5 6 7
    · · · · · · · 
    · · · · · · · 
    · · · · · · · 
    · · · · · · · 
    · ○ · · ○ · · 
    · ○ ● ● ● ● · 
    >>> test_ligne(config)
    True
    >>> config1 = [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [2, 1, 0, 0, 0, 0, 0]]
    >>> aff_evolution_jeu(config1)
    1 2 3 4 5 6 7
    · · · · · · · 
    · · · · · · · 
    · · · · · · · 
    · · · · · · · 
    · · · · · · · 
    ○ ● · · · · · 
    >>> test_ligne(config1)
    False
    """
	pass

def test_diagonale_up(configuration,joueur):
    """
    Renvoie True si alignement selon diagonale montante des jetons de joueur sinon False
    >>> config = [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 1, 0], [0, 0, 0, 1, 1, 2, 0], [0, 1, 1, 2, 1, 1, 0], [0, 1, 2, 2, 2, 1, 0]]
    >>> aff_evolution_jeu(config)
    1 2 3 4 5 6 7
    · · · · · · · 
    · · · · · · · 
    · · · · ● ● · 
    · · · ● ● ○ · 
    · ● ● ○ ● ● · 
    · ● ○ ○ ○ ● · 
    >>> test_diagonale_up(config)
    True
    >>> config1 = [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [2, 1, 0, 0, 0, 0, 0]]
    >>> aff_evolution_jeu(config1)
    1 2 3 4 5 6 7
    · · · · · · · 
    · · · · · · · 
    · · · · · · · 
    · · · · · · · 
    · · · · · · · 
    ○ ● · · · · · 
    >>> test_diagonale_up(config1)
    False
    """
	pass

def test_diagonale_down(configuration,joueur):
    """
    Renvoie True si alignement selon diagonale descendante des jetons de joueur sinon False
    >>> config = [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 1, 1, 0], [0, 0, 2, 1, 1, 2, 0], [0, 1, 1, 2, 1, 1, 0], [0, 1, 2, 2, 2, 1, 0]]
    >>> aff_evolution_jeu(config)
    1 2 3 4 5 6 7
    · · · · · · · 
    · · · · · · · 
    · · ● · ● ● · 
    · · ○ ● ● ○ · 
    · ● ● ○ ● ● · 
    · ● ○ ○ ○ ● · 
    >>> test_diagonale_down(config)
    True
    >>> config1 = [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [2, 1, 0, 0, 0, 0, 0]]
    >>> aff_evolution_jeu(config1)
    1 2 3 4 5 6 7
    · · · · · · · 
    · · · · · · · 
    · · · · · · · 
    · · · · · · · 
    · · · · · · · 
    ○ ● · · · · · 
    >>> test_diagonale_down(config1)
    False
    """
	pass

def evolution_jeu(valeur_joueur,param_jeu,choix_joueur):
    """
    : modifie la configuration du jeu en ajoutant le nouveau pion et en retournant le ou les pions de couleur opposée
    : param : param_jeu (list)
    : param : joueur (str) 
    : return : liste
    >>> s =[[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 1, 2, 0, 0, 0, 0]]
    >>> aff_evolution_jeu(s)
    1 2 3 4 5 6 7
    · · · · · · · 
    · · · · · · · 
    · · · · · · · 
    · · · · · · · 
    · · · · · · · 
    · ● ○ · · · · 
    >>> s1=evolution_jeu(False,s,2)
    >>> aff_evolution_jeu(s1)
    1 2 3 4 5 6 7
    · · · · · · · 
    · · · · · · · 
    · · · · · · · 
    · · · · · · · 
    · ● · · · · · 
    · ● ○ · · · · 
    >>> aff_evolution_jeu(evolution_jeu(True,s1,3))
    1 2 3 4 5 6 7
    · · · · · · · 
    · · · · · · · 
    · · · · · · · 
    · · · · · · · 
    · ● ○ · · · · 
    · ● ○ · · · · 
    >>> aff_evolution_jeu(evolution_jeu(True,s1,2))
    1 2 3 4 5 6 7
    · · · · · · · 
    · · · · · · · 
    · · · · · · · 
    · ○ · · · · · 
    · ● ○ · · · · 
    · ● ○ · · · · 
    """
	pass

def test_validite_choix(valeur_joueur,lechoix,param_jeu):
    """
    : teste la validité d'une colonne
    : param : valeur_joueur : bool
    : param : lechoix : int
    : param : param_jeu : list
    : return : bool
    >>> config = [[0, 1, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0]]
    >>> aff_evolution_jeu(config)
    1 2 3 4 5 6 7
    · ● · · · · · 
    · ● · · · · · 
    · ● · · · · · 
    · ● · · · · · 
    · ● · · · · · 
    · ● · · · · · 
    >>> test_validite_choix(False,2,config)
    False
    >>> test_validite_choix(True,1,config)
    True
    """  
	pass

def choix_joueur(valeur_joueur,param_jeu):
    """
    : Demande au joueur d'effectuer un choix de position
    : param : bool(valeur_joueur) identification du joueur (True:I;False:II)
    : param : param_jeu : list 
    : return : choix du joueur
    """
	pass

def test_jeu_rempli(param_jeu):
    """
    Renvoie True si le jeu est rempli sinon False
    """
	pass

def etat_final(param_jeu):
    """
    : vérification si fin jeu
    : param : int(param_jeu)
    : return : bool(fini),bool(per_gag)
    Exemple:
    >>> config = [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 1, 2, 0, 2, 0, 0], [0, 1, 2, 2, 2, 0, 0], [0, 1, 2, 1, 1, 0, 0], [0, 2, 1, 2, 2, 0, 0]]
    >>> aff_evolution_jeu(config)
    1 2 3 4 5 6 7
    · · · · · · · 
    · · · · · · · 
    · ● ○ · ○ · · 
    · ● ○ ○ ○ · · 
    · ● ○ ● ● · · 
    · ○ ● ○ ○ · · 
    """
	pass

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)

```
