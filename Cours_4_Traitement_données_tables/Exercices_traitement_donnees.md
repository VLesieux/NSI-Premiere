## Exercices traitement de données en table

### Exercice 1

Réaliser un fichier au format CSV appelé `bon_commande.csv` décrivant le bon de commande ci-dessous, dans lequel les colonnes référence et désignation contiennent des chaînes de caractères, la colonne prix des nombres décimaux et la colonne quantité des nombres entiers.

<table>
<tr>
<td>reference</td>
<td>designation</td>
<td>prix</td>
<td>quantite</td>
</tr>
<tr>
<td>18635</td>
<td>lot crayons HB</td>
<td>2,30</td>
<td>1</td>
</tr>
<tr>
<td>15223</td>
<td>stylo rouge</td>
<td>1,50</td>
<td>3</td>
</tr>
<tr>
<td>20112</td>
<td>cahier petits carreaux</td>
<td>3,50</td>
<td>2</td>
</tr>
</table>

Écrire un programme qui lit le fichier CSV et en extrait une table de données sous la forme d'une liste appelée `table_commande1` puis sous la forme d'un dictionnaire.
Ce dernier sera obtenu par compréhension ; les clés sont les références et les valeurs associées sont les listes [designation,prix,quantite].

```python
>>> %Run exercice_traitement_donnees_table.py
{'18635': ['lot crayons HB', 2.3, 1], '15223': ['stylo rouge', 1.5, 3], '20112': ['cahier petites carreaux', 3.5, 2]}
```

Remarque : Pour transformer `,` en `.` utiliser : 

```python
>>> "2,3".replace(",",".")
'2.3'
```

### Exercice 2

On donne le code pour vérifier les tests des docstrings.

```python
if __name__ == '__main__':
    import doctest
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS, verbose=True)
```

1) Reprendre l'exercice précédent et réaliser une fonction `verifie_quantites(table)` qui analyse le bon de commande et renvoie True si pour chaque produit commandé la quantité est bien positive.

```python
def verifie_quantites(table):
    """
    Renvoie True si les quantités sont positives, False sinon
    param : table : list
    return : bool
    >>> verifie_quantites(table_commande1)
    True
    """
```

2) Réaliser une fonction `nombre_produit(table)` qui renvoie le nombre total de produits demandés dans un bon de commande donné en argument.

```python
def nombre_produit(table):
    """
    Renvoie le nombre de produit commandé
    param : table : list
    return : int
    >>> nombre_produit(table_commande1)
    6
    """
```

3) Écrire une fonction `prix(table)` qui renvoie le prix total d'un bon de commande.

```python
def prix(table):
    """
    Renvoie le montant de la commande
    param : table : list
    return : int
    >>> prix(table_commande1)
    13.8
    """
```

### Exercice 3

Écrire une fonction `tri(table)` qui renvoie un dictionnaire dont les clés sont les désignations des produits et les valeurs leurs prix, classés par ordre de prix décroissant.

```python
def tri(table):
    """
    Renvoie un dictionnaire où les valeurs sont rangées dans l'ordre décroissant
    param : table : list
    return : dict
    >>> tri(table_commande1)
    {'cahier petites carreaux': 3.5, 'lot crayons HB': 2.3, 'stylo rouge': 1.5}
    """
```

Indications :

- créer d'abord une liste triée `table_tri` en utilisant la fonction anonyme `lambda`
- créer le dictionnaire par compréhension

### Exercice 4

Réaliser un fichier au format CSV appelé `marques.csv` décrivant les marques des différents matériels

<table>
<tr>
<td>designation</td>
<td>marques</td>
</tr>
<tr>
<td>lot crayons HB</td>
<td>BUC</td>
</tr>
<tr>
<td>stylo rouge</td>
<td>PALOT</td>
</tr>
<tr>
<td>cahier petits carreaux</td>
<td>CLOSEFONTAINE</td>
</tr>
</table>

On réalise ainsi une nouvelle table de données appelée `table_commande2`.

Écrire la fonction `fusion(table1,table2)` pour réaliser maintenant la fusion des deux tables afin d'obtenir la nouvelle table représentée ci-dessous.

<table>
<tr>
<td>reference</td>
<td>designation</td>
<td>prix</td>
<td>quantite</td>
<td>marques</td>
</tr>
<tr>
<td>18635</td>
<td>lot crayons HB</td>
<td>2,30</td>
<td>1</td>
<td>BUC</td>
</tr>
<tr>
<td>15223</td>
<td>stylo rouge</td>
<td>1,50</td>
<td>3</td>
<td>PALOT</td>
</tr>
<tr>
<td>20112</td>
<td>cahier petits carreaux</td>
<td>3,50</td>
<td>2</td>
<td>CLOSEFONTAINE</td>
</tr>
</table>

```python
def fusion(table1,table2):
    """
    Renvoie la fusion des tables en réalisant leur jointure
    param : table1 : list
    param : table2 : list
    return : list
    >>> fusion(table_commande1,table_commande2)
    [['18635', 'lot crayons HB', 2.3, 1, 'BUC'], ['15223', 'stylo rouge', 1.5, 3, 'PALOT'], ['20112', 'cahier petits carreaux', 3.5, 2, 'CLOSEFONTAINE']]
    """
```

### Exercice 5

1. Dans un premier temps réaliser une table appelée `table_des_donnees` obtenue grâce à l'extraction des données du fichier csv appelé `les_salles_de_cinemas_en_ile-de-france.csv`  présent dans le dossier `Assets`.

Dans la console, noter les résultats affichés :

a) print(len(table_des_donnees)) 

b) print(table_des_donnees[0]) 

c) print(len(table_des_donnees[0])) 

d) print(table_des_donnees[0].index('dep')) 

e) print(table_des_donnees[0].index('entrees_2020'))  

f) print(table_des_donnees[0].index('geo')) 

Donnez la signification de ces résultats.   

2. On se demande combien il y a de cinémas dans le département 95.   

Compléter la fonction `denombre` pour que sa docstring soit vérifiée.  
On dénombre en effet 30 salles de cinéma dans le département 93.

```Python

def denombre(departement,tableau):
    """
    Renvoie le nombre de salles de cinéma dans departement après le parcours de tableau 
    param : departement : str
    param : tableau : list
    return : int
    >>> denombre("93",table_des_donnees)
    30
    """
        
if __name__ == '__main__':
    import doctest
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS, verbose=True)
```

3. Quel est le nom du cinéma d'Île de France (tous départements confondus) qui a fait le plus d'entrée en 2020 ?

**Indication** : utiliser `sorted` après avoir réalisé une fonction de tri appelée `tri_selon_entree_2020`.

4. Quel est le nom du cinéma du département 95 qui a fait le plus d'entrée en 2020 ?

**Indications** : réaliser une fonction de filtrage `filtre_selon_code(code,tableau)`.

5. On se propose de répondre à la question suivante : combien y-a-t-il de cinéma à moins de 10 km de Paris ?    

Pour cela, on importe un programme appelé `calcul_distance_latitude_longitude.py` en ajoutant dans notre code 

```Python
import calcul_distance_latitude_longitude as distance
```

Ce programme se trouve également dans le dossier Assets. Il possède une fonction `a_paris(geo)` qui renvoie la distance en *mètre* par rapport à Paris d'un point dont les coordonnées géographiques sont données sous forme de tuple (latitude,longitude) ; pour l'appeler et l'utiliser dans notre programme, il suffit d'écrire la fonction `distance.a_paris` par exemple 

```Python
>>> distance.a_paris('48.873073,2.298394')
4346.833687547045`
```

**Indications** : réaliser une fonction de filtrage `filtre_selon_distance_a_Paris(tableau,rayon_a_Paris)`.