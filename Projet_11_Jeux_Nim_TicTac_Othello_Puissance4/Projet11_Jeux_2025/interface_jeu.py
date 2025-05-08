choix=int(input('Choisissez votre jeu : 1.morpion  ; 2. nim ; 3. Othello ; 4. Puissance 4 : '))
#si 1 importer fichier fonctions voyelle
if choix==1:
    module = 'jeu_nim'
elif choix==2:
    module='jeu_morpion'
elif choix==3:
    module='jeu_othello'
elif choix==4:
    module='jeu_puissance4'
    
jeu=__import__(module)

def aff_mess_vainqueur(valeur_joueur,per_gag,module):
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

    if module=='jeu_nim' or module=='jeu_morpion' or module=='jeu_puissance4':
        if per_gag:
            print('Egalité !!!!')
        else:
            if valeur_joueur:
                #gagné
                print('Le joueur {} a gagné'.format(joueur))
            else:
                #perdu
                print('Le joueur {} a gagné'.format(joueur))
    elif module=='jeu_othello':
        if per_gag==True:
            print('Le joueur I a gagné')
        else:
            print('Le joueur II a gagné')
            

    return None

param_jeu = jeu.situation_init()    #création de la situation courante initiale

valeur_joueur=False #Détermination du premier joueur courant

jeu.aff_evolution_jeu(param_jeu)    #Affichage de l'état du jeu

fini=False  #Initialisation de la situation du jeu

while not fini: # Voir le point 3 de l'introduction : si le jeu n'est pas fini

    choix=jeu.choix_joueur(valeur_joueur,param_jeu)
    param_jeu=jeu.evolution_jeu(valeur_joueur,param_jeu,choix)
    jeu.aff_evolution_jeu(param_jeu)
    fini,per_gag=jeu.etat_final(param_jeu)
    valeur_joueur=not(valeur_joueur)

aff_mess_vainqueur(not(valeur_joueur),per_gag,module)   # jeu fini et affichage du résultat.
# cette ligne de code sera réalisée lorsque la partie sera finie

