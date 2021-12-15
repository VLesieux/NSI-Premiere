## Exercices Thème D : interactions entre l'homme et la machine sur le Web

## Exercice 1

Écrire un programme dans une page HTML qui demande successivement de saisir un montant en euro puis le taux de change d'une monnaie ; le résultat de la conversion est affiché après avoir cliqué sur un bouton.

<img src="assets/programme1.png"> 


## Exercice 2

Écrire un programme dans une page HTML qui consiste à trouver un nombre mystère choisi au hasard entre 1 et 100.   
À chaque proposition du joueur, le programme répond " trop petit ! " ou " trop grand ! " ou " Bravo, vous avez trouvé en ... coups ".   
Le nombre de coup est limité à 10.

<img src="assets/programme2_tropbas.png"> 
<img src="assets/programme2_tropgrand.png"> 
<img src="assets/programme2_bravo.png"> 
<img src="assets/programme2_perdu.png"> 

Indication : 

On obtient un nombre au hasard entre 0 compris et 1 exclu en utilisant Math.random().

```js
Math.random()
0.40961663444922125
```
Pour prendre la partie entière d'un nombre, utiliser Math.floor().

```js
Math.floor(0.40961663444922125)
0
```

Pour avoir un nombre compris entre 1 et 100 compris, on peut utiliser : Math.floor(Math.random()*100+1) 

## Exercice 3

Réaliser une calculatrice sur une page HTML.  
Le bouton AC permet de vider l'affichage.  
Le bouton DEL permet de supprimer le dernier caractère affiché.   
Le bouton (-) permet de multiplier par -1.  
Le bouton Mem permet de mémoriser le résultat du dernier calcul et de rappeler ce résultat dans un nouveau calcul.

<img src="assets/calculatrice.png"> 

Indication : pour transformer une chaîne de caractère en une expression calculable, utiliser eval.

```js
eval("3*8+7")
31
```

## Exercice 4

S'approprier le code expliqué de ce [quiz anglais](http://isnangellier.alwaysdata.net/php/Creation_quizz.html) et réalisez vous-même un quiz sur le thème de votre choix.

