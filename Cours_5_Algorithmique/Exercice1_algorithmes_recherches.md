## Exercices sur les algorithmes de recherche

Pour chacun des exercices, écrire les docstrings et proposer des tests à vérifier.

On rappelle le code pour valider les tests des docstrings.

```Python
if __name__ == '__main__':
  import doctest
  doctest.testmod(verbose=True)
```

#### Exercice 1 : Recherche de l'indice d'une valeur dans un tableau

[Sujet Bac Terminale exercice 1](https://github.com/VLesieux/NSI-Terminale/blob/master/Evaluation_pratique/21_NSI_01/21-NSI-01.pdf)

#### Exercice 2 : Recherche d'un minimum pour une fonction donnée

[Sujet Bac Terminale exercice 2](https://github.com/VLesieux/NSI-Terminale/blob/master/Evaluation_pratique/21_NSI_01/21-NSI-01.pdf)

#### Exercice 3 : Recherche d'une moyenne

[Sujet Bac Terminale exercice 1](https://github.com/VLesieux/NSI-Terminale/blob/master/Evaluation_pratique/21_NSI_02/21-NSI-02.pdf)


#### Exercice 4 : Recherche par dichotomie

[Sujet Bac Terminale exercice 2](https://github.com/VLesieux/NSI-Terminale/blob/master/Evaluation_pratique/21_NSI_03/21_NSI_03.pdf)


#### Exercice 5 : Recherche d'un mot dans un texte

```Python
def recherche_mot_dans_un_texte(mot,texte):
    """
    Renvoie, si elle existe, la première occurence du mot dans le texte
    param : mot : str
    param : texte : str
    return : int
    >>> recherche_mot_dans_un_texte("oui","ce n'était pas si dur, oui, il fallait y croire")
    23
    >>> recherche_mot_dans_un_texte("oui","ce n'était pas si dur, il fallait y croire")
    'Le mot est absent du texte'
    """
```

Proposer deux écritures avec les deux types de boucle.