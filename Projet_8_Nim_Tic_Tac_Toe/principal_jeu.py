# coding: UTF-8

import jeu_nim  #importation des fonctions du jeu Nim

import jeu_tic_tac_toe

def aff_mess_vainqueur(valeur_joueur,per_gag):
    """
    : affichage du gagnant
    : param : bool(valeur_joueur)  identification du joueur (True:I;False:II)
    : param : bool(per_gag)  identification gagné ou égalité (True:gagné;False:égalité)
    : return : None
    Exemple:
    >>> aff_mess_vainqueur(True,False)
    Le joueur I a gagné
    """

    if valeur_joueur:
        joueur='I'
    else:
        joueur='II'
        
    if per_gag:
        print('Egalité !!!!')
    else:
        if valeur_joueur:
            #gagné
            print('Le joueur {} a gagné'.format(joueur))
        else:
            #perdu
            print('Le joueur {} a gagné'.format(joueur))

    return None

param_jeu = jeu_tic_tac_toe.situation_init()    #création de la situation courante initiale

valeur_joueur=False #Détermination du premier joueur courant

jeu_tic_tac_toe.aff_evolution_jeu(param_jeu)    #Affichage

fini=False  #Initialisation de la situation du jeu
while not fini: # Début de la partie 3 (si le jeu n'est pas fini) du déroulement des jeux à deux joueurs

    valeur_joueur= not valeur_joueur
    choix_joueur=jeu_tic_tac_toe.choix_joueur(valeur_joueur,param_jeu)
    param_jeu=jeu_tic_tac_toe.evolution_jeu(valeur_joueur,param_jeu,choix_joueur)
    jeu_tic_tac_toe.aff_evolution_jeu(param_jeu)    
    fini,per_gag=jeu_tic_tac_toe.etat_final(param_jeu)

aff_mess_vainqueur(valeur_joueur,per_gag)   #Partie 4 jeu fini et affichage du résultat.
