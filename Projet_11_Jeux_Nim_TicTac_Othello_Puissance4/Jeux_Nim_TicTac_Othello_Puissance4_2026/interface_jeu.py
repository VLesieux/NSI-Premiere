###########################################################################################################################
import random
choix_du_jeu=int(input('Saisir le jeu : [jeu nim : 1 |  jeu tic tac toe : 2 |  jeu othello :  3 | jeu puissance 4 : 4 ] : '))

if choix_du_jeu==1:
    module = 'jeu_nim'
elif choix_du_jeu==2:
    module='jeu_tic_tac_toe'
elif choix_du_jeu==3:
    module='jeu_othello'
elif choix_du_jeu==4:
    module='jeu_puissance4'
    
type_jeu=int(input('Saisir le type de jeu : [contre humain : 1 | contre machine simple : 2 | contre machine intelligente : 3 ] : '))
    
jeu=__import__(module)
#################################################################LES DIFFERENTS COUPS DE LA MACHINE##############################################################
def coup_machine_aleatoire(param_jeu):
    coups = jeu.coups_possibles(param_jeu)
    return random.choice(coups)
##########
def coup_machine_simple(param_jeu, valeur_joueur):#############pas de recherche avancée : la machine regarde si elle peut gagner immédiatement, ou se place là où l'adversaire peut gagner, ou hasard
    """
    La machine joue un coup gagnant s'il existe, sinon elle joue au hasard.
    """
    coups = jeu.coups_possibles(param_jeu)########les coups possibles en fonction du jeu
    
#1.Est-ce que je peux gagner maintenant ?
    
    for ligne, colonne in coups:######on fait le tour de ces coups possibles
        # on copie le plateau
        copie = [row[:] for row in param_jeu]

        # on simule le coup sur cette copie
        copie= jeu.evolution_jeu(valeur_joueur,copie,(ligne,colonne))

        # on regarde si ça gagne sur cette évolution du jeu
        per_gag, fini = jeu.etat_final(copie)

        if per_gag:
            return (ligne, colonne)######si le coup est gagnant, on le renvoie

#2. Si je ne fais rien… est-ce que l’adversaire gagne au prochain coup ?
        
    adversaire=not valeur_joueur#######la machine se met à la place de l'adversaire humain
    
    for ligne, colonne in coups:######on fait le tour de ces coups possibles
        # on copie le plateau
        copie = [row[:] for row in param_jeu]

        # on simule le coup sur cette copie
        copie= jeu.evolution_jeu(adversaire,copie,(ligne,colonne))

        # on regarde si ça gagne
        per_gag, fini = jeu.etat_final(copie)

        if per_gag:
            return (ligne, colonne) 
    ################################cas particulier du jeu_tic_tac_toe###################
        if choix_du_jeu==3:
    # 3. prendre le centre si possible
            if (1, 1) in coups:
                return (1, 1)
    # 4. prendre un coin si possible
            coins = [(0,0), (0,2), (2,0), (2,2)]
            for coin in coins:
                if coin in coups:
                    return coin
    ##############################
    # 5. sinon la machine joue au hasard
    return random.choice(coups)
################################################################L'ALGORITHME DU MINIMAX SANS PROFONDEUR#################################
##########utilisé dans le cas du jeu tic_tac_toe#############
def minimax(param_jeu, valeur_joueur):
    """
    Renvoie la valeur d'une position.
    valeur_joueur = False : c'est à la machine de jouer, elle maximise.
    valeur_joueur = True  : c'est à l'humain de jouer, il minimise.
    """
    per_gag, fini = jeu.etat_final(param_jeu)
    if fini:####c'est la condition qui permet de sortir de la fonction récursive
        return jeu.evaluation(param_jeu)
    
    coups = jeu.coups_possibles(param_jeu)

    if valeur_joueur == False:#########cas de la machine
        meilleur_score = -1000

        for coup in coups:
            copie = [row[:] for row in param_jeu]
            copie = jeu.evolution_jeu(False, copie, coup)
            score = minimax(copie, True)##############################minimax est une fonction récursive

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
################################################################L'ALGORITHME DU MINIMAX AVEC PROFONDEUR#################################
#########################utilisé dans le cas du puissance 4, ou du jeu Othello, la profondeur est choisie au départ, ici on prend 3###########
def minimax_profondeur(param_jeu, valeur_joueur, profondeur):
    """
    Envoie la valeur d'une position.
    """
    fini, per_gag = jeu.etat_final(param_jeu)

    if fini or profondeur == 0:#c'est la condition qui permet de sortir de la fonction récursive
        return jeu.evaluation(param_jeu)

    coups = jeu.coups_possibles(param_jeu)

    if valeur_joueur == False:  # machine : elle maximise
        meilleur_score = -1000

        for coup in coups:
            copie = [row[:] for row in param_jeu]
            copie = jeu.evolution_jeu(False, copie, coup)

            score = minimax_profondeur(copie, True, profondeur - 1)#la profondeur diminue d'une unité à chaque appel de la fonction minimax_profondeur

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
#########################################################################COUP DE LA MACHINE##################################################    
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
            score = minimax_profondeur(copie, True,3)#on choisit une profondeur de 3        

        if score > meilleur_score:####on cherche le meilleur coup qui donne le meilleur score
            meilleur_score = score
            meilleur_coup = coup

    return meilleur_coup
#########################################################################MESSAGE DU VAINQUEUR ou DE L'ÉGALITÉ#############################
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

################################LA BOUCLE COMMUNE À TOUS LES JEUX################################################
while not fini:
    
    if type_jeu==1:#contre humain
        choix=jeu.action_joueur(valeur_joueur,param_jeu)
        
    elif type_jeu==2:#contre machine simple
        if valeur_joueur:
            choix=jeu.action_joueur(valeur_joueur,param_jeu)
        else:
            choix=coup_machine_simple(param_jeu, valeur_joueur)
            print()

    else:#contre machine intelligente
        if valeur_joueur:
            choix=jeu.action_joueur(valeur_joueur,param_jeu)
        else:
            choix = coup_machine_minimax(param_jeu)
            print()        
                    
    param_jeu=jeu.evolution_jeu(valeur_joueur,param_jeu,choix)#########on fait évoluer le jeu
    jeu.aff_evolution_jeu(param_jeu)#########on affiche le jeu
    per_gag,fini=jeu.etat_final(param_jeu)#######on regarde l'état du jeu
    valeur_joueur=not(valeur_joueur)#########on change de joueur

############################################################################################

aff_mess_vainqueur(not(valeur_joueur),per_gag)   # jeu fini et affichage du résultat.
# cette ligne de code sera réalisée lorsque la partie sera finie, à la sortie de la boucle précédente.

