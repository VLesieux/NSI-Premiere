##########################################################################################################
from tkinter import*
fenetre=Tk()
canvas1=Canvas(fenetre,width=400,height=40)
canvas1.grid(row=1, column=0)

choix_colonne=None

fini=False

class Bouton(object):
    def __init__(self,canvas,x,y,number):
        self.x=x
        self.y=y
        self.number=number
        self.canvas1=canvas1    
    def represente(self):
        self.canvas1.create_rectangle(self.x-20, self.y-20,self.x,self.y)
        self.canvas1.create_text(self.x-10, self.y-10,text=self.number)

boutons=[(i,(40*i+50,40)) for i in range(1,8)]

Boutons=[]

for i in range(len(boutons)):
    Boutons.append(Bouton(canvas1,boutons[i][1][0],boutons[i][1][1],i+1))
    Boutons[i].represente()
    
limites=[(i,(40*i+30,40*i+50)) for i in range(1,8)]

#def jouer(choix_colonne):
#    global config
#    global joueur_courant
#    if test_valide(config,choix_colonne,JOUEUR_NOIR):            
#        config = incrementer_config(config,choix_colonne,JOUEUR_NOIR)
#        afficher_config(config)
#    if est_jeu_fini(config):
#        afficher_fin(config,joueur_courant)
#    joueur_courant = incrementer_joueur(joueur_courant)
#    config = incrementer_config(config,meilleur_coup,JOUEUR_BLANC)
#    afficher_config(config)

def aff_mess_vainqueur(plateau):
    """
    : affichage du gagnant
    : param : bool(valeur_joueur)  identification du joueur (True:I;False:II)
    : param : bool(per_gag)  identification gagné ou égalité (True:gagné;False:égalité)
    : return : None
    """
    if etat_final(plateau):
        if test_ligne(plateau,True) or test_colonne(plateau,True) or test_diagonale_up(plateau,True) or test_diagonale_down(plateau,True):
            print('Le joueur I a gagné')
        elif test_ligne(plateau,False) or test_colonne(plateau,False) or test_diagonale_up(plateau,False) or test_diagonale_down(plateau,False):
            print('Le joueur II a gagné')
        else:
            print('Egalité')


def detec_clic(event):
    global valeur_joueur
    valeur_joueur=not(valeur_joueur)
    global choix_colonne
    global config
    global fini
    x , y = event.x, event.y
    if y>=20 and y<=40 and not fini:
        for valeurs in range(len(limites)):
            if x>=limites[valeurs][1][0] and x<=limites[valeurs][1][1]:                
                choix_colonne=limites[valeurs][0]
                evolution_jeu(valeur_joueur,config,choix_colonne)
                afficher_config(config)
                aff_evolution_jeu(config)
    fini=etat_final(config)
    if fini:
        aff_mess_vainqueur(config)
   
canvas1.bind("<Button-1>", detec_clic)

canvas2=Canvas(fenetre,width=400,height=500,bg="green")
canvas2.grid(row=2, column=0)

class Jeton(object):
    def __init__(self,canvas,x,y,couleur):
        self.x=x
        self.y=y
        self.couleur=couleur
        self.canvas2=canvas2
    def represente(self):
        self.canvas2.create_oval(self.x-15,self.y-15,self.x+15,self.y+15,width=1,fill=self.couleur)


Jetons=[]

def afficher_config(config):
    for ligne in range(6):
        for colonne in range(7):
            if config[ligne][colonne]==0:
                Jetons.append(Jeton(canvas2,40*colonne+80,35*ligne+35,"white"))
            elif config[ligne][colonne]==1:
                Jetons.append(Jeton(canvas2,40*colonne+80,35*ligne+35,"red"))
            else:
                Jetons.append(Jeton(canvas2,40*colonne+80,35*ligne+35,"blue"))                
    for i in range(len(Jetons)):
        Jetons[i].represente() 

##########################################################################################################
valeur_joueur=False

def situation_init():
    """
    : création de la situation initiale du jeu
    : renvoie le plateau initiale
    : param : Rien
    Exemple:
    """
    plateau=[
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    ]
    return plateau


def aff_evolution_jeu(plateau):
    """
    : permet d'afficher le nombre d'allumettes restantes
    : param : int(param_jeu) nombres d'allumettes
    : return : None
    Exemple:
    >>> config = [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 1, 0, 0], [0, 1, 2, 2, 2, 2, 0]]
    >>> aff_evolution_jeu(config)
    1 2 3 4 5 6 7
    · · · · · · · 
    · · · · · · · 
    · · · · · · · 
    · · · · · · · 
    · ■ · · ■ · · 
    · ■ □ □ □ □ · 
    """
    print("1 2 3 4 5 6 7")
    numero=1
    for ligne in plateau:
        for element in ligne:
            if element==0:
                print('\u00B7',end=' ')
            if element==1:
                print( '■',end=' ')
            if element==2:
                print( '□',end=' ')
        print()

def test_jeu_rempli(plateau):
    """
    >>> test_jeu_rempli(situation_init())
    False
    """
    for i in range(8):
        for j in range(8):
            if plateau[i][j]==0:
                return False
    return True

def choix_joueur(valeur_joueur,plateau):
    """
    : Demande au joueur d'effectuer un choix d'allumettes à enlever (2 ou 3)
    : param : bool(valeur_joueur) identification du joueur (True:I;False:II)
    : param : int(param_jeu) nombres d'allumettes
    : return : int(choix) choix du joueur
    Remarque: Ne pas faire de doctest sur des fonctions d'entrées /sorties
    """
    if valeur_joueur:
        joueur='I blanc'
    else:
        joueur='II noir'
    #init choix jeu
    choix=False
    #Les joueurs doivent ramasser tour à tour 2 ou 3 allumettes
    while choix !=True:
        question= input('JOUEUR {} : Choisir la position de votre pion : '.format(joueur))
        position= int(question[0])
        choix=test_validite_choix(valeur_joueur,position,plateau)
    return position

def evolution_jeu(valeur_joueur,plateau,choix_joueur):
    """
    : permet de faire évoluer le jeu
    : param : int(param_jeu) nombres d'allumettes
    : param : bool(valeur_joueur) identification du joueur (True:I;False:II)
    : return : int(param_jeux) le nombres d'allumettes restantes
    >>> jeu=situation_init()
    >>> aff_evolution_jeu(evolution_jeu(True,jeu,7))
    1 2 3 4 5 6 7
    · · · · · · · 
    · · · · · · · 
    · · · · · · · 
    · · · · · · · 
    · · · · · · · 
    · · · · · · □ 
    >>> config = [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 1, 0, 0], [0, 1, 2, 2, 2, 2, 0]]
    >>> aff_evolution_jeu(config)
    1 2 3 4 5 6 7
    · · · · · · · 
    · · · · · · · 
    · · · · · · · 
    · · · · · · · 
    · ■ · · ■ · · 
    · ■ □ □ □ □ · 
    >>> aff_evolution_jeu(evolution_jeu(False,config,2))
    1 2 3 4 5 6 7
    · · · · · · · 
    · · · · · · · 
    · · · · · · · 
    · ■ · · · · · 
    · ■ · · ■ · · 
    · ■ □ □ □ □ · 
    >>> aff_evolution_jeu(evolution_jeu(True,config,1))
    1 2 3 4 5 6 7
    · · · · · · · 
    · · · · · · · 
    · · · · · · · 
    · ■ · · · · · 
    · ■ · · ■ · · 
    □ ■ □ □ □ □ · 
        
    """
    dernier=0
    for i in range(5,-1,-1):
        if plateau[i][choix_joueur-1]==0:
            dernier=i
            break
    if valeur_joueur==True:
        pion=2
        plateau[dernier][choix_joueur-1]=2
    else:
        pion=1
        plateau[dernier][choix_joueur-1]=1  
    return plateau
# 
# 
def test_validite_choix(valeur_joueur,le_choix,plateau):
    """
    : test de la validité de la position
    : param : bool(valeur_joueur) identification du joueur (True:I;False:II)
    : param le_choix: tuple
    : param plateau : la grille de jeu
    : return : le choix validé ou non du joueur
    """
    if not (le_choix in [1,2,3,4,5,6,7]):
        return False
    else:
        return True
           

def action_joueur(valeur_joueur,param_jeu):
    """
    : permet de connaitre le nombre d'allumettes à enlever
    : param : bool(valeur_joueur) identification du joueur (True:I;False:II)
    : return : int(choix) choix du joueur
    """
    lechoix=choix_joueur(valeur_joueur,param_jeu)
    return lechoix

def test_ligne(plateau,joueur):
    """
    Renvoie True si alignement selon colonne des jetons de joueur sinon False
    >>> config = [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 1, 0, 0], [0, 1, 2, 2, 2, 2, 0]]
    >>> aff_evolution_jeu(config)
    1 2 3 4 5 6 7
    · · · · · · · 
    · · · · · · · 
    · · · · · · · 
    · · · · · · · 
    · ■ · · ■ · · 
    · ■ □ □ □ □ · 
    >>> test_ligne(config,True)
    True
    >>> test_ligne(config,False)
    False
    """
    if joueur:
        pion=2
    else:
        pion=1   
    for i in range(6):
        for j in range(4):
            if plateau[i][j]==pion and plateau[i][j]==plateau[i][j+1] and plateau[i][j+1]==plateau[i][j+2] and plateau[i][j+2]==plateau[i][j+3]:
                return True
    return False
    
def test_colonne(plateau,joueur):
    """
    Renvoie True si alignement selon colonne des jetons de joueur sinon False
    >>> config = [[0, 1, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0], [0, 2, 0, 0, 2, 0, 0], [0, 2, 0, 0, 2, 0, 0]]
    >>> aff_evolution_jeu(config)
    1 2 3 4 5 6 7
    · ■ · · · · · 
    · ■ · · · · · 
    · ■ · · · · · 
    · ■ · · · · · 
    · □ · · □ · · 
    · □ · · □ · · 
    >>> test_colonne(config,False)
    True
    >>> test_colonne(config,True)
    False
    """
    if joueur:
        pion=2
    else:
        pion=1   
    for i in range(3):
        for j in range(7):
            if plateau[i][j]==pion and plateau[i][j]==plateau[i+1][j] and plateau[i+1][j]==plateau[i+2][j] and plateau[i+2][j]==plateau[i+3][j]:
                return True
    return False

def test_diagonale_up(plateau,joueur):
    """
    Renvoie True si alignement selon diagonale montante des jetons de joueur sinon False
    >>> config = [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 1, 0], [0, 0, 0, 1, 1, 2, 0], [0, 1, 1, 2, 1, 1, 0], [0, 1, 2, 2, 2, 1, 0]]
    >>> aff_evolution_jeu(config)
    1 2 3 4 5 6 7
    · · · · · · · 
    · · · · · · · 
    · · · · ■ ■ · 
    · · · ■ ■ □ · 
    · ■ ■ □ ■ ■ · 
    · ■ □ □ □ ■ · 
    >>> test_diagonale_up(config,False)
    True
    >>> test_diagonale_up(config,True)
    False
    """
    if joueur:
        pion=2
    else:
        pion=1   
    for i in range(6):
        for j in range(7):
            try:
                if plateau[i][j]==pion and plateau[i][j]==plateau[i-1][j+1] and plateau[i-1][j+1]==plateau[i-2][j+2] and plateau[i-2][j+2]==plateau[i-3][j+3]:
                    return True
            except IndexError:
                pass
    return False

def test_diagonale_down(plateau,joueur):
    """
    Renvoie True si alignement selon diagonale descendante des jetons de joueur sinon False
    >>> config = [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 1, 1, 0], [0, 0, 2, 1, 1, 2, 0], [0, 1, 1, 2, 1, 1, 0], [0, 1, 2, 2, 2, 1, 0]]
    >>> aff_evolution_jeu(config)
    1 2 3 4 5 6 7
    · · · · · · · 
    · · · · · · · 
    · · ■ · ■ ■ · 
    · · □ ■ ■ □ · 
    · ■ ■ □ ■ ■ · 
    · ■ □ □ □ ■ · 
    >>> test_diagonale_down(config,False)
    True
    >>> test_diagonale_down(config,True)
    False
    """
    if joueur:
        pion=2
    else:
        pion=1   
    for i in range(6):
        for j in range(7):
            try:
                if plateau[i][j]==pion and plateau[i][j]==plateau[i+1][j+1] and plateau[i+1][j+1]==plateau[i+2][j+2] and plateau[i+2][j+2]==plateau[i+3][j+3]:
                    return True
            except IndexError:
                pass
    return False    

def etat_final(plateau):
    """
    """
    if test_jeu_rempli(plateau):
        fini=True
    else:
        fini=False
    if test_ligne(plateau,True) or test_ligne(plateau,False) or test_colonne(plateau,True) or test_colonne(plateau,False) or test_diagonale_up(plateau,True) or test_diagonale_up(plateau,False) or test_diagonale_down(plateau,True) or test_diagonale_down(plateau,False):
        fini=True
    return fini

#################################################################################################
config = situation_init()
afficher_config(config)

fenetre.mainloop()

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)