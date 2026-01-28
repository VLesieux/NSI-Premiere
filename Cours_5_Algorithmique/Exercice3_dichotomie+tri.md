<!-- -*- coding: UTF-8 -*- -->

La recherche par dichotomie permet en mathématiques la recherche d'une solution non évidente de l'équation f(x)=0

Dans le cas présent, la fonction considérée est :

f(x)=x**3−2x−5


<img src="courbe.png" width="600"/>


On admet pour cela le théorème mathématique selon lequel si f(a)*f(b)<0 alors il existe un réel x entre a et b tel que f(x)=0


Proposer une recherche par dichotomie qui permet de déterminer cette solution avec la précision requise en validant le test de la documentation.



```
def recherche_solution_dichotomie(fonction,a,b,precision):
    """
    Renvoie la valeur approchée de l'équation f(x)=0 avec x entre a et b 
	avec la precision demandée, ainsi que le nombre d'opérations effectuée
    param : f : function
    param : a : float
    param : b : float
    param : precision : float
    return : tuple
    >>> recherche_solution_dichotomie(f,1,3,0.001)
    (2.0947265625, 11)
    """
```


