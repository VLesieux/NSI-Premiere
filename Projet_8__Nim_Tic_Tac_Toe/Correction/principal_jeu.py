# coding: UTF-8

import jeu_tic_tac as jeu  #importation des fonctions du jeu Nim 
import jeu_nim as jeu

choix=int(input('Choisir le jeu : 1.jeu_nim  ou  2. jeu_tic_tac : '))

if choix==1:
    module = 'jeu_nim'
else:
    module='jeu_tic_tac'
    
jeu=__import__(module)

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

param_jeu = jeu.situation_init()    #création de la situation courante initiale

valeur_joueur=False #Détermination du premier joueur courant

jeu.aff_evolution_jeu(param_jeu)    #Affichage

fini=False  #Initialisation de la situation du jeu

while not fini:
    
    choix_joueur=jeu.action_joueur(valeur_joueur,param_jeu)
            
    if jeu.test_validite_choix(valeur_joueur,choix_joueur,param_jeu):
                
        param_jeu = jeu.evolution_jeu(valeur_joueur,param_jeu,choix_joueur)
        
        valeur_joueur=not(valeur_joueur)
        
        jeu.aff_evolution_jeu(param_jeu)
        
    fini,per_gag=jeu.etat_final(param_jeu)[0],jeu.etat_final(param_jeu)[1]    
    

aff_mess_vainqueur(not(valeur_joueur),per_gag)   # jeu fini et affichage du résultat.



