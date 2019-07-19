
# Générateur de phrases de passe

Ce TP s'inspire de cet [article de Micah Lee sur _the Intercept_](https://firstlook.org/theintercept/2015/03/26/passphrases-can-memorize-attackers-cant-guess/).


## Le contexte

Il faut des mots de passe pour la plupart des plateformes
informatiques que nous utilisons (ordinateurs, smartphones, sites
bancaires, réseaux Wifi, protection de trousseaux de clés
cryptographiques, etc.).


Pour offrir une sécurité suffisante, il est souvent déconseillé
d'utiliser des mots significatifs que l'on peut trouver dans des
listes de mots (dictionnaires par exemple). En effet, une attaque
envisageable contre un tel mot de passe consiste à essayer les uns à
la suite des autres chacun des mots de cette liste jusqu'à trouver le
bon, ce qui est à la portée d'un programme informatique si la liste
contient quelques milliers ou dizaines de milliers de mots. On parle
d'[attaque par force brute](https://fr.wikipedia.org/wiki/Attaque_par_force_brute). 

Pour un bon mot de passe, on conseille plutôt d'utiliser une chaîne de
caractères d'au moins huit caractères contenant des lettres majuscules
et minuscules, des chiffres, voire d'autres caractères encore, chacun
des caractères étant choisi au hasard. \
En considérant des mots de passe de longueur huit élaborés à partir
d'une centaine de caractères (par exemple les 96 caractères ASCII dits
imprimables (ceux de code compris entre 32 et 126)), le nombre de mots
de passe est environ égal à *100^8 = 10^{16}* (soit dix millions de
milliards), nombre qui commence à compliquer sérieusement la tâche
d'un attaquant qui envisagerait de trouver votre mot de passe en
essayant une à une toutes les chaînes de caractères de longueur
huit. \
L'inconvénient de tels mots de passe est qu'il est difficile de
les mémoriser (sauriez vous mémoriser facilement des mots de passe de
la forme `1)_N2@!A` ?


Plutôt que d'envisager des chaînes de caractères aléatoires
construites avec des caractères quelconques, il est possible de
construire des mots de passe en assemblant plusieurs mots d'une liste
fixée de mots (par exemple des mots français), qu'il sera plus facile
à mémoriser. Voici un exemple de tel assemblage de cinq mots :
`visita-housse-degorge-rinciez-effrita`. On nomme souvent de tels mots
de passe *phrases de passe* (*passphrases* en anglais).


## Construction de phrases de passe

Comment construire des phrases de passe ?

Il est possible de construire des phrases de passe « à la main » si on dispose

   1. d'une liste de mots ;
   2. et d'un dé.

C'est ce que vous allez découvrir dans ce qui suit.

## Le matériel de base : une liste de mots

Pour construire des passe-phrases, vous avez besoin d'une liste dans laquelle vous puiserez des mots choisis au hasard.

Pour cela vous utiliserez le fichier Python
[liste_7776_mots.py](liste_7776_mots.py) qui définit une variable
nommée `LISTE_MOTS`. Pour utiliser cette variable il vous suffit donc
de l'importer depuis son module.

```python
from liste_7776_mots import LISTE_MOTS
```

La variable `LISTE_MOTS` contient une liste de 7776 mots.

### À faire

Vérifiez que la valeur que définit cette variable est bien de type tuple.

Vérifiez que la longueur est bien celle annoncée.



Nous admettrons que

   * tous les éléments de cette liste sont des chaînes de caractères (des mots de la langue française) ;
   * chacune de ces chaînes ne contient que des lettres (non accentuées) ;
   * tous les mots sont différents.

### À faire

Vérifiez que ces hypothèses sont vérifiées, à l'exclusion du fait
qu'il s'agit bien de "vrais" mots de la langue française bien sûr.

_Aide._ Étudiez les documentations des fonctions prédéfinies
(*built-in*) `all()`, `isinstance()` et d'une des méthodes `upper()`
ou `lower()` du type `str`, elles peuvent vous être utiles.


### À faire

Calculez les longueurs minimales et maximales des mots de cette liste.


### À faire

Écrivez **une** instruction qui imprime le mot de cette liste,
le dernier et celui d'indice 2094. Pour chaque mot, on aura quelque
chose comme :

```pyhton
0 : montes
7775 : tour
2094 : morigener
```

_Remarque._ Ces trois mots pourront servir dans les doctests de
certaines fonctions qui vont suivre. 


## Convertir des lancers de dés en un nombre entier"

Dans cette partie nous allons répondre à deux questions :

  1. Pourquoi la liste de mots contient-elle 7776 mots ?
  2. Comment en lançant des dés nous pouvons choisir un mot au hasard dans cette liste ?


Commençons par étudier la première question.


### À faire

Vérifiez que *6^5 = 7776*.


On en déduit que la liste contient autant de mots qu'il y a de résultats possibles dans une séquence de cinq lancers d'un dé à six faces.

Il est donc possible d'associer chaque séquence de cinq lancers de dés à un mot de la liste de sorte que

   1. deux séquences différentes soient associées à deux mots différents ;
   2. tout mot de la liste soit associé à une séquence.

(En employant un vocabulaire mathématique, cela signifie qu'on peut
établir une bijection entre l'ensemble des séquences de cinq lancers
de dés et l'ensemble des mots de la liste.)

Une application de ce constat, c'est qu'une fois une telle association
établie, il suffit de lancer cinq fois de suite un dé et de noter les
faces apparues pour obtenir un mot choisi au hasard dans la liste.

Reste à construire une association entre les séquences de cinq lancers
et les mots.

Les mots de la liste sont tous implicitement associés à un nombre :
leur indice dans le tuple. Le premier mot de la liste est donc
associé à l'indice 0, le deuxième à l'indice 1, jusqu'au dernier
qui est associé à l'indice 7775.

Associer une séquence de lancers à un mot revient donc à associer
 cette séquence à un nombre compris entre 0 et 7775.

Il suffit donc de trouver un moyen de convertir une séquence de cinq
lancers de dés en un nombre compris entre 0 et 7775, en s'assurant que
ce procédé vérifie bien

   1. que deux séquences soient associées à deux nombre différents ;
   2. et que tout nombre compris entre 0 et 7775 soit associé à une séquence.

Une solution naturelle pour établir une telle association consiste à
ranger les 7776 séquences selon l'ordre lexicographique (i.e. l'ordre
alphabétique).


On obtient alors l'association

```
seq   : ind  : mot
11111 :    0 : montes
11112 :    1 : troue
11113 :    2 : alliais
11114 :    3 : annotes
11115 :    4 : vairon
11116 :    5 : tirer
11121 :    6 : sulkys
11122 :    7 : bornant
11123 :    8 : museaux
11124 :    9 : patrons
...
24521 : 2094 : morigener
...
66653 : 7766 : zelees
66654 : 7767 : valant
66655 : 7768 : exocet
66656 : 7769 : dejoua
66661 : 7770 : redises
66662 : 7771 : gril
66663 : 7772 : planta
66664 : 7773 : sourcil
66665 : 7774 : souda
66666 : 7775 : tour
```

En désignant par *c\_0c\_1c\_2c\_3c\_4* une séquence de cinq lancers
de dés, les *c_k* étant des chiffres de 1 à 6, comment peut-on
calculer l'indice associé selon la méthode décrite ci-dessus ?

*Le raisonnement suivant consiste à expliquer qu'il s'agit de
considérer qu'il s'agit de l'écriture en base 6 d'un nombre, avec un
décalage de +1 pour chacun des chiffres. Vous pouvez donc le passer si
cela est clair pour vous et aller directement à sa conclusion.*

Étudions le cas de la séquence *c\_0c\_1c\_2c\_3c\_4=24521* pour
laquelle la table ci-dessus nous indique que l'indice associé est
2094. Voici les différentes étapes de cette étude :

  1. Comme *c\_0=2*, cela signifie que toutes les séquences commençant par 1 se situent avant. Et il y a *6^4=1296* telles séquences.

  2. Comme *c\_1=4*, toutes les séquences débutant par  `21`, `22` et `23` sont situées avant `24521`. Or il y a *6^3=216* séquences débutant par `21`, et de même pour celles débutant par `22` et ` 23`. Il y a donc *3x6^3 = 648* séquences débutant par `21`, `22` ou `23` situées avant `24521`.
	 
  3. Comme *c\_2=5*, toutes les séquences débutant par `241`, `242`,
  `243` et `244` sont situées avant `24521`. Or il y a *6^2=36*
  séquences débutant par chacun de ces triplets. Il y a donc *4x6^2 = 144* séquences débutant par `241`, `242`, `243` ou `244` situées avant `24521`.

  4. Comme *c\_3=2*, toutes les séquence débutant par `2451` sont situées avant `24521`. Il y a donc *6^1 = 6* séquences débutant par `2451` situées avant `24521`.

  5. Enfin, comme *c\_4=1*, il n'y a aucune séquence débutant par `2452` située avant `24521`.

  6. Au final, il y a *1296 + 648 + 144 + 6 + 0 = 2094* séquences situées avant la séquence `24521`. Et donc l'indice correspondant à cette séquence est bien 2094.
	
_Remarque._ La somme donnant l'indice peut se mettre sous la forme 

*(c\_0 - 1)x6^4 + (c\_1 - 1)x6^3 + (c\_2 - 1)x6^2 + (c\_3 - 1)x6^1 + (c\_4 - 1)x6^0.*

_Conclusion._ L'indice associé à la séquence *c\_0c\_1c\_2c\_3c\_4* est obtenue par

*indice = (c\_0 - 1)x6^4 + (c\_1 - 1)x6^3 + (c\_2 - 1)x6^2 + (c\_3 - 1)x6^1 + (c\_4 - 1)x6^0.*

On peut généraliser ce résultat pour déterminer le nombre associé à une séquence de longueur *n* :

**N = Somme_{k=0}^{n-1} (c\_k - 1)x6^{n-1-k}.**


### À faire

Réalisez une fonction nommée `en_nombre`, paramétrée par une séquence
de lancers de dés représentée par une chaîne de caractères, qui
renvoie un nombre entier obtenu par le procédé décrit
ci-dessus. Ainsi, avec des séquences de cinq lancers de dés, on doit
obtenir un nombre compris entre 0 et 7775 inclus.

```python
>>> en_nombre('11111')
0
>>> en_nombre('66666')
7775
>>> en_nombre('24521')
2094
```



<!--
**Remarques :**
   * la réalisation précédente de la fonction `en_nombre` suit un algorithme classique de l'évaluation des polynômes : l'algorithme de Horner. Cet algorithme optimise le nombre d'opérations arithmétiques (addition/multiplication).
   * la réalisation précédente ne se limite pas aux séquences de longueur 5. Si on se limitait aux séquences de longueur 5 , on pourrait se dispenser de la boucle et précalculer les premières puissances de 6.
-->

<!--
### À chercher

Quels sont les cinq lancers de dés pour lesquels la fonction en_nombre renvoie le nombre 3000 ?

-->

### À faire

Réalisez une fonction qui donne le mot de la liste `LISTE_MOTS` correspondant à la séquence de cinq lancers de dés passée en paramètre.

Voici quelques exemples de ce que vous devez obtenir :

```python
>>> donne_mot('11111')
'montes'
>>> donne_mot('66666')
'tour'
>>> donne_mot('24521')
'morigener'
```


Vous voici armés pour construire des phrases de passe obtenues par lancers de dés.

Une phrase de passe peut contenir autant de mots que l'on veut. Bien entendu pour la produire, il faudra cinq lancers de dés pour chacun des mots. Donc si vous voulez une phrase de passe avec *n* mots, il faudra lancer *5n* fois le dé.


Le module `random` est l'un des modules prédéfinis de python. Sans
surprise ce module définit des fonctions qui permettent la manipulation de
générateurs pseudo-aléatoires.  Vous pouvez utiliser les fonctions qu'il
définit après avoir évalué l'expression

```python
import random
```

Vous pouvez par exemple étudier les documentations des fonctions
`random.randrange`, `random.randint` ou `random.choice`.

### À faire

Réalisez une fonction `genere_n_sequences_alea` paramétrée par un entier
`n` qui renvoie une chaîne de caractères constituée de `n` séquences
de 5 lancers de dés.

Voici un exemple de ce que vous pouvez obtenir :
```python
>>> genere_n_sequences_alea(2)
'5311514166'
>>> genere_n_sequences_alea(3)
'111116666624521'
```


### À faire

Réalisez une fonction `genere_phrase_passe` paramétrée par une
séquence de lancers de dés dont la longueur est un multiple de cinq
qui renvoie une phrase de passe dont le nombre de mots la constituant
dépend de la longueur de la séquence, chacun de ces mots étant séparés
par un trait d'union (caractère `-`).

Voici un exemple de ce que vous devez obtenir :
```python
>>> genere_phrase_passe('111116666624521')
'montes-tour-morigener'
```


## Augmenter l'entropie

Une première manière d'augmenter l'entropie des phrases de passe
générées est de perturber la chaine produite en y mélangeant
majuscules et minuscules. C'est ce que nous allons faire maintenant.

<!--
### À faire Réalisez un prédicat `est_lettre` paramétré par un
caractère et dont le résultat est `True` si ce caractère est l'une des 26
lettres non accentués de l'alphabet.

Voici un exemple de ce que vous devez obtenir :
```python
>>> est_lettre('a')
True
>>> est_lettre('B')
True
>>> est_lettre('1')
False
```
-->

### À faire

Réalisez une fonction `perturbe_chaine` paramétrée par une chaîne de
caractères `s` qui renvoie la chaîne obtenue en changeant
aléatoirement ou pas (une chance sur deux)  chacune des lettres de `s`
en sa majuscule ou minuscule. Les autres caractères de `s` restent
inchangés.

Voici un exemple de ce que vous pouvez obtenir :
```python
>>> perturbe_chaine("timoleon")
'timolEOn'
>>> perturbe_chaine("timoleon")
'tIMOlEON'
```

### À faire

Réalisez la fonction `genere_phrase_passe2` qui est une 
variante de `genere_phrase_passe` pour laquelle les lettres ont été
aléatoirement mises en majuscules ou minuscules.

Voici un exemple de ce que vous pouvez obtenir :
```python
>>> genere_phrase_passe2('111116666624521')
'MoNtEs-toUr-MOrIGENER'
```



## Augmenter encore l'entropie

Une seconde manière d'ajouter de l'entropie consiste à remplacer
certaines lettres par des caractères particuliers. Par exemple le
`i`par un `1` et le `o` par un `0` pour que la chaîne `timoleon`
devienne `t1m0le0n`.

**Attention :** Cette partie utilise des dictionnaires. Mais si vous ne
  connaissez pas cette notion, cela n'est pas un problème. Nous
  l'aborderons ultérieurement dans la formation. Nous ne ferons ici
  qu'utiliser un dictionnaire défini sans le modifier. Pour faire court, un
  dictionnaire permet d'associer une valeur à une clef. On parle
  aussi de *liste associative*. Voici le dictionnaire que nous
  utiliserons dans la suite, sa définition se fait en énumérant les
  couples ` clef : valeur ` 

```python
EQUIVALENTS = {
    'a' : '@',
    'b' : '8',
    'e' : '3',
    'i' : '1',
    'o' : '0'
}
```

Dans un dictionnaire chaque clef est unique. La clef permet d'accéder
  directement à la valeur qui lui est associée. La notation est alors
  similaire à celle des accès indicés pour les chaînes ou les listes.
 
```python
>>> EQUIVALENTS['a']
'@'
>>> EQUIVALENTS['i']
'1'
```
 
Pour perturber un peu plus nos phrases de passe, nous allons continuer à
modifier aléatoirement les lettres en majuscules ou minuscules, mais
cette fois, en plus, lorsqu'une lettre n'aura pas été modifiée, s'il
s'agit de l'une des clefs de `EQUIVALENTS` alors on va aléatoirement
(une chance sur deux) la remplacer ou pas par la valeur qui lui est
associée.

### À faire

Prolongez la fonction `perturbe_chaine` en réalisant une fonction
`perturbe_chaine2` paramétrée par une chaîne de caractères `s` qui
renvoie la chaîne obtenue en modifiant `s` comme indiqué ci-dessus.

Voici un exemple de ce que vous pouvez obtenir :
```python
>>> perturbe_chaine2("timoleon")
'TiMol30N'
>>> perturbe_chaine2("timoleon")
'tiMol3on'
>>> perturbe_chaine2("timoleon")
'T1m0LeON'
```


### À faire

Réalisez la fonction `genere_phrase_passe3` qui applique la
perturbation précédente aux phrases de passe générée.

Voici un exemple de ce que vous pouvez obtenir :
```python
>>> genere_phrase_passe3('111116666624521')
'm0NTes-toUr-Morig3neR'
>>> genere_phrase_passe3('111116666624521')
'MonTeS-touR-mor1GENeR',
```
