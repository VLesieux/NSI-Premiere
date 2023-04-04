[shell]: images/arbre.png
[logo shell]: images/terminal-longshadow.png
[machine virtuelle]: images/virtuelleMachine.png
[pingus]: images/pingus.png
[verifier]: images/verifier.png
[qcm]: images/qcm.png
[dossier]: images/dossier.png
[droit]: images/droit.png
[question]: images/question.png
[python]: images/python.png

[lien wiki]: https://fr.wikipedia.org/wiki/Commandes_Unix#Fichiers_et_répertoires

# ![pingus][pingus] **Initiation au Shell et gestion des droits de permission** 
-----


### L’objectif de la séance fait ici référence au programme de première.

- **Architectures matérielles et système d'exploitation**
	+ Utiliser les commandes de base en ligne de commande.
	+ Gérer les droits et permissions.


- **Lien utile** : [La page wikipedia des commandes Unix][lien wiki].


## ![dossier][dossier] Première partie : Création de dossiers et fichiers.

**1. Rappels des commades utiles :**

- ```mkdir "nom du dossier" ``` : Création d'un dossier.
- ```touch "nom du fichier" ``` : Création d'un fichier.

**2. Démarrer la machine virtuelle** ![virtuelle][machine virtuelle]

**3. Lancer le terminale** ![logo][logo shell]

**4. Afficher le contenu du répertoire courant à l’aide de la commande ```ls```.**

- Le répertoire contient plusieurs dossiers parmi lesquels vous créerez le dossier Documents.
- Placer vous dans le répertoire Documents.

**5. Utiliser les commandes shell de base pour créer l’arborescence ci-dessous.**

+ Son affichage a été obtenu à l'aide de la commande ```tree```.
![arbre][shell]

![verifier][verifier] **Faire vérifier votre travail par le professeur.**

## ![dossier][dossier] Seconde partie : Gérer les droits de permission.

**1. Placer vous maintenant dans le répertoire France.**

**2. Utiliser l’éditeur ```nano``` (ou pico) pour éditer le fichier paris :**

a. Écrire : "Paris est la capitale de la France".

b. Enregistrer le fichier ainsi édité.

c. Faire une copie du fichier paris sous le nom capitale.

d. Visualiser le contenu du fichier paris à l’aide de la commande ```cat```. 

e. Utiliser la commande ```ls -l``` pour afficher les caractéristiques des fichiers paris, lille et capitale.

**3. Les droits d’accès**


![droit][droit]


| **La première lettre désigne le type de fichier** | **Les droits des fichiers** |
| :------------------------------------------:  | :---------------------: |
| ```-``` : fichier "classique" | ```r``` : read (droit de lecture) |
| ```d``` : répertoire (directory) | ```w``` : write (droit d'écriture) |
| ```l``` : lien symbolique (link) | ```x``` : execute (droit d'exécuter un fichier ou d'ouvrir un répertoire)|


Donner la signification de ```-rw-rw-r--```?


**4. Modification des droits d'accès**

On souhaite modifier ces droits de manière à obtenir : ```-rw-r--r--```

Pour cela, on pourra commencer par tester l’effet de la commande ```chmod og-r paris```.

Vérifier la modification des droits en tapant de nouveau ```ls -l```.

À vous de modifier de nouveau les droits de manière à obtenir ```-rw-r--r--```.

![verifier][verifier] **Faire vérifier votre travail par le professeur.**

 
**5. Notation numérique et système octal**

| Droit	| Valeur alphanumérique | Valeur octale <br>**<u>à compléter</u>** | Valeur binaire |
| :------: | :------: | :---------------: | :------: |
| aucun droit |	---	| ...| 000 |
| exécution seulement |	--x | ... | 001 |
| écriture seulement| -w- | ... |	010 |
| écriture et exécution	| -wx |	... |	011 |
| lecture seulement | r-- | ... | 100 |
| lecture et exécution | r-x | ...  | 101 |
| lecture et écriture | rw-	| ...	| 110 |
| tous les droits (lecture, écriture et exécution) | rwx | ...	| 111 | 

La numération octale peut être construite à partir de la numération en groupant les chiffres consécutifs en triplets (à partir de la droite). Par exemple, la représentation binaire du nombre décimal 74 est 1001010, que l'on groupe en (00)1 001 010 ; ainsi, la représentation octale est 1 pour 1, 1 pour le groupe 001, et 2 pour le groupe 010, ce qui donne 112. 


En combinant ainsi 3 chiffres décimaux on peut changer le mode d’accès pour l’ensemble des propriétaires.

On pourra tester la commande : ```chmod 777 paris```  puis ```chmod 000 paris```.

Vérifier la validité de cette dernière commande en tapant de nouveau ```ls -l```  puis en entrant la commande ```cat```.

Utiliser ensuite la commande décimale pour protéger votre fichier en mode "parano" avec ```-rw-------``` puis en mode standard avec ```-rw-r--r--```.

Remarque: la gestion des droits s’applique aussi aux répertoires. Modifier les droits du répertoire `france` afin que seul le propriétaire puisse lire, modifier et exécuter le contenu de celui-ci.

**6. Challenge Python** : compléter le code

```Python
def encode(chaine):
    """
    encode la chaine à partir du deuxième caractère
    param: chaine : str
    return : str
    >>> encode("-rw-rw-rw-")
    '110110110'
    """
	pass

def conversion_binaire_decimal(chaine):
    """
    renvoie la valeur décimale d'un code binaire
    param : chaine : str
    return : int
    >>> conversion_binaire_decimal("0100")
    4
    """
	pass

def donne_la_valeur_octale(chaine):
    """
    Renvoie la valeur octale d'une chaine
    >>> donne_la_valeur_octale("-rw-rw-rw-")
    ('fichier', '666')
    >>> donne_la_valeur_octale("drwxrwxrwx")
    ('repertoire', '777')
    """   
	pass


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
```



![verifier][verifier] **Faire vérifier votre travail par le professeur.**
