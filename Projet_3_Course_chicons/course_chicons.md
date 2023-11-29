La course du chicon
===================


**Objectifs** : Mettre en œuvre

-   le traitement des données en tables
-   l'utilisation des tris
-   la lecture des fichiers textes au format CSV


Introduction
------------

Le dimanche 27 octobre 2019 a eu lieu à Baisieux, commune du Nord frontalière de la Belgique, la "course du chicon".

Cette course se décline sur plusieurs distances de 15 km à 0.5 km. Nous ne nous intéresserons dans ce TP qu'à la version de 15 km.

Vous imaginez que vous avez la responsabilité du traitement informatique des données : gestion des inscriptions, récolte des performances des concurrents, publication des résultats.

Objectif
-----------

Dans le dossier `assets` se trouvent le sous-dossier [`data/`](./data) : il contient deux jeux de données dans quatre fichiers de données : un petit jeu  de données pour faire des tests simples `small_inscrits.csv` et `small_performances.csv`, et un gros jeu de données `inscrits.csv` et `performances.csv`.


L'objectif à atteindre est de publier les résultats de la course.   
Pour le petit jeu de données, on doit obtenir l'affichage :

     [7]: Archard Rivard (M - 10/6/1950)=>  0h 46mn 31s
     [8]: Cheney Chassé (M - 21/3/1949)=>  0h 48mn 10s
     [4]: Saville Marier (M - 19/11/1969)=>  0h 56mn 29s
     [5]: Namo Lereau (M - 26/3/1980)=>  1h 6mn 20s
     [10]: Sidney Charest (M - 5/3/1981)=>  1h 6mn 38s
     [1]: Sidney Robert (M - 21/7/1970)=>  1h 8mn 55s
     [6]: Romaine Hughes (F - 17/10/1943)=>  1h 17mn 8s
     [3]: Vincent Riquier (M - 16/9/1980)=>  1h 21mn 23s
     [9]: Avelaine CinqMars (F - 14/2/1983)=> None
     [2]: Paien Gilbert (M - 26/11/1953)=> None
     
On observe que les inscrits sont classés d'après leur performance à la course et que les non-inscrits apparaissent en dernier dans l'ordre alphabétique.


      


