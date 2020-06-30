# Le modèle objet 
(d'après le  [livre de G.Swinnen](https://github.com/VLesieux/NSI/blob/master/Ressources_Python/apprendre_python3_livre_Swinnen.pdf))

## 1) Quel sens donner au mot objet ?


Le concept d'objet représente : 

- un objet physique : une voiture, pièces d'une voiture, conducteur, passagers...
- un objet informatique : un fichier, une image, un son...
- un concept porteur d'une notion qu'il peut partager...

Chaque objet possède en soi les données qui le décrivent sous forme d'**attributs** mais également les **méthodes** nécessaires pour gérer ses propres données : modifier, mettre à jour, partager..

Le  développement objet consiste donc à créer un ensemble d'objets représentant le mieux possible ce qu'ils modélisent, puis à gérer leurs interactions.

## 2) Notion de classe

Une classe contient des instructions déclarant une variable qui devient un attribut de la classe ou une fonction qui devient alors méthode.
Une classe **encapsule** ainsi toutes ses données qui sont accessibles.
Elle est une description unique pouvant donner naissance à différents objets disposant de la même structure de données (mêmes noms et types d'attributs) et des mêmes méthodes. 
L'intérêt est que les différents objets utilisés peuvent être construits indépendamment les uns des autres éventuellement par des programmateurs différents. L'utilisation de classes permet entre autres avantages d'éviter au maximum l'emploi de variables globales qui peuvent être modifiées ou même redéfinies n'importe où dans le programme, en particulier si plusieurs programmateurs travaillent sur le programme dans le cas d'un logiciel.
Un second bénéfice de l'utilisation des classes est la possibilité de construire de nouveaux objets à partir d'ojets préexistants par des mécanismes dits de dérivation et de polymorphisme. La dérivation est la construction d'une classe enfant à partir d'une classe parente ; l'enfant acquiert toutes les propriétés et les fonctionnalités de son ancêtre. Le polymorphisme permet d'attribuer des comportements différents à des objets dérivant les uns des autres ou du même ojet en fonction du contexte.

## 3) Exemples

### a) Création d'une classe Point : les attributs

On crée ici une classe fondamentale, c'est-à-dire ne dérivant d'aucune autre, raison pour laquelle la référence à indiquer doit être le nom spécial **object**. 

Par ailleurs, une convention veut que leur nom commence par une majuscule.

```python
class Point(object):
    "Définition d'un point géométrique"
```

À partir de cette classe, on peut créer des **instances**.

```python
p9=Point()
```

On voit ainsi que les classes auxquelles on fait appel dans une instruction doivent toujours être accompagnées de parenthèses même si aucun argument n'est transmis, certaines classes cependant peuvent être appelées avec des arguments.

```python
>>> print(p9)
<__main__.Point object at 0x101ed2c18>
```

On voit ainsi que l'instance p9 est définie au niveau principal (main) du programme dans un emplacement bien déterminé de la mémoire vive ; cet emplacement est donné en notation hexadécimale.

```python
>>> print(p9.__doc__)
Définition d'un point géométrique
```

On appelle ici l'attribut prédéfini __doc__.

Nous pouvons maintenant donner des attributs à cet objet ou variables d'instance par une simple **instruction d'assignation**. On verra par la suite que ce n'est pas la bonne manière de procéder.

```python
p9.x=3.0
p9.y=4.0
```
```python
>>> print(p9.x)
3.0
```

Remarque : deux instances d'un objet sont différentes même si elles ont les mêmes attributs, on peut toutefois créer des allias l'un de l'autre.

```python
p1=Point()
p1.x=3.0
p1.y=4.0
```

```python
>>> p1==p9
False
```

```python
p2=p1
```

```python
>>> p1==p2
True
>>> print(p1)
<__main__.Point object at 0x10d427b70>
>>> print(p2)
<__main__.Point object at 0x10d427b70>
```

Les deux références p1 et p2 pointent vers le même emplacement mémoire.


Du fait de leur **encapsulation dans l'objet**, les attributs sont des variables distinctes d'autres variables qui pourraient porter le même nom.

#### Il est possible de passer un objet comme paramètre d'une fonction.   


Par exemple : 

```python
def affiche_point(p):
    print("coordonnée horizontale",p.x,"coordonnée verticale",p.y)
```

```python
>>> affiche_point(p9)
coordonnée horizontale 3.0 coordonnée verticale 4.0
```

#### Nous pouvons créer des objets composés d'objets.

Nous créons d'abord une classe permettant de définir les rectangles ; nous choisissons de les définir par la donnée de leur largeur, de leur hauteur et de la position du coin supérieur gauche.

```python
class Rectangle(object):
    "Définition d'une classe de rectangles"
````

Puis une instance :

```python
boite=Rectangle()
boite.largeur=50.0
boite.hauteur=35.0
boite.coin=Point()
boite.coin.x=12.0
boite.coin.y=27.0
````

L'attribut coin de l'objet boite possède les attributs x et y.

#### Nous pouvons avoir des objets comme valeurs de retour d'une fonction

```python
def trouve_centre(box):
    p=Point()
    p.x=box.coin.x+box.largeur/2.0
    p.y=box.coin.y+box.hauteur/2.0
    return p
````

```python
>>> centre=trouve_centre(boite)
>>> print(centre.x,centre.y)
37.0 44.5
````

#### Nous pouvons modifier des objets

Par exemple, nous pouvons modifier l'attribut de largeur d'une boite en réassignant cet attribut.

```python
boite.largeur=boite.largeur-5
>>> boite.largeur
45.0
````

En fait par la suite, il ne faudra plus modifier les attributs d'un objet par assignation directe depuis le monde extérieur, comme on l'a fait jusqu'à présent. Mais grâce à l'utilisation de méthodes ; l'ensemble des méthodes constitue l'interface de l'objet.

### b) Création d'une classe Time : les méthodes

```python
class Time(object):
    "Définition d'une classe pour les objets temporels"

instant=Time()
instant.heure=11
instant.minute=34
instant.seconde=25
````

Dans un premier temps, on se propose de créer une fonction qui affiche l'heure.

```python
def affiche_heure(t):
    print("{0}:{1}:{2}".format(t.heure,t.minute,t.seconde))
>>> affiche_heure(instant)
11:34:25
````

Dans le but de transformer cette fonction en méthode, nous allons placer cette fonction à l'intérieur de la définition de la classe en utilisant toujours le mot reservé def, la définition d'une méthode doit toujours comporter au moins un paramètre, lequel doit être la référence d'instance **self** qui doit être listée en premier. Ce paramètre self est nécessaire car il sert à désigner l'instance à laquelle la méthode sera associée.

```python
class Time(object):
    "Définition d'une classe pour les objets temporels"
    def affiche_heure(self):
        print("{0}:{1}:{2}".format(self.heure,self.minute,self.seconde))
>>> maintenant=Time()
>>> maintenant.heure=12
>>> maintenant.minute=28
>>> maintenant.seconde=35
>>> maintenant.affiche_heure()
12:28:35
````
#### Nous allons créer une méthode constructeur

Une méthode constructeur va permettre d'assigner des attributs par défaut ; les variables d'instance sont ainsi prédéfinies. La méthode constructeur est exécutée automatiquement lorsqu'on instancie un nouvel objet à partir d'une classe. Pour que cette méthode soit reconnue comme telle, elle devra obligatoirement s'appeler __init__.

```python
class Time(object):
    "Définition d'une classe pour les objets temporels"
    def __init__(self):
        self.heure=11
        self.minute=0
        self.seconde=0
    def affiche_heure(self):
        print("{0}:{1}:{2}".format(self.heure,self.minute,self.seconde))
>>> instant_donne=Time()
>>> instant_donne.affiche_heure()
11:0:0
````
Lors de son instanciation, l'objet instant_donne s'est vu attribuer immédiatement les attributs heure, minute et seconde.

Comme toute méthode, la méthode __init__() du constructeur peut être dotée de paramètres. Ceux-ci vont permettre d'initialiser certaines des variables d'instance au moment même de l'instanciation de l'objet.

```python
class Time(object):
    "Définition d'une classe pour les objets temporels"
    def __init__(self,h=11,m=0,s=0):
        self.heure=h
        self.minute=m
        self.seconde=s
    def affiche_heure(self):
        print("{0}:{1}:{2}".format(self.heure,self.minute,self.seconde))
````

Lorsque l'on écrit l'instruction d'instanciation d'un nouvel objet, et que l'on veut transmettre des arguments à sa méthode constructeur, il suffit de placer ceux-ci dans les parenthèses qui accompagnent le nom de la classe, de la même manière que lorsque l'on invoque une fonction quelconque.

```python
>>> nouvel_instant=Time(5,23,12)
>>> nouvel_instant.affiche_heure()
5:23:12
>>> nouvel_instant=Time(5,23)
>>> nouvel_instant.affiche_heure()
5:23:0
>>> nouvel_instant=Time(s=43)
>>> nouvel_instant.affiche_heure()
11:0:43
````
Si l'on omet un ou plusieurs arguments, on retrouve les valeurs par défaut.

### c) Exercices corrigés

1) Définissez une classe Domino() qui permet d'instancier des objets simulant les pièces d'un jeu de domino. Le constructeur de cette classe initialisera les valeurs des points présents sur les deux faces A et B du domino (valeurs par défaut = 0). Deux méthodes seront définies : affiche_points() qui affiche les points présents sur les deux faces et la méthode valeur() qui renvoie la somme des points présents sur les deux faces.

```python
class Domino(object):
    def __init__(self,a=0,b=0):
        self.faceA=a
        self.faceB=b
    def affiche_points(self):
        print("Face A",self.faceA,"Face B",self.faceB)
    def valeur(self):
        print(self.faceA+self.faceB)
>>> domino=Domino(5,6)
>>> domino.affiche_points()
Face A 5 Face B 6
>>> domino.valeur()
11
```

2) Définissez une classe CompteBancaire() qui permette d'instancier des objets tels que compte1, compte2...Le constructeur de cette classe initialisera deux attributs d'instance nom et solde, avec les valeurs par défaut 'Dupont' et 1000. Trois méthodes seront définies : depot(somme) qui permettra d'ajouter une certaine somme au solde, retrait(somme) qui permettra de retirer une certaine somme au solde et affiche() qui permettra d'afficher le nom du titulaire et le solde de son compte.

```python
class CompteBancaire(object):
    def __init__(self,nom='Dupont',solde=1000):
        self.nom=nom
        self.solde=solde
    def depot(self,somme):
        self.solde+=somme
    def retrait(self,somme):
        self.solde-=somme
    def affiche(self):
        print("Le solde de ",self.nom," vaut : ",self.solde)
        
>>> compte1=CompteBancaire('Duchemol',800)
>>> compte1.depot(200)
>>> compte1.affiche()
Le solde de  Duchemol  vaut :  1000
```

## 4) La dérivation

L'un des principaux atouts de la programmation objet réside dans le fait que l'on peut se servir d'une classe préexistante pour en créer une nouvelle, qui héritera toutes ses propriétés, mais qui pourra modifier certaines d'entre elles et/ou y ajouter les siennes propres.
Ce procédé s'appelle dérivation.

On peut ainsi par exemple créer la classe Mammifere() et à partir de cette classe parente créer plusieurs classes filles comme une classe Primate(), une classe Rongeur() ou encore une classe Carnivore() etc... qui hériteront toutes des caractéristiques de la classe Mammifere().

Puis à partir de la classe Carnivore(), on pourra dériver la classe Belette(), Loup(), Chien() etc...

```python
class Mammifere(object):
    caract1="Il allaite ses petits"
    
class Carnivore(Mammifere):
    caract2="Il se nourrit de la chair de ses proies"
    
class Chien(Carnivore):
    caract3="Son cri s'appelle l'aboiement"
    
>>> mirza=Chien()
>>> print(mirza.caract1,mirza.caract2,mirza.caract3)
Il allaite ses petits Il se nourrit de la chair de ses proies Son cri s'appelle l'aboiement
```

L'instance mirza peut modifier son attribut mais il ne peut pas modifier l'attribut de la classe, ce que l'on peut vérifier en créant une nouvelle instance.

```python
>>> mirza.carac2="Son corps est couvert de poils"
>>> mirza.carac2
'Son corps est couvert de poils'
>>> fido=Chien()
>>> fido.caract2
'Il se nourrit de la chair de ses proies'
```

Il y a donc deux variables différentes : l'une dans l'**espace des noms de l'objet** mirza, l'autre dans l'**espace des noms de la classe** Carnivore().
La règle de priorité est la suivante : Python commence par regarder la valeur d'une variable dans l'espace local, le plus interne, et la recherche s'arrête, sinon il examine l'espace des noms de la structure parente, et cela jusqu'au niveau principal du programme.

## 5) Héritage et polymorphisme

Exemple 1 : on crée une classe Atome() et une classe Ion() qui dérive de celle-ci.

```python
class Atome(object):
    "Atomes simplifiés parmi les 10 premiers éléments du tableau périodique"
    table=[None,('H',0),('He',2),('Li',4),('Be',5),('B',6),('C',6),('N',7),('O',8),('F',10),('Ne',10)]
    #Donnée des nombres de neutrons
    def __init__(self,Z):
        self.nb_protons=Z
        self.nb_electrons=Z
        self.nb_neutrons=Atome.table[Z][1]
    def affiche(self):
        print("Symbole de l'élément : ",Atome.table[self.nb_protons][0])
        print("{0} protons, {1} électrons, {2} neutrons".format(self.nb_protons,self.nb_electrons,self.nb_neutrons))

class Ion(Atome):
    "Les ions sont des atomes qui ont gagné ou perdu des électrons"
    def __init__(self,Z,charge):
        Atome.__init__(self,Z)
        self.charge=charge
        self.nb_electrons-=charge
    def affiche(self):
        Atome.affiche(self)
        print("Particule électrisée de charge :",self.charge)
>>> a1=Atome(6)
>>> a1.affiche()
Symbole de l'élément :  C
6 protons, 6 électrons, 6 neutrons
>>> a2=Ion(8,-2)
>>> a2.affiche()
Symbole de l'élément :  O
8 protons, 10 électrons, 8 neutrons
Particule électrisée de charge : -2
```

Les objets Atome() sont instanciés par leur nombre de proton Z (ou numéro atomique).
Les objets Ion() sont instanciés par leur nombre de proton Z et leur charge.
On observe que la même méthode affiche est utilisée dans les deux objets avec l'ajout d'une ligne supplémentaire dans le cas de l'ion.
On voit que dans la méthode constructeur d'une classe dérivée, il faut faire un appel à la méthode constructeur de la classe précédente.


Exemple 2 : création d'un module contenant des bibliothèques de classes

On crée un fichier formes.py que l'on peut appeler ensuite comme module dans un autre fichier.

```python
class Rectangle(object):
    "Classe des rectangles"
    def __init__(self,longueur=0,largeur=0):
        self.L=longueur
        self.l=largeur
        self.nom="rectangle"
    def perimetre(self):
        return "({0}+{1})*2={2}".format(self.L,self.l,(self.L+self.l)*2)
    def surface(self):
        return "{0}*{1}={2}".format(self.L,self.l,self.L*self.l)
    def mesures(self):
        print("Un {0} de {1} sur {2}".format(self.nom,self.L,self.l))
        print("a une surface de {0}".format(self.surface()))
        print("et un périmètre de {0}".format(self.perimetre()))

class Carre(Rectangle):
    "Classe des carrés"
    def __init__(self,cote):
        Rectangle.__init__(self,cote,cote)
        self.nom="carré"
        
>>> import formes
>>> f1=formes.Carre(5)
>>> f1.mesures()
Un carré de 5 sur 5
a une surface de 5*5=25
et un périmètre de (5+5)*2=20
```

La classe Carre() est construite par derivation de la classe Rectangle().

