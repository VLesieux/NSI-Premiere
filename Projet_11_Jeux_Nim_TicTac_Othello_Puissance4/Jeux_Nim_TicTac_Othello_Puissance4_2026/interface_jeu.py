# coding: UTF-8
import jeu_nim #importation des fonctions du jeu Nim
import jeu_tic_tac_toe #importation des fonctions du jeu tic tac toe
import jeu_othello

import random


choix_du_jeu=int(input('Saisir le jeu : 1.jeu nim  ou  2. jeu tic tac toe ou 3. jeu othello ou 4. jeu puissance 4 : '))
#si 1 importer fichier fonctions voyelle
if choix_du_jeu==1:
    module = 'jeu_nim'
elif choix_du_jeu==2:
    module='jeu_tic_tac_toe'
elif choix_du_jeu==3:
    module='jeu_othello'
elif choix_du_jeu==4:
    module='jeu_puissance4'
    
type_jeu=int(input('jeu contre humain : 1, ou contre machine hasard : 2, ou contre machine intelligente : 3 : '))

    
jeu=__import__(module)


def coup_machine_aleatoire(param_jeu):
    coups = jeu.coups_possibles(param_jeu)
    return random.choice(coups)


def coup_machine_simple(param_jeu, valeur_joueur):
    """
    La machine joue un coup gagnant s'il existe,
    sinon elle joue au hasard.
    """
    coups = jeu.coups_possibles(param_jeu)
    
#1.Est-ce que je peux gagner maintenant ?
    
    for ligne, colonne in coups:
        # on copie le plateau
        copie = [row[:] for row in param_jeu]

        # on simule le coup
        copie= jeu.evolution_jeu(valeur_joueur,copie,(ligne,colonne))

        # on regarde si ça gagne
        per_gag, fini = jeu.etat_final(copie)

        if per_gag:
            return (ligne, colonne)

#2. Si je ne fais rien… est-ce que l’adversaire gagne au prochain coup ?
        
    adversaire=not valeur_joueur
    for ligne, colonne in coups:
        # on copie le plateau
        copie = [row[:] for row in param_jeu]

        # on simule le coup
        copie= jeu.evolution_jeu(adversaire,copie,(ligne,colonne))

        # on regarde si ça gagne
        per_gag, fini = jeu.etat_final(copie)

        if per_gag:
            return (ligne, colonne) 

    # 3. prendre le centre si possible
    if (1, 1) in coups:
        return (1, 1)

    # 4. prendre un coin si possible
    coins = [(0,0), (0,2), (2,0), (2,2)]
    for coin in coins:
        if coin in coups:
            return coin

    # 5. sinon hasard
    return random.choice(coups)

def minimax(param_jeu, valeur_joueur):
    """
    Renvoie la valeur d'une position.

    valeur_joueur = False : c'est à la machine de jouer, elle maximise.
    valeur_joueur = True  : c'est à l'humain de jouer, il minimise.
    """
    per_gag, fini = jeu.etat_final(param_jeu)

    if fini:
        return jeu.evaluation(param_jeu)

    coups = jeu.coups_possibles(param_jeu)

    if valeur_joueur == False:
        meilleur_score = -1000

        for coup in coups:
            copie = [row[:] for row in param_jeu]
            copie = jeu.evolution_jeu(False, copie, coup)
            score = minimax(copie, True)

            if score > meilleur_score:
                meilleur_score = score

        return meilleur_score

    else:
        meilleur_score = 1000

        for coup in coups:
            copie = [row[:] for row in param_jeu]
            copie = jeu.evolution_jeu(True, copie, coup)
            score = minimax(copie, False)

            if score < meilleur_score:
                meilleur_score = score

        return meilleur_score
    
    
def minimax_profondeur(param_jeu, valeur_joueur, profondeur):
    fini, per_gag = jeu.etat_final(param_jeu)

    if fini or profondeur == 0:
        return jeu.evaluation(param_jeu)

    coups = jeu.coups_possibles(param_jeu)

    if valeur_joueur == False:  # machine : elle maximise
        meilleur_score = -1000

        for coup in coups:
            copie = [row[:] for row in param_jeu]
            copie = jeu.evolution_jeu(False, copie, coup)

            score = minimax_profondeur(copie, True, profondeur - 1)

            if score > meilleur_score:
                meilleur_score = score

        return meilleur_score

    else:  # humain : il minimise
        meilleur_score = 1000

        for coup in coups:
            copie = [row[:] for row in param_jeu]
            copie = jeu.evolution_jeu(True, copie, coup)

            score = minimax_profondeur(copie, False, profondeur - 1)

            if score < meilleur_score:
                meilleur_score = score

        return meilleur_score

    
def coup_machine_minimax(param_jeu):
    coups = jeu.coups_possibles(param_jeu)

    meilleur_score = -1000
    meilleur_coup = None

    for coup in coups:
        copie = [row[:] for row in param_jeu]
        copie = jeu.evolution_jeu(False, copie, coup)
        if choix_du_jeu==2:#morpion
            score = minimax(copie, True)       
        if choix_du_jeu==4:#puissance 4
            score = minimax_profondeur(copie, True,3)
        
        

        if score > meilleur_score:
            meilleur_score = score
            meilleur_coup = coup

    return meilleur_coup

def aff_mess_vainqueur(valeur_joueur,per_gag):
    """
    : affichage du gagnant
    : param : bool(valeur_joueur)  identification du joueur (True:I;False:II)
    : param : bool(per_gag)  identification gagné ou égalité (True:gagné;False:égalité)
    : return : None
    Exemple:
    >>> aff_mess_vainqueur(True,True)
    Le joueur I a gagné
    >>> aff_mess_vainqueur(False,True)
    Le joueur II a gagné
    >>> aff_mess_vainqueur(False,False)
    Egalité !!!!
    """
    if valeur_joueur:
        joueur='I'
    else:
        joueur='II'      
        
    if per_gag==False:
        print('Egalité !!!!')
    else:
        if valeur_joueur:
            #gagné
            print('Le joueur {} a gagné'.format(joueur))
        else:
            #perdu
            print('Le joueur {} a gagné'.format(joueur))

    return None

param_jeu = jeu.situation_init()    #création de la situation courante initiale

valeur_joueur=True #Détermination du premier joueur courant

jeu.aff_evolution_jeu(param_jeu)    #Affichage de l'état du jeu

fini=False  #Initialisation de la situation du jeu

while not fini: # Voir le point 3 de l'introduction : si le jeu n'est pas fini

################################################################################
    if type_jeu==1:
        choix=jeu.action_joueur(valeur_joueur,param_jeu)
    elif type_jeu==2:
        if valeur_joueur:
            choix=jeu.action_joueur(valeur_joueur,param_jeu)
        else:
#             choix=coup_machine_aleatoire(param_jeu)
            choix = coup_machine_minimax(param_jeu)

    else:
        if valeur_joueur:
            choix=jeu.action_joueur(valeur_joueur,param_jeu)
        else:
#             choix=coup_machine_simple(param_jeu, valeur_joueur)
            choix = coup_machine_minimax(param_jeu)
            print()        
            
        
    param_jeu=jeu.evolution_jeu(valeur_joueur,param_jeu,choix)
    jeu.aff_evolution_jeu(param_jeu)
    per_gag,fini=jeu.etat_final(param_jeu)
    valeur_joueur=not(valeur_joueur)

################################################################################

aff_mess_vainqueur(not(valeur_joueur),per_gag)   # jeu fini et affichage du résultat.
# cette ligne de code sera réalisée lorsque la partie sera finie

