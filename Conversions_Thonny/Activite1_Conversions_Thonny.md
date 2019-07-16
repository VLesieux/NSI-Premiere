# I) La représentation binaire d'un nombre

## 1) Comparaison représentation décimale - représentation binaire

Le but de cette activité est de se familiariser avec l'écriture binaire d'un nombre qui est l'écriture utilisée par les ordinateurs n'utilisant que les bits 0 et 1.

On utilise dans le quotidien l'écriture décimale d'un nombre, c'est-à-dire son écriture en base 10.  

Par exemple : 2391=2×1000+3×100+9×10+1×1.   
Soit en utilisant la décomposition en puissances décroissantes de 10 :      
 2391=2×10^3+3×10^2+9×10^1+1×10^0  


Ce qui peut se représenter :

| 10^3  | 10^2          | 10^1          | 10^0 |
| :--------------- |:---------------:| :---------------:|-----:|
| 2        | 3        |  9 | 1 |

L'écriture binaire est l'écriture en base 2 ; elle consiste à réaliser la décomposition du nombre en utilisant les puissances décroissantes de 2.

Les 8 premières puissances de 2 nous seront utiles pour écrire les nombres compris entre 0 et 255 sur un octet :  
 1 (2^0); 2 (2^1); 4 (2^2); 8 (2^3) ; 16 (2^4) ; 32 (2^5) ; 64 (2^6) ; 128 (2^7)

Ainsi 97 s'écrit : 97 = 64 + 32 + 1 = 1×2^6+1×2^5+1×2^0  

Ce qui peut  se représenter :  

|2^7|2^6| 2^5|2^4|2^3|2^2|2^1|2^0|
|:--------------- |:---------------|:---------------|:-----|:--------------- |:---------------| :---------------|-----:|
|0|1|1|0|0|0|0|1|   


Le mot binaire de 8 bits appelé octet de valeur décimale 97 s'écrit donc : (0,1,1,0,0,0,0,1).  
On peut l'écrire plus simplement 1100001 en supprimant les 0 _**non significatifs**_ de la partie gauche.

Remarque : un mot binaire de 8 bits offre 2 possibilités 0 ou 1 par bits, soit 2^8=256 possibilités de valeurs comprises entre 0 : 00000000 et 255 : 11111111


## 2) Passer de la notation binaire à la valeur décimale    

Il s'agit cette fois de réaliser l'opération inverse : déterminer la valeur décimale du nombre à partir de son écriture binaire.  

Par exemple, la valeur décimale du mot binaire 1000101 est : 2^6+ 2^2 + 2^0 = 64 + 4 + 1 = 69


## 3) Vérification dans le Shell de Thonny   

Dans l'_**invite de commande ou prompt**_ `>>>` entrer `bin(97)`
Le résultat `'0b1100001'` est cohérent : `'0b'` est la manière de désigner un nombre binaire.  


Dans l'invite de commande ou prompt `>>>` entrer maintenant `0b1000101` on retrouve 69.
 
#  II) Écriture d'un premier programme en python

## 1) Écriture d'un premier programme utilisant les outils natifs du language

On se propose d'écrire un premier programme qui demande un nombre entier et retourne sa représentation binaire.  
Pour demander à l'utisateur d'entrer un nombre entier on écrit :   ```x=input("Entrez un nombre entier : ")```.  
Après avoir enregistré ce programme au nom de Activite1.py et coché _Variables_ dans _View_, on voit apparaître dans le tableau des Variables le nom de la variable x dont la valeur est donnée entre guillemets : il s'agit donc d'une chaîne de caractères ou string.  
On le vérifie également en demandant dans le Shell le type de x : `>>> type(x)` on obtient `<class 'str'>`.  
Il faut dans un premier temps convertir en entier cette variable à l'aide de ```int(x)```avant d'en demander la conversion en binaire à l'aide de la fonction ```bin()```
Ce qui donne notre premier programme :  

```python
x=input("Entrez un nombre entier : ")
#ceci est un commentaire : on demande à l'utilisateur d'entrer un nombre qui sera la variable x
#pour passer une ligne de code en commentaire, prendre la ligne puis clic droit "Toggle Comment" 
# et à nouveau pour revenir à l'état initial
y=bin(int(x))
print(y)
```
ou plus simplement :   

```python
x=input("Entrez un nombre entier : ")
print(bin(int(x)))
```

Que se passe-t-il si on ne prend pas de précaution en écrivant simplement  `print(bin(x))` ? Examinons le message d'erreur donnée par l'_**interpréteur ou compilateur**_ :    

```python
Entrez un nombre : 25
Traceback (most recent call last):
  File "/Users/vincentlesieux/Desktop/SNT 2de/Programmation/Activite1_AdresseIP_masque_reseau.py", line 2, in <module>
    print(bin(x))
TypeError: 'str' object cannot be interpreted as an integer   
```
On comprend aisément la signification du message qui explicite le type d'erreur rencontré ainsi que la ligne où cette erreur est rencontrée.

Pour réaliser aisément la conversion d'un nombre binaire en un nombre décimal, on peut écrire :   

```python
x=input("Entrez un nombre binaire : ")
print(eval(x)) 
```
```
Entrez un nombre binaire : 0b1011110011
755
```

## 2) Un algorithme pour obtenir la représentation binaire d'un nombre  

Un _**algorithme**_ est une recette qui permet d'atteindre le résultat à condition de l'appliquer rigoureusement.
Pour obtenir la représentation binaire d'un nombre, il s'agit de réaliser un processus répétitif de divisions successives par 2 que l'on arrête dès lors que le quotient de la division est nul, on note alors les restes des divisions de bas en haut. Plus précisément, on observe que dans le processus le quotient devient le nouveau dividende ou que le nouveau dividende prend la valeur du quotient précédent.

Observons cette image qui représente la démarche à suivre sur papier :    


![Représentation binaire de 755 ](divisions.png)

## 3) Programmation de la conversion décimal-binaire en utilisant l'algorithme

On se propose de réaliser un processus qui sera répété aussi longtemps que la condition d'arrêt ne sera pas atteinte.  

L'idée est de garder en mémoire le reste de la division du dividende par 2 en ajoutant les valeurs de droite à gauche par **_concaténation_** pour obtenir le mot binaire final. D'autre part, il nous faudra traduire dans le programme que le quotient devient le nouveau dividende.   
On utilise la notation _**//**_ pour obtenir le quotient entier d'une division et la notation _**%**_ pour obtenir le reste d'une division :   

```python
>>> 377/2
188.5
>>> 377//2
188
>>> 377%2
1
```

```python
x=input("Entrez un nombre entier : ")
a=""
dividende=int(x)
#on prend soin de transformer le string x en entier
quotient=dividende//2
while quotient>0:#on réalise une boucle non bornée
    reste=dividende%2
    a=str(reste)+a
    quotient=dividende//2
    dividende=quotient
print(a) 
```

Dans ce programme, on utilise une _**boucle non bornée**_ dite _**boucle while**_ parce qu'on ne sait pas d'avance le nombre de tour à effectuer. On peut voir le déroulement du programme à l'aide du debugger, en entrant dans la boucle (step into) pour voir son déroulement.
On observera également l'_**indentation**_ qui a été réalisée pour écrire cette boucle.

## 4) Améliorations du programme

Une première amélioration consiste à prévenir l'arrêt du programme si l'utilisateur entre autre chose qu'un nombre, on pourra alors lui demander gentiment de recommencer la saisie. 
Dans Python le mécanisme de traitement des exceptions se fait avec les _**instructions**_ `try - except`.
De plus on peut demander au programme de réinterroger l'utilisateur après exécution ; celui-ci mettra fin au programme en cliquant sur le bouton STOP.

Deux _**fonctions**_ sont utilisées dans le programme.  
La première fonction `est_un_nombre_entier(valeur_entree)` retourne le _**booléen True**_ si l'utilisateur  entre effectivement un entier ; cette fonction admet comme _**paramètre**_ la valeur entrée au clavier.   
La deuxième fonction `convertir()` n'admet pas de paramètre et lance la conversion. 

```python
def est_un_nombre_entier(valeur_entree):#définition d'une première fonction
    try:
        return type(int(valeur_entree))==int
    except:
        print("veuillez entrer un nombre entier S.V.P ")
        convertir()
def convertir():#définition d'une deuxième fonction
    x=input("Veuillez entrer un nombre entier : ")
    if est_un_nombre_entier(x):#on utilise l'instruction conditionnelle if et un appel à la première fonction
        a=""
        dividende=int(x)
        quotient=dividende//2
        while quotient>0:
            reste=dividende%2
            a=str(reste)+a
            quotient=dividende//2
            dividende=quotient
        print(a)
        convertir()#pour faire des demandes réitérées, on appelle à nouveau la fonction
convertir()#pour réaliser la première demande, on appelle une première fois la fonction
```

## 5) Programmation de la conversion binaire-décimal

On demande à l'utilisateur d'entrer une chaîne de caractère correspondant au mot binaire.
On parcourt la chaîne de caractères en traitant les bits les uns après les autres pour obtenir la valeur décimale.
On réalise cette fois une _**boucle bornée**_ ou _**boucle for**_ car on sait combien de tours devront être effectués, c'est la longueur de la chaîne de caractère.

Pour bien comprendre le programme, voyons d'abord quelques manipulations sur une _**chaîne de caractère_** qui se comporte comme une _**liste**_.

```python
>>> liste=[1,5,"A",4,"e"]
>>> liste[2]#la liste est indicée en commençant par l'indice 0
'A'
>>> mot="jardin"
>>> mot[2]#on récupère l'élément de la chaîne d'indice 2
'r'
>>> mot[2:4]#on récupére tous les éléments de la chaîne entre l'indice 2 compris et l'indice 4 non compris
'rd'
>>> mot[2:]#on récupère tous les éléments à partir de l'indice 2
'rdin'
>>> mot[:3]#on récupère tous les éléments depuis l'indice 0 jusque 3 non compris
'jar'
>>> mot[2:5:2]#on récupère tous les élèments depuis l'indice 2 jusque 5 non compris avec un pas de 2
'ri'
>>> mot[5:2:-1]#on récupère tous les éléments depuis l'indice 5 à 2 non compris avec un pas de -1
'nid'
>>> mot[::-1]#on récupère la chaîne de caractère renversée ; c'est ce qu'on va utiliser pour notre programme
'nidraj'
>>> len(liste)
5
>>> len(mot)
6
```

Pour bien comprendre la boucle for, commençons par un exemple simple :

```python
x="jardin"
for i in range(5):# de 0 compris à 5 non compris
    print(x[i])
```
```
j  
a  
r   
d   
i   
```

```python
x="jardin"
for i in range(len(x)):#permet de parcourir tous les éléments d'une chaîne ou d'une liste
    print(x[i])
```
 
```
j  
a  
r   
d   
i  
n   
```

D'où la proposition de programme pour réaliser la conversion binaire-décimal : 

```python
a=0
x=input("Veuillez entrer un nombre binaire : ")
for i in range(len(x)):
    a+=int(x[::-1][i])*(2**i)  
#la notation 2**i signifie 2 à la puissance i
#il est nécessaire d'utiliser int pour transformer le caractère en entier
print(a)
```

**Application** : Écrire un programme de conversion décimal-hexadécimal (base 16) dans les deux sens utilisant les notations suivantes 10 = "A"; 11 = "B" ; 12 = "C" ; 13 = "D" ; 14 = "E" ; 15 = "F"
