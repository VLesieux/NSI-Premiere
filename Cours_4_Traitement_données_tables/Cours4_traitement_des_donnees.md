![Programme officiel ](assets/bo2.png)

## Exemple

### Extraction des données

On a créé un fichier Excel [à télécharger](assets/Tableau_capitales.xlsx)		

![](assets/Image_Excel.png)	

On l'a enregistré également avec l'extension csv pour avoir un fichier au format texte [à télécharger](assets/Tableau_capitales.csv)

![](assets/Image_csv.png)

L'objectif est d'extraire les données et de les enregistrer dans une liste composée de p-uplets.    
Avec ce premier code, on obtient une liste de listes.

```python
f=open("Tableau_capitales.csv","r")#la fonction open renvoie une valeur affectée à la variable f
table=[ligne.rstrip().split(';') for ligne in f]#construction d'une liste par compréhension
#str.rstrip() supprime les espaces
#str.split(';') renvoie une liste en utilisant ';' comme séparateur
f.close()
print(table)
>>>
[['Nom', 'Continent', 'Superficie', 'Population', 'Capitale'], ['Afghanistan', 'Asie', '652864.0', '34124800', 'Kaboul'], ['Angola', 'Afrique', '1246700.0', '30355900', 'Luanda'], ['Albanie', 'Europe', '28748.0', '2048000', 'Tirana'], ['Andorre', 'Europe', '468.0', '85600', 'Andorre-la-Vieille'], ['Argentine', 'Amerique du Sud', '2791800.0', '44293300', 'Buenos Aires'], ['Armenie', 'Asie', '29800.0', '3045200', 'Erevan'], ['Australie', 'Oceanie', '7692060.0', '23470100', 'Canberra'], ['Autriche', 'Europe', '83871.0', '8754400', 'Vienne']]
```

Avec ce code, on obtient un liste de tuples

```python
f=open("Tableau_capitales.csv","r")
table=[tuple(ligne.rstrip().split(';')) for ligne in f]
f.close()
print(table)
>>>
[('Nom', 'Continent', 'Superficie', 'Population', 'Capitale'), ('Afghanistan', 'Asie', '652864.0', '34124800', 'Kaboul'), ('Angola', 'Afrique', '1246700.0', '30355900', 'Luanda'), ('Albanie', 'Europe', '28748.0', '2048000', 'Tirana'), ('Andorre', 'Europe', '468.0', '85600', 'Andorre-la-Vieille'), ('Argentine', 'Amerique du Sud', '2791800.0', '44293300', 'Buenos Aires'), ('Armenie', 'Asie', '29800.0', '3045200', 'Erevan'), ('Australie', 'Oceanie', '7692060.0', '23470100', 'Canberra'), ('Autriche', 'Europe', '83871.0', '8754400', 'Vienne')]
```
Il s'agit maintenant de distinguer la première ligne qui contient la liste des champs des autres lignes. De plus, il s'agit de convertir les données sur la superficie de type string en float et les données sur la population de type string en int.

```python
f=open("Tableau_capitales.csv","r")
champs=f.readline().rstrip().split(";")#lecture et transformation en liste de la première ligne
#['Nom', 'Continent', 'Superficie', 'Population', 'Capitale']
lignes=f.readlines()
table=[]
for ligne in lignes:
    liste=ligne.rstrip().split(';')
    liste[2]=float(liste[2])
    liste[3]=int(liste[3])
    table.append(tuple(liste))
f.close()
print(table)
>>>
[('Afghanistan', 'Asie', 652864.0, 34124800, 'Kaboul'), ('Angola', 'Afrique', 1246700.0, 30355900, 'Luanda'), ('Albanie', 'Europe', 28748.0, 2048000, 'Tirana'), ('Andorre', 'Europe', 468.0, 85600, 'Andorre-la-Vieille'), ('Argentine', 'Amerique du Sud', 2791800.0, 44293300, 'Buenos Aires'), ('Armenie', 'Asie', 29800.0, 3045200, 'Erevan'), ('Australie', 'Oceanie', 7692060.0, 23470100, 'Canberra'), ('Autriche', 'Europe', 83871.0, 8754400, 'Vienne')]
```
### Recherche dans une table

Recherchons dans notre tableau les pays d'Europe contenant plus de 5 millions d'habitants.   
On commence par créer une liste contenant les indices des champs Nom, Continent, Superficie, Population.  

```python
indices=[champs.index('Nom'),champs.index('Continent'),champs.index('Population')]         
#[0, 1, 3]
rep=[]
for ligne in table:
    if ligne[indices[2]]>5000000 and ligne[indices[1]]=="Europe":
        rep.append(ligne[indices[0]])
print(rep)
>>>
['Autriche']
```
### Élimination des doublons

Cherchons à éliminer les doublons qui auraient par exemple tous les deux le même nom de pays.   

Premier cas : supposons que la table est déjà triée suivant les noms. 
Dans ce cas, il suffit de comparer les lignes de la table avec la dernière ligne enregistrée dans la nouvelle table.

```python
    rep=[table[0]]
    for ligne in table:
        if ligne[indice] != rep[-1][indice]:
            rep.append(ligne)
    return rep
```

Deuxième cas : supposons que la table n'est pas déjà triée suivant les noms.     
Pour chaque nouvelle ligne ajoutée, il faut vérifier son absence dans la nouvelle table.

```python
def sans_doublons(table,indice):
    rep=[table[0]]
    for i in range(1,len(table)):
        test=True
        ligne=table[i]
        valeur=ligne[indice]
        for j in range(len(rep)):
            if rep[j][indice]==valeur:
                test=False
                break
        if test:
            rep.append(ligne)
    return rep
```

On peut s'interroger sur le coût d'un tel algorithme et se demander s'il ne vaudrait pas mieux trier la table dans un premier temps pour lui appliquer ensuite la première version qui est plus simple.

### Tri d'une table

On se propose de trier la table par ordre de population décroissante.    

On peut faire un tri sur des objets complexes en utilisant les indices des objets en tant que clef.
Par exemple :

```python
>>> student_tuples = [('john', 'A', 15),('jane', 'B', 12),('dave', 'B', 10)]
>>> sorted(student_tuples, key=lambda student: student[2])
[('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]
```
```python
indices=[champs.index('Nom'),champs.index('Population')]         
tri=sorted(table,key=lambda ligne:ligne[indices[1]], reverse=True)
print(tri)
>>>
[('Argentine', 'Amerique du Sud', 2791800.0, 44293300, 'Buenos Aires'), ('Afghanistan', 'Asie', 652864.0, 34124800, 'Kaboul'), ('Angola', 'Afrique', 1246700.0, 30355900, 'Luanda'), ('Australie', 'Oceanie', 7692060.0, 23470100, 'Canberra'), ('Autriche', 'Europe', 83871.0, 8754400, 'Vienne'), ('Armenie', 'Asie', 29800.0, 3045200, 'Erevan'), ('Albanie', 'Europe', 28748.0, 2048000, 'Tirana'), ('Andorre', 'Europe', 468.0, 85600, 'Andorre-la-Vieille')]
```
### Fusion de tables

Deux situations : soit l'ajout d'enregistrements en faisant la **concaténation de tables**, soit l'ajout de champs, on parle alors de **jointure** entre tables.

1. Concaténation de tables

On suppose que les tables vérifient les conditions : mêmes champs dans le même ordre avec les mêmes domaines de valeurs.
```python
def ajout(table1,table2,indice):
    rep=table1+table2
    return sans_doublon(rep,indice)
>>> t1=[['France',67,643]]
>>> t2=[['Espagne',127,242]]
>>> ajout(t1,t2,0)
[['France', 67, 643], ['Espagne', 127, 242]]
```

2. Jointure entre tables

Supposons que nous disposions d'une deuxième table avec le nom de pays et d'autres champs comme le PIB, la langue officielle, etc... Nous allons construire une nouvelle table contenant toutes les informations des deux tables sans que le nom de pays figure deux fois. Si un pays est présent dans une table et pas dans l'autre, on donne la valeur *None* aux différents champs vides. On suppose que les deux tables sont sans doublon.
Les paramètres i1 et i2 sont les indices du champ 'Nom' dans chacune des deux tables.

```python
from copy import deepcopy
def fusion(table1,i1,table2,i2):
    rep=deepcopy(table1)#on fait une copie profonde de table1
    for ligne1 in rep:
        for ligne2 in table2:
            if ligne1[i1]==ligne2[i2]:
                for i in range(len(ligne2)):#parcours des champs de table2
                    if i !=i2:
                        ligne1.append(ligne2[i])
    return rep
>>> t1=[['France',67,643],['Espagne',127,242]]
>>> t2=[['français','France'],['espagnol','Espagne']]
>>> fusion(t1,0,t2,1)
[['France', 67, 643, 'français'], ['Espagne', 127, 242, 'espagnol']]
```

On construit également une nouvelle liste de champs.

```python
champs=deepcopy(champs1)
for i in range(len(champs2)):
    if i!=i2:#i2 est l'indice du champ 'Nom' dans champs2
        champs.append(champs2[i])
```
