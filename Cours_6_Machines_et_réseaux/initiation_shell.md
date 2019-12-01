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

**4. ![question][question] Afficher le contenu du répertoire courant à l’aide de la commande ```ls```.**

- Le répertoire contient plusieurs dossiers dont le dossier Documents.
- Placer vous dans le répertoire Documents.

**5. ![question][question] Utiliser les commandes shell de base pour créer l’arborescence ci-dessous.**

+ Son affichage a été obtenu à l'aide de la commande ```tree```.
![arbre][shell]

![verifier][verifier] **Faire vérifier votre travail par le professeur.**

## ![dossier][dossier] Seconde partie : Gérer les droits de permission.

**1. Placer vous maintenant dans le répertoire France.**

**2. Utiliser l’éditeur ```nano``` (ou pico) pour éditer le fichier paris :**

![question][question] Écrire : "Paris est la capitale de la France".

![question][question] Enregistrer le fichier ainsi édité.

![question][question] Faire une copie du fichier paris sous le nom capitale.

![question][question] Visualiser le contenu du fichier paris à l’aide de la commande ```cat```. 

![question][question] Utiliser la commande ```ls-l``` pour afficher les caractéristiques des fichiers paris, lille et capitale.

**3. Les droits d’accès**


![droit][droit]


| **La première lettre désigne le type de fichier** | **Les droits des fichiers** |
| :------------------------------------------:  | :---------------------: |
| ```-``` : fichier "classique" | ```r``` : read (droit de lecture) |
| ```d``` : répertoire (directory) | ```w``` : write (droit d'écriture) |
| ```l``` : lien symbolique (link) | ```x``` : execute (droit d'exécuter un fichier ou d'ouvrir un répertoire)|


![question][question] Donner la signification de ```-rw-rw-r--```?


**4. On souhaite modifier ces droits de manière à obtenir : **```-rw-r--r--```.

![question][question] On pourra tester par exemple l’effet de la commande ```chmod og -r paris```.

![question][question] Vérifier la modification des droits en tapant de nouveau ```ls -l```.

![question][question] Modifier de nouveau les droits de manière à obtenir ```-rw-r--r--```.

![question][question] puis de manière à obtenir ```-rw-rw-rw-```.

 
**5. Notation numérique et système octal**

| **Droit**	| **Valeur alphanumérique** | ![question][question] **Valeur octale à compléter** | **Valeur binaire** |
| :------: | :------: | :---------------: | :------: |
| aucun droit |	---	| ...| 000 |
| exécution seulement |	--x | ... | 001 |
| écriture seulement| -w- | ... |	010 |
| écriture et exécution	| -wx |	... |	011 |
| lecture seulement | r-- | ... | 100 |
| lecture et exécution | r-x | ...  | 101 |
| lecture et écriture | rw-	| ...	| 110 |
| tous les droits (lecture, écriture et exécution) | rwx | ...	| 111 | 

![verifier][verifier] **Faire vérifier votre travail par le professeur.**

En combinant 3 chiffres décimaux on peut changer le mode d’accès pour l’ensemble des propriétaires.

![question][question] On pourra tester la commande : ```chmod 777 paris```.

![question][question] puis ```chmod 000 paris```.

![question][question] Vérifier la validité de cette dernière commande en tapant de nouveau ```ls-l``` puis en entrant la commande ```cat```.

![question][question] Utiliser ensuite la commande décimale pour protéger votre fichier en mode **"parano"** avec ```-rw-------```.

![question][question] Puis en mode standard avec ```-rw-r--r--```.

**5. la gestion des droits s’applique aussi aux répertoires**

![question][question] Modifier les droits du répertoire france afin que seul le propriétaire puisse lire, modifier et exécuter le contenu de celui-ci.

**6. Challenge Python**

On donne les fonctions suivantes :

![python][python]

![question][question] Réaliser la docString et les docTest pour ces deux fonctions.

![question][question] Utiliser ces fonctions pour vérifier certaines de vos réponses données dans cette activité.

![verifier][verifier] **Faire vérifier votre travail par le professeur.**
