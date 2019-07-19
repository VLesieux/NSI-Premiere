# WA-TOR   :        règles du jeu et objectif à atteindre
**Simulation proie-prédateur** ([article wikipédia](https://en.wikipedia.org/wiki/Wa-Tor) (en anglais))

Wa-Tor est une simulation de type proie-prédateur. Dans une mer torique évoluent des thons (les proies) et des requins (les prédateurs). Les uns et les autres se déplacent et se reproduisent. Pour acquérir l'énergie suffisante à sa survie un requin doit manger un thon régulièrement. Un thon vit éternellement tant qu'il n'est pas mangé par un requin.


## La mer

La mer est représentée par une grille à deux dimensions torique. Chaque case a quatre voisines, une dans chacune des quatre directions cardinales (N, S, E O). 
Chaque case de cette grille représente une zone de mer qui peut être soit vide, soit occupée par un thon ou un requin.


## Les poissons

Chaque thon est caractérisé par son *temps de gestation*. Ce temps est initialisé à une valeur initiale commune à tous les thons, appelée *durée de gestation des thons*.

Chaque requin est caractérisé par son *temps de gestation* et son *énergie*. Ces deux valeurs sont initialisées à une valeur initiale commune à tous les requins, appelées respectivement *durée de gestation des requins* et *énergie des requins*.

## Simulation et comportements

À chaque pas de la simulation, une case de la mer est sélectionnée aléatoirement. Si elle est vide, il ne se passe rien. Si elle est occupée par un poisson, on applique alors son comportement. Les comportements de thons et des requins sont régis par des règles simples.

 * **Un thon** applique le comportement suivant :
   1. *Déplacement* Le thon choisit aléatoirement une case libre parmi ses voisines. S'il en existe une, le thon se déplace vers cette case. Il reste sur place sinon. 
   2. *Reproduction* 
     - Le temps de gestation du thon est diminué de 1. 
     - Si ce temps arrive à 0, le thon donne naissance à un nouveau thon qui nait sur la case qu'il vient de quitter s'il s'est déplacé. Sinon aucun thon ne nait. Le temps de gestation est remis à sa valeur initiale.

 * **Un requin** applique le comportement suivant :
   1. *Energie* Le requin perd un point d'énergie.
   2. *Déplacement* Le requin choisit aléatoirement parmi ses voisines une case occupée par un thon. S'il en existe une, le requin se déplace vers cette case et mange le thon. Son niveau d'énergie est alors remis à sa valeur initiale. Sinon il cherche à se déplacer vers une case voisine vide choisie au hasard. Il reste sur place s'il n'y en a aucune.
   3. *Mort* Si le niveau d'énergie du requin est à 0, il meurt. Dans ce cas l'étape suivante n'a évidemment pas lieu.
   4. *Reproduction* Le temps de gestation du requin est diminué de 1. Si ce temps arrive à 0, il donne naissance à un nouveau requin sur la case qu'il vient de quitter s'il s'est déplacé, sinon aucun requin ne nait. Son temps de gestation est remis à sa valeur initiale.



## Phénomènes proies-prédateurs émergents

Les durées de gestation des deux espèces et l'énergie récupérée par un requin lorsqu'il mange un thon sont des paramètres de la simulation. S'ils sont bien choisis on peut voir émerger un phénomène "périodique" d'évolution des populations.

Quand il y a peu de prédateurs, la population des proies augmente, mais cette abondance de proies permet alors aux prédateurs de facilement trouver l'énergie suffisante pour leur survie et leur reproduction. Leur population se met alors à croitre au détriment de celle de leur proie. Quand ces dernières deviennent trop rares, les prédateurs finissent par mourir sans se reproduire. Et quand il y a peu de prédateurs...

Pour obtenir ce phénomène cyclique,  il faut respecter les inégalités suivantes :

*temps gestation des thons < énergie des requins < durée gestation des requins*

Les valeurs suggérées sont 2, 3 et 5.

Il est également souhaitable de débuter avec une configuration dans
laquelle il y a un nombre de thons relativement important par rapport
au nombre de requins. Par exemple 30% des cases de la mer sont
initialement occupées par des thons et 10% par des requins.

## Travail à réaliser

Construire une activité qui amène les élèves à progressivement réaliser un programme qui permettre la simulation wa-tor pendant un nombre choisi de pas. 

Il est évidemment certainement souhaitable de réaliser le programme correspondant à votre proposition.

Du point de vue du programme, les questions à se poser concernent en particulier le choix des structures de données à utiliser et les étapes de décomposition du programme.
Vous essaierez d'identifier les points qui vous sembleront les plus problématiques pour les élèves ainsi que les notions que permet d'évaluer ce travail.


Une séance de *relecture par les pairs* sera organisée. Vous aurez par groupe de quatre à comparer et à discuter de vos propositions de progression pour cette activité.


## Compléments

Si on veut avoir un affichage de l'évolution de la mer, il est peut être pertinent de ne pas afficher toutes les étapes mais une tous les 100 (par exemple) et de faire une petite pause après chaque affichage grâce au module `time` et sa fonction `sleep` :


   ```
   import time
   time.sleep(0.1) # pause de 1/10ème de seconde
   ```


On pourra ajouter à la simulation des variables globales qui comptabilisent à chaque instant les nombres de requins et de thons. On peut alors enregister à chaque pas de simulation le triplet *(numéro du pas, nombre de thons, nombre de requins)*.

Le résultat du programme peut alors être la liste de ces triplets pour tous les pas. Les données collectées dans cette liste peuvent être utilisées pour dessiner les courbes des évolutions de population. On peut pour cela utiliser le module `pylab`.

Tracer une courbe avec `pylab`est assez simple. Il suffit de faire :


   ```
   import pylab
       
   data_x = *une liste d'abscisses*
   data_y = *une liste d'ordonnées*
   pylab.plot(data_x, data_y)
   pylab.title('courbe des points de coordonnées (x,y)')
   pylab.show()
   ```   

Voici alors ce que l'on peut obtenir pour une mer de taille 25x25 et 125000 pas ( = 25x25x200 ). On peut observer les cycles décalés d'évolution des populations (les thons sont en bleu et le requins en rouge) :

<img src="./evolutions-2-3-5-25x25.png" width="300"/>