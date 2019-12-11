```python

import src.Competitor as Competitor
import src.Time as Time

#Les deux modules Competitor et Time sont supposés être placés dans le dossier src

###################################Faire n°1#######################################

def read_competitors(text):
    """
    lit un fichier csv et retourne un dictionnaire dont les clés sont les numéros de brassard
    et les valeurs les tuples nommés contenant les informations sur les compétiteurs
    """
    try: 
        f=open(text,"r")
        champs=f.readline().rstrip('\n').split(";")
        lignes=f.readlines()
        dictionnaire={}
        brassard=0
        for ligne in lignes:
            brassard+=1
            liste=ligne.rstrip().split(';')
            dictionnaire[brassard]=Competitor.create(liste[0],liste[1],liste[2],liste[3],brassard)
        f.close()
        return(dictionnaire)
    except FileNotFoundError:
        print("Votre fichier n'est pas un csv lisible")
        
#read_competitors("data/small_inscrits.csv")


###################################Faire n°2#######################################

def affichage(competiteurs):
    """
    réalise un affichage des compétiteurs
    """
    for i in competiteurs:
        print(Competitor.to_string(competiteurs[i]))

#affichage(read_competitors("data/small_inscrits.csv"))



###################################Faire n°3#######################################

def select_competitor_by_bib(competiteurs,numero):
    try:
        return competiteurs[numero]
    except KeyError:
        return None
        
#select_competitor_by_bib(read_competitors("data/small_inscrits.csv"),8)   



###################################Faire n°4#######################################

def select_competitor_by_birth_year(competiteurs,age):
    liste=[]
    for i in competiteurs:
        if competiteurs[i]['birth_date'].endswith(str(age)):
            liste.append(competiteurs[i])
    return liste

#select_competitor_by_birth_year(read_competitors("data/small_inscrits.csv"),1980)

###################################Faire n°5#######################################

def select_competitor_by_name(competiteurs,nom):
    liste=[]
    for i in competiteurs:
        if nom in competiteurs[i]['last_name']:
            liste.append(competiteurs[i])
    return liste

#select_competitor_by_name(read_competitors("data/small_inscrits.csv"),"Ri")

###################################Faire n°6#######################################

def read_performances(text):
    """
    lit un fichier csv et retourne un dictionnaire dont les clés sont les numéros de brassard
    et les valeurs les tuples contenant les performances des compétiteurs
    """
    try: 
        f=open(text,"r")
        champs=f.readline().rstrip('\n').split(";")
        lignes=f.readlines()
        dictionnaire={}
        for ligne in lignes:
            liste=ligne.rstrip().split(';')
            dictionnaire[int(liste[0])]=Time.create(int(liste[1]),int(liste[2]),int(liste[3]))
        f.close()
        return(dictionnaire)
    except FileNotFoundError:
        print("Votre fichier n'est pas un csv lisible")
        
#read_performances("data/small_performances.csv")


###################################Faire n°7#######################################

def set_performances(dic1,dic2):
    for i in dic2:
        try :
            dic2[i]['performance']=Time.to_string(dic1[i])
        except KeyError:
            resultat=None
    return dic2

#set_performances(read_performances('data/small_performances.csv'),read_competitors("data/small_inscrits.csv"))


###################################Faire n°8#######################################

def sort_competitors_by_lastname(dic):
    new=dict([])
    liste=[]
    for i in dic:
        liste.append(dic[i]['last_name'])
    Tri.tri_selection(liste,Tri.compare_chaine_lexicographique)
    for i in range(len(liste)):
        for j in dic:
            if dic[j]['last_name']==liste[i]:
                new[j]=dic[j]
    return new
        
#sort_competitors_by_lastname(set_performances(read_performances('mat_course_chicon/data/small_performances.csv'),read_competitors('mat_course_chicon/data/small_inscrits.csv')))

###################################Faire n°9#######################################


######Méthode n°1################################

def sort_competitors_by_performance_methode1(dic):
    new=dict([])
    liste=[]
    for i in dic:
        if not (dic[i]['performance'] is None):
            liste.append(conversion_en_seconde(dic[i]['performance']))
        Tri.tri_selection(liste,Tri.compare_entier_croissant)
    for i in range(len(liste)):
        for j in dic:
            if conversion_en_seconde(dic[j]['performance'])==liste[i]:
                new[j]=dic[j]
                
    liste_sans_performance=[]
    for i in dic:
        if (dic[i]['performance'] is None):
            liste_sans_performance.append(dic[i]['last_name'])
    Tri.tri_selection(liste_sans_performance,Tri.compare_chaine_lexicographique)
    for i in range(len(liste_sans_performance)):
        for j in dic:
            if dic[j]['last_name']==liste_sans_performance[i]:
                new[j]=dic[j]                
    return new

#sort_competitors_by_performance_methode1(set_performances(read_performances('data/small_performances.csv'),read_competitors('data/small_inscrits.csv')))

######Méthode n°2################################

def sort_competitors_by_performance_methode2(dic1,dic2):
    new={}
    liste=[]
    for i in dic1:
        if not (dic1[i]['performance'] is None):
            liste.append(dic2[i])
        Tri.tri_selection(liste,Time.compare)
    for i in liste:
        for j in dic2:
            if dic2[j]==i:
                new[j]=dic1[j]
    
    liste_sans_performance=[]
    for i in dic1:
        if (dic1[i]['performance'] is None):
            liste_sans_performance.append(dic1[i]['last_name'])
    Tri.tri_selection(liste_sans_performance,Tri.compare_chaine_lexicographique)
    for i in range(len(liste_sans_performance)):
        for j in dic1:
            if dic1[j]['last_name']==liste_sans_performance[i]:
                new[j]=dic1[j]  
    return new
            
#sort_competitors_by_performance(set_performances(read_performances('data/small_performances.csv'),read_performances("data/small_performances.csv")))

###################################Faire n°10#######################################

def print_results(dic):
    for i in dic:
        print("[{bib_num}]: {first_name} {last_name} ({sex} - {birth_date})    => {performance}".format(**dic[i]))

#print_results(sort_competitors_by_performance_methode2(set_performances(read_performances('data/small_performances.csv'),read_competitors('data/small_inscrits.csv')),read_performances("data/small_performances.csv")))
   
###################################Faire n°11#######################################

def save_results(dic,text):
    sortie = open(text, 'w')
    sortie.writelines('Num_dossard;Prénom;Nom;Performance\n')
    for i in dic:
        if not (dic[i]['performance'] is None):
            sortie.writelines(str(dic[i]['bib_num'])+";"+dic[i]['first_name']+";"+dic[i]['last_name']+";"+dic[i]['performance']+"\n")
    sortie.close()

#save_results(sort_competitors_by_performance_methode2(set_performances(read_performances('data/small_performances.csv'),read_competitors('data/small_inscrits.csv')),read_performances("data/small_performances.csv")),"record")

###################################Faire n°12#######################################

def is_sexe_feminin(competitor):
    if competitor['sex']=="F":
        return True
    
def select_competitor(dic,predicat):
    liste=[]
    for i in dic:
        if predicat(dic[i]):
            liste.append(dic[i])
    return liste

#select_competitor(read_competitors('data/small_inscrits.csv'),is_sexe_feminin)

###################################Faire n°13#######################################

def conversion(date_naissance):
    age=int(date_naissance.split("/")[2])+int(date_naissance.split("/")[1])/12+int(date_naissance.split("/")[0])/365
    return age

def is_plus_age(competitor1,competitor2):
    return conversion(competitor2['birth_date'])-conversion(competitor1['birth_date'])

def selection_min(dic,i,comp):
    i_min=i
    for j in range(i+1,len(dic)):
        if comp(dic[j],dic[i_min])<0:
            i_min=j
    return i_min

def new_select_competitor_by_birth_year(dic,comp):
    for i in range(1,len(dic)):
        j=selection_min(dic,i,comp)
        dic[i],dic[j]=dic[j],dic[i]
    return dic

#new_select_competitor_by_birth_year(read_competitors('data/small_inscrits.csv'),is_plus_age)


###################################Faire n°14#######################################

def is_plus_avance_ordre_alpha(competitor1,competitor2):
    return Tri.compare_chaine_lexicographique(competitor2['last_name'],competitor1['last_name'])
  
def new_select_competitor_by_name(dic,comp):
    for i in range(1,len(dic)):
        j=selection_min(dic,i,comp)
        dic[i],dic[j]=dic[j],dic[i]
    return dic

#new_select_competitor_by_birth_year(read_competitors('data/small_inscrits.csv'),is_plus_avance_ordre_alpha)
```
