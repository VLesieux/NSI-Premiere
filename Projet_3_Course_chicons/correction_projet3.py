import src.Competitor as Competitor
import src.Time as Time
import src.Tri as Tri
import csv
##################################À faire n°1##############################################
def read_competitors(text):
    """
    lit un fichier csv et retourne un dictionnaire dont les clés sont les numéros de brassard
    et les valeurs les tuples contenant les informations sur les compétiteurs
    param : text : csv file
    return : dict
    >>> read_competitors("data/small_inscrits.csv")
    {1: {'bib_num': 1, 'first_name': 'Sidney', 'last_name': 'Robert', 'sex': 'M', 'birth_date': '21/7/1970', 'performance': None}, 2: {'bib_num': 2, 'first_name': 'Paien', 'last_name': 'Gilbert', 'sex': 'M', 'birth_date': '26/11/1953', 'performance': None}, 3: {'bib_num': 3, 'first_name': 'Vincent', 'last_name': 'Riquier', 'sex': 'M', 'birth_date': '16/9/1980', 'performance': None}, 4: {'bib_num': 4, 'first_name': 'Saville', 'last_name': 'Marier', 'sex': 'M', 'birth_date': '19/11/1969', 'performance': None}, 5: {'bib_num': 5, 'first_name': 'Namo', 'last_name': 'Lereau', 'sex': 'M', 'birth_date': '26/3/1980', 'performance': None}, 6: {'bib_num': 6, 'first_name': 'Romaine', 'last_name': 'Hughes', 'sex': 'F', 'birth_date': '17/10/1943', 'performance': None}, 7: {'bib_num': 7, 'first_name': 'Archard', 'last_name': 'Rivard', 'sex': 'M', 'birth_date': '10/6/1950', 'performance': None}, 8: {'bib_num': 8, 'first_name': 'Cheney', 'last_name': 'Chassé', 'sex': 'M', 'birth_date': '21/3/1949', 'performance': None}, 9: {'bib_num': 9, 'first_name': 'Avelaine', 'last_name': 'CinqMars', 'sex': 'F', 'birth_date': '14/2/1983', 'performance': None}, 10: {'bib_num': 10, 'first_name': 'Sidney', 'last_name': 'Charest', 'sex': 'M', 'birth_date': '5/3/1981', 'performance': None}}
    >>> read_competitors("no_file.csv")
    Votre fichier n'est pas un csv lisible ou il n'existe pas
    """
    try:
        f=open(text,"r")
        table=[ligne.rstrip().split(';') for ligne in f]
        f.close()
        del(table[0])
        dictionnaire={}
        for i in range(len(table)):
            dictionnaire[i+1]=Competitor.create(table[i][0],table[i][1],table[i][2],table[i][3],i+1)
        return dictionnaire
    except FileNotFoundError:
        print("Votre fichier n'est pas un csv lisible ou il n'existe pas")
##################################À faire n°2##############################################
def affichage(competiteurs):
    """
    Renvoie un affichage (avec print) du fichier des competiteurs
    param : competiteurs : csv
    return : None
    >>> affichage(read_competitors("data/small_inscrits.csv"))
    [1]: Sidney Robert (M - 21/7/1970) 
    [2]: Paien Gilbert (M - 26/11/1953) 
    [3]: Vincent Riquier (M - 16/9/1980) 
    [4]: Saville Marier (M - 19/11/1969) 
    [5]: Namo Lereau (M - 26/3/1980) 
    [6]: Romaine Hughes (F - 17/10/1943) 
    [7]: Archard Rivard (M - 10/6/1950) 
    [8]: Cheney Chassé (M - 21/3/1949) 
    [9]: Avelaine CinqMars (F - 14/2/1983) 
    [10]: Sidney Charest (M - 5/3/1981) 
    """
    for valeur in competiteurs.values():
        print(Competitor.to_string(valeur)+"\n")
    
##################################À faire n°3##############################################
def select_competitor_by_bib(competiteurs,numero):
    """
    Renvoie le competiteur à partir de son dossard
    param : competiteurs : csv
    param : numero : int
    return : dict
    >>> select_competitor_by_bib(read_competitors("data/small_inscrits.csv"),8)
    {'bib_num': 8, 'first_name': 'Cheney', 'last_name': 'Chassé', 'sex': 'M', 'birth_date': '21/3/1949', 'performance': None}    
    >>> select_competitor_by_bib(read_competitors("data/small_inscrits.csv"),0)
    Ce compétiteur n'existe pas    
    """
    try:
        return competiteurs[numero]
    except KeyError:
        print("Ce compétiteur n'existe pas")

##################################À faire n°4##############################################     
def select_competitor_by_birth_year(competiteurs,date_naissance):
    """
    Renvoie la liste des competiteurs de cet age
    param : competiteurs : csv
    param : age : int
    return : list
    >>> select_competitor_by_birth_year(read_competitors("data/small_inscrits.csv"),1980)
    [{'bib_num': 3, 'first_name': 'Vincent', 'last_name': 'Riquier', 'sex': 'M', 'birth_date': '16/9/1980', 'performance': None}, {'bib_num': 5, 'first_name': 'Namo', 'last_name': 'Lereau', 'sex': 'M', 'birth_date': '26/3/1980', 'performance': None}]
    >>> select_competitor_by_birth_year(read_competitors("data/small_inscrits.csv"),1960)
    Il n'y a pas de compétiteur ayant cette date de naissance
    """
    resultat=[]
    for valeur in competiteurs.values():
        if valeur['birth_date'].endswith(str(date_naissance)):
            resultat.append(valeur)
    if len(resultat)==0:
        print("Il n'y a pas de compétiteur ayant cette date de naissance")
    else:
        return resultat
##################################À faire n°5##############################################

def select_competitor_by_name(competiteurs,chaine):
    """
    Sélectionne un compétiteur si la chaine est contenu dans son nom de famille
    param : competiteurs : csv
    param : chaine : str
    return : list
    >>> select_competitor_by_name(read_competitors("data/small_inscrits.csv"),"Ri")
    [{'bib_num': 3, 'first_name': 'Vincent', 'last_name': 'Riquier', 'sex': 'M', 'birth_date': '16/9/1980', 'performance': None}, {'bib_num': 7, 'first_name': 'Archard', 'last_name': 'Rivard', 'sex': 'M', 'birth_date': '10/6/1950', 'performance': None}]    
    >>> select_competitor_by_name(read_competitors("data/small_inscrits.csv"),"Joe")
    Il n'y a pas de compétiteur dont le nom commence ainsi
    """
    resultat=[]
    for valeur in competiteurs.values():
        if chaine in valeur['last_name']:
            resultat.append(valeur)
    if len(resultat)==0:
        print("Il n'y a pas de compétiteur dont le nom commence ainsi")
    else:
        return resultat

##################################À faire n°6##############################################

def read_performances(text):
    """
    lit un fichier csv et retourne un dictionnaire dont les clés sont les numéros de brassard
    et les valeurs les tuples contenant les performances des compétiteurs
    param : text : csv
    return : dict
    >>> read_performances("data/small_performances.csv")
    {1: Time(hours=1, minutes=8, seconds=55), 3: Time(hours=1, minutes=21, seconds=23), 4: Time(hours=0, minutes=56, seconds=29), 5: Time(hours=1, minutes=6, seconds=20), 6: Time(hours=1, minutes=17, seconds=8), 7: Time(hours=0, minutes=46, seconds=31), 8: Time(hours=0, minutes=48, seconds=10), 10: Time(hours=1, minutes=6, seconds=38)}
    >>> read_performances("no_file.csv")
    Votre fichier n'est pas un csv lisible ou il n'existe pas    
    """
    try:
        f=open(text,"r")
        table=[ligne.rstrip().split(';') for ligne in f]
        f.close()
        del(table[0])
        dictionnaire={}
        for i in range(len(table)):
            dictionnaire[int(table[i][0])]=Time.create(int(table[i][1]),int(table[i][2]),int(table[i][3]))
        return dictionnaire
    except FileNotFoundError:
        print("Votre fichier n'est pas un csv lisible ou il n'existe pas")    


##################################À faire n°7##############################################

def set_performances(dic1,dic2):
    """
    fusionne les dictionnaires en utilisant la clé commune = numéro de brassard
    param : dic1 : dict
    param : dic2 : dict
    return : dict
    >>> set_performances(read_competitors("data/small_inscrits.csv"),read_performances('data/small_performances.csv'))
    {1: {'bib_num': 1, 'first_name': 'Sidney', 'last_name': 'Robert', 'sex': 'M', 'birth_date': '21/7/1970', 'performance': ' 1h 8mn 55s'}, 2: {'bib_num': 2, 'first_name': 'Paien', 'last_name': 'Gilbert', 'sex': 'M', 'birth_date': '26/11/1953', 'performance': None}, 3: {'bib_num': 3, 'first_name': 'Vincent', 'last_name': 'Riquier', 'sex': 'M', 'birth_date': '16/9/1980', 'performance': ' 1h 21mn 23s'}, 4: {'bib_num': 4, 'first_name': 'Saville', 'last_name': 'Marier', 'sex': 'M', 'birth_date': '19/11/1969', 'performance': ' 0h 56mn 29s'}, 5: {'bib_num': 5, 'first_name': 'Namo', 'last_name': 'Lereau', 'sex': 'M', 'birth_date': '26/3/1980', 'performance': ' 1h 6mn 20s'}, 6: {'bib_num': 6, 'first_name': 'Romaine', 'last_name': 'Hughes', 'sex': 'F', 'birth_date': '17/10/1943', 'performance': ' 1h 17mn 8s'}, 7: {'bib_num': 7, 'first_name': 'Archard', 'last_name': 'Rivard', 'sex': 'M', 'birth_date': '10/6/1950', 'performance': ' 0h 46mn 31s'}, 8: {'bib_num': 8, 'first_name': 'Cheney', 'last_name': 'Chassé', 'sex': 'M', 'birth_date': '21/3/1949', 'performance': ' 0h 48mn 10s'}, 9: {'bib_num': 9, 'first_name': 'Avelaine', 'last_name': 'CinqMars', 'sex': 'F', 'birth_date': '14/2/1983', 'performance': None}, 10: {'bib_num': 10, 'first_name': 'Sidney', 'last_name': 'Charest', 'sex': 'M', 'birth_date': '5/3/1981', 'performance': ' 1h 6mn 38s'}}
    """
    dictionnaire={}
    for cle2,valeur2 in dic2.items():
        for cle1 in dic1.keys():
            dictionnaire[cle1]=dic1[cle1]
            if cle1==cle2:
                dictionnaire[cle1]['performance']=Time.to_string(valeur2)
    return dictionnaire
            
##################################À faire n°8##############################################        

def sort_competitors_by_lastname(dic):
    """
    renvoie un dictionnaire trié dans l'ordre alphabétique croissant
    utilise la fonction de tri présente dans le module Tri
    param : dic : dict
    return : dict
    >>> sort_competitors_by_lastname(set_performances(read_competitors("data/small_inscrits.csv"),read_performances('data/small_performances.csv')))
    {10: {'bib_num': 10, 'first_name': 'Sidney', 'last_name': 'Charest', 'sex': 'M', 'birth_date': '5/3/1981', 'performance': ' 1h 6mn 38s'}, 8: {'bib_num': 8, 'first_name': 'Cheney', 'last_name': 'Chassé', 'sex': 'M', 'birth_date': '21/3/1949', 'performance': ' 0h 48mn 10s'}, 9: {'bib_num': 9, 'first_name': 'Avelaine', 'last_name': 'CinqMars', 'sex': 'F', 'birth_date': '14/2/1983', 'performance': None}, 2: {'bib_num': 2, 'first_name': 'Paien', 'last_name': 'Gilbert', 'sex': 'M', 'birth_date': '26/11/1953', 'performance': None}, 6: {'bib_num': 6, 'first_name': 'Romaine', 'last_name': 'Hughes', 'sex': 'F', 'birth_date': '17/10/1943', 'performance': ' 1h 17mn 8s'}, 5: {'bib_num': 5, 'first_name': 'Namo', 'last_name': 'Lereau', 'sex': 'M', 'birth_date': '26/3/1980', 'performance': ' 1h 6mn 20s'}, 4: {'bib_num': 4, 'first_name': 'Saville', 'last_name': 'Marier', 'sex': 'M', 'birth_date': '19/11/1969', 'performance': ' 0h 56mn 29s'}, 3: {'bib_num': 3, 'first_name': 'Vincent', 'last_name': 'Riquier', 'sex': 'M', 'birth_date': '16/9/1980', 'performance': ' 1h 21mn 23s'}, 7: {'bib_num': 7, 'first_name': 'Archard', 'last_name': 'Rivard', 'sex': 'M', 'birth_date': '10/6/1950', 'performance': ' 0h 46mn 31s'}, 1: {'bib_num': 1, 'first_name': 'Sidney', 'last_name': 'Robert', 'sex': 'M', 'birth_date': '21/7/1970', 'performance': ' 1h 8mn 55s'}}
    """
    noms=[]
    for valeur in dic.values():
        noms.append(valeur['last_name'])
    Tri.tri_selection(noms,Tri.compare_chaine_lexicographique)
    dictionnaire={}
    for nom in noms:
        for cle,valeur in dic.items():
            if valeur['last_name']==nom:
                dictionnaire[cle]=valeur
    return dictionnaire

##################################À faire n°9##############################################

#########################Méthode1################################
def conversion_en_seconde(time):
    """
    Renvoie time converti en seconde
    param : time : str
    return : int
    >>> conversion_en_seconde(' 1h 21mn 23s')
    4883
    """
    temps=int(time.strip(' ').split(' ')[0].strip('h'))*3600+int(time.strip(' ').split(' ')[1].strip('mn'))*60+int(time.strip(' ').split(' ')[2].strip('s'))
    return temps

def sort_competitors_by_performance_methode1(dic):
    """
    renvoie un dictionnaire des compétiteurs trié par performance
    utilise la méthode compare_entier_croissant du module Tri
    >>> sort_competitors_by_performance_methode1(set_performances(read_competitors("data/small_inscrits.csv"),read_performances('data/small_performances.csv')))
    {7: {'bib_num': 7, 'first_name': 'Archard', 'last_name': 'Rivard', 'sex': 'M', 'birth_date': '10/6/1950', 'performance': ' 0h 46mn 31s'}, 8: {'bib_num': 8, 'first_name': 'Cheney', 'last_name': 'Chassé', 'sex': 'M', 'birth_date': '21/3/1949', 'performance': ' 0h 48mn 10s'}, 4: {'bib_num': 4, 'first_name': 'Saville', 'last_name': 'Marier', 'sex': 'M', 'birth_date': '19/11/1969', 'performance': ' 0h 56mn 29s'}, 5: {'bib_num': 5, 'first_name': 'Namo', 'last_name': 'Lereau', 'sex': 'M', 'birth_date': '26/3/1980', 'performance': ' 1h 6mn 20s'}, 10: {'bib_num': 10, 'first_name': 'Sidney', 'last_name': 'Charest', 'sex': 'M', 'birth_date': '5/3/1981', 'performance': ' 1h 6mn 38s'}, 1: {'bib_num': 1, 'first_name': 'Sidney', 'last_name': 'Robert', 'sex': 'M', 'birth_date': '21/7/1970', 'performance': ' 1h 8mn 55s'}, 6: {'bib_num': 6, 'first_name': 'Romaine', 'last_name': 'Hughes', 'sex': 'F', 'birth_date': '17/10/1943', 'performance': ' 1h 17mn 8s'}, 3: {'bib_num': 3, 'first_name': 'Vincent', 'last_name': 'Riquier', 'sex': 'M', 'birth_date': '16/9/1980', 'performance': ' 1h 21mn 23s'}, 9: {'bib_num': 9, 'first_name': 'Avelaine', 'last_name': 'CinqMars', 'sex': 'F', 'birth_date': '14/2/1983', 'performance': None}, 2: {'bib_num': 2, 'first_name': 'Paien', 'last_name': 'Gilbert', 'sex': 'M', 'birth_date': '26/11/1953', 'performance': None}}
    """
    dictionnaire={}
    ##################
    temps=[]
    for valeur in dic.values():
        if valeur['performance'] !=None:
            temps.append(conversion_en_seconde(valeur['performance']))
    Tri.tri_selection(temps,Tri.compare_entier_croissant)
    for resultat in temps:
        for cle,valeur in dic.items():
            if valeur['performance'] !=None and conversion_en_seconde(valeur['performance'])==resultat:
                dictionnaire[cle]=valeur
    ##################
    noms_sans_performance=[]
    for valeur in dic.values():
        if valeur['performance']==None:
            noms_sans_performance.append(valeur['last_name'])
    Tri.tri_selection(noms_sans_performance,Tri.compare_chaine_lexicographique)
    for nom in noms_sans_performance:
        for cle,valeur in dic.items():
            if valeur['last_name']==nom:
                dictionnaire[cle]=valeur
    ##################    
    return dictionnaire    

#########################Méthode2################################
    
def set_performances_time(dic1,dic2):
    """
    fusionne les dictionnaires en utilisant la clé commune = numéro de brassard
    param : dic1 : dict
    param : dic2 : dict
    return : dict
    >>> set_performances_time(read_competitors("data/small_inscrits.csv"),read_performances('data/small_performances.csv'))
    {1: {'bib_num': 1, 'first_name': 'Sidney', 'last_name': 'Robert', 'sex': 'M', 'birth_date': '21/7/1970', 'performance': Time(hours=1, minutes=8, seconds=55)}, 2: {'bib_num': 2, 'first_name': 'Paien', 'last_name': 'Gilbert', 'sex': 'M', 'birth_date': '26/11/1953', 'performance': None}, 3: {'bib_num': 3, 'first_name': 'Vincent', 'last_name': 'Riquier', 'sex': 'M', 'birth_date': '16/9/1980', 'performance': Time(hours=1, minutes=21, seconds=23)}, 4: {'bib_num': 4, 'first_name': 'Saville', 'last_name': 'Marier', 'sex': 'M', 'birth_date': '19/11/1969', 'performance': Time(hours=0, minutes=56, seconds=29)}, 5: {'bib_num': 5, 'first_name': 'Namo', 'last_name': 'Lereau', 'sex': 'M', 'birth_date': '26/3/1980', 'performance': Time(hours=1, minutes=6, seconds=20)}, 6: {'bib_num': 6, 'first_name': 'Romaine', 'last_name': 'Hughes', 'sex': 'F', 'birth_date': '17/10/1943', 'performance': Time(hours=1, minutes=17, seconds=8)}, 7: {'bib_num': 7, 'first_name': 'Archard', 'last_name': 'Rivard', 'sex': 'M', 'birth_date': '10/6/1950', 'performance': Time(hours=0, minutes=46, seconds=31)}, 8: {'bib_num': 8, 'first_name': 'Cheney', 'last_name': 'Chassé', 'sex': 'M', 'birth_date': '21/3/1949', 'performance': Time(hours=0, minutes=48, seconds=10)}, 9: {'bib_num': 9, 'first_name': 'Avelaine', 'last_name': 'CinqMars', 'sex': 'F', 'birth_date': '14/2/1983', 'performance': None}, 10: {'bib_num': 10, 'first_name': 'Sidney', 'last_name': 'Charest', 'sex': 'M', 'birth_date': '5/3/1981', 'performance': Time(hours=1, minutes=6, seconds=38)}}
    """
    dictionnaire={}
    for cle2,valeur2 in dic2.items():
        for cle1 in dic1.keys():
            dictionnaire[cle1]=dic1[cle1]
            if cle1==cle2:
                dictionnaire[cle1]['performance']=valeur2
    return dictionnaire   
    
def sort_competitors_by_performance_methode2(dic):
    """
    renvoie un dictionnaire des compétiteurs trié par performance
    utilise la méthode compare du module Time
    param : dic : dict
    return : dict
    >>> sort_competitors_by_performance_methode2(set_performances_time(read_competitors("data/small_inscrits.csv"),read_performances('data/small_performances.csv')))
    {7: {'bib_num': 7, 'first_name': 'Archard', 'last_name': 'Rivard', 'sex': 'M', 'birth_date': '10/6/1950', 'performance': ' 0h 46mn 31s'}, 8: {'bib_num': 8, 'first_name': 'Cheney', 'last_name': 'Chassé', 'sex': 'M', 'birth_date': '21/3/1949', 'performance': ' 0h 48mn 10s'}, 4: {'bib_num': 4, 'first_name': 'Saville', 'last_name': 'Marier', 'sex': 'M', 'birth_date': '19/11/1969', 'performance': ' 0h 56mn 29s'}, 5: {'bib_num': 5, 'first_name': 'Namo', 'last_name': 'Lereau', 'sex': 'M', 'birth_date': '26/3/1980', 'performance': ' 1h 6mn 20s'}, 10: {'bib_num': 10, 'first_name': 'Sidney', 'last_name': 'Charest', 'sex': 'M', 'birth_date': '5/3/1981', 'performance': ' 1h 6mn 38s'}, 1: {'bib_num': 1, 'first_name': 'Sidney', 'last_name': 'Robert', 'sex': 'M', 'birth_date': '21/7/1970', 'performance': ' 1h 8mn 55s'}, 6: {'bib_num': 6, 'first_name': 'Romaine', 'last_name': 'Hughes', 'sex': 'F', 'birth_date': '17/10/1943', 'performance': ' 1h 17mn 8s'}, 3: {'bib_num': 3, 'first_name': 'Vincent', 'last_name': 'Riquier', 'sex': 'M', 'birth_date': '16/9/1980', 'performance': ' 1h 21mn 23s'}, 9: {'bib_num': 9, 'first_name': 'Avelaine', 'last_name': 'CinqMars', 'sex': 'F', 'birth_date': '14/2/1983', 'performance': None}, 2: {'bib_num': 2, 'first_name': 'Paien', 'last_name': 'Gilbert', 'sex': 'M', 'birth_date': '26/11/1953', 'performance': None}}
    """
    dictionnaire={}
    ##################
    temps=[]
    for valeur in dic.values():
        if valeur['performance'] !=None:
            temps.append(valeur['performance'])
    Tri.tri_selection(temps,Time.compare)
    for resultat in temps:
        for cle,valeur in dic.items():
            if valeur['performance'] !=None and valeur['performance']==resultat:
                dictionnaire[cle]=valeur
    ##################
    noms_sans_performance=[]
    for valeur in dic.values():
        if valeur['performance']==None:
            noms_sans_performance.append(valeur['last_name'])
    Tri.tri_selection(noms_sans_performance,Tri.compare_chaine_lexicographique)
    for nom in noms_sans_performance:
        for cle,valeur in dic.items():
            if valeur['last_name']==nom:
                dictionnaire[cle]=valeur
    ##################
    for valeur in dictionnaire.values():
        if valeur['performance'] !=None:
            valeur['performance']=Time.to_string(valeur['performance'])
    ##################            
    return dictionnaire    
##################################À faire n°10##############################################    
def print_results(dic):
    """
    affiche les résultats
    >>> print_results(sort_competitors_by_performance_methode2(set_performances_time(read_competitors("data/small_inscrits.csv"),read_performances('data/small_performances.csv'))))
     [7]: Archard Rivard (M - 10/6/1950)=>  0h 46mn 31s
     [8]: Cheney Chassé (M - 21/3/1949)=>  0h 48mn 10s
     [4]: Saville Marier (M - 19/11/1969)=>  0h 56mn 29s
     [5]: Namo Lereau (M - 26/3/1980)=>  1h 6mn 20s
     [10]: Sidney Charest (M - 5/3/1981)=>  1h 6mn 38s
     [1]: Sidney Robert (M - 21/7/1970)=>  1h 8mn 55s
     [6]: Romaine Hughes (F - 17/10/1943)=>  1h 17mn 8s
     [3]: Vincent Riquier (M - 16/9/1980)=>  1h 21mn 23s
     [9]: Avelaine CinqMars (F - 14/2/1983)=> None
     [2]: Paien Gilbert (M - 26/11/1953)=> None
     """
    for cle,valeur in dic.items():
        txt=" [{num}]: {Prenom} {Nom} ({Sexe} - {Date_naissance})=> {Perf}"
        print(txt.format(num=cle,Nom=valeur['last_name'],Prenom=valeur['first_name'],Sexe=valeur['sex'],Date_naissance=valeur['birth_date'],Perf=valeur['performance']))
##################################À faire n°11##############################################
def save_results(dic,nom):
    f=open(nom,"w")
    writer = csv.writer(f)
    descripteurs=["Num_dossard","Prénom","Nom","Performance"]
    writer.writerow(descripteurs)
    for valeur in dic.values():
        donnee=[valeur['bib_num'],valeur['first_name'],valeur['last_name'],valeur['performance']]
        writer.writerow(donnee)
    f.close()
##################################À faire n°12##############################################     
def is_sexe_feminin(competitor):
    """
    Renvoie True si le competitor est de sexe féminin
    param : competitor : csv
    return : bool
    >>> is_sexe_feminin({'bib_num': 6, 'first_name': 'Romaine', 'last_name': 'Hughes', 'sex': 'F', 'birth_date': '17/10/1943', 'performance': None})
    True
    """
    return competitor['sex']=='F'
    
def select_competitor(dic,predicat):
    """
    Renvoie des compétiteurs en fonction d'un prédicat
    param : dic : dict
    param : predicat : fonction définie
    return : list
    >>> select_competitor(read_competitors('data/small_inscrits.csv'),is_sexe_feminin)
    [{'bib_num': 6, 'first_name': 'Romaine', 'last_name': 'Hughes', 'sex': 'F', 'birth_date': '17/10/1943', 'performance': None}, {'bib_num': 9, 'first_name': 'Avelaine', 'last_name': 'CinqMars', 'sex': 'F', 'birth_date': '14/2/1983', 'performance': None}]
    """        
    selection=[]
    for valeur in dic.values():
        if predicat(valeur):
            selection.append(valeur)
    return selection
##################################À faire n°13##############################################

def conversion(date_naissance):
    """
    Convertit la date de naissance en année
    param : date_naissance
    return : float
    >>> conversion('14/2/1983')
    1983.2050228310502
    """
    resultat=int(date_naissance.split("/")[2])+int(date_naissance.split("/")[1])/12+int(date_naissance.split("/")[0])/365
    return resultat

def is_plus_age(competitor1,competitor2):
    """
    Renvoie un nombre négatif si age(competitor1)<age(competitor2)
    param : competitor1 : dict
    param : competitor2 : dict
    return : float
    >>> is_plus_age({'bib_num': 7, 'first_name': 'Archard', 'last_name': 'Rivard', 'sex': 'M', 'birth_date': '10/6/1950', 'performance': ' 0h 46mn 31s'},{'bib_num': 2, 'first_name': 'Paien', 'last_name': 'Gilbert', 'sex': 'M', 'birth_date': '26/11/1953', 'performance': None})
    -3.460502283105143
    """
    return conversion(competitor1['birth_date'])-conversion(competitor2['birth_date'])

def compare_entier_croissant(a, b):
    """
    :param a: (int) un entier
    :param b: (int) un entier
    :return: (int)  
             * >0  si a est supérieur à b
             * 0 si a est égal à b
             * <0 si a est inférieur à b
    :CU: aucune
    :Exemples:

    >>> compare_entier_croissant(1, 3) < 0
    True
    """
    return a-b

def selection_min(dic,i,comp):
    """
    Renvoie l'indice du minimum situé à partir de l'indice i
    param : dic ou list
    param : i : int
    param : comp : fonction
#    >>> selection_min([4,9,2,7],1,compare_entier_croissant)
#    2
    """
    i_min=i
    for j in range(i,len(dic)+1):
        if comp(dic[j],dic[i_min])<0:
            i_min=j
    return i_min

def new_select_competitor_by_birth_year(dic,comp):
    """
    Renvoie le dictionnaire avec un classement des compétiteurs du plus jeune au plus vieux
    param : dic : dict
    param : comp : fonction
    return : dict
    >>> new_select_competitor_by_birth_year(read_competitors('data/small_inscrits.csv'),is_plus_age)
    {1: {'bib_num': 6, 'first_name': 'Romaine', 'last_name': 'Hughes', 'sex': 'F', 'birth_date': '17/10/1943', 'performance': None}, 2: {'bib_num': 8, 'first_name': 'Cheney', 'last_name': 'Chassé', 'sex': 'M', 'birth_date': '21/3/1949', 'performance': None}, 3: {'bib_num': 7, 'first_name': 'Archard', 'last_name': 'Rivard', 'sex': 'M', 'birth_date': '10/6/1950', 'performance': None}, 4: {'bib_num': 2, 'first_name': 'Paien', 'last_name': 'Gilbert', 'sex': 'M', 'birth_date': '26/11/1953', 'performance': None}, 5: {'bib_num': 4, 'first_name': 'Saville', 'last_name': 'Marier', 'sex': 'M', 'birth_date': '19/11/1969', 'performance': None}, 6: {'bib_num': 1, 'first_name': 'Sidney', 'last_name': 'Robert', 'sex': 'M', 'birth_date': '21/7/1970', 'performance': None}, 7: {'bib_num': 5, 'first_name': 'Namo', 'last_name': 'Lereau', 'sex': 'M', 'birth_date': '26/3/1980', 'performance': None}, 8: {'bib_num': 3, 'first_name': 'Vincent', 'last_name': 'Riquier', 'sex': 'M', 'birth_date': '16/9/1980', 'performance': None}, 9: {'bib_num': 10, 'first_name': 'Sidney', 'last_name': 'Charest', 'sex': 'M', 'birth_date': '5/3/1981', 'performance': None}, 10: {'bib_num': 9, 'first_name': 'Avelaine', 'last_name': 'CinqMars', 'sex': 'F', 'birth_date': '14/2/1983', 'performance': None}}    
    """
    for i in dic.keys():
        j=selection_min(dic,i,comp)
        dic[i],dic[j]=dic[j],dic[i]
    return dic

##################################À faire n°14##############################################

def is_plus_avance_ordre_alpha(competitor1,competitor2):
    """
    Renvoie la comparaison des noms de famille par rapport à l'ordre alphabétique
    param : competitor1 : dict
    param : competitor2 : dict
    return : int
    >>> is_plus_avance_ordre_alpha({'bib_num': 2, 'first_name': 'Paien', 'last_name': 'Gilbert', 'sex': 'M', 'birth_date': '26/11/1953', 'performance': None},{'bib_num': 3, 'first_name': 'Vincent', 'last_name': 'Riquier', 'sex': 'M', 'birth_date': '16/9/1980', 'performance': ' 1h 21mn 23s'})
    -1    
    """
    return Tri.compare_chaine_lexicographique(competitor1['last_name'], competitor2['last_name'])


def new_select_competitor_by_name(dic,comp):
    """
    Renvoie le dictionnaire avec un classement des compétiteurs du plus jeune au plus vieux
    param : dic : dict
    param : comp : fonction
    return : dict
    >>> new_select_competitor_by_name(read_competitors('data/small_inscrits.csv'),is_plus_avance_ordre_alpha)
    {1: {'bib_num': 10, 'first_name': 'Sidney', 'last_name': 'Charest', 'sex': 'M', 'birth_date': '5/3/1981', 'performance': None}, 2: {'bib_num': 8, 'first_name': 'Cheney', 'last_name': 'Chassé', 'sex': 'M', 'birth_date': '21/3/1949', 'performance': None}, 3: {'bib_num': 9, 'first_name': 'Avelaine', 'last_name': 'CinqMars', 'sex': 'F', 'birth_date': '14/2/1983', 'performance': None}, 4: {'bib_num': 2, 'first_name': 'Paien', 'last_name': 'Gilbert', 'sex': 'M', 'birth_date': '26/11/1953', 'performance': None}, 5: {'bib_num': 6, 'first_name': 'Romaine', 'last_name': 'Hughes', 'sex': 'F', 'birth_date': '17/10/1943', 'performance': None}, 6: {'bib_num': 5, 'first_name': 'Namo', 'last_name': 'Lereau', 'sex': 'M', 'birth_date': '26/3/1980', 'performance': None}, 7: {'bib_num': 4, 'first_name': 'Saville', 'last_name': 'Marier', 'sex': 'M', 'birth_date': '19/11/1969', 'performance': None}, 8: {'bib_num': 3, 'first_name': 'Vincent', 'last_name': 'Riquier', 'sex': 'M', 'birth_date': '16/9/1980', 'performance': None}, 9: {'bib_num': 7, 'first_name': 'Archard', 'last_name': 'Rivard', 'sex': 'M', 'birth_date': '10/6/1950', 'performance': None}, 10: {'bib_num': 1, 'first_name': 'Sidney', 'last_name': 'Robert', 'sex': 'M', 'birth_date': '21/7/1970', 'performance': None}}
    """
    for i in dic.keys():
        j=selection_min(dic,i,comp)
        dic[i],dic[j]=dic[j],dic[i]
    return dic    
################################################################################
if __name__ == '__main__':
    import doctest
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS, verbose=True)