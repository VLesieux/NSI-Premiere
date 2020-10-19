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

Écrire un programme qui lit le fichier CSV et en extrait une table de données sous la forme d'un tableau de dictionnaires.

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


1) Reprendre l'exercice précédent et réaliser une fonction `verifie_quantites` qui analyse le bon de commande et renvoie True si pour chaque produit commandé la quantité est bien positive.

2) Réaliser une fonction `nombre_produit` qui renvoie le nombre total de produits demandés dans un bon de commande donné en argument.

3) Écrire une fonction `prix` qui renvoie le prix total d'un bon de commande.


### Exercice 3

Écrire une fonction `trie` qui renvoie un dictionnaire dont les clés sont les désignations des produits et les valeurs leurs prix, classés par ordre de prix décroissant.

```python
>>> tri(table)
{'cahier petites carreaux': 3.5, 'lot crayons HB': 2.3, 'stylo rouge': 1.5}
```

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

Réaliser la fusion des deux tables pour obtenir la nouvelle table.

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
