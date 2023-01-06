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

On trouve au casino le jeu de roulette :

<img src="assets/roulette.jpeg"> 

Réaliser une simulation du jeu dont les règles vous sont données ici : 

```Le jeu de roulette consiste à parier sur le numéro ou la couleur sur lequel la bille va atterrir sur une roue tournante. La roue est divisée en 37 (en Europe) ou 38 (aux États-Unis) cases numérotées de 0 à 36. Les cases sont alternées de couleur rouge et noir, excepté pour la case 0 qui est verte.
Voici comment le jeu se déroule :
Les joueurs font leurs paris en plaçant leurs jetons sur la table de jeu. Ils peuvent parier sur un seul numéro, une combinaison de numéros, la couleur rouge ou noir, ou encore sur un groupe de numéros (par exemple, les chiffres de 1 à 18 ou de 19 à 36).
Le croupier tourne la roue dans un sens et lance la bille dans la direction opposée.
Quand la bille commence à perdre de la vitesse, le croupier annonce « Rien ne va plus » et les joueurs ne peuvent plus placer de nouveaux paris.
La bille finit par atterrir dans une case de la roue. Si vous avez parié sur ce numéro ou cette couleur, vous gagnez. Les gains sont payés selon les odds (cotes) associées à chaque type de pari.```


## Exercice 5

S'approprier le code expliqué de ce [quiz anglais](http://isnangellier.alwaysdata.net/php/Creation_quizz.html) et réalisez vous-même un quiz sur le thème de votre choix.

