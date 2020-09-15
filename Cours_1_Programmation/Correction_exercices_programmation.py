#######################################
#Exercice 3
def somme_premiers_carre(k):
    """
    Renvoie la somme des k premiers carrés
    param : k : int
    return : int
    >>> somme_premiers_carre(3)
    14
    """
    somme=0
    for i in range(1,k+1):
        somme+=i*i
    return somme
#######################################
#Exercice 4
def somme_diviseurs(n):
    """
    Renvoie la somme des diviseurs de n
    param : n : int
    return : int
    >>> somme_diviseurs(9)
    13
    """
    somme=0
    for i in range(1,n+1):
        if n%i==0:
            somme+=i
    return somme

def est_parfait(n):
    """
    Renvoie True si la somme des diviseurs est le double de n
    False sinon
    param : n : int
    return : bool
    >>> est_parfait(6)
    True
    """
    if somme_diviseurs(n)==2*n:
        return True
    else:
        return False

#for i in range(1,100):
#    if est_parfait(i):
#        print(i)
#for i in range(100,1000):
#    if est_parfait(i):
#        print(i)
#######################################
#Exercice 5
def est_premier(n):
    """
    Renvoie True si le nombre est premier, False sinon
    param : n : int
    return : bool
    >>> est_premier(6)
    False
    >>> est_premier(13)
    True
    """
    for i in range(2,n):
        if n%i==0:
            return False
    return True

def premiers(n):
    """
    Renvoie la liste des nombres premiers inférieurs à n
    param : n : int
    return : bool
    >>> premiers(10)
    [2, 3, 5, 7]
    """
    liste=[]
    for i in range(2,n):
        if est_premier(i):
            liste.append(i)
    return liste
#######################################
#Exercice 6
import random

def pourcentage_de_six(n):
    somme=0
    for i in range(n):
        if random.randint(1,6)==6:
            somme+=1
    return 100*somme/n
#######################################
#Exercice 7
def double(mot):
    """
    Renvoie le mot doublé
    param : mot : str
    return : str
    >>> double('bon')
    'bboonn'
    """
    resultat=''
    for i in mot:
        resultat+=i*2
    return resultat

def double_autre(mot):
    """
    Renvoie le mot doublé
    param : mot : str
    return : str
    >>> double_autre('bon')
    'bboonn'
    """
    resultat=''
    for i in range(len(mot)):
        resultat+=mot[i]*2
    return resultat
#######################################
#Exercice 8
def a_meme_debut_et_fin(mot):
    """
    Renvoie True si la lettre de début et de fin sont identiques
    param : mot : str
    return : bool
    >>> a_meme_debut_et_fin("appela")
    True
    """
    return (mot[0]==mot[len(mot)-1])

def meme_debut_et_fin(mot1,mot2):
    """
    Renvoie True si les deux mots ont la même lettre de début et de fin
    param : mot : str
    return : bool
    >>> meme_debut_et_fin("tomba","tonna")
    True
    """
    return (mot1[0]==mot2[0] and mot1[len(mot1)-1]==mot2[len(mot2)-1])
#######################################
#Exercice 9

from random import choice

def test1():
    liste=['a','b','c','d']
    for i in range(100):
        choix=choice(liste)
        if choix not in liste:
            return False
    return True
         
from random import sample
def test2():
    liste=['a','b','c','d']
    for i in range(100):
        for k in range(len(liste)):
            extrait=sample(liste,k)
            for choix in extrait:
                if choix not in liste:
                    return False
    return True
#######################################
#Exercice 10   

from turtle import *

def carre(n):
    for i in range(4):
        forward(n)
        left(90)

#for i in range(10,201,10):
#    carre(i)
#    left(18)

#######################################
#Exercice 11
    
import matplotlib.pyplot as plt

def g(x):
    return x**2 

def trace(a,b,f,n):
    intervalle=(b-a)/(n-1)
    
    x=[a+i*intervalle for i in range(n)]
    y=[f(u) for u in x]
    plt.plot(x,y)
    plt.grid()
    plt.show()
    
#trace(-5,5,g,100)
#######################################    
if __name__ == '__main__':
  import doctest
  doctest.testmod(verbose=True)