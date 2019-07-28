La course du chicon
===================


**Objectifs**

-   les dictionnaires
-   tuples nommés
-   modules
-   traitement des données en tables
-   utilisation des tris
-   lecture/écriture de fichiers textes et format CSV

On s'intéresse donc ici en particulier à cette partie du programme de NSI de 1ère :

<img src="./extrait-programme.png" width="500"/>


Introduction
------------

Le dimanche 27 octobre 2019 aura lieu à Baisieux, commune du Nord
frontalière de la Belgique, la [course du chicon](http://courirabaisieux.fr/la-course-du-chicon/).

Cette course se décline sur plusieurs distances de 15km à 0.5km. Nous ne nous intéresserons dans ce TP qu'à la
version 15km.

Vous avez la responsabilité du traitement informatique des données :
gestion des inscriptions, récolte des performances des concurrents,
publication des résultats.

Préparation
-----------


1.  **Archive**

Récupérez l'[archive](mat_course_chicon.zip) et décompressez la.

 Cette archive contient trois dossiers :

 -   [`src/`](./src) contient le module  [src/Competitor.py](src/Competitor.py)
 - `docs/` contient la documentation du module `Competitor`, accessible depuis le fichier index.html
 -  [`data/`](./data)  contient deux jeux de données dans quatre fichiers de données : un
     petit jeu  de données pour faire des tests simples
 ([data/small\_inscrits.csv](data/small_inscrits.csv) et
 [data/small\_performances.csv](data/small_performances.csv)), et un gros jeu de données
 ([data/inscrits.csv](data/inscrits.csv) et [data/performances.csv](data/performances.csv)).




2.  **Documentation**

Consultez la documentation du module fourni.


Le module `Competitor.py` permet de manipuler des valeurs représentant les compétiteurs de la course. On peut considérer qu'il permet la définition d'un type `Competitor`.
L'étude de la documentation permet de déduire les différentes informations contenues dans une telle donnée.

Vous pouvez bien sûr examiner le code (accessible depuis la
documentation), mais **se limiter à la lecture de la documentation est
un bon exercice**, car il implique de se limiter à manipuler les
données de type `Competitor` via l'interface fournie, sans se
préoccuper de l'implémentation qui en a été réalisée (c'est ce qui se
passe de fait, par exemple, dans les langages objets pour lesquels la
notion d'attribut *privé* à un sens).

On dispose ainsi d'un **constructeur**  (`create`) et les différentes informations qui décrivent une donnée `Competitor` sont ainsi accessibles via les différents **accesseurs** (`get_XXX`). On constate de plus que le seul **modificateur** concerne la performance d'un compétiteur (`set_performance`).

3. **Création du module `Time`**

Les performances des compétiteurs vont être représentées par leur temps de course exprimé en heures, minutes et secondes.

On décide de représenter ces données par un tuple nommé. Ces données étant non mutables, utiliser les *named tuples* de Python pour les représenter semble être un choix  pertinent.

Pour rappel, cette notion est définie dans le module `collections` de Python. Il convient donc d'importer

```python
from collections import namedtuple
```

**À faire**

Créer un module `Time.py` qui définit :

 * le type `Time` qui correspond à un tuple nommé possédant trois champs `hours`, `minutes` et `seconds` ;
 * une fonction `create` à trois arguments, permettant de créer une donnée de ce type, dont le résultat est la donnée `Time` créée (on peut envisager un contrôle de validité des valeurs des paramètres pour ce constructeur) ;
 * une fonction `compare` qui définit une relation d'ordre sur les données de type `Time`. De manière classique le résultat de cette fonction, à deux paramètres de type `Time`, est négatif si son premier paramètre est inférieur au second, positif s'il lui est plus grand et nul quand ils sont égaux.
 * une fonction `to_string` qui a pour résultat une représentation sous la forme d'une chaîne de caractères de son paramètre de type `Time`.




Gestion des inscrits
--------------------

Les fonctions suivantes sont a priori à définir dans le module `course_chicon` qui regroupera les fonctions utiles à la gestion de la course.

Il sera bien sûr nécessaire d'importer les modules `Competitor` et `Time`.


Votre première tâche est de construire la liste des compétiteurs inscrits à
la compétition.

Les données concernant ces compétiteurs se trouvent dans le fichier
`data/inscrits.csv` (ou `data/small_inscrits.csv`) qui
est un fichier au format
[CSV](https://fr.wikipedia.org/wiki/Comma-separated_values),
c'est-à-dire un fichier texte contenant des données tabulées.

La première ligne de ce fichier est constituée des libellés des données
qui suivent :

``` {.sourceCode .text}
Prénoms;Noms;Sexes;Date naiss.
```

Elle précise donc que chacune des lignes qui suivent contient dans cet
ordre le prénom, le nom, le sexe et la date de naissance du compétiteur
inscrit. Ces informations sont séparées par un point-virgule.

Avec ces données vous allez construire des compétiteurs à l'aide de la
fonction `Competitor.create`. Il vous faudra attribuer à chacun de ces
compétiteurs un numéro de dossard, obtenu par simple incrémentation d'un
compteur. 

Tous les compétiteurs seront rassemblés dans un dictionnaire dont les clés seront les numéros de dossard et les valeurs les compétiteurs associés.


**À faire**

Réalisez une fonction nommée `read_competitors` paramétrée par le nom du
fichier CSV contenant les données des inscrits, qui a pour résultat le dictionnaire de
ces inscrits.


Vous pouvez envisager de gérer la situation où aucun fichier ne correspond au paramètre fourni. Cela peut être fait en capturant l'exception `FileNotFoundError` qui est alors déclenchée.

*Indication* Pensez à la méthode `split` des chaînes de caractères. La méthode `rstrip` peut également être utilisée pour supprimer les marqueurs de fin de ligne.

**À faire**

Testez la validité de votre fonction avec le fichier
`data/small_inscrits.csv`. 
Vérifiez par exemple la taille du dictionnaire obtenu, ainsi que le
contenu de quelques éléments.

Manipulations du dictionnaire
-----------------------------

### Affichage

**À faire**

Réalisez une fonction qui prend en paramètre une liste de données de type `Competitor` et affiche sur la sortie standard chacune de ces données à raison d'une par ligne (utilisez la fonction `to_string` de `Competitor`).

Utilisez votre fonction pour afficher les compétiteurs contenus dans le dictionnaire produit par la fonction `read_competitors` (c'est le moment de penser à utiliser `values()`).


### Sélections

Nous allons écrire quelques fonctions de recherche dans un dictionnaire de valeurs qui satisfont un critère. Dans cette section les compétiteurs sont passés en paramètre de chacune des fonctions sous la forme d'un dictionnaire tel que celui construit par la fonction `read_competitors`. Les fonctions à écrire disposent d'un autre paramètre qui correspond, d'une manière ou d'une autre, au critère de sélection des compétiteurs dans le dictionnaire.
Les fonctions ont pour résultat soit une donnée de type `Competitor`, soit une liste de telles données. Ce résultat correspond à la sélection selon le critère cherché.

**À faire**
Écrivez une fonction `select_competitor_by_bib` qui a pour résultat le compétiteur dont le numéro de dossard est passé en paramètre.

Comment proposez-vous de  gérer la situation où aucun compétiteur ne correspond au dossard fourni ? 

*Suggestion* cela peut être l'occasion de tester la levée d'exception.

**À faire**

Écrivez une fonction `select_competitor_by_birth_year` dont le résultat est la liste des compétiteurs dont l'année de naissance correspond à une valeur passée en paramètre.

*Suggestion* Étudiez la documentation de la fonction `endswith` des chaînes de caractères.

Quel résultat renvoyer si aucun compétiteur ne correspond à l'année fournie ?

*NB* Dans le petit jeu de données, deux compétiteurs sont nés en 1980.

**À faire**

Écrivez une fonction `select_competitor_by_name` dont le résultat est la liste des compétiteurs dont le nom (*last name*) contient la chaîne de caractères passée en paramètre.

*Suggestion* Pensez à utiliser `in` pour les chaînes de caractères.


**Remarque**  En fin de sujet, la section **Compléments** propose d'aller un peu plus loin dans le travail sur ces sélections.


Report des performances
-----------------------

La course achevée, votre tâche consiste à reporter les
performances des compétiteurs dans les fiches de la liste de ces compétiteurs.

### Lecture des performances

Les données concernant les performances se trouvent dans le fichier
`data/performances.csv` (ou
`data/small_performances.csv`) qui est un fichier au format
CSV.

La première ligne de ce fichier est constituée des libellés des données
qui suivent :

``` {.sourceCode .text}
bib_num;hours;minutes;seconds
```

Elle précise donc que chacune des lignes qui suivent contient dans cet
ordre le numéro de dossard, le nombre d'heures, de minutes et de
secondes du temps de parcours d'un compétiteur, ces informations étant
séparées par un point-virgule.

Seuls les compétiteurs ayant effectivement participé et achevé la
course figurent dans ce fichier.  Avec ces données vous allez
construire un dictionnaire des performances qui associe à un numéro de
dossard un objet de type `Time` du module que vous avez défini.


**À faire**

Réalisez une fonction nommée `read_performances` paramétrée par le nom
du fichier CSV contenant les données des performances, qui renvoie le dictionnaire
des performances contenues dans ce fichier.



**À faire**

Testez la validité de votre fonction avec le fichier
`data/small_performances.csv`.
Vérifiez en particulier la taille du dictionnaire obtenu, ainsi que le
contenu de quelques éléments.


### Report

Maintenant que vous disposez des données sur les compétiteurs et leurs
performances sous forme de dictionnaires qui partagent les mêmes
clefs, votre travail consiste à reporter les performances dans les
fiches de ces compétiteurs.


**À faire**

Réalisez une fonction nommée `set_performances` paramétrée par les deux
dictionnaires qui modifie les fiches des compétiteurs en reportant leur
performance. Cette fonction ne renvoie pas de valeur.

**À faire**

Testez la validité de votre fonction avec les listes produites par le
petit jeu de données.

# Tris
(manipulation du dictionnaire - suite)

Vous allez avoir l'occasion de réutiliser l'un des tris que vous avez
réalisés dans le cadre des activités du bloc 2. 

Récupérez le fichier contenant les fonctions de tris étudiées,
faites votre choix d'une fonction parmi les tris étudiés et importez
cette fonction.


**À faire**

Sur le modèle des fonctions de comparaison que vous avez déjà
rencontrées, complétez le module `Competitor` pour lui ajouter une
fonction nommée `compare_lastname` qui définit une relation d'ordre
sur les compétiteurs selon l'ordre alphabétique de leurs noms.

Utilisez cette fonction pour définir une fonction `sort_competitors_by_lastname` qui prend en paramètre un dictionnaire de compétiteurs, comme défini précédemment, et a pour résultat la liste des compétiteurs triée par ordre alphabétique  de leurs noms.


**À faire**

De manière similaire, faites le travail nécessaire pour définir une
fonction `sort_competitors_by_performance` qui produit la liste des
compétiteurs triée par ordre croissant des performances réalisées. Les
compétiteurs sans résultat sont placés en fin de liste par ordre
alphabétique.


**Remarque**  En fin de sujet, la section **Compléments** propose d'aller un peu plus loin dans le travail sur ces tris.





Publication et sauvegarde des résultats
---------------------------------------

### Affichage des résultats

Il est temps de procéder à la publication des résultats.


**À faire**

Réalisez une fonction nommée `print_results` paramétrée par un dictionnaire de
compétiteurs qui imprime sur la sortie standard cette liste en précisant
leur prénom, nom, sexe, numéro de dossard et performance.

Par exemple, avec le petit jeu de données, et en supposant que le report
des performances a été effectué et la liste de compétiteurs triée par
ordre de performance, on pourrait obtenir un affichage de la forme :

``` {.sourceCode .bash}
[7]: Archard Rivard (M - 10/6/1950)      =>  0h46mn31s
[8]: Cheney Chassé (M - 21/3/1949)       =>  0h48mn10s
[4]: Saville Marier (M - 19/11/1969)     =>  0h56mn29s
[5]: Namo Lereau (M - 26/3/1980)         =>  1h 6mn20s
[10]: Sidney Charest (M - 5/3/1981)      =>  1h 6mn38s
[1]: Sidney Robert (M - 21/7/1970)       =>  1h 8mn55s
[6]: Romaine Hughes (F - 17/10/1943)     =>  1h17mn 8s
[3]: Vincent Riquier (M - 16/9/1980)     =>  1h21mn23s
[9]: Avelaine CinqMars (F - 14/2/1983)   => 
[2]: Paien Gilbert (M - 26/11/1953)      => 
```

**À faire**

Produisez l'affichage des résultats par ordre alphabétique, et par
ordre des performances.


### Sauvegarde des résultats

Enfin pour la pérennité de ces résultats, il est important de les
sauvegarder dans un fichier.


**À faire**

Réalisez une fonction nommée `save_results` paramétrée par un dictionnaire de
compétiteurs et un nom de fichier de sauvegarde, qui crée un fichier au
format CSV contenant

-   les libellés en première ligne

    ``` {.sourceCode .text}   
    Num_dossard;Prénom;Nom;Performance
    ```

-   les résultats sur les lignes suivantes

    ``` {.sourceCode .text}   
    7;Archard;Rivard; 0h46mn31s
    8;Cheney;Chassé; 0h48mn10s
    ...
    ```

**À faire**

Testez votre fonction avec le petit jeu de données puis sauvegardez les résultats complets de la course.

**L'équipe organisatrice de la course du chicon vous remercie
chaleureusement pour votre contribution à son bon déroulement.**


# Compléments

## Pour les fonctions de sélection

**Allons un peu plus loin** *(optionnel)*

On peut constater que les deux fonctions de sélection réalisées sont
assez similaires et on pourrait imaginer d'autres fonctions de
sélection (par sexe, par tranche d'âge, etc.) qui le
seraient tout autant.  À chaque fois, il s'agit de filtrer parmi les
valeurs du dictionnaire, celles qui satisfont un critère de
sélection. Ce critère pourrait être défini par un **prédicat**, c'est-à-dire
une fonction dont le résultat est un booléen, dont le paramètre serait
un compétiteur. Le résultat de cette fonction est `True` si le
compétiteur doit être sélectionné (on dit qu'il vérifie le prédicat)
et `False` dans le cas contraire.


**À faire**
Lors de l'étude des tris vous avez vu, avec les fonctions de comparaison passées en paramètre des fonctions de tri, qu'une fonction pouvait être paramètre d'une fonction.
En reprenant ce principe, définissez une fonction `select_competitor` dont le premier paramètre est un dictionnaire de compétiteurs et le second est une fonction prédicat.
Le résultat de `select_competitor` est la liste des compétiteurs qui vérifient le prédicat.

**À faire**
Après avoir défini les prédicats qui conviennent proposez une seconde version des fonctions  `select_competitor_by_birth_year` et `select_competitor_by_name`.

Définissez une prédicat qui vérifie si son paramètre de type `Competitor` est de sexe féminin, puis sans définir de nouvelle fonction produisez la liste des compétiteurs de sexe féminin.	

**Encore un peu plus loin ?** (seulement si vous en avez envie)

Python permet de définir des *fonctions anonymes* (comme en javascript si vous avez déjà réalisé cela). On parle de **lambda** ou *lambda expression* ou *lambda fonction*.
Il s'agit, en Python, de fonction dont le corps est constitué d'une seule expression et pour lesquels le `return` est implicite.

Voici un exemple de lambda qui calcule le carré de son paramètre
```python
>>> lambda x : x*x
<function <lambda> at 0x000002B1CA9D9730>
```
On peut s'en servir pour définir une fonction
```python
>>> carre = lambda x: x*x
>>> carre(4)
16
```

Il est possible d'avoir plusieurs paramètres :
```python
>>> add = lambda x,y: x+y
>>> add(3,6)
9
```

Fondamentalement, les lambdas n'apportent rien de particulier par rapport aux fonctions définies par `def`. Leur intérêt réside principalement dans les situations où l'on souhaite passer une fonction comme paramètre sans avoir à définir une fonction nommée.

Vous pouvez lire [cette page](https://book.pythontips.com/en/latest/map_filter.html) et en déduire comment vous pouvez utiliser les lambdas et la fonction `filter` pour écrire une troisième version des fonctions de sélection précédentes qui utilise `filter` 
qui est de fait une fonction prédéfinie qui réalise le travail demandé.

## Pour les tris


**Allons un peu plus loin** (une nouvelle fois)

Selon le même principe que pour la sélection on peut constater des similitudes dans les deux fonctions de tris (`sort_competitors_by_lastname` et `sort_competitors_by_performance`) étudiées dans le sujet.
Déduisez en la définition d'une fonction qui prend en paramètre le dictionnaire et la fonction de comparaison pour produire la liste de compétiteurs triée selon la relation d'ordre.

**Et toujours pour aller un peu plus loin**

Il est possible d'utiliser la fonction prédéfinie `list.sort` (cf. [doc python](https://docs.python.org/fr/3.7/library/stdtypes.html#list.sort)).
Il est alors certainement intéressant de consulter au préalable le [Guide pour le tri](https://docs.python.org/fr/3.7/howto/sorting.html).
C'est l'occasion de  rencontrer à nouveau une situation où les lambdas peuvent être utilisées.
