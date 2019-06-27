#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
:mod:`triangle_pascal` module
:date: mai 2019
:auteur: Équipe pédagogique DIU EIL LILLE

"""

def factorielle(n):
    '''
    renvoie la factorielle de l'entier n

    :param n: (int)
    :return: (int) n! (= 1x2x3x...xn)
    :CU: n >= 0

    >>> factorielle(6)
    720
    '''
    fact = 1
    for i in range(2, n+1):
        fact *= i
    return fact

def binomial(n, p):
    '''
    renvoie le coefficient binomial (n,p) 

    :param n, p: (int)
    :return: (int)
    :CU: 0 <= p <= n

    >>> binomial(4, 2)
    6
    '''
    return factorielle(n) // (factorielle(n-p)*factorielle(p))

def cree_triangle_pascal(nmax):
    '''
    construit un triangle de Pascal sous forme d'une liste de listes de coeffts binomiaux

    :param nmax: (int) valeur maximal des coeffts binomiaux (= nbre de lignes du triangle - 1)
    :return: (list) liste de listes d'entiers telle que l[n][p] = binomial(n, p)
    :CU: aucune (si n <= 0 liste vide)

    >>> cree_triangle_pascal(2)
    [[1], [1, 1], [1, 2, 1]]
    '''
    triangle = []
    for n in range(nmax+1):
        ligne = []
        for p in range(n+1):
            ligne.append(binomial(n, p))
        triangle.append(ligne)
    return triangle
    
def imprimer_ligne(liste):
    '''
    imprime le contenu de la liste sur une ligne
    
    :param liste: (list) une liste d'entiers
    :return: (NoneType) aucune valeur renvoyée
    :effet de bord: imprime le contenu de liste
    :CU: aucune
    
    >>> imprimer_ligne([1, 2, 1])
    1 2 1 
    '''
    for k in liste:
        print(k, end=' ')
    print() # pour passer à la ligne
        
def imprimer_triangle(liste_listes):
    '''
    imprime le contenu de liste_listes, à raison d'une ligne par listes

    :param liste_listes: (liste) une liste de listes
    :return: (NoneType) aucune valeur renvoyée
    :effet de bord: imprime chacune des listes de liste_listes sur une ligne
    :CU: aucune 

    >>> imprimer_triangle([[1], [1, 1], [1, 2, 1]])
    1 
    1 1 
    1 2 1 
    '''
    for liste in liste_listes:
        imprimer_ligne(liste)


import doctest
doctest.testmod(verbose=True)


N_MAX = 6
imprimer_triangle(cree_triangle_pascal(N_MAX))

