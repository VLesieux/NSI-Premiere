# Classification sur les Pokemon

Table des matières

1.  [Matériel fourni](#matériel-fourni)
    1.  [Fichiers csv](#fichiers-csv)
    2.  [Le module `pokemon.py`](#le-module-pokemonpy)
    3.  [Le module `knn_pokemon`](#le-module-knn_pokemon)
2.  [Travail à réaliser](#travail-à-réaliser)
3.  [Pour aller plus loin](#pour-aller-plus-loin)

------------------------------

Les pokemons sont des animaux imaginaires inventés par Nintendo. Ils possèdent tous
des caractéristiques différentes :

-   Un nom (`name`)
-   Un nombre de points d'attaque (`attack`)
-   Un nombre de pas pour le faire éclore (`base_egg_steps`)
-   Un type principal (`type1`)
-   Un éventuel type secondaire (`type2`)
-   Un nombre de points de vie (`hp`)
-   Un nombre de points de défense (`defense`)
-   Un nombre de points d'attaque spéciale (`sp_attack` )
-   Un nombre de points de défense spéciale (`sp_defense` )
-   Un nombre caractérisant sa vitesse (`speed`)
-   Un entier indiquant la génération du pokemon (`generation`)
-   Un booléen indiquant si le pokemon est légendaire ou non (`is_legendary`)

Ces données proviennent du jeu Pokemon Go. Les pokemons sont consignés dans des fichiers `csv`. 
Ces fichiers contiennent les données sous forme de table :


| "name"       | "attack" | "base_egg_steps" | "base_happiness" | "capture_rate" | "classfication"      | "defense" | "experience_growth" | "height_m" | "hp" | "pokedex_number" | "sp_attack" | "sp_defense" | "speed" | "type1"    | "type2"  | "weight_kg" | "generation" | "is_legendary" |
|--------------|----------|------------------|------------------|----------------|----------------------|-----------|---------------------|------------|------|------------------|-------------|--------------|---------|------------|----------|-------------|--------------|----------------|
| "Magmar"     | 95       | 6400             | 70               | 45             | "Spitfire Pokémon"   | 57        | 1000000             | "1.3"      | 65   | 126              | 100         | 85           | 93      | "fire"     |          | "44.5"      | 1            | 0              |
| "Pinsir"     | 155      | 6400             | 70               | 45             | "Stagbeetle Pokémon" | 120       | 1250000             | "1.5"      | 65   | 127              | 65          | 90           | 105     | "bug"      |          | "55.0"      | 1            | 0              |
| "Tauros"     | 100      | 5120             | 70               | 45             | "Wild Bull Pokémon"  | 95        | 1250000             | "1.4"      | 75   | 128              | 40          | 70           | 110     | "normal"   |          | "88.4"      | 1            | 0              |
| "Magikarp"   | 10       | 1280             | 70               | 255            | "Fish Pokémon"       | 55        | 1250000             | "0.9"      | 20   | 129              | 15          | 20           | 80      | "water"    |          | "10.0"      | 1            | 0              |
| "Gyarados"   | 155      | 1280             | 70               | 45             | "Atrocious Pokémon"  | 109       | 1250000             | "6.5"      | 95   | 130              | 70          | 130          | 81      | "water"    | "flying" | "235.0"     | 1            | 0              |
| "Lapras"     | 85       | 10240            | 70               | 45             | "Transport Pokémon"  | 80        | 1250000             | "2.5"      | 130  | 131              | 85          | 95           | 60      | "water"    | "ice"    | "220.0"     | 1            | 0              |
| "Ditto"      | 48       | 5120             | 70               | 35             | "Transform Pokémon"  | 48        | 1000000             | "0.3"      | 48   | 132              | 48          | 48           | 48      | "normal"   |          | "4.0"       | 1            | 0              |
| "Eevee"      | 55       | 8960             | 70               | 45             | "Evolution Pokémon"  | 50        | 1000000             | "0.3"      | 55   | 133              | 45          | 65           | 55      | "normal"   |          | "6.5"       | 1            | 0              |
| "Vaporeon"   | 65       | 8960             | 70               | 45             | "Bubble Jet Pokémon" | 60        | 1000000             | "1.0"      | 130  | 134              | 110         | 95           | 65      | "water"    |          | "29.0"      | 1            | 0              |
| "Jolteon"    | 65       | 8960             | 70               | 45             | "Lightning Pokémon"  | 60        | 1000000             | "0.8"      | 65   | 135              | 110         | 95           | 130     | "electric" |          | "24.5"      | 1            | 0              |
| "Flareon"    | 130      | 8960             | 70               | 45             | "Flame Pokémon"      | 60        | 1000000             | "0.9"      | 65   | 136              | 95          | 110          | 65      | "fire"     |          | "25.0"      | 1            | 0              |
| "Porygon"    | 60       | 5120             | 70               | 45             | "Virtual Pokémon"    | 70        | 1000000             | "0.8"      | 65   | 137              | 85          | 75           | 40      | "normal"   |          | "36.5"      | 1            | 0              |
| "Omanyte"    | 40       | 7680             | 70               | 45             | "Spiral Pokémon"     | 100       | 1000000             | "0.4"      | 35   | 138              | 90          | 55           | 35      | "rock"     | "water"  | "7.5"       | 1            | 0              |
| "Omastar"    | 60       | 7680             | 70               | 45             | "Spiral Pokémon"     | 125       | 1000000             | "1.0"      | 70   | 139              | 115         | 70           | 55      | "rock"     | "water"  | "35.0"      | 1            | 0              |
| "Kabuto"     | 80       | 7680             | 70               | 45             | "Shellfish Pokémon"  | 90        | 1000000             | "0.5"      | 30   | 140              | 55          | 45           | 55      | "rock"     | "water"  | "11.5"      | 1            | 0              |
| "Kabutops"   | 115      | 7680             | 70               | 45             | "Shellfish Pokémon"  | 105       | 1000000             | "1.3"      | 60   | 141              | 65          | 70           | 80      | "rock"     | "water"  | "40.5"      | 1            | 0              |
| "Aerodactyl" | 135      | 8960             | 70               | 45             | "Fossil Pokémon"     | 85        | 1250000             | "1.8"      | 80   | 142              | 70          | 95           | 150     | "rock"     | "flying" | "59.0"      | 1            | 0              |
| "Snorlax"    | 110      | 10240            | 70               | 25             | "Sleeping Pokémon"   | 65        | 1250000             | "2.1"      | 160  | 143              | 65          | 110          | 30      | "normal"   |          | "460.0"     | 1            | 0              |
| "Articuno"   | 85       | 20480            | 35               | 3              | "Freeze Pokémon"     | 100       | 1250000             | "1.7"      | 90   | 144              | 95          | 125          | 85      | "ice"      | "flying" | "55.4"      | 1            | 1              |
| "Zapdos"     | 90       | 20480            | 35               | 3              | "Electric Pokémon"   | 85        | 1250000             | "1.6"      | 90   | 145              | 125         | 90           | 100     | "electric" | "flying" | "52.6"      | 1            | 1              |



Dans ce TP, on cherche à répondre à cette question :

Étant données les caractéristiques d'un pokemon dont on ne sait s'il est légendaire ou non, 
peut-on prédire si ce pokemon est légendaire ou non ?


# Matériel fourni

## Fichiers csv

Cinq jeux de données sont fournis :

-   le fichier [pokemon_train.csv](pokemon_train.csv) contient les pokemons sur lesquels va se baser l'apprentissage.
-   le fichier [pokemon_test.csv](pokemon_test.csv) contient les pokemons grâce auxquels nous allons tester la qualité de l'apprentissage.
-   le fichier [pokemon_small.csv](pokemon_small.csv) contient les caractéristiques de 20 pokemons, utilisés pour les doctests.
-   le fichier [pokemon_suspect1.csv](pokemon_suspect1.csv) contient les caractéristiques de certains pokemons.
-   le fichier [pokemon_suspect2.csv](pokemon_suspect2.csv) contient les caractéristiques de certains pokemons.


## Le module `pokemon.py`

Le fichier [`pokemon_squel.py`](pokemon_squel.py) contient :

-   la définition du type  `Pokemon` ,
-   la fonction `read_pokemon_csv` permettant de lire le fichier de données.
-   la fonction `split_pokmeons` permettant de séparer l'ensemble des données en deux sous-ensembles.
-   la fonction `min_max_values` permettant de calculer les valeurs minimales et maximale d'un attribut numérique d'une liste 
    de pokemons.
-   les fonctions  `pokemon_euclidian_distance` (à compléter) et `pokemon_manhattan_distance` permettant de calculer
    la distance entre deux pokemons. Pour des questions de normalisation, ces méthodes prennent également en paramètre un dictionnaire
    associant à chaque attribut numérique le couple (mini, maxi) des valeurs minimales et maximale de l'attribut.


## Le module `knn_pokemon`

Le fichier [`knn_pokemon_squel.py`](knn_pokemon_squel.py) contient les
en-têtes des fonctions nécessaires à l'implémentation de l'algorithme
des $`k`$ plus proches voisins (`knn`).


# Travail à réaliser

-   Renommer le fichier `pokemon_squel.py` fourni en `pokemon.py`, puis compléter la fonction de 
    distance `pokemon_euclidian_distance`. Les attributs utilisés pour calculer la distance sont
    fournis dans la variable `POKE_PROP_USED_FOR_DISTANCE`. 
-   Renommer le fichier `knn_pokemon_squel.py` fourni en `knn_pokemon.py`, puis compléter les fonctions :
-   `nearest_neighbors` : renvoie la liste des $`k`$ plus proches pokemons.   
	Vous pourrez par exemple construire la liste des couples $(distance, voisin)$, puis la trier selon la première clé.
-   `knn` : effectue la prédiction de l'attribut en déterminant l'attribut majoritaire dans le voisinage.
-   Utiliser les fonctions précédentes pour compléter le tableau suivant :
    
| Fichier                | Meilleur $`k`$ pour la distance euclidienne | Meilleur $`k`$ pour la distance de Manhattan |
|------------------------|---------------------------------------------|----------------------------------------------|
| `pokemon_test.csv`     |                                             |                                              |
| `pokemon_suspect1.csv` |                                             |                                              |
| `pokemon_suspect2.csv` |                                             |                                              |
    
**Méthodologie :** 
    
On charge les quatre jeux de données :

```python
train = read_pokemon_csv('pokemon_train.csv')
test = read_pokemon_csv('pokemon_test.csv')
suspect1 = read_pokemon_csv('pokemon_suspect1.csv')
suspect2 = read_pokemon_csv('pokemon_suspect2.csv')
````
	
- Première ligne du tableau : utiliser la fonction `knn_data` avec `train` et `test` pour estimer les meilleurs $`k`$. : 

    ```python
    [ knn_data(test, train, k , ...) for k in range(5, 20) ]
	```
	
- Deuxième ligne du tableau : 
  - Utiliser la fonction `knn_data` avec `suspect1` et `test`.
  - Que constate-t-on ? Pourquoi ?
- Troisième ligne du tableau :
  - Utiliser la fonction `knn_data` avec `suspect2` et `test`.
  - Que constate-t-on ? Pourquoi ?

	(remarque : c'est moins flagrant ici, la méthode continue de bien classer les pokemons. Il faudrait modifier les attributs utilisés dans la fonction distance pour constater une dégradation)



# Pour aller plus loin

-   Ajouter d'autres attributs dans le calcul de la distance. Constatez que cela peut dégrader le 
    résultat.
-   Déterminer les pokemons mal classés, découvrir pourquoi.
-   Modifier la méthode de vote dans la fonction `knn` pour que les voisins les plus proches 
    aient davantage de poids.
-   Modifier la fonction de distance en attribuant un poids à chaque attribut.

