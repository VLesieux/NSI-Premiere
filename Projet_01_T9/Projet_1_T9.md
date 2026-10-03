# Un clavier prédictif T9

## Objectifs

![T9 ](assets/T9.png)

Les anciens téléphones portables ne possédaient généralement pas de
clavier alphabétique complet. Les lettres étaient réparties sur les
touches numériques de **2 à 9** :

   Touche   Lettres
  -------- ---------
     2       a b c
     3       d e f
     4       g h i
     5       j k l
     6       m n o
     7      p q r s
     8       t u v
     9      w x y z

Le système **T9** permettait de saisir un mot en appuyant une seule fois
sur la touche correspondant à chaque lettre.

Ainsi :

``` text
bonjour → 2665687
```

Le problème est que plusieurs mots ou débuts de mots peuvent
correspondre à la même suite de chiffres.

Par exemple :

``` text
bon → 266
con → 266
```

Le téléphone doit donc déterminer **quel mot est le plus probable**.

Dans cette activité, nous allons programmer un système simplifié de
saisie prédictive T9.

Nous utiliserons notamment des **dictionnaires Python** afin d'obtenir
rapidement la meilleure proposition.

------------------------------------------------------------------------

# 1. Associer une lettre à une touche

On considère la chaîne suivante :

``` python
t9 = "22233344455566677778889999"
#     abcdefghijklmnopqrstuvwxyz
```

On rappelle que `ord(x) - ord("a")` permet d'obtenir la position de la
lettre `x` dans l'alphabet.
En effet, ord(x) donne la valeur décimale dans le système ASCII associée à la lettre x. Cette valeur croît dans l'ordre de l'alphabet.

### À faire 1

Compléter la fonction `lettre_chiffre`.

``` python
def lettre_chiffre(x):
    """
    Renvoie la touche du clavier T9 correspondant à la lettre x.

    >>> lettre_chiffre("a")
    '2'
    >>> lettre_chiffre("c")
    '2'
    >>> lettre_chiffre("d")
    '3'
    >>> lettre_chiffre("o")
    '6'
    >>> lettre_chiffre("s")
    '7'
    >>> lettre_chiffre("z")
    '9'
    """
    assert "a" <= x <= "z"
    # À compléter
```

------------------------------------------------------------------------

# 2. Coder un mot

### À faire 2

``` python
def mot_code(mot):
    """
    Renvoie le code T9 correspondant à mot.

    >>> mot_code("bonjour")
    '2665687'
    >>> mot_code("salut")
    '72588'
    >>> mot_code("chat")
    '2428'
    >>> mot_code("python")
    '798466'
    >>> mot_code("oui")
    '684'
    """
    # À compléter
```

### Question 1

Vérifier :

``` python
>>> mot_code("bon")
'266'
>>> mot_code("con")
'266'
```

Pourquoi cela pose-t-il un problème pour un système de saisie prédictive
?

------------------------------------------------------------------------

# 3. Un dictionnaire de mots

``` python
dico_test = [
    ("bonjour", 100),
    ("bonsoir", 60),
    ("bon", 40),
    ("comme", 80),
    ("comment", 50),
    ("connu", 20),
    ("chat", 70),
    ("chien", 90)
]
```

Chaque élément est un couple `(mot, poids)`. Plus le poids est élevé,
plus le mot est supposé fréquemment utilisé.

------------------------------------------------------------------------

# 4. Les préfixes d'un mot

Les préfixes non vides de `"chat"` sont `c`, `ch`, `cha`, `chat`.

### À faire 3

``` python
def prefixes(mot):
    """
    Renvoie la liste des préfixes non vides de mot.

    >>> prefixes("chat")
    ['c', 'ch', 'cha', 'chat']
    >>> prefixes("bon")
    ['b', 'bo', 'bon']
    >>> prefixes("a")
    ['a']
    """
    # À compléter
```

------------------------------------------------------------------------

# 5. Calculer le poids des préfixes

Pour :

``` python
dico = [
    ("bonjour", 100),
    ("bonsoir", 60),
    ("bon", 40)
]
```

les préfixes `"b"`, `"bo"` et `"bon"` ont chacun un poids total de
`200`.

### À faire 4

``` python
def frequences_prefixes(dico):
    """
    Renvoie un dictionnaire associant à chaque préfixe
    le poids total des mots possédant ce préfixe.

    >>> dico = [("bonjour", 100), ("bonsoir", 60), ("bon", 40)]
    >>> freq = frequences_prefixes(dico)
    >>> freq["b"]
    200
    >>> freq["bo"]
    200
    >>> freq["bon"]
    200
    >>> freq["bonj"]
    100
    >>> freq["bons"]
    60
    >>> freq["bonjour"]
    100
    """
    # À compléter
```

### Indication

``` python
if prefixe in freq:
    ...
else:
    ...
```

------------------------------------------------------------------------

# 6. Comprendre le dictionnaire obtenu

Avec :

``` python
dico = [
    ("bonjour", 100),
    ("bonsoir", 60),
    ("bon", 40),
    ("connu", 20)
]
freq = frequences_prefixes(dico)
```

### Question 2

Déterminer sans Python :

``` python
freq["b"]
freq["bo"]
freq["bon"]
freq["c"]
freq["co"]
freq["con"]
```

Puis vérifier.

### Question 3

Sachant que `"bon"` et `"con"` ont tous deux le code `266`, quel préfixe
le téléphone devrait-il proposer ? Justifier à l'aide des poids.

------------------------------------------------------------------------

# 7. Construire les propositions

Le dictionnaire `prop` associera à chaque séquence numérique le préfixe
de poids maximal correspondant.

### À faire 5

``` python
def propositions(freq):
    """
    Renvoie un dictionnaire associant à chaque code T9
    le préfixe de poids maximal.

    >>> freq = {"b": 200, "bo": 200, "bon": 200, "con": 20}
    >>> prop = propositions(freq)
    >>> prop["2"]
    'b'
    >>> prop["26"]
    'bo'
    >>> prop["266"]
    'bon'
    """
    prop = {}

    for prefixe in freq:
        code = mot_code(prefixe)
        # À compléter

    return prop
```

------------------------------------------------------------------------

# 8. Construire le système T9

### À faire 6

``` python
def predictive_text(dico):
    """
    Construit le dictionnaire des prédictions T9.

    >>> dico = [("bonjour", 100), ("bonsoir", 60), ("bon", 40), ("connu", 20)]
    >>> prop = predictive_text(dico)
    >>> prop["2"]
    'b'
    >>> prop["26"]
    'bo'
    >>> prop["266"]
    'bon'
    >>> prop["2665"]
    'bonj'
    >>> prop["26656"]
    'bonjo'
    >>> prop["2665687"]
    'bonjour'
    """
    # À compléter
```

------------------------------------------------------------------------

# 9. Faire une proposition

### À faire 7

``` python
def propose(prop, seq):
    """
    Renvoie la proposition correspondant à seq.
    Renvoie None si aucune proposition n'existe.

    >>> dico = [("bonjour", 100), ("bonsoir", 60), ("bon", 40), ("connu", 20)]
    >>> prop = predictive_text(dico)
    >>> propose(prop, "2")
    'b'
    >>> propose(prop, "26")
    'bo'
    >>> propose(prop, "266")
    'bon'
    >>> propose(prop, "2665")
    'bonj'
    >>> propose(prop, "26656")
    'bonjo'
    >>> propose(prop, "266568")
    'bonjou'
    >>> propose(prop, "2665687")
    'bonjour'
    >>> propose(prop, "999999") is None
    True
    """
    # À compléter
```

------------------------------------------------------------------------

# 10. Observer le fonctionnement du T9

``` python
dico = [
    ("bonjour", 100),
    ("bonsoir", 60),
    ("bon", 40),
    ("comme", 80),
    ("comment", 50),
    ("connu", 20),
    ("chat", 70),
    ("chien", 90)
]

prop = predictive_text(dico)
```

### Question 4

Tester successivement les codes `"2"`, `"26"`, `"266"`, `"2665"`,
`"26656"`, `"266568"` et `"2665687"` avec `propose`. Que constatez-vous
?

------------------------------------------------------------------------

# 11. Simuler la saisie sur un téléphone

### À faire 8

``` python
def affiche_saisie(prop, seq):
    """
    Affiche les propositions successives du système T9.

    >>> dico = [("bonjour", 100), ("bonsoir", 60), ("bon", 40), ("connu", 20)]
    >>> prop = predictive_text(dico)
    >>> affiche_saisie(prop, "2665687")
    2 -> b
    26 -> bo
    266 -> bon
    2665 -> bonj
    26656 -> bonjo
    266568 -> bonjou
    2665687 -> bonjour
    """
    # À compléter
```

------------------------------------------------------------------------

# 12. Pourquoi utiliser des dictionnaires ?

Une première solution consisterait, à chaque touche saisie, à parcourir
tous les mots. Notre programme construit auparavant le dictionnaire
`prop`, puis effectue essentiellement une recherche `prop[seq]`.

### Question 5

Quel est l'intérêt de faire une partie importante des calculs **avant**
que l'utilisateur commence à saisir son texte ?

### Question 6

Pourquoi un dictionnaire Python est-il particulièrement adapté pour
stocker les propositions ?

### Question 7

Supposons que le téléphone contienne 50 000 mots. À chaque touche
saisie, quelle solution semble préférable : parcourir les 50 000 mots ou
rechercher directement la séquence saisie dans `prop` ? Justifier.

------------------------------------------------------------------------

# 13. Pour aller plus loin --- personnaliser le T9

Un téléphone pourrait apprendre les habitudes de son utilisateur en
augmentant le poids des mots choisis régulièrement.

### Question 8

Quel effet l'augmentation du poids d'un mot pourrait-elle avoir sur les
propositions du système ?

### Question 9

Proposer un principe permettant au téléphone d'adapter progressivement
les poids des mots aux habitudes de son utilisateur.

------------------------------------------------------------------------

# 14. Programme principal

À la fin de l'activité, votre programme devra contenir :

``` python
def lettre_chiffre(x):
    ...

def mot_code(mot):
    ...

def prefixes(mot):
    ...

def frequences_prefixes(dico):
    ...

def propositions(freq):
    ...

def predictive_text(dico):
    ...

def propose(prop, seq):
    ...

def affiche_saisie(prop, seq):
    ...
```

Pour lancer les doctests :

``` python
if __name__ == "__main__":
    import doctest
    doctest.testmod()
```

------------------------------------------------------------------------

# Défi

Créer un petit programme interactif permettant à l'utilisateur de saisir
progressivement les chiffres de `2` à `9`. Après chaque chiffre, le
programme devra afficher le préfixe considéré comme le plus probable.

Exemple :

``` text
Saisir une touche : 2
Proposition : b

Saisir une touche : 6
Proposition : bo

Saisir une touche : 6
Proposition : bon

...

Saisir une touche : 7
Proposition : bonjour
```
