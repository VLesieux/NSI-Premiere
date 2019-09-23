![Programme officiel ](assets/bo2.png)

Le type d'une variable est l'ensemble des valeurs qui peuvent être affectées à cette variable.

On distingue :   
- les **types simples** : `int` (les nombres entiers), `bool` (les valeurs booléennes True ou False), `float` (nombres réels), `str` (abréviation de string ou chaîne de caractères écrite entre des guillemets " " ou des apostrophes ' '), `None` qui n'a pas de valeur


Opérations sur les types simples

```Python
>>> 1+2#addition
3
>>> 1-2#soustraction
-1
>>> 1*2#multiplication
2
>>> 1/2#division
0.5
>>> 1//2#division entière : renvoie le quotient entier de la division
0
>>> 5%2#renvoie le reste de la division
1#c'est le cas des entiers impairs
>>> 4%2
0#c'est le cas des entiers pairs

#existence de raccourcis d'écriture
>>> x=5
>>> x+=1
>>> x
6
>>> x*=2
>>> x
12

#opérations sur les chaînes de caractères
>>> chaine="poisson"
>>> chaine[1]#une chaîne est indicée à partir de 0 de gauche à droite
'o'
>>> chaine[-2]#on peut indicer de droite à gauche avec des indices négatifs
'o'
>>> chaine[2:4]#on réalise une découpe la chaîne (slice) entre 2 inclus et 4 non inclus
'is'
>>> chaine+" plat"#ajout de chaînes à la suite l'une de l'autre : concaténation à l'aide de l'opérateur +
#l'opérateur - ne s'applique pas sur les chaînes de caractères
'poisson plat'
>>> len(chaine)#longueur de la chaîne de caractères
7
>>> chaine*2
'poissonpoisson'
>>> float('100.5')
100.5#convertit une chaîne de caractères contenant un flottant en flottant
>>> int('100')
100#convertit une chaîne de caractères contenant un entier en entier
```


- les **types composés ou types construits** : 

`tuple` : p-uplet

```Python
>>> p_uplet=(1,"a") # les tuples sont des éléments séparés par des virgules entre des parenthèses
ou >>> p_uplet=1,"a" # les parenthèses ne sont pas obligatoires mais elles sont préférées
>>> len(p_uplet)#pour obtenir la longueur du tuple
2
>>> p_uplet[0]#les tuples sont indicés, le premier indice est 0
1
>>> p_uplet[1]
'a'
>>> p_uplet[1]='b'
Traceback (most recent call last):
  File "<pyshell>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment   
# !!!!!!!! les tuples ne sont pas des objets mutables, on ne peut pas les modifier par affectation
>>> p_uplet[2]='c'
Traceback (most recent call last):
  File "<pyshell>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment     
# !!!!!!!!! les tuples ne sont pas des objets mutables, on ne peut donc pas leur ajouter d'élément
t=((1,2,3),('bonjour','auto'),4)#un tuple peut être constitué lui-même de tuples
>>> t[1][0]
'bonjour'# on va chercher l'élément d'indice 0 dans le tuple d'indice 1
>>> 4 in t
True #condition d'appartenance de 4 au tuple t, 4 est effectivement présent à l'indice 2
>>> (2,4)*3 
(2, 4, 2, 4, 2, 4)#et non (6,12)
Remarque : l'affectation multiple résulte de l'égalité des tuples
x,y,z=3,4,x+y
>>> t=((1,2,3),('bonjour','auto'),4)
>>> for i in t:#on parcourt ainsi les éléments de la liste, i représente un élément constitutif de t
    print(i)  
(1, 2, 3)
('bonjour', 'auto')
4
```

> On considère le n-uplet t=(3,5,1). Qu'obtient-on après l'instruction t[1]=4 ?

`list` : liste ou tableau

```Python
>>> liste=[1,"a"]# les listes sont des éléments séparés par des virgules entre des crochets
>>> len(liste)#la longueur de la liste
2
>>> liste[0]#accès à l'élément d'indice 0
1
>>> liste[1]#accès à l'élément d'indice 1
'a'
>>> liste[1]="b"#modification de l'élément d'indice 1
>>> liste
[1, 'b']#les listes sont mutables
>>> liste[2]="c"
Traceback (most recent call last):
  File "<pyshell>", line 1, in <module>
IndexError: list assignment index out of range
#une erreur de dépassement d'index signifie qu'on ne peut pas accéder à un élément en dehors de la taille de la liste
>>> liste.append("c")#on utilise la méthode append pour ajouter un élément à la liste
>>> liste
[1, 'b', 'c']
>>> liste[-1]#on compte négativement les indices de droite à gauche en commençant par - 1
'c'
>>> nouvelle_liste=[liste,'d']#une liste peut contenir une liste
>>> nouvelle_liste
[[1, 'b', 'c'], 'd']
>>> nouvelle_liste[0][1]#pour accéder à l'élément d'indice 1 de l'élément d'indice 0 de nouvelle_liste
'b'
>>> nouvelle_liste.pop()#renvoie le dernier élément de la liste et le supprime 
'd'
>>> nouvelle_liste
[[1, 'b', 'c']]
>>> 'b' in nouvelle_liste#condition d'appartenance de 'b' à la liste
False
>>> 'b' in nouvelle_liste[0]
True
>>> nouvelle_liste[0].index('b')#renvoie l'indice de position d'un élément dans une liste
1
>>> nouvelle_liste.insert(1,'e')#insère un élément dans une liste à un index donné
>>> nouvelle_liste
[[1, 'b', 'c'], 'e']
>>> liste=[1,5,3,2]
>>> liste.sort()#ordonne la liste
>>> liste
[1, 2, 3, 5]
>>> liste.reverse()#renverse la liste
>>> liste
[5, 3, 2, 1]
>>> liste1=[3,4,5]
>>> liste2=[6,7,8]
>>> liste=liste1+liste2#l'opération + n'a pas d'effet de bord et ne modifie pas les listes 1 et 2
>>> liste
[3, 4, 5, 6, 7, 8]
>>> liste1=[1,5,7]
>>> liste2=liste1
>>> liste2[2]=10
>>> liste1
[1, 5, 10]#les deux listes qui contiennent une référence vers le même objet sont modifiées simultanément
>>> liste1=[1,5,7]
>>> liste2=list(liste1)#création d'un nouvel objet distinct de l'objet initial
>>> liste2[2]=10
>>> liste1
[1, 5, 7]
>>> liste2
[1, 5, 10]
>>> list(('a','b',5))
['a', 'b', 5]#un tuple peut être transformé en liste
>>> liste="1;a;5".split(";")
>>> liste
['1', 'a', '5']#une liste peut être créée à partir d'une chaîne de caractère en appliquant la méthode str.split()
>>> tuple(['a', 'b', 5])
('a', 'b', 5)#une liste peut être transformée en tuple en utilisant la fonction tuple()
>>> x=[i*2 for i in range(10)]####construction d'une liste par compréhension####
>>> x
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
>>> verbes_premiere_personne=["mange","parle","marche"]
>>> verbes_infinitif=[i+"r" for i in verbes_premiere_personne]
>>> verbes_infinitif
['manger', 'parler', 'marcher']
>>> liste=[[x,y] for x in range(3) for y in range(3)]# méthode de création d'une matrice ou listes emboîtées
>>> liste
[[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2]]
>>> matrice=[]
>>> for n in range(4):
    	ligne=[4*n+i for i in range(1,5)]
    	matrice.append(ligne)
>>> matrice
[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]#autre méthode de création d'une matrice
>>> matrice2=matrice#les deux matrices pointent sur le même objet
>>> matrice2[0][2]=5
>>> matrice2
[[1, 2, 5, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
>>> matrice
[[1, 2, 5, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
>>> from copy import deepcopy
>>> matrice3=deepcopy(matrice)#matrice3 est une copie profonde de matrice2 distincte de celle-ci
>>> matrice3[0][2]=8
>>> matrice3
[[1, 2, 8, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
>>> matrice
[[1, 2, 5, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
```

> Soit la liste L=[[1,2,3],[4,5,6],[7,8,9]], quelle est la valeur de L[1][2]?    

> Soit l'instruction L=[[i,i+1] for i in range(2)]. Quelle est la valeur de L?

> On construit une matrice avec le code ci-dessous ; quelle est la valeur de cette matrice ?

```Python
m=[3*[0] for i in range(3)]
for i in range(3):
    m[i][i]=i+1
    m[0][i]=m[0][i]+i+1
    m[i][2]=m[i][2]+i+1
```

`dict` : dictionnaire

```Python
>>> frequences={"do4":523.25,"la3":440}#dictionnaire clé-valeur : clé=nom de la note, valeur=fréquence en Hz à l'intérieur d'une accolade
>>> frequences=[["do4",523.25],["la3",440]]
>>> dico=dict(frequences)
>>> dico
{'do4': 523.25, 'la3': 440}#un dictionnaire peut être créé à partir d'une liste, ce qui est pratique.
>>> frequences["do4"]#on cherche la valeur associée à la clé "do4"
523.25
>>> frequences["la3"]=660
>>> frequences
{'do4': 523.25, 'la3': 660}#un dictionnaire est mutable
>>> frequences["la3"]=440
>>> frequences["mi4"]=659.26#ajout d'un nouveau couple clé-valeur au dictionnaire
>>> frequences
{'do4': 523.25, 'la3': 440, 'mi4': 659.26}
>>> frequences["mi5"]
Traceback (most recent call last):
  File "<pyshell>", line 1, in <module>
KeyError: 'mi5'#Erreur de clé KeyError car la clé 'mi5' demandée n'existe pas
>>> frequences.get('mi5')
>>> #pas de réponse mais ne provoque pas de signalement d'erreur KeyError en l'absence de la clé
>>> len(frequences)#longueur du dictionnaire
3
>>> frequences.keys()#la méthode keys renvoie les clés du dictionnaire
dict_keys(['do4', 'la3', 'mi4'])
>>> for j in frequences.keys():
    print("les notes sont",j)    
les notes sont do4
les notes sont la3
>>> frequences.values()#la méthode values renvoie les valeurs des clés du dictionnaire
dict_values([523.25, 440, 659.26])
>>> for j in frequences.values():
    print("les fréquences sont",j)    
les fréquences sont 523.25
les fréquences sont 440
>>> frequences.items()
dict_items([('do4', 523.25), ('la3', 440), ('mi4', 659.26)])
>>> for j in frequences.items():
    print("item",j)   
item ('do4', 523.25)
item ('la3', 440)
>>> 'do4' in frequences
True
>>> for cle,val in frequences.items():
    print(cle,val)    
do4 523.25
la3 440
mi4 659.26
>>> del(frequences['la3'])#supprime une clé du dictionnaire
>>> frequences
{'do4': 523.25, 'mi4': 659.26}
>>> frequences2=frequences#les deux dictionnaires pointent vers le même objet
>>> frequences2["mi4"]=600
>>> frequences2
{'do4': 523.25, 'mi4': 600}
>>> frequences
{'do4': 523.25, 'mi4': 600}
>>> from copy import deepcopy
>>> frequences3=deepcopy(frequences)#frequences3 est une copie profonde de frequences2 distincte de celle-ci
>>> frequences3["mi4"]=659.26
>>> frequences
{'do4': 523.25, 'mi4': 600}
>>> frequences3
{'do4': 523.25, 'mi4': 659.26}
>>> d={x:x**2 for x in  range(1,5)}#construction d'un dictionnaire par compréhension
>>> d
{1: 1, 2: 4, 3: 9, 4: 16}
>>> pays={'France':{'capitale':'Paris','superficie':643800},'Portugal':{'capitale':'Lisbonne','superficie':92300}}#création de dictionnaire de dictionnaire
>>> pays["France"]["superficie"]
643800
Remarques:
>>> dictionnaire={"DK":1300}
>>> dictionnaire[(2,6)]=23
>>> dictionnaire
{'DK': 1300, (2, 6): 23}#une clé de dictionnaire peut être un tuple
>>> dictionnaire[[3,6]]=12
Traceback (most recent call last):
  File "<pyshell>", line 1, in <module>
TypeError: unhashable type: 'list'#une clé de dictionnaire ne peut pas être une liste
```
> Qu'obtient-on avec le code ci-dessous ?

```Python
d={"if":"si","yes":"oui","no":"non"} 
for c in d:
    print(d[c])
```