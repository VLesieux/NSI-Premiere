# Les iris : un exemple de l'algorithme des k plus proches voisins


## 1. Introduction

L’algorithme des k plus proches voisins appartient à la famille des **algorithmes d’apprentissage automatique** ou machine learning. L’idée d’apprentissage automatique ne date pas d’hier, puisque le terme de machine learning a été utilisé pour la première fois par l’informaticien américain Arthur Samuel en 1959. Les algorithmes d’apprentissage automatique ont connu un fort regain d’intérêt au début des années 2000 notamment grâce à la quantité de données disponibles sur internet. L’algorithme des k plus proches voisins est un algorithme d’apprentissage supervisé, il est nécessaire d’avoir des données labelli-sées. À partir d’un ensemble E de données labellisées, il sera possible de classer (déterminer le label) d’une nouvelle donnée (pour une donnée n’appartenant pas à E). À noter qu’il est aussi possible d’utiliser l’algorithme des k plus proches voisins à des fins de régression (on cherche dans ce cas à déterminer une valeur à la place d’une classe), mais cet aspect des choses ne sera pas abordé ici. L’algorithme des k plus proches voisins est une bonne introduction aux principes des algorithmes d’apprentissage automatique, il est en effet relativement simple à appréhender. Cette première approche des algorithmes d’apprentissage peut aussi amener les élèves à réfléchir sur l’utilisation de leurs données personnelles : de nombreuses sociétés utilisent les données concernant leurs utilisateurs afin de ”nourrir” des algorithmes de machine learning qui permettront à ces sociétés d’en savoir tou-jours plus sur nous et ainsi de mieux cerné nos ”besoins” en termes de consommation.

## 2. Principe de l'algorithme

L’algorithme de k plus proches voisins ne nécessite pas de phase d’apprentissage à proprement parler, il faut juste stocker le jeu de données d’apprentissage. Soit un ensemble E contenant n données labellisées : E={(yi, xi)} avec i compris entre 1 et n, où yi correspond à la classe (le label) de la donnée i et où le vecteur xi de dimension p (xi=(x1i, x2i, ..., xpi)) représente les variables prédictrices de la donnée i. Soit une donnée u qui n’appartient pas à E et qui ne possède pas de label (u est uniquement caractérisée par un vecteur x de dimension p). Soit d une fonction qui renvoie la distance entre la donnée i et une donnée quelconque appartenant à E. Soit un entier k inférieur ou égal à n. Voici le principe de l’algorithme de k plus proches voisins :  
▷ On calcule les distances entre la donnée u et chaque donnée appartenant à E à l’aide de la fonction d  
▷ On retient les k données du jeu de données E les plus proches de u  
▷ On attribue à u la classe qui est la plus fréquente parmi les k données les plus proches. 

## 3. Étude d'un exemple

### 3.1. Les données

Nous avons choisi ici de nous baser sur le jeu de données ”iris de Fisher” dont les trois espèces sont représentées ci-dessous :

*Iris_virginica*   
![Iris_virginica](assets/Iris_virginica.jpg)  
*Iris_versicolor*  
![](assets/Iris_versicolor_3.jpg)  
*Iris_setosa*   
![](assets/Iris_setosa.jpg)

Ce jeu de données est composé de 50 entrées, pour chaque entrée nous avons :   

▷ la longueur des sépales (en cm)  
▷ la largeur des sépales (en cm)  
▷ la longueur des pétales (en cm)  
▷ la largeur des pétales (en cm)  
▷ l’espèce d’iris : Iris setosa, Iris virginica ou Iris versicolor (label)

Dans un souci de simplification, nous avons choisi de travailler uniquement sur la longueur des pétales.
Par ailleurs, il est nécessaire d’encoder les espèces avec des chiffres : 0 pour Iris setosa, 1 pour Iris virginica et 2 pour Iris versicolor (ce processus d’encodage des données textuelles est relativement classique en apprentissage automatique).