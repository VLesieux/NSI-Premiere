# coding: UTF-8

import othello_new_2023 as jeu  #importation des fonctions du jeu Nim 

def aff_mess_vainqueur(plateau):
    """
    : affichage du gagnant
    : param : bool(valeur_joueur)  identification du joueur (True:I;False:II)
    : param : bool(per_gag)  identification gagné ou égalité (True:gagné;False:égalité)
    : return : None
    Exemple:
    >>> aff_mess_vainqueur(True,False)
    Le joueur I a gagné
    """
    if jeu.compte_points(plateau)[0]==jeu.compte_points(plateau)[1]:
        print('Egalité !!!!')
    elif jeu.compte_points(plateau)[0]>jeu.compte_points(plateau)[1]:
        print('Le joueur II a gagné')
    else:
        print('Le joueur I a gagné')


param_jeu = jeu.situation_init()    #création de la situation courante initiale

valeur_joueur=False #Détermination du premier joueur courant

jeu.aff_evolution_jeu(param_jeu)    #Affichage de l'état du jeu

fini=False  #Initialisation de la situation du jeu

while not fini: # Voir le point 3 de l'introduction : si le jeu n'est pas fini
    le_choix=jeu.action_joueur(valeur_joueur,param_jeu)
    param_jeu=jeu.evolution_jeu(valeur_joueur,param_jeu,le_choix)     
    jeu.aff_evolution_jeu(param_jeu)
    fini=jeu.etat_final(param_jeu)
    valeur_joueur=not(valeur_joueur)        
    
aff_mess_vainqueur(param_jeu)   # jeu fini et affichage du résultat.
# cette ligne de code sera réalisée lorsque la partie sera finie

