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