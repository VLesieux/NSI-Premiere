def situation_init():
    """
    : création de la situation initiale du jeu
    : renvoie le nombre d'allumettes du tas
    : param : Rien
    : return : nb_allumettes
    Exemple:
    >>> situation_init()
    11
    """
    nb_allumettes=11
    return nb_allumettes

def choix_joueur(valeur_joueur,param_jeu):
    """
    : Demande au joueur d'effectuer choix d'allumettes à enlever (2 ou3)
    : param : int(param_jeu) nombres d'allumettes
    : return : int(choix) choix du joueur
    Remarque: Ne pas faire de doctest sur des fonctions d'entrées /sorties
    """
    if valeur_joueur:
        joueur='I'
    else:
        joueur='II'
    #init choix jeu
    nb_enlev=0
    #si pas 1 ou 2 attente choix correct
    while (nb_enlev!=2 and nb_enlev!=3):
        nb_enlev= int(input('JOUEUR {} :Choisir le nombre d\'allumettes à enlever : '.format(joueur)))

    choix=test_validite_choix(valeur_joueur,nb_enlev,param_jeu)
    return choix

def test_validite_choix(valeur_joueur,lechoix,tas):
    """
    : test de la validité du choix 2 ou 3
    : param lechoix: (int) valeur allumettes à supprimer
    : param tas: (int) le nombre d'allumettes presentes
    : return : int(choix) choix du joueuraff_evolution_jeu(9) 
    """
    correct=False
    if (((lechoix==2) &(tas>=2))|((lechoix==3) &(tas>=3))):
        correct=True
    else:
        lechoix=choix_joueur(valeur_joueur,tas)
        return lechoix
    if correct:
        return lechoix
    return None

def action_joueur(valeur_joueur,param_jeu):
    """
    : permet de connaitre le nombre d'allumettes à enlever
    : param : bool(valeur_joueur) identification du joueur (True:I;False:II)
    : return : int(choix) choix du joueur
    """
    lechoix=choix_joueur(valeur_joueur,param_jeu)
    return lechoix

def evolution_jeu(valeur_joueur,param_jeu,choix_joueur):
    """
    : permet de faire évoluer le jeu
    : param : int(param_jeu) nombres d'allumettes
    : param : bool(valeur_joueur) identification du joueur (True:I;False:II)
    : return : int(param_jeux) le nombres d'allumettes restantes
    Exemple:
    >>> evolution_jeu(True,11,2)
    9
    """
    param_jeu=param_jeu-choix_joueur

    return param_jeu

def aff_evolution_jeu(param_jeu):
    """
    : permet d'afficher le nombre d'allumettes restants
    : param : int(param_jeu) nombres d'allumettes
    : return : None
    Exemple:
    >>> aff_evolution_jeu(9)
    Il reste 9 allumettes sur la table
    """
    print('Il reste {} allumettes sur la table'.format(param_jeu))
    return None

def etat_final(param_jeu):
    """
    : vérification si fin jeu
    : param : int(param_jeu) nombres d'allumettes
    : return : bool(fini)
    Exemple:
    >>> etat_final(0)
    (True, False)
    """
    per_gag=False
    if ((param_jeu==0)|(param_jeu==1)):
        fini=True
        if param_jeu==1:
            per_gag=True
    else:
        fini=False
    return fini,per_gag

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
