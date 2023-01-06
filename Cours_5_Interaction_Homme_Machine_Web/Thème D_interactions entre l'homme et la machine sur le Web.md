
# Thème D : interactions entre l'homme et la machine sur le Web

<img src="assets/programme.png" width="800" height="800" />

# Notions de HTML5, le Web côté client et le Web côté serveur

## I.	Comment fonctionne un site web et de quoi a-t-on besoin ?

Lorsqu’on entre dans un navigateur l’_**adresse**_ ou _**url**_ (Uniform Resource Locateur) d’un _**site web**_, on produit une _**requête**_ auprès du _**serveur**_ qui héberge les fichiers du site web afin qu’il nous envoie grâce au _**protocole HTTP (Hypertext Transfer Protocol)**_  ou grâce au _**protocole HTTPS (Hypertext Transfer Protocol Secure)**_ le ou les fichiers nécessaires pour créer la page sur notre ordinateur _**client**_. Ces fichiers sont alors décodés par le _**navigateur**_ de notre ordinateur (Firefox, Chrome..) pour donner naissance à la page web.   
En fait deux autres types de fichiers peuvent accompagner le fichier possédant l'extension _**.html**_ : un fichier javascript possédant l'extension _**.js**_ et un fichier possédant l'extension _**.css**_. Le rôle du fichier _**HTML**_ (_**HyperText Markup Language**_) dont la dernière version actuelle est _**HTML5**_ et dont la première version date de 1991 est d’organiser le fond c’est-à-dire le contenu brut de la page, le rôle du fichier _**JavaScript**_ est d’assurer le fonctionnement d’un programme éventuellement placé sur la page permettant une interaction avec l'utilisateur, le rôle du fichier _**CSS (Cascading Style Sheets)**_ dont la dernière version est CSS3 et la première date de 1996, est de gérer la mise en forme c’est-à-dire l’apparence de la page web.

Par exemple : https://fr.wikipedia.org

Dans la zone de recherche, on recherche informatique, on est dirigé vers 
https://fr.wikipedia.org/wiki/Informatique 

On peut aussi écrire : https://fr.wikipedia.org/wiki/Index.php?search=informatique
; on transmet ainsi un paramètre par le biais d'une adresse.


Pour créer votre site internet, vous n’avez besoin que d’un éditeur de texte (Notepad ++, Sublime Text ...), il vous suffira d’ajouter l’extension appropriée .html, .js ou .css lors de l’enregistrement, d’un hébergeur et d’un logiciel client FTP (File Transfer Protocol) tel que FileZilla pour déposer vos fichiers sur le serveur de l’hébergeur.  
Il existe également des programmes tels que Adobe Dreamweaver (WYSIWYG : What You See Is What You Get) qui facilitent grandement la création des pages html mais un bon créateur de site web doit absolument connaître les règles de base des langages HTML et CSS.

## II.	Création d’une page HTML

Comme son nom l’indique, un fichier html est constitué de _**balises**_ (markups) qui permettent au navigateur de savoir comment afficher le contenu.

On peut distinguer deux types de balises :  

-	les balises en paires : une ouvrante, une fermante. Par exemple, celles qui permettent de donner un titre à une page : ```<title> Le titre de ma page web </title>``` ou encore celles qui délimitent le corps de la page : ```<body></body>```


-	les balises orphelines :``` <img />```

Les balises possèdent généralement des options appelées _**attributs**_.  
Ainsi ```<image src= "maphoto.jpg" />``` ;  l’attribut src indique le chemin vers le fichier source de cette image.

_**Écrire des commentaires**_ : ```<!--  ceci est un commentaire  -->```  : il est très utile d’en écrire pour se retrouver dans son code et savoir le relire ultérieurement 

**Remarque**: tout le monde peut lire le code de n’importe quelle page html avec un clic droit « Afficher le code source de la page ».

_**Structure de base d’une page HTML**_ : observez comment les balises s'ouvrent et se ferment.
```html
<!DOCTYPE html><!--  on indique qu’il s’agit d’une page html   -->
<html><!--  la balise principale qui englobe tout le contenu de la page   -->
<head><!--  la section head donne des informations générales sur la page   -->
<meta charset="UTF-8"><!--  l’encodage utilisé par le fichier html, UTF8 permet d’afficher pratiquement tous les symboles de toutes les langues  -->
<title>NSI Lycée Angellier Dunkerque</title><!--  le titre qui s’affiche dans l’onglet du navigateur, il apparaît également dans les résultats de recherche des moteurs tels que Google   -->
<link rel="stylesheet" href="style_snt.css" /><!--  le lien vers le fichier css de mise en forme   -->
</head>
<body><!--  c’est le corps de la page qui va contenir tout le texte   -->
</body>
</html>
```

Des balises pour organiser et structurer le texte :

-	Organiser le texte en _**paragraphes**_ :``` <p> pour débuter un paragraphe``` et ``` </p> pour le terminer```
-	Aller à la ligne : la balise orpheline : ```<br/>```
-	Créer des titres avec des niveaux de titres de moins en moins importants. :  ```<h1> </h1> ``` ;  ```<h2> </h2> ``` ; ….. ;  ```<h6> </h6>  ``` 
-	Mettre en valeur du texte (emphasize) : ``` <em> </em> ```
-	Mettre en gras :  ```<strong> </strong> ```
- 	Souligner un texte (underline) : ```<u> </u> ```
-	Surligner le texte :  ```<mark> </mark> ```
-	Créer des listes non ordonnées ou _**listes à puces**_ :
 ```html
 <ul>
<li>premier élément </li>
<li>deuxième élément </li>
<li>troisième élément </li>
</ul>
 ```
Pour créer  une _**liste ordonnée**_, il suffit de remplacer  ```<ul> ``` et  ```</ul> ``` par  ```<ol> ``` et  ```</ol> ```

 ```html
 <ol>
<li>premier élément </li>
<li>deuxième élément </li>
<li>troisième élément </li>
</ol>
 ```

- _**Créer des liens**_

	-	Lien vers un site existant : ```<a href="http://adresse.com"> Lien vers le site qui a cet url </a>```
	-	Lien relatif vers une page2.html de mon site à partir d’une page1.html :``` <a href="page2.html">Lien vers la page2 </a>```  
	Remarque : en l’occurrence les deux fichiers doivent se trouver dans le même dossier ; si ce n’est pas le cas, on l’indiquera comme ceci : ```<a href="dossier2/page2.html">Lien vers la page2 située dans le dossier 2</a>```
	-	Lien vers une ancre, c’est-à-dire un repère dans la page, ce qui peut être utile si la page est longue. On choisit pour cela n’importe quelle balise à l’endroit approprié à laquelle on donne un identifiant :  
	 ```<p id="monparagraphe"> Mon paragraphe</p>``` puis ```<a href="#monparagraphe">Lien vers mon paragraphe</a>```

Remarque :  on peut forcer l’ouverture du lien dans une nouvelle fenêtre en ajoutant dans la balise l’attribut ```target="_blank"``` ; pour faire un lien pour télécharger un fichier, on fait un lien en indiquant simplement le nom du fichier à télécharger :``` <a href="monfichierimage.jpg">Fichier à télécharger< /a> ``` 
	
	
- _**Insérer des images**_

La taille de l’image ne doit pas être trop importante évidemment pour éviter un temps de chargement trop long aussi utilise-t-on en général le format JEPG à l’extension .jpg ou .jpeg qui est le format le plus compressé pour les photos. Pour les graphiques, on utilise le format PNG 8bits : 2^8=256 couleurs ou PNG 24 bits : 2^24=16 millions de couleurs.
L’insertion de l’image se fait avec la balise orpheline ```<img />```  et l’attribut source src :
```<img src="monimage.jpg" />```

- _**Insérer des boutons : événement côté client**_


1. Première méthode

On utilise `<button id="executer" onclick="action()" type="button">Appuyer</button>`

```html
<!DOCTYPE html>
<html>
<head>
<title>Page Title</title>
<meta charset="UTF-8">
</head>
<body>

Nom :<input style="font-size: 14px;text-align:center;width:140px" id="nom" value=""></input>

<button id="executer" onclick="action()" type="button">Appuyer</button>
<p id="demo"></p>
<script>

function action() {
  document.getElementById("demo").innerHTML = "YOU CLICKED ME and YOU WROTE "+document.getElementById("nom").value;
}
</script>
</body>
</html>
```

Remarque : on voit que le nom entré dans la barre d'input par l'utilisateur est contenu dans l'élément dont l'attribut `id` est 'nom'.

2. Deuxième méthode

On a ajouté un **écouteur d'événement** qui attend l'événement `click`.

```html
<!DOCTYPE html>
<html>
<head>
<title>Page Title</title>
<meta charset="UTF-8">
</head>
<body>

Nom :<input style="font-size: 14px;text-align:center;width:140px" id="nom" value=""></input>

<button id="executer" type="button">Appuyer</button>
<p id="demo"></p>
<script>
document.getElementById("executer").addEventListener("click", action);

function action() {
  document.getElementById("demo").innerHTML = "YOU CLICKED ME and YOU WROTE "+document.getElementById("nom").value;
}
</script>
</body>
</html>
```

3. Troisième méthode

On sépare le fichier JavaScript du fichier html, en plaçant dans le premier fichier dont l'extension est `.html` un lien vers le fichier d'extension `.js`, cela se fait avec :
`<script language="javascript" type="text/javascript" src="script.js"> </script>`

<u>action.html</u>

```html
<!DOCTYPE html>
<html>
<head>
<title>Page Title</title>
<meta charset="UTF-8">

</head>
<body>

Nom :<input style="font-size: 14px;text-align:center;width:140px" id="nom" value=""></input>

<button id="executer" type="button">Appuyer</button>
<p id="demo"></p>

</body>
<script language="javascript" type="text/javascript" src="action.js"></script>
</html>
```


<u>action.js</u>

```js
document.getElementById("executer").addEventListener("click", action);

function action() {
  document.getElementById("demo").innerHTML = "YOU CLICKED ME and YOU WROTE "+document.getElementById("nom").value;
}
```

- _**Insérer un tableau**_

 ```html
<!DOCTYPE html>
<html>
<head>
<title>Page Title</title>
<meta charset="UTF-8">
</head>
<body>
<table style='border:3px solid #6495ed;'>	
<tr >
<td style='border:2px solid #ff0000;'>Cellule 1
</td>
<td>Cellule 2
</td>
<td>Cellule 3
</td>
</tr>
<tr>
<td>Cellule 4
</td>
<td>Cellule 5
</td>
<td>Cellule 6
</td>
</tr>
</table>
</body>
</html>
 ```
- _**Création d'un formulaire : événement côté serveur**_

On retiendra que lors de la consultation d'une page web, le langage HTML est exécuté **côté client** tandis que le langage PHP est exécuté **côté serveur**. Il faut donc disposer d'un serveur qui herberge les pages (comme alwaysdata.net), il existe aussi des **serveur web local** tels que MAMP (le logiciel MAMP, abbréviation de Macintosh, Apache, Mysql and PHP) qui permet de lancer un serveur sur une machine fonctionnant sur le système d'exploitation Mac OS X (cela est utilisé pour essayer son code php avant de le mettre en ligne).

On observera dans la console la différence entre les deux méthodes GET et POST.

Première méthode :  `**GET** ` : 
[formulaire GET à expérimenter sur le serveur alwaysdata](http://isnangellier.alwaysdata.net/php/formulaire1.html)

formulaire1.html

 ```html
<html>
<body>
<head>
<title>Formulaire1</title>
<meta charset="UTF-8">
</head>

<form method="get" action="exploitation1.php">
Nom : <input type="text" name="nom" size="12">
<br>
Prénom : <input type="text" name="prenom" size="12">
<input type="submit" value="OK">
</form>
</body>
</html>
 ```

exploitation1.php

 ```html
<html>
<head>
<title>Réception</title>
<meta charset="UTF-8">
</head>
<body>
<?php
$prenom = $_GET['prenom'];
$nom = $_GET['nom'];
?> 
Bonjour <?php echo($prenom.' '.$nom);?> 
</body>
</html>
 ```

Deuxième méthode :  `**POST** `  : 
[formulaire POST à expérimenter sur le serveur alwaysdata](http://isnangellier.alwaysdata.net/php/formulaire2.html)

formulaire2.html

 ```html
<html>
<body>
<head>
<title>Formulaire2</title>
<meta charset="UTF-8">
</head>

<form method="post" action="exploitation2.php">
Nom : <input type="text" name="nom" size="12">
<br>
Prénom : <input type="text" name="prenom" size="12">
<input type="submit" value="OK">
</form>
</body>
</html>
 ```

exploitation2.php

 ```html
<html>
<head>
<title>Réception</title>
<meta charset="UTF-8">
</head>
<body>
<?php
$prenom = $_POST['prenom'];
$nom = $_POST['nom'];
?> 
Bonjour <?php echo($prenom.' '.$nom);?> 
</body>
</html>
 ```

À retenir :

- On observe ainsi qu'un **formulaire** en HTML commence par la balise **`<form>`**.
- La **méthode POST** est plus appropriée que la **méthode GET** quand il s'agit d'envoyer dans le formulaire d'une page web des paramètres sensibles tels que des mots de passe car ces paramètres apparaissent dans l'adresse avec la méthode GET.


# Utilisation du CSS

Comment place-t-on le code CSS ?

On crée un fichier externe de mise en forme à l'extension `.css `, par exemple  `mon_style.css ` qui accompagnera le fichier de contenu brut  `ma_page.html `. Pour cela dans le fichier à l'extension  `.html `, il suffira d’ajouter dans la section  `head ` de la page :

 ```html
<link rel="stylesheet" href="mon_style.css" />
 ```
 
**Remarque** : on peut aussi insérer le code CSS directement à l'intérieur de la balise ```<style> </style>``` dans la section head de la page html. Une autre technique plus ancienne mais qui reste cependant utilisable est d’insérer les informations de style dans une balise html : 

 ```<p style="color :blue ; font-size :10px ;"> Mon paragraphe en bleu de taille 10px </p> ```  
 
Il est conseillé néanmoins d’utiliser un fichier css externe pour distinguer nettement le fond de la forme ; par ailleurs, et c’est là le plus important, si le site comporte plusieurs pages, on peut affecter la même mise en forme pour toutes les pages du site en plaçant simplement le lien ```<link rel="stylesheet" href="style.css" /> ``` dans la section  `head ` de toutes les pages. Ainsi une modification dans le seul fichier css affectera immédiatement la mise en forme de toutes les pages du site.

_**Structure générale du code CSS**_

On trouve dans le code CSS :

-	des noms de balises appelés _**sélecteurs**_
-	des _**propriétés**_ CSS
-	des _**valeurs**_

Il faut respecter la structure suivante :

```css
balise1
{ 
propriete1 : valeur1 ;
propriete2 : valeur2 ;
propriete3 : valeur3 ;
}
balise2
{ 
propriete1 : valeur4 ;
propriete2 : valeur5 ;
propriete3 : valeur6 ;
}
 ```
 
**Remarque 1** : si deux balises possèdent la même mise en forme, on peut éviter la répétition de la manière suivante :

```css
balise1, balise2
{ 
propriete1 : valeur1 ;
propriete2 : valeur2 ;
propriete3 : valeur3 ;
}
 ```
 
**Remarque 2** : on peut donner une mise en forme uniquement aux balises 2 situées à l’intérieur des balises 1 de la manière suivante, cette fois-ci sans la virgule entre balise1 et balise 2

```css
balise1 balise2
{ 
propriete1 : valeur1 ;
propriete2 : valeur2 ;
propriete3 : valeur3 ;
}
 ```
 
On peut également ajouter des commentaires dans le code CSS en utilisant : ``` /* mon commentaire */ ```


**Amélioration du code CSS** : utilisation des attributs _**class**_ et _**id**_, ainsi que les balises universelles telles que p

Si l’on écrit :

```css
p
{
color : blue ;
}
 ```
 
Tous les paragraphes seront de couleur bleue.

Si on veut mettre en bleu un ou certains paragraphes en particulier uniquement, on utilise l’attribut _**class**_, il faudra procéder en deux temps :  

Dans la page html, attribuer une classe à la balise :

 ```<p class="mon_paragraphe_en_bleu">mon paragraphe à mettre en bleu</p>```   

Puis dans le css : 

```css
.mon_paragraphe_en_bleu
{
color : blue ;
}
```

Ainsi tous les paragraphes qui possèdent la classe `mon_paragraphe_en_bleu` seront de couleur bleue sur la page.

On utilise également l’attribut _**id**_ pour affecter un style à un élément unique de la page html, de plus id prend le dessus sur class.
  
Dans le html : ```<p id="monparagrapheenbleu">mon paragraphe à mettre en bleu</p>```  

Puis dans le css :

```css
#monparagrapheenbleu
{
color : blue ;
}
```

Mais le fait que class ou id soient des attributs de balise ne restreint pas pour autant leur utilisation aux balises communes telles que ```<p>```,``` <img />```….

En effet, il existe d’autres balises appelées balises universelles qui n’ont pas de signification particulière mais auxquelles nous pourrons affecter ces attributs.

-	la balise de type inline : ```<span> </span>``` : elle permet de sélectionner certains mots en particulier dans un paragraphe
-	la balise de type block : ```<div> </div>``` : elle permet de sélectionner un bloc de texte.

_**Application au formatage du texte**_

-	la taille du texte
	-	en absolue : par exemple : ```font-size : 16px``` ;
	-	en relatif : par exemple : ```font-size : small (large, medium, large)```;
-	la police du texte : par exemple : ```font-family : Verdana``` ;
-	la mise en forme : par exemple : ```font-style : italic``` ; ```font-weight : bold``` ; ```text-decoration : underline```
-	l’alignement : ```text-align : left (center,right,justify)``` ;
-	la couleur du texte : par exemple : ```color : blue``` (le nom anglais des couleurs communes) ou ```#0000FF``` en notation hexadécimale (les deux premières valeurs indiquent le niveau de rouge de 00 à FF (15×16+15=255), puis le niveau de vert et enfin le niveau de bleu ; voir ici le codage hexadécimal des couleurs (http://isnangellier.alwaysdata.net/php/colours.html) ; on peut aussi utiliser la notation ```rgb(250,25,124)```.
-	la couleur du fond : par exemple : ```background-color : black ```;

_**Mise en place de bordures**_

3 valeurs permettent de modifier l’apparence d’une bordure
-	la largeur en px
-	la couleur
-	le type de bordure : solid (un trait simple) ; dotted (pointillés) ; dashed (tirets) ; ridge (effet de relief)  
Par exemple, pour entourer les titres importants de type h1 d’une bordure noire de 4px en pointillé

```css
h1
{
border : 4px black dotted ;
}
```

On peut aussi distinguer les côtés droit, gauche, haut, bas

```css
h1
{
border-right : 4px black dotted ;
border-bottom : 2px red solid ;
}
```

On peut aussi créer une bordure arrondie :

```css
h1
{
border-radius : 10px;
}
```

_**Mise en place d’apparences dynamiques**_

On peut faire des changements d’apparence :

-	au survol : hover
-	lors du clic : active
-	lors du focus, c’est-à-dire de la sélection d’un élément : focus
-	lorsqu’un lien a été consulté : visited

Par exemple, pour décider qu’un lien non survolé soit bleu et qu’il devienne rouge au survol

```css
a
{
color :blue ;
}

a:hover 
{
color: red;
}
```

_**Organiser la page : le positionnement des blocs**_

On peut organiser la page en blocs en utilisant des balises structurantes introduites pour délimiter différentes zones qui constituent la page web :
 
-	```<header>``` : en-tête
-	```<footer>``` : pied de page
-	```<nav>``` : liens principaux de navigation
-	```<section> ```: section de page
-	```<aside>``` : informations complémentaires
-	```<article>``` : article indépendant

Ces balises structurantes n’ont d’autre utilité que d’indiquer le positionnement du contenu mais on peut tout aussi bien utiliser la balise universelle ```div```.

On dispose de propriétés, exprimées en px ou en pourcentage, de largeur ```width``` et de hauteur ```height```. 


_**Utilisation de marges**_  

Deux types de marge peuvent être utilisés :

-	marge intérieure entre la bordure (qui peut avoir une certaine épaisseur) et le début du contenu : ```padding``` en px
on peut préciser pour les quatre directions :  ```padding -top``` ; ```padding -bottom``` ; ```padding -left``` ; ```padding -right```

-	marge extérieure entre la bordure et l'extérieur : ```margin``` en px
on peut préciser pour les quatre directions :```margin-top``` ; ```margin-bottom``` ; ```margin-left``` ; ```margin-right```.

![Représentation binaire de 755 ](assets/marges.png#center)   

Pour centrer un bloc après lui avoir donné une largeur, utiliser : ```margin : auto```.  
Si le texte contenu dans le bloc dépasse ses limites, le navigateur peut ajouter des barres de défilement : ```overflow : auto```  
Le positionnement ```inline-block``` permet de transformer, grâce à la propriété ```display```, en inline-block deux éléments que l’on veut placer côte à côte, par exemple un menu de navigation et une section du centre de la page.

```css
nav
{ 
display : inline-block ;
width :150px ;
border : 1px solid black ;
}
section
{
display : inline-block ;
border : 1 px solid blue ;
}
```

La propriété ```vertical-align``` permet de modifier l’alignement vertical des éléments   

```baseline``` : aligne selon la ligne de la base de l’élément  
```top``` : aligne en haut    
```middle``` : centre verticalement   
```bottom``` : aligne en bas    
```valeur en px ou %``` : aligne à une certaine distance de la ligne de base    


Ainsi, pour aligner en haut les blocs nav et section, on écrira :

```css
nav
{ 
display : inline-block ;
vertical-align:top;
width :150px ;
border : 1px solid black ;
}
section
{
display : inline-block ;
vertical-align:top;
border : 1 px solid blue ;
}
```

Une autre méthode est le positionnement absolu qui permet de placer l’élément n’importe où sur la page :

```css
element  
{
position : absolute ;
left : 50px ;
right : 100 px ;
top : 10% :
bottom : 120px ;
}
```

Lorsque des éléments se chevauchent, la propriété z-index permet de préciser quel élément est situé au dessus de l’autre.

Le positionnement fixe permet de fixer la position du bloc même si on descend dans la page.

```css
element  
{
position : fixed ;
left : 50px ;
right : 100 px ;
}
```

Le positionnement relatif permet de décaler le bloc par rapport à sa position initiale.

```css
element
{
position : relative ;
left : 50px ;
right : 100 px ;
}
```

_**Utiliser les outils de développement du navigateur**_

Pour cela, faire un clic droit sur la page et faire l’**inspection** de l’élément ; à gauche le code html, à droite le code css. Possibilité de changer le code, d’observer directement l’effet des modifications effectuées sur la page puis de copier-coller ces modifications pour mettre à jour votre page.

--> Exemple [de page web](http://vfsilesieux.free.fr/exemple_page_web_SNT.html) à inspecter.

